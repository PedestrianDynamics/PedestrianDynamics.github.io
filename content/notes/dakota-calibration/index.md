---
title: "Calibrating a pedestrian model against real data, part 1: the bottleneck"
date: 2026-09-05
draft: true
summary: We calibrated JuPedSim's Collision Free Speed model with Dakota on an open bottleneck experiment and checked the result on two widths the optimizer never saw. The defaults miss the flow by a factor of two. Calibration brings it mostly within ten percent, though neither calibrated set passes the stated tolerance everywhere, and two optimizer starts give two different parameter sets.
math: true
aliases: [/blog/dakota-calibration/]
thumbnail: fig5.png
---

{{< callout type="info" icon="information-circle" >}}
**Abstract.** This is the first of two parts. We calibrated JuPedSim's Collision Free Speed model with Dakota against the Hermes bottleneck experiment, three widths in the fit and two held out, with the same open analysis code on experiment and simulation. The defaults miss the measured flow by a factor of two. After calibration, flow, density and speed in front of the opening are mostly within ten percent, including at the two held-out widths, but not everywhere: both calibrated sets overshoot the flow at 3.0 m and undershoot it at 5.0 m. Two optimizer starts give two parameter sets with near-equal residual norms that differ by factors of two to four. The held-out widths are an interpolation test inside one experiment, not an independent validation. [Part 2]({{< relref "/notes/dakota-validation" >}}) takes the same parameters to a half-metre gate and an unguided entrance, where they fail.
{{< /callout >}}

Pedestrian simulations are used to size exits, plan events and argue about safety, so the question whether a model is right is not academic. The simulation community settled the vocabulary long ago. Verification asks whether the software implements the model correctly. Validation asks whether the model, within the domain it is meant for, reproduces reality with an accuracy that is good enough for its purpose (Sargent 1984, 2008; ISO 16730 as summarised by Ronchi et al. 2013). Sargent adds two points that are easy to forget: a model is never valid in the abstract but only for a purpose, and confidence in a model costs money, so one always stops somewhere short of certainty.

Two lessons from this field's own validation work shape what follows. Liao et al. (2014) calibrated FDS+Evac on the very experiment we use here, by hand, to match the flow at one width. The flow matched. The density in front of the bottleneck was too low and the speed too high, so the model reached the right flow for the wrong reasons. Their follow-up (Liao et al. 2017) turned that into a rule: a single characteristic cannot validate a model, and the comparison has to combine several. Kurtc et al. (2018) drew the second lesson: the assessment should be automated, including the search for parameters, or it will not be done consistently. Kretz et al. (2026) reached the first lesson from the other side with a social force model: a single-parameter fit to the mean flow matched the flow either way, and only the individual travel times told a good calibration from a bad one.

