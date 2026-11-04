---
title: A column at the top of a stair
date: 2026-11-04
summary: At Copenhagen Airport a column stands right where people turn onto a stair. I rebuilt the spot in JuPedSim. In the simulations, the column pushes people towards the glass, makes them step onto the stair at an angle, and slows a crowd down.
thumbnail: fig2.mp4
---

{{< callout type="info" icon="none" >}}
**Abstract.** On the way to the train at Copenhagen Airport, I nearly walked into a glass balustrade at the top of a stair. The reason seemed to be a column standing exactly where you turn onto the first step. I rebuilt the spot in JuPedSim, with dimensions estimated from photos. In the simulations, the column leaves too little room to straighten up before the stair. People pass the end of the glass closely and step onto the stair at an angle, and both get worse when they hurry. In a crowd arriving from one side, the column becomes a bottleneck. When people keep right on the stair, people coming up get past it without trouble, unless they carry luggage and have to go round the column across the people coming down. These are simulation results for a reconstructed geometry, not observations of real people at this stair.
{{< /callout >}}

On my way to the train at Copenhagen Airport I nearly bumped into the glass. The stair is an open wooden one near the SAS area, and at its top, right where you turn onto the first step, stands a column. It blocks the view of the stair, and it seemed to get in the way of everyone walking past it. A column like that is probably there for a good structural reason. From a pedestrian dynamics point of view, though, it is in an unfortunate place. It almost felt as if the stair had been fitted around the column as an afterthought. I have no drawings, so that remains a guess.

So I asked a simpler question I can actually test: does a column in that position make the turn onto the stair harder?

## The stair

{{< figure src="fig1.png" caption="Top: the column at the top of the stair. Walking up to it (left), it hides the way down until you are next to it; from below (right) it stands right behind the top step. Bottom: the plan used in the simulations, with the way I walked in red. People come in from the right, turn around the end of the right glass, pass the column and turn again onto the stair." >}}

All dimensions are estimates from my photos, using the step depth as a scale. The stair is about 2 m wide between the glass walls. The column is about 0.5 m across and stands about 1 m back from the top step. Between the column and the right-hand glass there are only about 65 cm, so people go round the wide side, as I did.

I compared the stair as built with the same stair without the column. For each simulated person I measured two things near the top step:

- **the gap**: the closest distance between the person's body and any glass pane;
- **the angle**: how far their walking direction is off the stair direction when they step onto it.

## One person in a hurry

I started with people walking alone, using JuPedSim's social force model. In this model people have inertia: they need some time and space to change direction, as real people do.

{{< video
    src="fig2.mp4"
    caption="The same stair at a normal walking speed (left) and in a hurry (right). A person turns red when they come closer than 10 cm to the glass."
>}}

At a normal pace, people pass the end of the left glass about 15 cm away. Without the column, the gap is about 65 cm. When people hurry, the gap with the column shrinks to about 10 cm, while without the column it stays the same.

The angle tells the same story. With the column, people reach the first step still turning, at about 35° to the stair. Without it, they walk onto the stair almost straight. That is the moment I felt at the airport: you are still finishing the turn while your foot goes onto the step.

{{< figure src="fig3.png" caption="Gap to the glass (left) and angle onto the stair (right) against walking speed, for four layouts and, dashed grey, for a model without inertia. Moving the column 2 m back does not help; putting it against the right glass helps. Each point is the median over 160 simulated people." >}}

## Does it depend on the model?

Pedestrian models disagree in exactly this kind of detail, so I ran the same stair with two other JuPedSim models.

{{< figure src="fig4.png" caption="Top: people in a hurry with each model, stair as built. Bottom: gap and angle against walking speed for each model; solid lines with the column, dashed without. In the model without inertia, people without the column cut the corner and pass close to the right-hand glass instead, which explains its low dashed line on the left." >}}

WarpDriver, a model in which people anticipate collisions a few seconds ahead, also brings people closer to the glass and onto the stair at an angle. In this model, though, hurrying makes no difference: people plan the turn early, so they never overshoot it. The collision-free speed model, in which people turn instantly, shows almost no effect at all. That fits the explanation: the problem is overshooting a turn, and only a model with inertia can do that.

## When a plane unloads

Walking alone, the problem is the turn. In a crowd, nobody walks fast any more, and something else happens: the column narrows the top of the stair.

{{< video
    src="fig6.mp4"
    caption="80 people arriving at 1.5 per second, shown at twice the speed. With the column (left), a queue forms around it."
>}}

