---
title: How do you validate a pedestrian model against real data?
date: 2026-09-05
summary: Validation is the step everyone agrees on and few do. We took an open bottleneck experiment, an open model and an open calibration toolkit, and ran the whole procedure, from screening to held-out validation, in a way anyone can repeat.
math: true
thumbnail: fig5.png
---

Pedestrian simulations are used to size exits, plan events and argue about safety, so the question whether a model is right is not academic. The simulation community settled the vocabulary long ago. Verification asks whether the software implements the model correctly. Validation asks whether the model, within the domain it is meant for, reproduces reality with an accuracy that is good enough for its purpose (Sargent 1984, 2008; ISO 16730 as summarised by Ronchi et al. 2013). Sargent adds two points that are easy to forget: a model is never valid in the abstract but only for a purpose, and confidence in a model costs money, so one always stops somewhere short of certainty.

In pedestrian dynamics the models multiplied faster than the data to test them. Seyfried and Schadschneider (2008) showed that even the fundamental diagram, the most basic relation of the field, differs between handbooks by a factor of two in capacity, and that part of the discrepancy comes from the measurement method rather than the crowd. Reliable validation data were so scarce that Oh et al. (2014) validated a bottleneck model with mice. The NIST review of evacuation model verification and validation (Ronchi et al. 2013) lists the open questions bluntly: what accuracy counts as good enough, how many tests, and who runs them.

Two lessons from this field's own validation work shape what follows. Liao et al. (2014) calibrated FDS+Evac on the very experiment we use here, by hand, to match the flow at one width. The flow matched. The density in front of the bottleneck was too low and the speed too high, so the model reached the right flow for the wrong reasons. Their follow-up (Liao et al. 2017) turned that into a rule: a single characteristic cannot validate a model, and the comparison has to combine several. Kurtc et al. (2018) drew the second lesson: the assessment should be automated, including the search for parameters, or it will not be done consistently.

