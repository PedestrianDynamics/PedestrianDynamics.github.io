---
title: Why do roaming crowds drift counterclockwise — and where?
date: 2026-06-29
summary: A Nature Communications paper reports that freely roaming crowds drift counterclockwise. We rebuilt the experiment in simulation to test whether a slight individual left-turn bias explains it.
math: true
aliases: [/blog/counterclockwise-crowds/]
thumbnail: fig1.mp4
---

{{< figure src="fig0.png" >}}

Recently a [paper in Nature Communications](https://www.nature.com/articles/s41467-026-73713-w) (Echeverría-Huart et al.) reports something simple and odd. If you put people in a circular arena and let them walk around freely, the crowd slowly drifts counterclockwise. The authors saw it in experiments in Spain and Japan, so it is not a fluke of one room or one group. Their explanation is that the drift does not come from people avoiding each other. It comes from each person, on their own, having a slight tendency to turn left. (The paper even made it into The New York Times.)

This sounds intriguing, so we explored it a bit further.

We used [JuPedSim](https://www.jupedsim.org/). It splits the problem into two parts. One part is how people avoid bumping into each other, which JuPedSim handles with a couple of operational models. The other part is where each person wants to go next, which is up to us. We give each agent a desired direction; JuPedSim returns motion without collisions. That split is convenient here. We drive each agent ourselves with direct steering: every step, we pick a heading and place the agent's target just ahead of it.

```python
sim = jps.Simulation(model=jps.SocialForceModel(), geometry=disk)
steering = sim.add_direct_steering_stage()
journey  = sim.add_journey(jps.JourneyDescription([steering]))
while sim.agent_count() > 0:
    for agent in sim.agents():
        heading = roam(agent, cfg)
        agent.target = ahead(agent.position, heading)
    sim.iterate()
```

The `for` loop is our little model. `sim.iterate()` is JuPedSim's machinery. Here is one agent following the target we hand it each step:

{{< video
    src="fig1.mp4"
    caption="One roaming agent (blue) and the target we set each step (red ring, dashed line). With a single agent there is nothing to avoid, so this shows only the steering loop."
>}}

The collision model is set on the first line, so we can later run the exact same behavior through different JuPedSim models. This also gives us a clean test of the paper's claim. The collision handling has no built-in left or right preference. So if a crowd with symmetric rules does not rotate, that supports the idea that the bias is individual. And if adding the bias makes the crowd rotate, that supports the proposed mechanism. We model a 5 m arena with agents roaming in random directions. We measure the same quantity as the paper: M, each person's velocity projected onto the counterclockwise direction, averaged over the crowd. M̄ > 0 means the crowd circulates counterclockwise.

## Symmetric avoidance does not rotate

With no bias, the crowd does not rotate. Across crowd sizes and random seeds, M̄ stays near zero. The collision model on its own picks no direction.

This observation is model agnostic. JuPedSim ships several collision models, some velocity-based and some force-based, and they work quite differently inside. So we ran the same no-bias case through four of them: Social Force, WarpDriver, Collision-Free Speed, and Anticipation Velocity. All four stay within a few hundredths of zero, far below the experimental value. No rotation comes out of symmetric avoidance, whatever model you use. It has to be added.

{{< video
    src="fig2.mp4"
    caption="One real experimental run next to the four model controls. The real crowd circulates counterclockwise; the bare models just mill around."
>}}

{{< figure
    src="fig3.png"
    caption="The no-bias case for four collision models, against the experimental M̄ (dashed line). All four sit near zero."
>}}

## Adding the bias

The paper's main claim is an always-on individual bias: a slight per-person tendency to turn left, present at every step, even when walking alone with no walls. The specific "turn left when facing a wall" rule comes from earlier work the authors build on, and is one concrete way that bias could show up. We tried both.

We first tried putting the bias in free-space curvature, a constant gentle left turn at every step, which is the closest simple stand-in for the always-on bias. On its own that did not give the confined rotation (more on why below). So we also tried the wall-only rule, and bingo, that reproduced the effect.

How strong the rotation gets depends on how many people have the bias. A single turn strength saturates, so the useful knob is the fraction of people who turn left, which also matches the paper's mixed population. With nobody biased the crowd does not rotate. With everybody biased it rotates strongly. With about a third of the crowd turning left, we get M̄ ≈ 0.2, the experimental value.

{{< figure
    src="fig4.png"
    caption="Mean polarization against the share of left-turners. Zero with no bias, rising with the fraction; about a third matches the experiment."
>}}

{{< figure
    src="fig5.png"
    caption="The distribution of M. The control sits on zero; adding left-turners shifts it counterclockwise, as in the paper."
>}}

{{< video
    src="fig6.mp4"
    caption="Three crowds side by side (0%, ~45%, 100% left-turners). The control mills without a net direction; more left-turners make the crowd circulate."
>}}

## Matching the number is not matching the mechanism

The paper's data let us go past the single number M̄. Their trajectory files include a per-agent polarization value, and recomputing it with our metric matches theirs exactly. So we can compare not just the average rotation but where in the arena it happens. This was the most useful test, because it can disagree with us instead of just confirming us. (Shout out to the authors for sharing their data on [Zenodo](https://zenodo.org/records/19592341)!)

The experiment shows a rotation that fills the disk. It is positive at every radius, weak at the center, strongest in the outer-middle, then easing right at the wall. We compared this against two simple models: the turn-left-at-wall rule above, and an "intrinsic" version where every agent has a small constant left veer at every step, which is closer to a bias that is present even away from walls.

Neither matches the experiment, and they fail in different ways. The wall-turn model gets the total amount of rotation right but puts it in the wrong place: a thin spike at the rim and an almost still interior, because the bias only acts at the wall. The intrinsic veer spreads rotation into the interior, closer to where the experiment peaks, but it comes out clockwise, the wrong sign. In open space a left veer does turn counterclockwise, and we checked that directly. But once the arena is closed, the way the veer meets the wall flips the net direction.

{{< figure
    src="fig7.png"
    caption="Local rotation against distance from the center, for the experiment and the two models. The experiment is positive throughout and peaks in the outer-middle; the wall-turn model spikes at the rim; the intrinsic veer goes negative."
>}}

{{< figure
    src="fig8.png"
    caption="The same three as spatial maps (blue counterclockwise, red clockwise). The experiment is mostly blue across the disk; the wall-turn model is a blue ring; the intrinsic veer is a red band."
>}}

We read this as support for the paper. It seems that matching one number with a single knob is easy. The spatial pattern of the real rotation does not fall out of either simple rule, so more work needs to be done on the model.

## What we learned, and what's open

We set out to test the mechanism behind a real effect, and we learned a few concrete things. Symmetric collision avoidance produces no preferred rotation. A turn-left-at-wall rule recovers counterclockwise motion at roughly the reported strength. And looking at where the rotation lives shows that matching the average is the easy part, while matching the spatial structure is far from being a trivial task.

There is more to do. The experiment also reports counterclockwise motion with no walls at all, and for people walking alone, which neither of our simple models covers. Reproducing the full spatial field will need a richer individual model than one knob. That leaves the real open question: with no wall to turn at and no crowd to follow, what makes a single person drift counterclockwise? The authors checked the obvious candidates — handedness, footedness, eye dominance — and ruled them all out, calling the cause an individual bias that is "most likely biologically rooted" and leaving the origin open. So this is a known open problem, worth further research.

A last thought about the tool. None of this is a simulator telling us the right answer, or even ruling out the wrong ones. It does not work that way, and no simulator does. But what it gave us was a cheap way to ask: what if avoidance is symmetric, what if a third of people turn left, what if the bias is at the wall instead of everywhere. Each one is a few lines in the `roam()` rule, run, and looked at. We did not find the mechanism here, but we did sharpen the question and make a couple of stories look more or less likely — and that is most of what a simulation is good for.

## Code and credits

Code, full-quality videos, and data: [github.com/PedestrianDynamics/clockwise](https://github.com/PedestrianDynamics/clockwise)

Credit for the phenomenon and the experiments goes to Iñaki Echeverría Huarte, Claudio Feliciani, Iker Zuriguel Ballaz and colleagues. There was a charming talk at TGF26 by Iker Zuriguel Ballaz — here is the [abstract](https://bpb-eu-w2.wpmucdn.com/blogs.bristol.ac.uk/dist/1/1202/files/2026/05/TGF26_abstract_11.pdf).

{{< icon "pencil-alt" >}} By: [Mohcine Chraibi]({{< relref "/authors#MohcineChraibi" >}})
