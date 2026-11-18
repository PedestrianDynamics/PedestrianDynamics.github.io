---
title: A column at the top of a stair
date: 2026-11-04
summary: At Copenhagen Airport a column stands right where people turn onto a stair. I rebuilt the spot in JuPedSim. In the simulations, the column pushes people towards the glass, makes them step onto the stair at an angle, and slows a crowd down.
thumbnail: fig2.mp4
---

{{< callout type="info" icon="none" >}}
**Abstract.** 
On my way to the train at Copenhagen Airport, I nearly bumped into the glass at the top of the stairs. A column stands right where you turn onto the first step. It blocks the view and, at least for me, made the turn awkward.
The column probably has a good structural reason to be there. Still, looking at the layout, I wondered whether someone had fitted the stairs around it as an afterthought. Or maybe I was just absent-minded.
On my way back from HBiF, I took some more photos and decided to rebuild the spot in JuPedSim. Would the simulations show anything resembling my awkward turn?
{{< /callout >}}

The main character of this study is a column near the SAS area in the Copenhagen airport. It blocks the view of the stair, and it seemed to get in the way of everyone walking past it. A column like that is there for a good structural reason, no doubt about that. From a pedestrian dynamics point of view, though, it is in an unfortunate place. Or maybe not?

I'm not really sure. On my way back from the HBiF, I thought maybe I should take some more photos and try to find out whether the column in that position makes the turn onto the stair harder.

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

With the column, people reach the first step still turning, at about 35° to the stair. Without it, they walk onto the stair almost straight. That is the moment I felt at the airport: you are still finishing the turn while your foot goes onto the step.

{{< figure src="fig3.png" caption="Gap to the glass (left) and angle onto the stair (right) against walking speed, for four layouts and, dashed grey, for a model without inertia. Moving the column 2 m back does not help; putting it against the right glass helps. Each point is the median over 160 simulated people." >}}

## Does it depend on the model?

Pedestrian models disagree in exactly this kind of detail, so I ran the same stair with two other JuPedSim models.

{{< figure src="fig4.png" caption="Top: people in a hurry with each model, stair as built. Bottom: gap and angle against walking speed for each model; solid lines with the column, dashed without. In the model without inertia, people without the column cut the corner and pass close to the right-hand glass instead, which explains its low dashed line on the left." >}}

WarpDriver, a model in which people anticipate collisions a few seconds ahead, also brings people closer to the glass and onto the stair at an angle. In this model, though, hurrying makes no difference: people plan the turn early, so they never overshoot it. The collision-free speed model, in which people turn instantly, shows almost no effect at all.
The models differ in both the turn itself and how it changes with speed. So the effect depends partly on how the model handles changes in walking direction.

## When a plane unloads

Walking alone, the problem is the turn. When more people arrive, there is less room to move, and the column also becomes a bottleneck.

{{< video
    src="fig6.mp4"
    caption="80 people arriving at 1.5 per second, shown at twice the speed. With the column (left), a queue forms around it."
>}}

I let 120 people arrive from the right, as when a plane unloads. When they arrive slowly, one per second, the stair copes either way. When they arrive at two per second, all three models agree that the column slows things down. In the social force model, the last person reaches the bottom of the stair after about 100 s with the column and about 80 s without it. The models disagree on how much slower, but not on the direction.

{{< figure src="fig5.png" caption="Crowd results for the three models: the time until all 120 people are down, the flow onto the stair, and the median time each person needs from arrival to the bottom of the stair. Solid lines with the column, dashed without; five simulation runs per point." >}}

## When someone comes up

For this test, I assumed that people would keep right, both going up and coming down.
So for this test I assigned agents checkpoints along their right-hand side of the stair and around the end of the glass. Agents coming up then walk straight into the narrow gap between the column and the glass. I used the collision-free speed model and 20 agents, a quarter or half of them coming up.

{{< video
    src="fig7.mp4"
    caption="Twenty people keeping right, half of them coming up (amber), in the collision-free speed model. People coming up pass through the narrow gap between the column and the glass."
>}}

Nobody got stuck, with or without the column, and the column did not cost any time. With everyone keeping right, the column even works as a divider between the two directions. The gap is narrow for a 50 cm wide body, but the model lets people pass it without slowing down.

My first try did not use lanes, and the social force model and WarpDriver got stuck at the gap in most runs. 
I would not interpret these jams as evidence that people would get stuck there. The models cannot represent someone turning sideways to pass.

## With luggage

This is an airport, though, and many people carry a bag or pull a suitcase. 
For this test, I assumed that people with luggage would avoid the narrow gap and go round the column on its wide side, right across the people coming down.

The model I used does not explicitly represent suitcases, so I made agents with luggage wider (60 cm instead of 50 cm) and a bit slower (80 % of the normal speed). Agents coming up with luggage kept right on the stair and then crossed over to pass the column on its left. Everybody else used the same lanes as before. I ran 40 people, half of them coming up, at up to two arrivals per second.

{{< video
    src="fig8.mp4"
    caption="Forty people, half coming up (amber), half with luggage (dot), shown at twice the speed. With the column (left), people coming up with luggage cross over at the top and a knot forms; without it (right), the two directions keep their lanes."
>}}

Without luggage, the column made no difference at any of these flows. With luggage, it did. At 1.5 to 2 arrivals per second, the last person was through after about 85 to 90 s with the column, against 60 to 70 s without it. People going down took about 70 % longer for the same stair, because they kept waiting for someone crossing in front of them.

{{< figure src="fig9.png" caption="Time until all 40 people are through, without luggage (left) and with half of them carrying luggage (right). Solid red with the column, dashed without; points are the median of 10 simulation runs, bars the middle half." >}}

## Limitations

I reconstructed the stairs from my photos, so all the dimensions are estimates. I varied the width of the stairs, the size and position of the column, and where the glass panel on the right ends. For the route I walked, the column made the turn more awkward in every layout I tested, although the size of the effect varied. The approach matters, too. In the simulations, the column had less effect on people coming from behind it or along the gallery on the left. What bothered me at the airport was also how the column blocked my view of the stairs. None of the models accounts for that.

When people walked in both directions, the result depended on the model and on whether agents were to keep right. Without lanes, people in the collision-free speed model got stuck facing each other even when I removed the column. When I gave them routes that kept them on the right, they passed through the 65 cm gap without difficulty. With the same routes, people in the social force model and WarpDriver still got stuck at the gap.

For the luggage runs, I represented a traveller with a suitcase as a wider circle. A suitcase pulled behind you takes up space mostly behind you. I also chose the route around the column for people coming up with luggage, so their decision to avoid the gap was part of the setup. I took no measurements of how travellers actually use these stairs. I’d be curious to see which way someone pulling a suitcase goes when they reach that gap.

The simulations give me some reason to think the column's placement is awkward. How much it matters depends on the model and on the routes I gave agents in the simulation. I would still like to see how travellers actually use this spot, especially with luggage.

Could a floor marking or an earlier handrail help people start the turn sooner? 


## Code and data

Code, simulation results and all assumptions: [github.com/PedestrianDynamics/copenhagen-stair](https://github.com/PedestrianDynamics/copenhagen-stair)

{{< icon "pencil-alt" >}} By: [Mohcine Chraibi]({{< relref "/authors#MohcineChraibi" >}})
