---
title: How do you calibrate a pedestrian model against real data?
date: 2026-09-05
summary: Open data, an open model and an open calibration toolkit. We calibrated JuPedSim's Collision Free Speed model against the Hermes bottleneck experiments with Dakota, and everything in the chain can be rerun by anyone.
math: true
thumbnail: fig5.png
---

Every pedestrian model has parameters, and every paper that uses one has a sentence like "parameters were chosen according to the literature". Usually that means the defaults. Calibrating properly means experimental data, a model you can run thousands of times, and a tool that turns those runs into a systematic study. Ten years ago each of those was locked up somewhere: the data on a hard disk in one institute, the model in a licensed package, the study in a pile of private scripts. Today all three are open. We wanted to see how far that gets you.

The tools are [JuPedSim](https://jupedsim.org) for the simulation, [PedPy](https://pedpy.readthedocs.io) for the analysis of both experiment and simulation, and [Dakota](https://dakota.sandia.gov), Sandia's toolkit for sensitivity analysis, uncertainty quantification and optimization. Dakota has been around for decades in engineering, but it is rarely seen in pedestrian dynamics. That is a pity: it turns "which parameters matter, and what values fit the data" from an afternoon of hand-written loops into a text file.

## Step 1 — the experiment

The [Hermes bottleneck experiment](https://ped.fz-juelich.de/db/doku.php?id=hermes_bottleneck) from 2009 sent about 350 people through a bottleneck whose width was varied between 2.4 and 5.0 m in five runs. The trajectories are open data. Since 2024 they come as HDF5 files that carry the geometry along, so PedPy loads both with one call each:

```python
import pedpy, pathlib
f = pathlib.Path("ao-360-400.h5")
traj = pedpy.load_trajectory_from_ped_data_archive_hdf5(f)
area = pedpy.load_walkable_area_from_ped_data_archive_hdf5(f)
```

We measure three things per run: the flow through the bottleneck, from the slope of the N(t) curve at a line across the gap; and the density and mean speed in a 2.8 by 2 m area directly in front of it, averaged over the jam phase. The same three functions are applied to the simulated trajectories, so any difference is the model's, not the analysis'.

{{< figure
    src="fig1.png"
    caption="Measurement setup for the 2.4 m and 5.0 m runs. Red: the flow line across the gap. Blue: the area for density and speed. The dashed line is the simulation geometry, which closes the walls to the sides and extends the waiting area so all 350 agents fit. The dotted lines mark the camera window."
>}}

## Step 2 — the defaults are wrong by a factor of two

We rebuilt the geometry in JuPedSim, placed 350 agents on a lattice in the waiting area and let them walk to an exit line behind the bottleneck, using the Collision Free Speed model with its default parameters.

{{< figure
    src="fig2.png"
    caption="Measured N(t) curves (solid) against the default model (dashed), and flow against bottleneck width. The defaults give about 40 % of the measured flow at every width."
>}}

This is not a surprise if you know the model. Its specific flow is bounded by roughly one over the time gap parameter, which defaults to one second, so the model cannot exceed about one person per metre per second. The experiment shows close to three. No amount of tweaking the desired speed fixes that. The question is which of the seven parameters do.

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
    caption="Morris screening. Each cell is the mean absolute effect of a parameter on an observable, scaled to the strongest parameter in that column. The time gap and the agent radius drive the flow, the neighbor repulsion drives the density, and the two wall parameters barely matter."
>}}

One thing the screening also revealed: in a third of the evaluations the model pushed agents through the walls and JuPedSim aborted the run. Those combinations have strong, long-range neighbor repulsion and weak wall repulsion. We narrowed the bounds accordingly and froze the wall parameters at their defaults. Knowing where a model breaks is part of what you learn.

With five parameters left, a Sobol analysis with 280 evaluations gives the proper variance decomposition. Dakota computes the indices itself; the only change to the input file is one keyword, `variance_based_decomp`.