This note puts the two together with tools that are open and generic. The simulation is [JuPedSim](https://jupedsim.org), the analysis of experiment and simulation alike is [PedPy](https://pedpy.readthedocs.io), and the screening, sensitivity analysis and calibration are run by [Dakota](https://dakota.sandia.gov), Sandia's toolkit for exactly this kind of study. Dakota has been used in engineering for decades and almost never in pedestrian dynamics. It turns "which parameters matter, and what values fit the data" from a pile of private scripts into a text file.

## What validation means here

Following Sargent, we state the purpose first. The model should reproduce the flow through wide bottlenecks in a dense, motivated crowd, and it should do so with the right density and speed in front of the bottleneck, not only the right flow. Three observables therefore enter every comparison. The acceptance criterion is the uncertainty of the comparison itself: the run-to-run spread of the simulation plus a plausible measurement error, a few percent on each observable. And the validation data are held out. The optimizer sees three bottleneck widths and never the other two.

## Step 1 — the experiment

The [Hermes bottleneck experiment](https://ped.fz-juelich.de/db/doku.php?id=hermes_bottleneck) was run in May 2009 in Hall 2 of the Düsseldorf fairground with about 350 participants (Seyfried et al. 2009; Liao et al. 2014). The bottleneck was built from boards higher than two metres, 1 m long, and its width was varied from 2.4 to 5.0 m in five runs. Participants waited in a semicircular holding area of radius 8.6 m directly in front of the bottleneck, which puts the initial density at three persons per square metre, and walked through on command. The free walking speed of 42 participants was measured separately: 1.55 m/s with a spread of 0.18 m/s.

The trajectories are open data with a DOI. Since 2024 they come as HDF5 files that carry the geometry along, so PedPy loads both with one call each:

```python
import pedpy, pathlib
f = pathlib.Path("ao-360-400.h5")
traj = pedpy.load_trajectory_from_ped_data_archive_hdf5(f)
area = pedpy.load_walkable_area_from_ped_data_archive_hdf5(f)
```

We measure three things per run: the flow through the bottleneck, from the slope of the N(t) curve at a line across the gap; and the density and mean speed in a 2.8 by 2 m area directly in front of it, averaged over the jam phase. The same three functions are applied to the simulated trajectories. Seyfried and Schadschneider's warning about measurement methods is answered the simplest way: there is only one method, applied to both sides.

{{< figure
    src="fig1.png"
    caption="Measurement setup for the 2.4 m and 5.0 m runs. Red: the flow line across the gap. Blue: the area for density and speed. The dashed line is the simulation geometry: a 20 m wide corridor with the bottleneck boards as a wall band. The dotted lines mark the camera window of the experiment."
>}}

## Step 2 — the defaults are wrong by a factor of two

We rebuilt the setup in JuPedSim: the corridor, the boards, the semicircular holding area with 350 agents at three per square metre, and an exit line behind the bottleneck. The model is the Collision Free Speed model (Tordeux et al. 2016) with its default parameters.

{{< figure
    src="fig2.png"
    caption="Measured N(t) curves (solid) against the default model (dashed), and flow against bottleneck width. The defaults give between 35 and 45 % of the measured flow."
>}}

This is not a surprise if you know the model. Its specific flow is bounded by roughly one over the time gap parameter, which defaults to one second, so the model cannot exceed about one person per metre per second through a jammed opening. The experiment shows close to three. No amount of tweaking the desired speed fixes that. The question is which of the seven parameters do.

## Step 3 — let Dakota find the parameters that matter

Dakota needs two things: an input file describing the study, and a driver script that turns a parameter vector into responses. Our driver reads Dakota's parameter file, runs one JuPedSim simulation per bottleneck width, computes the three observables with PedPy and writes them back. That is all the coupling there is.

```
method
  psuade_moat
    samples = 80
    partitions = 3

variables
  continuous_design = 7
    descriptors 'desired_speed' 'radius' 'time_gap' 'strength_neighbor'
                'range_neighbor' 'strength_geometry' 'range_geometry'
    lower_bounds 0.8 0.12 0.10  2.0 0.02  1.0 0.01
    upper_bounds 1.8 0.25 1.20 15.0 0.50 10.0 0.20

interface
  fork
    analysis_drivers = 'python3 driver.py'
    parameters_file = 'params.in'
    results_file = 'results.out'
    work_directory named 'runs/run' directory_tag
  asynchronous evaluation_concurrency = 3

responses
  response_functions = 9
  no_gradients
  no_hessians
```

The first stage is a Morris screening: 80 evaluations, each one a short walk through parameter space changing one parameter at a time. It is cheap and it ranks the parameters per observable.

{{< figure
    src="fig3.png"
    caption="Morris screening. Each cell is the mean absolute effect of a parameter on an observable, scaled to the strongest parameter in that column, computed on the trajectories where no run failed. The time gap and the agent radius drive the flow, the neighbor repulsion drives the density, and the two wall parameters barely matter."
>}}

The screening also revealed something no fit would have: in 28 of the 80 evaluations the model pushed agents through the walls and JuPedSim aborted the run. Those combinations have strong, long-range neighbor repulsion and weak wall repulsion. We narrowed the bounds accordingly and froze the wall parameters at their defaults. Knowing where a model breaks is part of validating it.

With five parameters left, a Sobol analysis with 280 evaluations gives the proper variance decomposition. Dakota computes the indices itself; the only change to the input file is one keyword, `variance_based_decomp`.

{{< figure
    src="fig4.png"
    caption="Sobol indices for the five remaining parameters, 280 evaluations, none failed. The time gap owns the flow and the speed, the radius and the neighbor repulsion range own the density. The desired speed explains little of any observable: in a jammed crowd it is nearly unidentifiable from jam observables, which matters below. With 40 base samples the estimates carry noise of a few hundredths, which is why some main indices exceed their totals; the ranking is robust, the decimals are not."
>}}

## Step 4 — calibration, and why we did not use gradients

Our first attempt at calibration used a classic gradient-based least-squares solver. It stalled at the starting point. Two simulations whose parameters differ in the sixth digit produce evacuation times that differ by seconds, because the dynamics of 350 interacting agents are chaotic. Finite-difference gradients of such a function are noise.

The method that works is Dakota's `efficient_global`: it fits a Gaussian process to the evaluations so far and picks the next point where the expected improvement is largest. It needs no gradients, it copes with noise, and it treats each evaluation as expensive, which ours are. We calibrated on the 2.4, 3.6 and 5.0 m runs, nine residuals weighted by their uncertainty, and kept the 3.0 and 4.4 m runs untouched for validation.

```
method
  efficient_global
    max_iterations = 60

responses
  calibration_terms = 9
    weights = 7.6 3.2 977  3.4 4.3 517  1.45 6.0 252
  no_gradients
  no_hessians
```

After 42 evaluations, about twenty minutes on a laptop, the optimizer converged. All nine residuals were within the noise. And the desired speed had gone to the lower bound of its range, 0.8 m/s, half the free speed measured on the participants.

This is the moment where a fit and a validation part ways. The Sobol analysis had already said that the desired speed explains almost nothing in a jammed crowd, so the optimizer was free to put it anywhere, and it put it where the residuals were a hair smaller. A model with participants walking at 0.8 m/s reproduces the bottleneck. It does not reproduce the participants. Sargent calls this data validity: parameters that were measured are data, not fitting variables. Liao et al. (2014) made the same move for FDS+Evac. So we fixed the desired speed at the measured 1.55 m/s and calibrated the remaining four parameters. That converged in 24 evaluations.

| parameter | default | all five free | desired speed fixed |
|---|---|---|---|
| desired speed [m/s] | 1.2 | 0.80 (at bound) | 1.55 (measured) |
| radius [m] | 0.20 | 0.14 | 0.13 |
| time gap [s] | 1.0 | 0.56 | 0.81 |
| neighbor repulsion strength | 8 | 6.1 | 2.1 |
| neighbor repulsion range [m] | 0.10 | 0.15 | 0.25 |

Both parameter sets fit the three calibration widths to within a few percent. They are nowhere near each other. Time gap, repulsion strength and range all shift by factors of two or three to compensate for the change in desired speed. Three observables at three widths do not pin five parameters, and a good fit says nothing about whether the parameters mean what their names say. Fixing the one parameter that was measured removes the freedom to be wrong in that direction.

## Step 5 — does it hold on the widths it never saw?

{{< figure
    src="fig5.png"
    caption="Flow, density and speed against bottleneck width: experiment, default model and calibrated model. The dotted widths, 3.0 and 4.4 m, were not used in the calibration. Error bars are the spread over three random seeds."
>}}

With the desired speed fixed, the model holds on the two widths the optimizer never saw. At 3.0 m the flow is 9 % high and density and speed within 5 %. At 4.4 m the flow is within 3 %, the density 7 % high and the speed 11 % low. That is at the edge of the acceptance criterion we set, and honest about where the model is weakest: it reaches the right flow at 4.4 m with slightly too many, slightly too slow agents in front of the gap, a milder version of what Liao et al. (2014) saw in FDS+Evac.

| width [m] | flow exp / sim [1/s] | density exp / sim [1/m²] | speed exp / sim [m/s] |
|---|---|---|---|
| 2.4 | 6.1 / 6.3 | 5.6 / 5.9 | 0.32 / 0.30 |
| 3.0 (held out) | 7.2 / 7.9 | 5.1 / 5.2 | 0.37 / 0.39 |
| 3.6 | 9.0 / 9.4 | 4.8 / 4.8 | 0.44 / 0.44 |
| 4.4 (held out) | 10.9 / 11.2 | 4.0 / 4.3 | 0.55 / 0.49 |
| 5.0 | 13.8 / 12.4 | 4.1 / 4.0 | 0.63 / 0.53 |

The largest miss is at 5.0 m, a calibration width: the measured flow jumps above the linear trend there and the model does not follow. Either the widest run is different in a way three scalar observables cannot see, or the model's flow really is linear in the width. That is a question about the model, and now a well-posed one.

## What we learned about validating

- **State the purpose, then pick the observables.** Flow alone would have passed a model with the wrong density, as it did in 2014. Three observables, one per mechanism, is the minimum.
- **Analyse experiment and simulation with the same code.** The measurement method is part of the result. PedPy loads both, so the observables are defined once.
- **Screen before you calibrate.** The Morris run costs 80 evaluations, removed two of seven parameters, and mapped a whole region where the model fails outright.
- **Do not use gradients on an agent-based model.** Surrogate-based optimization converged in a few dozen evaluations where the gradient solver never left the start.
- **Hold something back.** Calibrating on three widths and validating on two is the difference between a fit and a validated model, and it is the only way to see where the model, not the parameters, is at fault.
- **Dakota's job is orchestration, not physics.** It knows nothing about pedestrians. It knows how to run a driver in parallel a few hundred times and what to make of the numbers that come back. That is the part you do not want to write yourself, and the part that makes the procedure repeatable.

## Why openness is the method here

Sargent drew the cost of validation against the confidence it buys as a curve that rises steeply near the end. Everything in this study is about pushing that curve down. The trajectories are on a public archive with a DOI and the geometry attached. The model is open source and scriptable. The analysis library is the same one used on the experiment. The calibration toolkit has been maintained by a national laboratory for 25 years. The only thing we added is one driver script and three input files, and they are in the repository linked below.

That has consequences beyond convenience. Anyone can rerun the calibration with a different observable, a different model or a different experiment from the same archive and compare numbers with ours. Someone who thinks a remaining discrepancy is a model deficiency can test it this afternoon. And a validation that lives in a text file can be reviewed, which a sentence like "parameters were chosen according to the literature" never could. Open data and open software are often argued for on principle. This is the practical version of the argument: put together, they turn validation from a private craft into a shared, checkable result.

## References

- Kurtc, V., Chraibi, M., Tordeux, A. (2018). Automated quality assessment of space-continuous models for pedestrian dynamics. [arXiv:1809.01862](https://arxiv.org/abs/1809.01862).
- Liao, W., Chraibi, M., Seyfried, A., Zhang, J., Zheng, X., Zhao, Y. (2014). Validation of FDS+Evac for pedestrian simulations in wide bottlenecks. IEEE ITSC 2014, 554–559. [doi:10.1109/ITSC.2014.6957748](https://doi.org/10.1109/ITSC.2014.6957748).
- Liao, W., Zhang, J., Zheng, X., Zhao, Y. (2017). A generalized validation procedure for pedestrian models. Simulation Modelling Practice and Theory 77, 20–31. [doi:10.1016/j.simpat.2017.05.002](https://doi.org/10.1016/j.simpat.2017.05.002).
- Oh, H., Lyu, J., Yoon, S., Park, J. (2014). Validation of evacuation dynamics in bottleneck with various exit angles. Transportation Research Procedia 2, 752–759.
- Ronchi, E., Kuligowski, E. D., Reneke, P. A., Peacock, R. D., Nilsson, D. (2013). The process of verification and validation of building fire evacuation models. NIST Technical Note 1822.
- Sargent, R. G. (1984). Simulation model validation. In: Simulation and Model-Based Methodologies: An Integrative View, Springer, 537–555.
- Sargent, R. G. (2008). Verification and validation of simulation models. Proceedings of the Winter Simulation Conference, 157–169.
- Seyfried, A., Schadschneider, A. (2008). Fundamental diagram and validation of crowd models. ACRI 2008, LNCS 5191, 563–566.
- Seyfried, A., Passon, O., Steffen, B., Boltes, M., Rupprecht, T., Klingsch, W. (2009). New insights into pedestrian flow through bottlenecks. Transportation Science 43, 395–406.
- Tordeux, A., Chraibi, M., Seyfried, A. (2016). Collision-free speed model for pedestrian dynamics. Traffic and Granular Flow '15, 225–232.
- Experiment data: Hermes bottleneck experiment, Düsseldorf 2009, [doi:10.34735/ped.2009.6](https://doi.org/10.34735/ped.2009.6). Dakota: Adams et al., Sandia National Laboratories, version 6.24.

Code, Dakota input files and results: [github.com/PedestrianDynamics/jupedsim-dakota-calibration](https://github.com/PedestrianDynamics/jupedsim-dakota-calibration)

{{< icon "pencil-alt" >}} By: [Mohcine Chraibi]({{< relref "/authors#MohcineChraibi" >}})
