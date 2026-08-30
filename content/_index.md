---
title: Pedestrian Dynamics
toc: true
cascade:
  type: docs
---

## Basic questions and applications

Pedestrian dynamics studies how people move in crowds. Crowd flow shows
emergent behavior on many length and time scales, and physics provides useful
tools to describe and model it. The composition of the crowd matters as well:
who is walking, with whom, and for what purpose all influence how a crowd
moves.

{{< figure
    src="images/crowd.webp"
    caption="Image design: Panar Ege Uesten."
>}}

The field matters to scientists and practitioners alike because it addresses
three concerns of everyday life: efficient **transport systems**, **safety**,
and **comfort**.

### Transportation Improvement

Train stations and airports work well when people can move through them
easily. As cities grow, understanding how pedestrians behave in such
facilities becomes essential for designing transportation systems that
function. Quantities such as the flow through a bottleneck or the number of
people a facility can evacuate per hour help planners reduce congestion and
support sustainable urban mobility. A basic tool here is the fundamental
diagram, which relates density, speed, and flow. A good reference on this
topic is [75 Years of the Fundamental Diagram for Traffic Flow Theory:
Greenshields Symposium](https://www.trb.org/Publications/Blurbs/165625.aspx),
covering the history, developments, and practical applications of traffic flow
theory.

{{<
    figure
    src="images/fd.png"
    caption="The fundamental diagram describes the relationship of flow and density and helps to understand the formation of congestions."
>}}

Further reading on the fundamental diagram is found in this dissertation:
[Pedestrian fundamental diagrams: Comparative analysis of experiments in
different geometries](https://juser.fz-juelich.de/record/128157)

Pedestrian dynamics also applies to large events. The arrival and departure of
thousands of visitors happens in stages, each with its own behavior, such as
waiting in queues. Knowing how pedestrians queue, and how long queues take to
clear, helps organizers keep crowds moving.

{{<
    figure
    src="images/queue.jpg"
    caption="[Photo](https://unsplash.com/photos/aerial-photography-of-people-Nzb4LBsctyQ) by [Hal Gatewood](https://unsplash.com/@halacious) on [Unsplash](https://unsplash.com)"
>}}

### Safety and Comfort

Analyzing pedestrian movement helps identify bottlenecks, hazardous areas, and
workable evacuation strategies, so that crowds stay safe in emergencies. The
same analysis improves comfort: public spaces with smooth pedestrian flow are
more pleasant to use.

How safe people *feel* in a crowd is a research topic of its own. Perceived
safety is subjective, so researchers develop tools and methods to measure it
as objectively as possible and to capture how crowd members actually
experience a situation.

{{<
    figure
    src="images/crowd_station.jpg"
    caption="[Photo](https://unsplash.com/photos/people-standing-and-walking-on-stairs-in-mall-mVhd5QVlDWw) by [Anna Dziubinska](https://unsplash.com/@annadziubinska) on [Unsplash](https://unsplash.com/)"
>}}

## Collective phenomena

Collective phenomena emerge when many individuals interact. A central question
in pedestrian dynamics is how individuals form a crowd. Answering it involves
social interactions, behavior, emotions, and culture, and the answer differs
between social groups.

Typical collective phenomena in pedestrian crowds include:

- **Lane Formation**: In bidirectional streams, pedestrians spontaneously form
  lanes, which reduces friction between the opposing directions.

{{<
    video
    src="images/lane-formation.mp4"
    caption="Spontaneous emergence of lane formation in a bi-directional flow"
>}}

- **Clogging at Bottlenecks**: Near a narrow passage, several people (or
  particles) can form an arch that jams the opening and reduces, or even
  stops, the flow.

{{<
    figure
    src="images/clogging.webp"
    caption="Clogging in a bottleneck"
>}}

- **Stop-and-Go Waves**: In congested crowds, as in vehicle traffic, people
  alternate between moving and standing, and these fluctuations travel through
  the crowd as waves.

{{<
    video
    src="images/stop-go.mp4"
    caption="Emergence of stop-and-go waves in a system with closed boundary conditions"
>}}

Understanding these phenomena is the basis for crowd management, whether at a
football match, a music festival, or a train station.

For further reading see this
[review](https://link.springer.com/article/10.1007/s10489-023-04924-7) on
collective behavior modeling and simulation: building a link between cognitive
psychology and physical action.

## Interactions and relationships: From individuals to groups, from communities to cities

The key to understanding the different forms of collective organization lies in
the type and the nature of interactions between individuals and groups of
individuals. One factor is the **distance**: The closer we are to each other,
the more senses are used to 'feel' the presence of others. When bodies are
touching, we can feel the heat and, in some cases, even other people's
heartbeats.

{{<
    figure
    src="images/distance-modell.png"
    caption="Edward T. Hall's interpersonal distances of man ([The Hidden Dimension](https://archive.org/details/hiddendimension000hall))"
>}}


This creates a sensation that may be unpleasant in a crowded train but can help
lead to the emergence of helpful behavior in case of dangerous situations. When
walking in a crowded space, **sight** plays an important role. However, what we
see and how we process visual clues largely depends on the distance. From a
close distance, we can read someone's facial expression and understand, for
example, where someone is looking. This information, in addition to shoulder
orientation and other minor cues, can help us understand where someone is
heading and whether that person is looking at us. From a greater distance, it
becomes challenging to discern the intentions of other people. However, if we
can see them, we can choose to either join a crowded place or avoid it, so the
mere presence of people will also influence our decisions. For instance, people
sitting along a river and seeking privacy or intimacy will often avoid others,
typically choosing a spot equidistant from other groups of people. On the other
hand, in an unfamiliar place where we are aware that specific customs are
followed, we may choose to line up by following others, as is the case in
places like a city hall, for example.

The
[article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0177328)
discusses pedestrian dynamics in gatherings, emphasizing that pedestrians not
only respond to stimuli but also act based on social norms and identities. It
proposes integrating social psychology with natural sciences, suggesting three
categories for study: phenomena, behavior, and action.

{{<
    video
    src="images/interaction.mp4"
    caption="Experimental study on entrance to a bottleneck."
>}}

Many aspects of interactions and relationships within a crowd follow
exponential laws. Distance thresholds
defined to characterize different degrees of personal space usually grow larger
and larger the less familiar we are with someone. A distance of a few
centimeters can create a different feeling in a packed train, but it takes a
change of several meters to feel distant from a person already dozens of meters
apart. Similarly, collision avoidance is also subject to exponential laws.
Steering maneuvers are performed much more quickly when people are approaching
very quickly, and minimum corrections are made for distant individuals. See for
instance the direction model in the [collision free speed
model](/models/collision_free_speed_model/). Even more interesting is that
higher-level aggregations also follow similar laws. In a given country, only a
few cities exceed a population of one or several million, while hundreds of
cities may have several dozens of thousands of people. A large number of
villages can also be found with small populations. This dimension also changes
with culture, reflecting differences at the microscopic scale in some way. What
may be considered a small city in Asian countries could be considered a
metropolis in Europe or South America. Yet, the same principle typically
applies to each distinct geographical area, demonstrating the universal nature
of human social organization.

In short, our **perception and cognition** shape the world in which we live and
the way we interact with other people. Although we can only walk short
distances and move within limited spaces, our planning occurs on larger scales,
and migration, while slow, can span significant distances. Not surprisingly,
collective organization at a microscopic scale is reflected in similar laws
found on a macroscopic scale. We cannot escape from our human nature, as we are
a part of the natural world, which also adheres to similar laws.


## Methods

Research into Pedestrian Dynamics employs various methods, including
simulations, experiments under laboratory conditions, real-life measurements,
and qualitative observations. The emergence of computer vision technology has
enabled the integration of insights from simulation studies with systematic
data collection efforts.

### Experiments

In the early 2000s, laboratory experiments became a leading method:
participants walk through controlled setups under the supervision of
experimenters, often wearing colored vests and helmets that make tracking
easier and more accurate. Controlled settings allow precise definition of
conditions such as density, geometry, and even emotional state. Their limits
are the small number of volunteers, restricted time, and possible
psychological bias. Even so, laboratory data remain a benchmark for the
field.

{{<
    video
    src="images/experiments.mp4"
    caption="Experiments under laboratory conditions. See [IAS-7 Data Archive](https://ped.fz-juelich.de/db)"
>}}

### Field observations

Field observations, in contrast, allow continuous data collection throughout
the year and capture behavior beyond the average case. Virtual reality has
also proven useful for studying pedestrian movement and behavior, thanks to
its low cost and high experimental control; how well findings from virtual
worlds transfer to real ones is an ongoing research question.

{{<
    figure
    src="images/corbetta1.png"
    caption="Real-life anonymous pedestrian tracking in the train station of Eindhoven (NL). [Source](https://research.tue.nl/en/publications/continuous-measurements-of-real-life-bidirectional-pedestrian-flo)"
>}}

Machine learning and computer vision now allow accurate real-time tracking in
such settings. Tracking crowds around the clock in public locations yields
sample sizes out of reach for any other method: millions of trajectories.
The challenge is that conditions cannot be imposed. Crowd density, flow
direction, and the presence of groups, all controllable in the laboratory,
become random variables in real life. Statistical analysis then requires
selecting and aggregating similar instances, for example by representing the
data as graphs.

{{<
    video
    src="images/voronoi-moving.mp4"
    caption="Identified silhouettes of individuals in transit and their associated Voronoi diagrams. [Source](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.98.062310)"
>}}

### Modeling

Mathematical and physical models have evolved from laboratory and qualitative
studies. Early qualitative models helped explore crowd phenomena and showed
that quantitative modeling is feasible. More recently, data-based models using
machine learning have gained popularity.

Pedestrian dynamics modeling can be broken down based on the scale of
application: strategic (which deals with route and departure choices in
buildings), tactical (focusing on path or exit choices in rooms), and
operational (which examines interactions among pedestrians and infrastructure).
At the operational level, there are three primary types of models:

1. **Macroscopic Models**: Derived from fluid dynamics, these models study
   averages like density, speed, or flow.
2. **Mesoscopic Models**: Rooted in thermodynamics, they deal with the
   probability density of pedestrian movements over time, position, and speed.
3. **Microscopic Models**: View pedestrians as individual entities interacting
   with each other.

{{<
    figure
    src="images/co140311.f1.jpeg"
    caption="[Physics of Human Crowds](https://www.annualreviews.org/doi/abs/10.1146/annurev-conmatphys-031620-100450), Corbetta & Toschi. Annual Review of Condensed Matter Physics, vol. 14, 1, p.311-333, 2023"
>}}


Microscopic models further differ based on parameters such as time, space,
modeling approach, and fidelity. Other specific models include:

- **Cellular Automaton (CA)**: Here, systems are divided into cells,
  representing spaces that can be free or occupied by pedestrians. These models
  use space-based rules to determine movement.

{{<
    figure
    src="images/ca.png"
    caption="Potential movement paths on a grid, along with their associated transition probabilities, are outlined for the von Neumann neighborhood scenario"
>}}

- **Force-based Models**: These continuous models utilize systems of equations
  to determine pedestrian motion, considering factors like repulsion from
  others or attractions to certain routes.

- **Speed Models**: Unlike force-based ones, these models focus on speed and
  don't consider inertia. Some are vision-based, determining pedestrian
  movement based on predicted movements of surrounding individuals.

{{<
    figure
    src="images/ellipses.png"
    caption="In continuous space models, whether force-based or velocity-based, pedestrians are depicted as two-dimensional figures (like ellipses, circles, etc.). The distance between these figures determines the repulsive interactions among them"
>}}

- **Agent-based Models**: Treat pedestrians as individual agents, using a
  detailed set of parameters to model their behaviors.

The approaches differ in scale, detail, and the behaviors they aim to
capture.

Models need validation. This
[paper](https://link.springer.com/chapter/10.1007/978-3-540-79992-4_77)
examines why different sources and experiments report different fundamental
diagrams and shows, by analyzing experimental trajectories, that the
measurement method itself influences the result.

A review and critique of mathematical studies on modeling and simulating human
crowds, with an emphasis on behavioral dynamics, can be found in
[Bellomo2023](https://link.springer.com/article/10.1007/s10489-023-04924-7).

These three approaches—simulations, experiments under laboratory conditions,
qualitative observations—complement and intertwine with each other.
Experimental data, whether from controlled or real-life settings, are
increasingly employed to validate and fine-tune simulation models.

## Further reading

Several review articles offer a deeper look at the field.

{{<
    figure
    src="images/reading.jpg"
    caption="[Photo](https://unsplash.com/photos/people-inside-library-1mwPOXb_pB8) by [Benjamin Ashton](https://unsplash.com/@bashton) on [Unsplash](https://unsplash.com)"
>}}

[Haghani2023](https://www.sciencedirect.com/science/article/pii/S0925753523002345?via%3Dihub)
discusses current challenges in crowd safety through the Swiss Cheese Model,
argues for a global Vision Zero target, and calls for closer collaboration
between stakeholders.

[Physics of Human
Crowds](https://doi.org/10.1146/annurev-conmatphys-031620-100450) reviews
crowd behaviors that appear universally, independent of individual differences
or crowd density, and shows how methods from physics contribute to
understanding pedestrian dynamics.

[What Is Crowd Management?](https://doi.org/10.1007/978-3-030-90012-0_1)
defines the term, distinguishes crowd management from crowd control, and
presents strategies that address both safety and comfort.

A [data guidance
paper](https://collective-dynamics.eu/index.php/cod/article/view/A141)
documents crowd management experiments with nearly 1000 participants,
motivated by physical and social-psychological theories of behavior at
railway stations.

A [glossary
article](https://collective-dynamics.eu/index.php/cod/article/view/A19)
explains terms that appear frequently in human crowd research.

Finally, a [review](https://doi.org/10.1007/978-3-030-05129-7_4) connects
empirical and theoretical pedestrian dynamics studies and shows how empirical
results are used to calibrate and validate pedestrian models.

## References

1. [ 75 Years of the Fundamental Diagram for Traffic Flow Theory: Greenshields
   Symposium ](https://www.trb.org/Publications/Blurbs/165625.aspx)
2. [Pedestrian fundamental diagrams: Comparative analysis of experiments in
   different geometries](https://juser.fz-juelich.de/record/128157)
3. [A review on collective behavior modeling and simulation: building a link
   between cognitive psychology and physical
   action](https://link.springer.com/article/10.1007/s10489-023-04924-7)
4. [The Hidden Dimension](https://archive.org/details/hiddendimension000hall)
5. [Collective phenomena in crowds—Where pedestrian dynamics need social
   psychology](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0177328)
6. [Continuous measurements of real-life bidirectional pedestrian flows on a
   wide
   walkway](https://research.tue.nl/en/publications/continuous-measurements-of-real-life-bidirectional-pedestrian-flo)
7. [Physics-based modeling and data representation of pairwise interactions
   among
   pedestrians](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.98.062310)
8. [Physics of Human
   Crowds](https://www.annualreviews.org/doi/abs/10.1146/annurev-conmatphys-031620-100450)
9. [Fundamental Diagram and Validation of Crowd
   Models](https://link.springer.com/chapter/10.1007/978-3-540-79992-4_77)
10. [A review on collective behavior modeling and simulation: building a link
    between cognitive psychology and physical
    action](https://link.springer.com/article/10.1007/s10489-023-04924-7)
11. [A roadmap for the future of crowd safety research and practice:
    Introducing the Swiss Cheese Model of Crowd Safety and the imperative of a
    Vision Zero
    target](https://www.sciencedirect.com/science/article/pii/S0925753523002345?via%3Dihub)
13. [What Is Crowd Management?](https://doi.org/10.1007/978-3-030-90012-0_1)
14. [Pedestrian Crowd Management Experiments: A Data Guidance Paper
    ](https://collective-dynamics.eu/index.php/cod/article/view/A141)
15. [A Glossary for Research on Human Crowd
    Dynamics](https://collective-dynamics.eu/index.php/cod/article/view/A19)
16. [Pedestrian Dynamics: From Empirical Results to
    Modeling](https://doi.org/10.1007/978-3-030-05129-7_4)


## Contributors

This article is a collaborative work, with contributions from various authors
listed in alphabetical order:


- [Mohcine Chraibi]({{< relref "/authors#MohcineChraibi" >}})
- [Alessandro Corbetta]({{< relref "/authors#AlessandroCorbetta" >}})
- [Claudio Feliciani]({{< relref "/authors#ClaudioFeliciani" >}})
- [Milad Haghani]({{< relref "/authors#MiladHaghani" >}})
- [Enrico Ronchi]({{< relref "/authors#EnricoRonchi" >}})
- [Jette Degenhardt]({{< relref "/authors#JetteDegenhardt" >}})
- [Antoine Tordeux]({{< relref "/authors#AntoineTordeux" >}})
- [Ezel Üsten]({{< relref "/authors#EzelÜsten" >}})