{{< figure
    src="fig4.png"
    caption="Sobol indices for the five remaining parameters, 280 evaluations. The time gap owns the flow and the speed, the radius and the neighbor repulsion range own the density. With 40 base samples the estimates carry noise of a few hundredths, which is why some main indices exceed their totals; the ranking is robust, the decimals are not."
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

After 36 evaluations, about half an hour on a laptop, the optimizer converged:

| parameter | default | calibrated |
|---|---|---|
| desired speed [m/s] | 1.2 | 0.95 |
| radius [m] | 0.20 | 0.14 |
| time gap [s] | 1.0 | 0.55 |
| neighbor repulsion strength | 8 | 9.1 |
| neighbor repulsion range [m] | 0.10 | 0.13 |

The fit is within a few percent for flow, density and speed at all three calibration widths. Note the desired speed: it came out below the usual 1.2 m/s, and that is a genuine finding about the experiment rather than the model. In a crowd of 350 that has just been released from a waiting area, nobody walks at their free speed.

## Step 5 — does it hold on the widths it never saw?

{{< figure
    src="fig5.png"
    caption="Flow, density and speed against bottleneck width: experiment, default model and calibrated model. The dotted widths, 3.0 and 4.4 m, were not used in the calibration. Error bars are the spread over three random seeds."
>}}

It holds. On the two widths the optimizer never saw, the calibrated model is within 7 % in flow, 5 % in density and 8 % in speed, which is about the spread between seeds. The one visible miss is at 5.0 m, a calibration width: the measured flow jumps above the linear trend there and the model does not follow. Either the widest run is different in a way three scalar observables cannot see, or the model's flow really is linear in the width. That is a question for the model, and now a well-posed one.

The same table, in numbers:

| width [m] | flow exp / sim [1/s] | density exp / sim [1/m²] | speed exp / sim [m/s] |
|---|---|---|---|
| 2.4 | 6.1 / 6.1 | 5.6 / 5.6 | 0.32 / 0.30 |
| 3.0 (held out) | 7.2 / 7.7 | 5.1 / 5.0 | 0.37 / 0.40 |
| 3.6 | 9.0 / 9.0 | 4.8 / 4.7 | 0.44 / 0.45 |
| 4.4 (held out) | 10.9 / 11.2 | 4.0 / 4.2 | 0.55 / 0.55 |
| 5.0 | 13.8 / 12.7 | 4.1 / 3.9 | 0.63 / 0.59 |

## What we learned about the workflow

- **Analyse experiment and simulation with the same code.** PedPy loads both, so the observables are defined once.
- **Screen before you calibrate.** The Morris run costs 80 evaluations and removed two of seven parameters and a whole failing region of parameter space.
- **Do not use gradients on an agent-based model.** Surrogate-based optimization converged in 36 evaluations where the gradient solver never left the start.
- **Hold something back.** Calibrating on three widths and validating on two is the difference between a fit and a model.
- **Dakota's job is orchestration, not physics.** It knows nothing about pedestrians. It knows how to run a driver in parallel a few hundred times and what to make of the numbers that come back. That is exactly the part you do not want to write yourself.

## Why openness is the method here

Nothing in this study is ours to keep. The trajectories are on a public archive with a DOI and a geometry file attached. The model is open source and scriptable. The analysis library is the same one used on the experiment. The calibration toolkit has been maintained by a national laboratory for 25 years. The only thing we added is one driver script and three input files, and they are in the repository linked below.

That has consequences beyond convenience. Anyone can rerun the calibration with a different observable, a different model or a different experiment from the same archive and compare numbers with ours. Someone who thinks the linear flow at 5.0 m is a model deficiency can test it this afternoon. And a calibration that lives in a text file can be reviewed, which a sentence like "parameters were chosen according to the literature" never could. Open data and open software are often argued for on principle. This is the practical version of the argument: put together, they turn model calibration from a private craft into a shared, checkable result.

## Code and credits

Experiment: Seyfried et al., Hermes bottleneck experiment, Düsseldorf 2009, [doi:10.34735/ped.2009.6](https://doi.org/10.34735/ped.2009.6). Dakota: Adams et al., Sandia National Laboratories, version 6.24.

Code, Dakota input files and results: [github.com/PedestrianDynamics/jupedsim-dakota-calibration](https://github.com/PedestrianDynamics/jupedsim-dakota-calibration)

{{< icon "pencil-alt" >}} By: [Mohcine Chraibi]({{< relref "/authors#MohcineChraibi" >}})