This note puts the two lessons together with tools that are open and generic. The simulation is [JuPedSim](https://jupedsim.org), the analysis of experiment and simulation alike is [PedPy](https://pedpy.readthedocs.io), and the screening, sensitivity analysis and calibration are run by [Dakota](https://dakota.sandia.gov), Sandia's toolkit for exactly this kind of study. Dakota has been used in engineering for decades and almost never in pedestrian dynamics. It turns "which parameters matter, and what values fit the data" from a pile of private scripts into a text file.

## What validation means here

Following Sargent, we state the purpose first. **The model should reproduce the flow through wide bottlenecks in a dense, motivated crowd, and it should do so with the right density and speed in front of the bottleneck, not only the right flow.** Three observables therefore enter every comparison: throughput and the two components of the upstream state. They are the complementary quantities we chose for this study, not a canonical minimum. The decision rule is a fixed relative tolerance per observable, 6 % on flow and 10 % on density and speed, and a comparison passes when the mean over simulation seeds lies within it. The same numbers weight the calibration residuals. They were set before any calibration was run, from the seed-to-seed spread of the simulation plus an allowance for measurement error, but they were chosen as calibration weights. Adopting them as the acceptance tolerance is a decision we made when the results were assessed, not a pre-registered one. **Two of the five bottleneck widths are held out: the optimizer sees 2.4, 3.6 and 5.0 m and never 3.0 and 4.4 m.** That is an interpolation test within one apparatus and one participant pool. It is a stronger check than a fit, and a weaker one than a second experiment.

## Step 1 — the experiment

{{< figure
    src="exp1.jpg"
    caption="The Hermes bottleneck experiment, Düsseldorf 2009: overhead view of a run, and the setup sketch with the semicircular holding zones at 3 persons per square metre. Images: Pedestrian Dynamics Data Archive, Forschungszentrum Jülich."
>}}

The [Hermes bottleneck experiment](https://ped.fz-juelich.de/db/doku.php?id=hermes_bottleneck) was run in May 2009 in Hall 2 of the Düsseldorf fairground with about 350 participants (Seyfried et al. 2009; Liao et al. 2014). The bottleneck was built from boards higher than two metres, 1 m long, and its width was varied from 2.4 to 5.0 m in five runs, one run per width. Participants waited in a semicircular holding area of radius 8.6 m directly in front of the bottleneck, which puts the initial density at three persons per square metre, and walked through on command. The free walking speed of 42 participants was measured separately: 1.55 m/s with a spread of 0.18 m/s.

The trajectories are open data with a DOI. Since 2024 they come as HDF5 files that carry a geometry along, so PedPy loads both with one call each. One caveat, found only by reading the paper next to the file: the polygon in the archive is a 12 m box around the camera window with the wall blocks cut off at its edges, and three of its five gaps are 0.1 m narrower than the run's stated width. The simulation therefore takes the gap width from the run parameter and the corridor and holding area from the paper. A corrected polygon for each run is in the repository. The initial positions are not the measured ones either: the simulation places 350 agents on a jittered lattice inside the semicircle at the stated density, so the holding area is an initialization region, not a reconstructed crowd.

```python
import pedpy, pathlib
f = pathlib.Path("ao-360-400.h5")
traj = pedpy.load_trajectory_from_ped_data_archive_hdf5(f)
area = pedpy.load_walkable_area_from_ped_data_archive_hdf5(f)
```

We measure three things per run: the flow through the bottleneck, from the slope of the N(t) curve at a line across the gap; and the density and mean speed in a 2.8 by 2 m area directly in front of it, averaged over the jam phase. The area is the same for all widths, so it covers more than the 2.4 m opening and only the middle of the 5.0 m one. These are local measurements of the crowd state upstream of the gap, and the calibration compares them like for like. The same three functions are applied to the simulated trajectories. Seyfried and Schadschneider's (2008) warning that the measurement method changes the result is answered the simplest way: there is only one method, applied to both sides.

{{< figure
    src="fig1.png"
    caption="Measurement setup for the 2.4 m and 5.0 m runs. Red: the flow line across the gap. Blue: the area for density and speed. The dashed line is the simulation geometry: a 20 m wide corridor with the bottleneck boards as a wall band. The dotted lines mark the camera window of the experiment."
>}}

## Step 2 — the defaults are wrong by a factor of two

We rebuilt the setup in JuPedSim: the corridor, the boards, the semicircular holding area with 350 agents at three per square metre, and an exit line behind the bottleneck. The model is the Collision Free Speed model (Tordeux et al. 2016) with its default parameters.

{{< figure
    src="fig2.png"
    caption="Measured N(t) curves (solid) against the default model (dashed), and flow against bottleneck width. The defaults underpredict the flow by a factor of two to three, worst at the widest opening."
>}}

This is not a surprise if you know the model. In the Collision Free Speed model the time gap sets the headway an agent keeps to the one in front, and the radius sets how close agents can pack side by side; together with the neighbor repulsion they fix the throughput of a jammed opening, and the desired speed hardly enters once the crowd is jammed. **With the defaults, one second of headway and a 0.2 m radius, the model delivers a third to a half of the measured flow. No amount of tweaking the desired speed fixes that.** The question is which of the seven parameters do, and by how much.

## Step 3 — let Dakota find the parameters that matter

Dakota needs two things: an input file describing the study, and a driver script that turns a parameter vector into responses. Our driver reads Dakota's parameter file, runs one JuPedSim simulation per bottleneck width, computes the three observables with PedPy and writes them back. That is all the coupling there is.

```
method
  psuade_moat
    samples = 160
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

The first stage is a Morris screening: twenty trajectories of eight evaluations each, every step changing one parameter at a time, 160 evaluations in all. It is cheap and it ranks the parameters per observable. It is a ranking, not a measurement, and it is conditional on the ranges it was sampled over.

{{< figure
    src="fig3.png"
    caption="Morris screening over the full parameter ranges, twenty trajectories. Each cell is the mean absolute elementary effect of a parameter on an observable, scaled to the strongest parameter in that column. Steps where either end failed were discarded, and n per row is the number of valid steps out of the twenty drawn. The time gap, the radius and the neighbor repulsion range dominate; the desired speed has a moderate effect on flow and speed over this wide range; the two wall parameters are weakest."
>}}

**The screening also revealed something no fit would have: in 43 of the 160 evaluations, about a quarter, the model pushed agents through the walls and JuPedSim aborted the run.** Those combinations have strong, long-range neighbor repulsion and weak wall repulsion. This is a failure of the model's numerical domain, not an observation about pedestrians, but it is one an engineer can land in by hand. We narrowed the bounds accordingly and froze the wall parameters at their defaults.

With five parameters left, and narrower ranges, a Sobol analysis gives the variance decomposition. Dakota computes the indices itself; the input file changes the method block to `sampling` with `variance_based_decomp`, the variables become uncertain variables with uniform distributions over the narrowed ranges, and the cost is the base sample size times the number of parameters plus two. Each parameter point uses simulation seed 1; seed variability is measured separately later rather than treated as another physical input.

How many samples are enough is an empirical question, so we answered it empirically: three replicate runs with 40 base samples, then 80 and 160, 2520 evaluations in all. The magnitudes are not converged: the time gap's total index on flow and speed still rises from about 0.4 to about 0.7 between 80 and 160 samples. **What is stable across every run is the small group of influential parameters per observable:** time gap and radius for flow, radius and neighbor range for density, time gap and neighbor range for speed, with the desired speed a minor contributor. Since only the grouping is used below, we did not spend further computation on the numbers.

{{< figure
    src="fig4.png"
    caption="Sobol indices for the five remaining parameters from the run with 160 base samples, 1120 evaluations, none failed. The time gap dominates flow and speed with total indices of 0.6 to 0.8; the radius dominates density with 0.5 to 0.6, followed by the neighbor repulsion range with about 0.3; the desired speed contributes 0.06 to flow and 0.12 to 0.17 to speed."
>}}

{{< figure
    src="fig9.png"
    caption="Sobol total indices against the base sample size. Bars at 40 span three replicate runs with different seeds. The group of influential parameters per observable is the same in every run; the magnitudes are not settled at 160 base samples."
>}}

## Step 4 — calibration, and why we did not use gradients

Our first attempt at calibration, on a simpler two-room test case before touching the experiment, used Dakota's gradient-based least-squares solver with finite-difference gradients. It stalled at the starting point: two simulations whose parameters differ in the sixth digit produced evacuation times that differed by seconds, and the differences used as gradients were noise. We did not repeat the test on the Hermes objective, so this is an observation about that solver on that test case, not a property of the calibration problem here.

The method we used instead is Dakota's `efficient_global`, an implementation of Efficient Global Optimization (Jones et al. 1998). The objective is a weighted sum of squared residuals over the nine observables, three per calibration width,

$$
f(\theta) = \sum_{i=1}^{9} w_i \,\bigl(y_i(\theta) - \hat{y}_i\bigr)^2 ,
$$

where \(\theta\) is the parameter vector, \(y_i(\theta)\) the simulated observable, \(\hat{y}_i\) the measured one, and \(w_i = 1/\sigma_i^2\) with \(\sigma_i\) the assumed uncertainty, 6 % of the measured flow and 10 % of the measured density and speed; the weights in the input file below are these inverse squared uncertainties. The residual norm quoted throughout is \(\sqrt{f}\), in units of the assumed uncertainty. Each evaluation of \(f\) costs three JuPedSim runs at one fixed seed, so the optimizer sees a single realization of a stochastic simulator; seed variability is measured afterwards, not modelled in the fit. Finite differences of such an objective are noise, so the optimizer never differentiates it. Instead it fits a Gaussian process to all evaluations made so far, which gives a prediction \(\mu(\theta)\) and a standard deviation \(s(\theta)\) at every untried point, and it picks the next point where the expected improvement over the best value \(f_{\min}\) seen so far is largest:

$$
\mathrm{EI}(\theta) = \bigl(f_{\min} - \mu(\theta)\bigr)\,\Phi(z) + s(\theta)\,\varphi(z),
\qquad z = \frac{f_{\min} - \mu(\theta)}{s(\theta)} ,
$$

with \(\Phi\) and \(\varphi\) the standard normal distribution and density functions. The first term rewards points the surrogate expects to be good, the second rewards points where it is uncertain, so the search balances exploiting the current best region against exploring the rest of the box. It stops when the largest expected improvement falls below a threshold, or when the new point is too close to an evaluated one, or at the iteration cap. Each step costs one simulation batch and a surrogate fit, so a calibration takes a few dozen evaluations rather than the hundreds a gradient method would spend on noise.

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

After 42 evaluations, about twenty minutes on a laptop, the optimizer converged with all nine residuals below one standard deviation of the assumed uncertainty. And the desired speed had gone to the lower bound of its range, 0.8 m/s, half the free speed measured on the participants.

This is the moment where a fit and a validation part ways. The Sobol analysis had already said that the desired speed is a minor influence on the jam observables, so the misfit is flat along it and the optimizer was free to put it wherever the residuals were a hair smaller. **A model with participants walking at 0.8 m/s reproduces the bottleneck. It does not reproduce the participants.** Sargent calls this data validity: parameters that were measured are data, not fitting variables. Liao et al. (2014) made the same move for FDS+Evac. So we fixed the desired speed at the measured 1.55 m/s and calibrated the remaining four parameters. That converged in 24 evaluations.

| parameter | default | all five free | speed fixed, set A | speed fixed, set B |
|---|---|---|---|---|
| desired speed [m/s] | 1.2 | 0.80 (at bound) | 1.55 (measured) | 1.55 (measured) |
| radius [m] | 0.20 | 0.14 | 0.13 | 0.15 |
| time gap [s] | 1.0 | 0.56 | 0.81 | 0.55 |
| neighbor repulsion strength | 8 | 6.1 | 2.1 | 9.4 |
| neighbor repulsion range [m] | 0.10 | 0.15 | 0.25 | 0.10 |
| weighted residual norm (six-seed recalculation) | | | 2.7 | 2.4 |

Set B is the reason for the last column. A surrogate-based optimizer with a few dozen evaluations can settle in one region of a flat landscape, so we repeated the fixed-speed calibration from a different optimizer seed. Dakota reported objective norms of 1.0 and 1.5 at the selected evaluations. Recomputing the norm from the six-seed means used for the later comparison gives 2.7 for set A and 2.4 for set B; those are the values in the table. We have no uncertainty on these norms, the observables are correlated, and we did not sample the objective's seed distribution, so we cannot say that the two sets are statistically equivalent or that the landscape has exactly two optima. What two starts do show is that the reported optimum depends on where the optimizer started. **Reported without a second start, a calibrated parameter set is one sample.**

Both sets reproduce flow and density at the three calibration widths to within about ten percent, and speed to within twenty, with residual norms we cannot distinguish. They are nowhere near each other. Time gap, repulsion strength and range shift by factors of two to four between them. Three observables at three widths do not pin four free parameters, and a good fit says nothing about whether the parameters mean what their names say. Fixing the one parameter that was measured removes the freedom to be wrong in that direction. It does not make the others physical: the radius that comes out, 0.13 to 0.15 m, is an effective size in a model with round bodies, and the remaining parameters still compensate for one another.

## Step 5 — does it hold on the widths it never saw?

{{< figure
    src="fig5.png"
    caption="Flow, density and speed against bottleneck width: experiment with the acceptance band (6 % on flow, 10 % on density and speed, the uncertainty assumed in the calibration weights), default model, and the two calibrated sets with the desired speed fixed. Error bars are the minimum and maximum over six simulation seeds; the experiment is one run per width. The dotted widths, 3.0 and 4.4 m, were not used in the calibration."
>}}

With the desired speed fixed, both calibrated sets improve every observable substantially, at the held-out widths too. Applied as a decision rule, the tolerance passes neither set everywhere. Both overshoot the flow at the held-out 3.0 m by 10 to 13 %; set A's speed is 12 % low at the held-out 4.4 m; and at the 5.0 m calibration width both are 10 % low on flow. Where the two sets differ is what else they get wrong at the wide end. Set A follows the measured increase of speed with width up to 3.6 m and then flattens, 17 % low at 5.0 m, while it keeps the density within tolerance. Set B keeps the speed within tolerance at every width and instead lets the density fall 10 % short at 5.0 m. So at the widest opening set A preserves the local density and underpredicts the speed, set B improves the speed and underpredicts the density, and both underpredict the flow. That is a milder version of what Liao et al. (2014) saw in FDS+Evac.

Deviation of the simulation from the experiment, mean over six seeds, with the band at 6 % for flow and 10 % for density and speed:

| width [m] | flow A / B | density A / B | speed A / B |
|---|---|---|---|
| 2.4 | +3 % / +5 % | +7 % / +1 % | −6 % / −5 % |
| 3.0 (held out) | +10 % / +13 % | +2 % / −3 % | +5 % / +9 % |
| 3.6 | +3 % / +4 % | 0 % / −6 % | −3 % / +4 % |
| 4.4 (held out) | +2 % / +4 % | +8 % / −1 % | −12 % / +1 % |
| 5.0 | −11 % / −10 % | −1 % / −10 % | −17 % / −4 % |

The seed-to-seed standard deviation is 2 to 4 % for flow and density and 3 to 6 % for speed, so the differences between A and B at the wide openings are larger than the simulation noise. The experiment, however, is one run per width, and we have not quantified its measurement error; the band is an assumption, not a measured interval.

**The honest summary of Step 5 is: a substantial improvement over the defaults, and a partial transfer to the held-out widths, but not a model validated for the full 2.4 to 5.0 m range by the stated rule.** At the calibration widths 2.4 and 3.6 m both sets meet the tolerance on all three observables, which is a fit, not validation. The held-out evidence is two widths: at 4.4 m set B meets the tolerance on all three observables and set A fails it on speed; at 3.0 m both fail it on flow. And both miss the widest calibration opening in a way the two calibrations move between speed and density but neither removes. Whether that is acceptable depends on the purpose, which is why the purpose has to be stated first.

## What part 1 establishes, and what it does not

- **A reproducible calibration.** Every step is a Dakota input file and a driver script in the repository. Anyone can rerun it with another observable, model or experiment from the same archive.
- **The defaults are not usable for this purpose.** They miss the flow by a factor of two to three, and no single parameter fixes it.
- **Two parameter sets, not one.** Two optimizer starts give sets with near-equal residual norms that differ by factors of two to four. The data do not identify the parameters; they constrain combinations of them.
- **Partial width transfer.** Held-out widths inside one experiment are an interpolation test. The model passes it in part. This is not evidence for any other geometry, crowd or motivation.
- **A pipeline audit.** Between the first draft and this one, reviews found participants missing from simulations, unwritten final trajectory frames and a geometry error. Each was corrected and every dependent result recomputed; the Hermes steady-phase observables changed by less than half a percent. The evaluation status files and the commit history in the repository carry the record.

The natural next question is what the two sets do outside this experiment. [Part 2]({{< relref "/notes/dakota-validation" >}}) takes both to a half-metre gate and to an unguided entrance. One of them stalls, the other is too fast, and a second calibration on the new data disagrees with the first about which parameters matter.

## References

- Jones, D. R., Schonlau, M., Welch, W. J. (1998). Efficient global optimization of expensive black-box functions. Journal of Global Optimization 13, 455–492. [doi:10.1023/A:1008306431147](https://doi.org/10.1023/A:1008306431147).
- Kretz, T., Eckes, L., Knappik, L., Diz, J., Lipp, D., Müller, S. (2026). Using empirical travel time distributions for calibration of a model of pedestrian dynamics. EURO Journal on Transportation and Logistics 15, 100179. [doi:10.1016/j.ejtl.2026.100179](https://doi.org/10.1016/j.ejtl.2026.100179).
- Kurtc, V., Chraibi, M., Tordeux, A. (2018). Automated quality assessment of space-continuous models for pedestrian dynamics. [arXiv:1809.01862](https://arxiv.org/abs/1809.01862).
- Liao, W., Chraibi, M., Seyfried, A., Zhang, J., Zheng, X., Zhao, Y. (2014). Validation of FDS+Evac for pedestrian simulations in wide bottlenecks. IEEE ITSC 2014, 554–559. [doi:10.1109/ITSC.2014.6957748](https://doi.org/10.1109/ITSC.2014.6957748).
- Liao, W., Zhang, J., Zheng, X., Zhao, Y. (2017). A generalized validation procedure for pedestrian models. Simulation Modelling Practice and Theory 77, 20–31. [doi:10.1016/j.simpat.2017.05.002](https://doi.org/10.1016/j.simpat.2017.05.002).
- Ronchi, E., Kuligowski, E. D., Reneke, P. A., Peacock, R. D., Nilsson, D. (2013). The process of verification and validation of building fire evacuation models. NIST Technical Note 1822.
- Sargent, R. G. (1984). Simulation model validation. In: Simulation and Model-Based Methodologies: An Integrative View, Springer, 537–555.
- Sargent, R. G. (2008). Verification and validation of simulation models. Proceedings of the Winter Simulation Conference, 157–169.
- Seyfried, A., Schadschneider, A. (2008). Fundamental diagram and validation of crowd models. ACRI 2008, LNCS 5191, 563–566.
- Seyfried, A., Passon, O., Steffen, B., Boltes, M., Rupprecht, T., Klingsch, W. (2009). New insights into pedestrian flow through bottlenecks. Transportation Science 43, 395–406.
- Tordeux, A., Chraibi, M., Seyfried, A. (2016). Collision-free speed model for pedestrian dynamics. Traffic and Granular Flow '15, 225–232.
- Experiment data: Hermes bottleneck experiment, Düsseldorf 2009, [doi:10.34735/ped.2009.6](https://doi.org/10.34735/ped.2009.6). Dakota: Adams et al., Sandia National Laboratories, version 6.24.

## Code

Driver scripts, Dakota input files, results and figures for every step: [github.com/PedestrianDynamics/jupedsim-dakota-calibration](https://github.com/PedestrianDynamics/jupedsim-dakota-calibration)

Software used in this study:

- [Dakota](https://dakota.sandia.gov) 6.24
- [JuPedSim](https://jupedsim.org) 1.4.2
- [PedPy](https://pedpy.readthedocs.io) 1.4.0

{{< icon "pencil-alt" >}} By: [Mohcine Chraibi]({{< relref "/authors#MohcineChraibi" >}})
