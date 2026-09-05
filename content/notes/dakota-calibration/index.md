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

{{< figure
    src="exp1.jpg"
    caption="The Hermes bottleneck experiment, Düsseldorf 2009: overhead view of a run, and the setup sketch with the semicircular holding zones at 3 persons per square metre. Images: Pedestrian Dynamics Data Archive, Forschungszentrum Jülich."
>}}

The [Hermes bottleneck experiment](https://ped.fz-juelich.de/db/doku.php?id=hermes_bottleneck) was run in May 2009 in Hall 2 of the Düsseldorf fairground with about 350 participants (Seyfried et al. 2009; Liao et al. 2014). The bottleneck was built from boards higher than two metres, 1 m long, and its width was varied from 2.4 to 5.0 m in five runs. Participants waited in a semicircular holding area of radius 8.6 m directly in front of the bottleneck, which puts the initial density at three persons per square metre, and walked through on command. The free walking speed of 42 participants was measured separately: 1.55 m/s with a spread of 0.18 m/s.

The trajectories are open data with a DOI. Since 2024 they come as HDF5 files that carry a geometry along, so PedPy loads both with one call each. One caveat, found only by reading the paper next to the file: the polygon in the archive is a 12 m box around the camera window with the wall blocks cut off at its edges, and three of its five gaps are 0.1 m narrower than the run's stated width. The simulation therefore takes the gap width from the run parameter and the corridor and holding area from the paper. A corrected polygon for each run is in the repository.

```python
import pedpy, pathlib
f = pathlib.Path("ao-360-400.h5")
traj = pedpy.load_trajectory_from_ped_data_archive_hdf5(f)
area = pedpy.load_walkable_area_from_ped_data_archive_hdf5(f)
```

We measure three things per run: the flow through the bottleneck, from the slope of the N(t) curve at a line across the gap; and the density and mean speed in a 2.8 by 2 m area directly in front of it, averaged over the jam phase. The area is the same for all widths, so it covers more than the 2.4 m opening and only the middle of the 5.0 m one. These are local measurements of the crowd state upstream of the gap, not averages over the whole opening, and the calibration compares them like for like. The same three functions are applied to the simulated trajectories. Seyfried and Schadschneider's warning about measurement methods is answered the simplest way: there is only one method, applied to both sides.

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

This is not a surprise if you know the model. In the Collision Free Speed model the time gap sets the headway an agent keeps to the one in front, and the radius sets how close agents can pack side by side; together with the neighbor repulsion they fix the throughput of a jammed opening, and the desired speed hardly enters once the crowd is jammed. With the defaults, one second of headway and a 0.2 m radius, the model delivers a third to a half of the measured flow. No amount of tweaking the desired speed fixes that. The question is which of the seven parameters do, and by how much.

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

The first stage is a Morris screening: 80 evaluations, each one a short walk through parameter space changing one parameter at a time. It is cheap and it ranks the parameters per observable. It is a ranking, not a measurement: with ten trajectories the estimates are coarse, and any ranking of this kind is conditional on the ranges it was sampled over.

{{< figure
    src="fig3.png"
    caption="Morris screening over the full parameter ranges. Each cell is the mean absolute elementary effect of a parameter on an observable, scaled to the strongest parameter in that column. An elementary effect is one step of one parameter along a Morris trajectory; steps where either end of the pair failed were discarded, so the count n per row is the number of valid steps that survived, between four and seven of the ten drawn. The time gap, the radius and the neighbor repulsion range dominate; the desired speed has a moderate effect on flow and speed; the two wall parameters are weakest."
>}}

The screening also revealed something no fit would have: in 28 of the 80 evaluations the model pushed agents through the walls and JuPedSim aborted the run. Those combinations have strong, long-range neighbor repulsion and weak wall repulsion. We narrowed the bounds accordingly and froze the wall parameters at their defaults. Knowing where a model breaks is part of validating it.

With five parameters left, and narrower ranges, a Sobol analysis with 280 evaluations gives the variance decomposition. Dakota computes the indices itself; the only change to the input file is one keyword, `variance_based_decomp`. Because the ranges and the fixed parameters changed between the two stages, the two rankings are not expected to coincide exactly; sensitivity is always relative to the ranges assumed.

{{< figure
    src="fig4.png"
    caption="Sobol indices for the five remaining parameters, 280 evaluations, none failed. The time gap has the largest first-order contribution to flow and, together with the neighbor repulsion range, to speed; the radius and the neighbor repulsion range dominate the density. The desired speed contributes a total index of 0.13 to 0.19 to the speed, small but not negligible. With 40 base samples the estimator is coarse: several first-order indices exceed their totals by 0.1, which is impossible for exact indices, so these are preliminary estimates. The broad ranking is what we use, not the decimals."
>}}

## Step 4 — calibration, and why we did not use gradients

Our first attempt at calibration, on a simpler two-room test case before touching the experiment, used a classic gradient-based least-squares solver. It stalled at the starting point. Two simulations whose parameters differ in the sixth digit produce evacuation times that differ by seconds, because the dynamics of a few hundred interacting agents are chaotic. Finite-difference gradients of such a function are noise, and we did not try them again.

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

After 42 evaluations, about twenty minutes on a laptop, the optimizer converged with all nine residuals below one standard deviation of the assumed uncertainty. And the desired speed had gone to the lower bound of its range, 0.8 m/s, half the free speed measured on the participants.

This is the moment where a fit and a validation part ways. The Sobol analysis had already said that the desired speed is a minor influence on the jam observables, so the misfit is flat along it and the optimizer was free to put it wherever the residuals were a hair smaller. A model with participants walking at 0.8 m/s reproduces the bottleneck. It does not reproduce the participants. Sargent calls this data validity: parameters that were measured are data, not fitting variables. Liao et al. (2014) made the same move for FDS+Evac. So we fixed the desired speed at the measured 1.55 m/s and calibrated the remaining four parameters. That converged in 24 evaluations.

| parameter | default | all five free | speed fixed, set A | speed fixed, set B |
|---|---|---|---|---|
| desired speed [m/s] | 1.2 | 0.80 (at bound) | 1.55 (measured) | 1.55 (measured) |
| radius [m] | 0.20 | 0.14 | 0.13 | 0.15 |
| time gap [s] | 1.0 | 0.56 | 0.81 | 0.55 |
| neighbor repulsion strength | 8 | 6.1 | 2.1 | 9.4 |
| neighbor repulsion range [m] | 0.10 | 0.15 | 0.25 | 0.10 |
| weighted residual norm | | | 2.0 | 2.3 |

Set B is the reason for the last column. Because a surrogate-based optimizer with a few dozen evaluations can settle in one basin of a flat landscape, we repeated the fixed-speed calibration from a different optimizer seed. It converged, in 23 evaluations, on a different parameter set: a short time gap with strong, short-range repulsion instead of a long gap with weak, long-range repulsion. Its misfit is 2.3 against 2.0 in units of the assumed uncertainty, a difference well below what the seed-to-seed noise of the simulation can resolve. The first run had visited the same basin on its way and rated it 2.9. So there are at least two calibrated parameter sets for this experiment, and the data cannot choose between them.

All these sets fit the three calibration widths to within about ten percent. They are nowhere near each other. Time gap, repulsion strength and range shift by factors of two to four between them. Three observables at three widths do not pin five parameters, and a good fit says nothing about whether the parameters mean what their names say. Fixing the one parameter that was measured removes the freedom to be wrong in that direction; it does not remove the valley the others live in.

## Step 5 — does it hold on the widths it never saw?

{{< figure
    src="fig5.png"
    caption="Flow, density and speed against bottleneck width: experiment with the acceptance band (6 % on flow, 10 % on density and speed, the uncertainty assumed in the calibration weights), default model, and the two calibrated sets with the desired speed fixed. Error bars are the minimum and maximum over six simulation seeds; the experiment is one run per width. The dotted widths, 3.0 and 4.4 m, were not used in the calibration."
>}}

With the desired speed fixed, both calibrated sets improve every observable substantially, at the held-out widths too, and the figure shows the acceptance band we set, 6 % on flow and 10 % on density and speed. It also shows where the model leaves it, and this is where the two sets part ways. Set A follows the measured increase of speed with width up to 3.6 m and then flattens, ending 12 % low at 4.4 m and 17 % low at 5.0 m, while it keeps the density inside the band. Set B keeps the speed inside the band at every width and instead lets the density fall 10 % short at 5.0 m. Both overshoot the flow by 10 to 13 % at 3.0 m and undershoot it by 10 % at 5.0 m. The flow at the widest opening, where the measured value jumps above the linear trend, is missed by both, and neither set reaches it with the right density and speed at once: one gets there with too many slow agents, the other with too few fast ones. That is a milder version of what Liao et al. (2014) saw in FDS+Evac, and because it holds for both ends of the identifiability valley, it is a property of the model in this regime rather than of a parameter choice.

Deviation of the simulation from the experiment, mean over six seeds, with the band at 6 % for flow and 10 % for density and speed:

| width [m] | flow A / B | density A / B | speed A / B |
|---|---|---|---|
| 2.4 | +3 % / +5 % | +7 % / +1 % | −6 % / −5 % |
| 3.0 (held out) | +10 % / +13 % | +2 % / −3 % | +5 % / +9 % |
| 3.6 | +3 % / +4 % | 0 % / −6 % | −3 % / +4 % |
| 4.4 (held out) | +2 % / +4 % | +8 % / −1 % | −12 % / +1 % |
| 5.0 | −11 % / −10 % | −1 % / −10 % | −17 % / −4 % |

The seed-to-seed standard deviation is 2 to 4 % for flow and density and 3 to 6 % for speed, so the differences between A and B at the wide openings are real.

So the honest summary of Step 5 is: a substantial improvement over the defaults, most points inside the band for either set, and at the widest opening a shortfall that the calibration can move between speed and density but not remove. Whether that passes depends on the purpose, which is exactly why the purpose has to be stated first.

## Step 6 — a second experiment, and where the model stops

{{< figure
    src="exp2.jpg"
    caption="The CrowdQueue experiment, Wuppertal 2018: a run in the 5.6 m corridor seen from above, and the setup with the 0.5 m gate at the origin. Images: Pedestrian Dynamics Data Archive, Forschungszentrum Jülich."
>}}

A calibration is only validated within the domain it was tested in. To find the edge of that domain we took a second open dataset, the [CrowdQueue experiment](https://ped.fz-juelich.de/db/doku.php?id=crowdqueue) from Wuppertal 2018 (Adrian et al. 2020): a crowd in front of an entrance again, but through a 0.5 m gate instead of a 2.4 to 5 m opening, in corridors from 1.2 to 5.6 m wide. The archive files carry the full geometry and everyone's starting position, so each simulation starts from the measured first frame of its run.

Each run is simulated three times and every seed is shown, because averages hide the thing that matters here. A seed counts as emptied if everyone has passed the gate within 120 s, twice the longest experiment; otherwise it counts as clogged, and its flow is the number who passed divided by the run time. No seed in this figure aborted.

The transfer test comes first: the Hermes parameters applied to the 21 usable runs without refitting. With set A, 8 of 63 seeds emptied; the rest clogged at the funnel, most of them after a handful of people, some after most of the crowd. The weak, long-range neighbor repulsion that fits a wide bottleneck lets round agents form stable arches in a half-metre gap. Set B, with its strong short-range repulsion, does somewhat better, 19 of 63 seeds, and where it flows it overshoots the measured gate flow by 20 to 30 %. Neither Hermes optimum transfers. Recalibrating on the baseline runs, with the wall parameters free because the 1.2 m corridors exercise them, helps but does not cure it: 22 of 63 seeds empty, the gate flow of the emptied and late-clogging seeds sits near 1.1 persons per second, and in the narrow corridors the outcome of a run still depends on the seed. A second optimizer seed found a different parameter set here too, with strong short-range repulsion and default-like wall parameters, at the same misfit, and it behaves the same way: 22 of 63 seeds empty. The radius went to its lower bound in both, the optimizer's way of pushing round agents through an opening that people pass by turning their shoulders.

The low-motivation runs make the central point of this note in one row of the figure. Take the first of them, the 1.2 m corridor with 24 people: the calibrated model matches the measured flow, 1.1 against 1.06 persons per second, and at the same time has the corridor 60 % denser than measured, 2.9 against 1.8 per square metre, with people moving at half the measured speed, 0.28 against 0.51 m/s. The flow is right because the upstream state is wrong in two ways that cancel. A validation on flow alone would have passed this run.

{{< figure
    src="fig6.png"
    caption="CrowdQueue: experiment (bars) against the Hermes parameters, set A (blue), the model recalibrated on CrowdQueue (orange) and the joint calibration (green), one marker per seed, columns ordered by corridor width with the run number; asterisks mark the runs used in the calibration. Filled markers: the run emptied within 120 s; open markers: it clogged and the flow is what passed over the run. Top: baseline motivation, bottom: low motivation."
>}}

The one high-motivation run, 11 people through the 1.2 m corridor at 2.1 persons per second, is not in the figure because it needs its own: a sweep of the time gap with everything else fixed.

{{< figure
    src="fig8.png"
    caption="The high-motivation run: flow, density and speed in the corridor against the time gap, all other parameters at the CrowdQueue calibration, three seeds per point, from the one-dimensional Dakota sweep. Grey band: the measured value with its assumed uncertainty. Only a time gap below 0.3 s reaches the measured flow, and there the density is five times and the speed four times the measured values."
>}}

That is the domain boundary in numbers: this model, calibrated this way, is valid within its acceptance band for wide bottlenecks in a dense crowd, and not for single-file passage through a narrow gate, where the outcome of a run depends on the seed and the parameters cannot fix that. Our reading is that the circular body and the arching it produces are the limiting factors; that is a hypothesis the figures are consistent with, not something they prove.

## Step 7 — a third experiment, without barriers

{{< figure
    src="exp3.jpg"
    caption="The BaSiGo entrance experiment, Düsseldorf 2013: the crowd in front of the unguided entrance, top right. Image: Pedestrian Dynamics Data Archive, Forschungszentrum Jülich."
>}}

The last test uses the [BaSiGo entrance experiment](https://ped.fz-juelich.de/da/doku.php?id=entrance_semicircle) from 2013 (Sieben et al. 2017): an entrance with two half-metre lanes and no guiding barriers, 319 people told that their favourite artist is playing and they want to be first in, 273 of them tracked. Nothing was fitted to it. The crowd shape is entirely the model's own doing, which makes it the kind of validation Liao et al. (2017) asked for, a spatial profile rather than a number. People enter the camera view during the run, so the simulation injects each of the 273 tracked agents at the time and place where the data first see them, and everything after that is the model.

{{< figure
    src="fig7.png"
    caption="Time-averaged density in front of the entrance, 20 to 110 s into the run, on a 0.5 m grid: the experiment and each simulation seed separately, with its entrance flow and the number of people who passed. Grey: the entrance barriers. The CrowdQueue parameters are missing because every seed pushed an agent through the wall."
>}}

The maps are averaged over time only, 20 to 110 s into the run, and each seed is shown on its own. White is zero density; the maps stop at the edge of the grid, which is the tracked area. The Hermes parameters produce a semicircle, but the wrong one. Its density is concentrated at the entrance and falls off regularly, with peaks around 6 per square metre; the measured crowd is dense to 10 per square metre over a region that extends two to three metres upstream and is visibly asymmetric, heavier to the left of the entrance. And the model drains the crowd at 1.3 persons per second where the people, pushing to be first, achieved 0.6. The CrowdQueue parameters, with their weak wall repulsion, fail outright: in every seed the crowd pushes an agent through the entrance wall and the simulation stops. The joint parameters do not land in one place: two seeds drain the crowd at 1.1 to 1.4 persons per second and the third clogs after 63 people, with a density peak of 15 at the gate. What the model lacks is a hypothesis, not a finding of this figure: we suspect the pressure of a crowd that wants to be first, and the shoulder rotation that gets real people through half a metre, but the maps only show that the shape, the extent and the flow are all wrong.

## What changed between the calibrations, and what it means for simulations

The parameter sets found along the way, all with the desired speed fixed at the measured 1.55 m/s except the first calibration:

| parameter | default | Step 4, all free | Step 4, set A | Step 4, set B | Step 6, CrowdQueue (two seeds) | Step 7, joint |
|---|---|---|---|---|---|---|
| desired speed [m/s] | 1.2 | 0.80 (at bound) | 1.55 | 1.55 | 1.55 | 1.55 |
| radius [m] | 0.20 | 0.14 | 0.13 | 0.15 | 0.10 (at bound) / 0.11 | 0.11 |
| time gap [s] | 1.0 | 0.56 | 0.81 | 0.55 | 0.96 / 0.90 | 0.81 |
| neighbor repulsion strength | 8 | 6.1 | 2.1 | 9.4 | 1.7 / 7.9 | 2.5 |
| neighbor repulsion range [m] | 0.10 | 0.15 | 0.25 | 0.10 | 0.34 / 0.10 | 0.28 |
| wall repulsion strength | 5 | 5 (fixed) | 5 (fixed) | 5 (fixed) | 1.4 / 5.1 | 4.4 |
| wall repulsion range [m] | 0.02 | 0.02 (fixed) | 0.02 (fixed) | 0.02 (fixed) | 0.11 / 0.04 | 0.07 |
| fitted to | | Hermes 2.4, 3.6, 5.0 m | Hermes 2.4, 3.6, 5.0 m | Hermes 2.4, 3.6, 5.0 m | CrowdQueue h0, 1.2, 3.4, 5.6 m | both |

Where two values are given, two optimizer seeds converged on different parameter sets with the same misfit.

It is worth being plain about what happened to the "calibrated model" over the course of this note. After Hermes we had two parameter sets, not one, that reproduced flow, density and speed at five bottleneck widths, two of them unseen, mostly within ten percent, and that disagreed with each other on what the model gets wrong at the widest opening. That set clogged at a half-metre gate in 55 of 63 CrowdQueue seeds. The set calibrated on CrowdQueue reached the gate flow in wide corridors, stalled in narrow ones, could not reproduce a motivated crowd, and pushed agents through walls at the unguided entrance. The joint calibration on Hermes and CrowdQueue together, the single best compromise Dakota could find, overshoots the Hermes flow by 15 to 25 % at four of five widths, clogs in 30 of 63 CrowdQueue seeds, and is bimodal at the entrance. There is no parameter set for this model that covers both regimes; the compromise is worse than either specialist in its own regime. The one parameter that was actually measured, the free speed, was the one the optimizer most wanted to change.

None of this is a verdict on the Collision Free Speed model in particular. It is what validation looks like when it is done across regimes instead of within one, and the same pattern would appear for any pedestrian model with a handful of scalar parameters and round agents. The practical consequences, for anyone who runs pedestrian simulations for a living:

- **A calibration is a statement about a regime, not about a model.** Parameters fitted to wide bottlenecks are parameters for wide bottlenecks. Using them for a turnstile, a narrow door or an unguided entrance is an extrapolation, and this note shows how far it can be off: not by percent, but by clogging or not clogging.
- **Report the domain with the parameters.** A parameter set in a paper or a project file should come with the experiments it was fitted to and the ones it was tested on. Without that, "calibrated" is not information.
- **Some behaviour is not a parameter.** Motivation changed the measured flow through the same gate by a factor of two. No value of the time gap reproduces that without breaking density and speed. A model that treats a pushing crowd as a faster orderly one will be wrong in exactly the situations that matter for safety.
- **Measured quantities beat fitted ones.** Fixing the free speed at its measured value cost a little fit quality and bought a parameter set that means what it says. The fit had been buying its accuracy with an unphysical value.
- **Run the optimizer twice.** One calibration gives one point in a valley. A second run from another seed, twenty minutes here, showed that the valley has two ends with different physics and the same misfit. Any parameter set reported without that check is a sample, not a result.
- **Failure modes are results.** A third of the screening runs pushed agents through walls. That region of parameter space is where the model breaks, and it is worth knowing before an engineer lands in it by hand.
- **The tooling is the cheap part.** Every calibration and every test here is a text file and a driver script. What is expensive is the honesty of running the test that might fail. Open data makes that test available to everyone, which is the strongest argument for it.

## What we learned about validating

- **State the purpose, then pick the observables.** Flow alone would have passed a model with the wrong density, as it did in 2014. Three observables, one per mechanism, is the minimum.
- **Analyse experiment and simulation with the same code.** The measurement method is part of the result. PedPy loads both, so the observables are defined once.
- **Screen before you calibrate.** The Morris run costs 80 evaluations, removed two of seven parameters, and mapped a whole region where the model fails outright.
- **Do not use gradients on an agent-based model.** Surrogate-based optimization converged in a few dozen evaluations where the gradient solver never left the start.
- **Hold something back, then change the experiment.** Calibrating on three widths and validating on two is the difference between a fit and a validated model. A second experiment in a different regime is what finds the domain boundary, and here it found it within an afternoon.
- **Dakota's job is orchestration, not physics.** It knows nothing about pedestrians. It knows how to run a driver in parallel a few hundred times and what to make of the numbers that come back. That is the part you do not want to write yourself, and the part that makes the procedure repeatable.

## A note on open-source software

Sargent drew the cost of validation against the confidence it buys as a curve that rises steeply near the end. Everything in this study is about pushing that curve down. The trajectories are on a public archive with a DOI and the geometry attached. The model is open source and scriptable. The analysis library is the same one used on the experiment. The calibration toolkit has been maintained by a national laboratory for 25 years. The only thing we added is one driver script and three input files, and they are in the repository linked below.

That has consequences beyond convenience. Anyone can rerun the calibration with a different observable, a different model or a different experiment from the same archive and compare numbers with ours. Someone who thinks a remaining discrepancy is a model deficiency can test it this afternoon. And a validation that lives in a text file can be reviewed, which a sentence like "parameters were chosen according to the literature" never could. Open data and open software are often argued for on principle. This is the practical version of the argument: put together, they turn validation from a private craft into a shared, checkable result.

## References

- Adrian, J., Seyfried, A., Sieben, A. (2020). Crowds in front of bottlenecks at entrances from the perspective of physics and social psychology. Journal of the Royal Society Interface 17, 20190871. [doi:10.1098/rsif.2019.0871](https://doi.org/10.1098/rsif.2019.0871).
- Kurtc, V., Chraibi, M., Tordeux, A. (2018). Automated quality assessment of space-continuous models for pedestrian dynamics. [arXiv:1809.01862](https://arxiv.org/abs/1809.01862).
- Liao, W., Chraibi, M., Seyfried, A., Zhang, J., Zheng, X., Zhao, Y. (2014). Validation of FDS+Evac for pedestrian simulations in wide bottlenecks. IEEE ITSC 2014, 554–559. [doi:10.1109/ITSC.2014.6957748](https://doi.org/10.1109/ITSC.2014.6957748).
- Liao, W., Zhang, J., Zheng, X., Zhao, Y. (2017). A generalized validation procedure for pedestrian models. Simulation Modelling Practice and Theory 77, 20–31. [doi:10.1016/j.simpat.2017.05.002](https://doi.org/10.1016/j.simpat.2017.05.002).
- Oh, H., Lyu, J., Yoon, S., Park, J. (2014). Validation of evacuation dynamics in bottleneck with various exit angles. Transportation Research Procedia 2, 752–759.
- Ronchi, E., Kuligowski, E. D., Reneke, P. A., Peacock, R. D., Nilsson, D. (2013). The process of verification and validation of building fire evacuation models. NIST Technical Note 1822.
- Sargent, R. G. (1984). Simulation model validation. In: Simulation and Model-Based Methodologies: An Integrative View, Springer, 537–555.
- Sargent, R. G. (2008). Verification and validation of simulation models. Proceedings of the Winter Simulation Conference, 157–169.
- Sieben, A., Schumann, J., Seyfried, A. (2017). Collective phenomena in crowds — where pedestrian dynamics need social psychology. PLOS ONE 12(6), e0177328. [doi:10.1371/journal.pone.0177328](https://doi.org/10.1371/journal.pone.0177328).
- Seyfried, A., Schadschneider, A. (2008). Fundamental diagram and validation of crowd models. ACRI 2008, LNCS 5191, 563–566.
- Seyfried, A., Passon, O., Steffen, B., Boltes, M., Rupprecht, T., Klingsch, W. (2009). New insights into pedestrian flow through bottlenecks. Transportation Science 43, 395–406.
- Tordeux, A., Chraibi, M., Seyfried, A. (2016). Collision-free speed model for pedestrian dynamics. Traffic and Granular Flow '15, 225–232.
- Experiment data: Hermes bottleneck experiment, Düsseldorf 2009, [doi:10.34735/ped.2009.6](https://doi.org/10.34735/ped.2009.6); CrowdQueue experiment, Wuppertal 2018, [doi:10.34735/ped.2018.1](https://doi.org/10.34735/ped.2018.1); BaSiGo entrance experiment, Düsseldorf 2013, [doi:10.34735/ped.2013.2](https://doi.org/10.34735/ped.2013.2). Dakota: Adams et al., Sandia National Laboratories, version 6.24.

## Code

Driver scripts, Dakota input files, results and figures for every step: [github.com/PedestrianDynamics/jupedsim-dakota-calibration](https://github.com/PedestrianDynamics/jupedsim-dakota-calibration)

Software used in this study:

- [Dakota](https://dakota.sandia.gov) 6.24
- [JuPedSim](https://jupedsim.org) 1.4.2
- [PedPy](https://pedpy.readthedocs.io) 1.4.0

{{< icon "pencil-alt" >}} By: [Mohcine Chraibi]({{< relref "/authors#MohcineChraibi" >}})