I let 120 people arrive from the right, as when a plane unloads. When they arrive slowly, one per second, the stair copes either way. When they arrive at two per second, all three models agree that the column slows things down. In the social force model, the last person reaches the bottom of the stair after about 100 s with the column and about 80 s without it. The models disagree on how much slower, but not on the direction.

{{< figure src="fig5.png" caption="Crowd results for the three models: the time until all 120 people are down, the flow onto the stair, and the median time each person needs from arrival to the bottom of the stair. Solid lines with the column, dashed without; five simulation runs per point." >}}

## When someone comes up

People on a stair do not take the shortest path: they keep to the right, going down as well as coming up. So for this test I gave everyone checkpoints along their right-hand side of the stair and around the end of the glass. People coming up then walk straight into the 65 cm gap between the column and the glass. I used the collision-free speed model and 20 people, a quarter or half of them coming up.

{{< video
    src="fig7.mp4"
    caption="Twenty people keeping right, half of them coming up (amber), in the collision-free speed model. People coming up pass through the narrow gap between the column and the glass."
>}}

Nobody got stuck, with or without the column, and the column did not cost any time. With everyone keeping right, the column even works as a divider between the two directions. The gap is narrow for a 50 cm wide body, but the model lets people pass it without slowing down.

My first try did not use lanes, and the social force model and WarpDriver got stuck at the gap in most runs. That was the models, not the stair: their simulated bodies cannot squeeze through, while real people turn sideways or wait.

## With luggage

This is an airport, though, and many people carry a bag or pull a suitcase. Someone with luggage will not aim for a 65 cm gap. They go round the column on its wide side, right across the people coming down.

A pedestrian model has no suitcases, so I made people with luggage wider (60 cm instead of 50 cm) and a bit slower (80 % of the normal speed). Half of the people carried luggage. People coming up with luggage kept right on the stair and then crossed over to pass the column on its left. Everybody else used the same lanes as before. I ran 40 people, half of them coming up, at up to two arrivals per second.

{{< video
    src="fig8.mp4"
    caption="Forty people, half coming up (amber), half with luggage (dot), shown at twice the speed. With the column (left), people coming up with luggage cross over at the top and a knot forms; without it (right), the two directions keep their lanes."
>}}

Without luggage, the column made no difference at any of these flows. With luggage, it did. At 1.5 to 2 arrivals per second, the last person was through after about 85 to 90 s with the column, against 60 to 70 s without it. People going down took about 70 % longer for the same stair, because they kept waiting for someone crossing in front of them.

{{< figure src="fig9.png" caption="Time until all 40 people are through, without luggage (left) and with half of them carrying luggage (right). Solid red with the column, dashed without; points are the median of 10 simulation runs, bars the middle half." >}}

## What this does not show

- **The geometry is a reconstruction.** All dimensions come from photos. I varied stair width, column size and position, and where the right glass ends. The column made things worse in every combination; only the numbers changed.
- **The route is mine.** I made the simulated people take the way I walked. People coming from behind the column or along the gallery on the left are affected less.
- **Visibility is not in the models.** The column also blocks the view of the stair. None of the models includes that, so that part of the irritation remains untested.
- **Counterflow depends on the model.** Without lanes, the collision-free speed model jams head-on even without the column. With keep-right lanes it shows no problem, while the social force model and WarpDriver still jam at the 65 cm gap.
- **Luggage is a wider circle.** A pulled suitcase makes a person longer, not wider, and that shape is not in the model. That people with luggage avoid the gap is my assumption, not something the model decides.
- **No real people were measured.** This is a simulation study of one stair, not an observation of how people actually use it.

Within these limits, the result is consistent. A column standing exactly where people turn onto a stair takes away the room they need to straighten up before the first step. The faster they walk, the more that matters, and in a crowd it costs flow. For people coming up, the column did not get in the way once everyone keeps right, until they carry luggage: then it pushes them across the people coming down. Small changes could help without touching the structure, for example a floor marking that leads people round earlier, or a handrail that starts before the turn. I have not tested those yet.

## Code and data

Code, simulation results and all assumptions: [github.com/PedestrianDynamics/copenhagen-stair](https://github.com/PedestrianDynamics/copenhagen-stair)

{{< icon "pencil-alt" >}} By: [Mohcine Chraibi]({{< relref "/authors#MohcineChraibi" >}})
