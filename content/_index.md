---
title: Pedestrian Dynamics
toc: true
cascade:
  type: docs
---

## Basic questions and applications

Understanding the dynamics of pedestrian movement is of paramount significance
due to the intricate nature of human crowd behavior. This field delves into the
complex flow of crowds, a phenomenon that exhibits emergent complexity across
various scales. Physics offers a versatile framework for interpreting and
modeling crowd dynamics, enabling insights into their behavior at different
lengthscales and timescales. Central to this study is the composition of the
crowd, which plays a pivotal role in unraveling the intricacies of pedestrian
dynamics.

{{< figure
    src="/images/crowd.png"
    caption="Image design: Panar Ege Uesten."
>}}

At first glance, the research in Pedestrian Dynamics may seem like the
exploration of ordinary flows of people in crowded places. However, beneath the
surface lies a fascinating and challenging science that addresses three
important pillars of our society that make it important to both scientists and
stakeholders: Improving **transport systems** in accordance with **safety** and
**comfort**.

### Transportation Improvement

Effortless movement of people within high-traffic infrastructure facilities
such as train stations and airports is a hallmark of pedestrian dynamics. This
discipline offers valuable perspectives for enhancing the efficiency of these
vital transit points. As urban centers experience population growth,
comprehending pedestrian behavior in these environments becomes indispensable
in crafting well-functioning transportation systems. Crucial metrics, including
the flow of individuals through bottlenecks and a facility's capacity to
evacuate per hour, empower us to optimize movement, alleviating congestion and
promoting sustainable urban mobility. One of the foundational aspects of this
understanding is the fundamental diagram, which represents the relationship
between these quantities. A notable reference on this topic is [75 Years of the
Fundamental Diagram for Traffic Flow Theory: Greenshields
Symposium](https://www.trb.org/Publications/Blurbs/165625.aspx), which provides
in-depth insights into the history, latest developments, and practical
applications of traffic flow theory, backed by empirical data and simulation
studies.

{{<
    figure
    src="/images/fd.png"
    caption="The fundamental diagram describes the relationship of flow and density and helps to understand the formation of congestions."
>}}

Further reading on the fundamental diagram is be found in this dissertation:
[Pedestrian fundamental diagrams: Comparative analysis of experiments in
different geometries](https://juser.fz-juelich.de/record/128157)

Moreover, the scope of pedestrian dynamics extends beyond these spaces and
includes scenarios in the context of large events. The arrival and departure
process of thousands of event visitors is a complex system consisting of
different stages and thus of different behaviors like waiting in queues.
Understanding how pedestrians queue and quantify the time it takes for queues
to be processed provides valuable insights for managing crowd flow, ensuring
smooth and enjoyable experiences at various gatherings.

{{<
    figure
    src="/images/queue.jpg"
    caption="[Photo](https://unsplash.com/photos/aerial-photography-of-people-Nzb4LBsctyQ) by [Hal Gatewood](https://unsplash.com/@halacious) on [Unsplash](https://unsplash.com)"
>}}

This broader scope underlines the versatile application of pedestrian dynamics,
enriching our ability to design spaces and processes that accommodate diverse
human movement patterns efficiently.

### Safety and Comfort

Safety and comfort are the cornerstones of any environment. Pedestrian Dynamics
explores intricate balance between these elements, guiding us toward designs
that prioritize the well-being of individuals. Through meticulous analysis, we
can identify potential bottlenecks, hazardous areas, and evacuation strategies,
ensuring the safety of crowds in emergencies. Moreover, optimizing pedestrian
flow enhances the overall comfort of public spaces, transforming them into
inviting spaces that offer positive experiences for everyone.

In the domain of crowd dynamics research, the assessment of the "perception of
safety and security" within crowded settings constitutes a central focus. This
endeavor fundamentally revolves around how crowd members perceive these
essential attributes. Crowd dynamics researchers bear the responsibility of
devising tools and methodologies to evaluate these qualitative perceptions,
potentially quantifying them while striving for objectivity. The aim is to
capture these perceptions with a high degree of accuracy, reflecting the
genuine sentiments of individuals.

{{<
    figure
    src="/images/crowd_station.jpg"
    caption="[Photo](https://unsplash.com/photos/people-standing-and-walking-on-stairs-in-mall-mVhd5QVlDWw) by [Anna Dziubinska](https://unsplash.com/@annadziubinska) on [Unsplash](https://unsplash.com/)"
>}}

## Collective Phenomena: Where Individuals Converge to Form Communities

Pedestrian dynamics fundamentally delve into collective phenomena, which
manifest through a rich tapestry of psychological and sociological
interactions. One core question that underpins the social dimension of
pedestrian dynamics is: *How do individuals unite to form the collective
crowd?* This multifaceted query embodies not only social interactions but also
behaviors, emotions, and cultural nuances, further compounded by variations
across different social groups.

Specifically, pedestrian dynamics give rise to certain collective phenomena,
such as:

- **Lane Formation**: This occurs in bidirectional pedestrian streams, where
  individuals spontaneously form lanes to streamline their movement in opposing
  directions.

{{<
    figure
    src="/images/lane-formation.gif"
    caption="Spontanous emergence of lane formation in a bi-directional flow"
>}}

- **Clogging at Bottlenecks**: Recognized by the jamming arch of multiple
  interacting individuals or particles near a bottleneck, clogging
  significantly reduces, or even halts, flow. This phenomenon arises
  predominantly when entities navigate through narrow constrictions, as often
  seen in crowded places.

{{<
    figure
    src="/images/clogging.webp"
    caption="Cloggging in a bottleneck"
>}}

- **Stop-and-Go Waves**: A distinct behavior observed in congested systems,
  such as traffic or densely packed crowds. Here, entities fluctuate between
  two states — motion and halt — creating waves of movement.

{{<
    figure
    src="/images/stop-go.gif"
    caption="Emergence of stop-and-go waves in a system with closed boundary conditions"
>}}

Comprehending these dynamics equips us to better understand and subsequently
influence crowd behaviors, paving the path for advanced crowd management
techniques. Whether it's an enthralled crowd at a football match, a harmonious
gathering at a music festival, or a bustling train station teeming with
purpose-driven individuals, pedestrian dynamics shed light on the intricate
webs of human interaction that unfold in myriad ways around us.

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
    src="/images/distance-modell.png"
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
    figure
    src="/images/interaction.gif"
    caption="Experimental study on entrance to a bottleneck."
>}}

What is interesting to note is that many aspects related to interactions and
relationships within a crowd follow exponential laws. Distance thresholds
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

In the early 2000s, laboratory investigations emerged as a leading method,
involving participants walking within controlled environments overseen by
experimenters. These experiments employed colored vests and helmets, which not
only added a systematic approach but also greatly enhanced tracking accuracy.
While these controlled environments excelled in accurately defining
experimental conditions such as density, geometry, and emotional states, they
did face challenges such as limited statistical significance stemming from
volunteer constraints, time limitations, and potential psychological biases.
Nevertheless, their controlled nature provided invaluable insights and set a
benchmark for further studies in the field.

{{<
    figure
    src="/images/experiments.gif"
    caption="Experiments under laboratory conditions. See [IAS-7 Data Archive](https://ped.fz-juelich.de/db)"
>}}

### Field observations

Conversely, field observation  enable continuous data collection throughout the
year, providing insights into Pedestrian Dynamics beyond average behaviors. For
example, virtual reality technology has been proven useful to explore several
aspects related to pedestrian movement and behavior given its low cost and high
experimental control. Research efforts are ongoing for the systematic
comparison of Pedestrian Dynamics in real and virtual worlds.

{{<
    figure
    src="/images/corbetta1.png"
    caption="Real-life anonymous pedestrian tracking in the train station of Eindhoven (NL). [Source](https://research.tue.nl/en/publications/continuous-measurements-of-real-life-bidirectional-pedestrian-flo)"
>}}

Recent technologies, often hinged in machine learning and computer vision,
allow real-time and accurate tracking in these settings. Real-life tracking
opens the possibility of collecting and analyzing datasets with sample sizes
unimaginable in any other measurement conditions (millions of trajectories can
be easily collected by crowd tracking in public locations adopting a 24/7
schedule). Real-life data collection comes with its challenges: data can
exhibit wide variations in terms of experimental parameters that, more often
than not, cannot be imposed. Crowd density, flow direction, and group presence,
that in laboratories can be imposed, in real-life become random variables.
Analyzing such diverse scenarios requires selecting and aggregating similar
instances for statistical analyses. This has been achieved e.g. representing
experimental data in terms of graphs.

{{<
    figure
    src="/images/voronoi-moving.gif"
    caption="Identified silhouettes of individuals in transit and their associated Voronoi diagrams. [Source](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.98.062310)"
>}}

### Modeling

Mathematical and physics models have evolved through insights from laboratory
and qualitative studies. Earlier qualitative models played a pivotal role in
exploring human crowd phenomena and suggesting the feasibility of quantitative
modeling. Alongside these, data-based models utilizing machine learning
techniques have gained popularity.

Pedestrian dynamics modeling can be broken down based on the scale of
application: strategic (which deals with route and departure choices in
buildings), technical (focusing on path or exit choices in rooms), and
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
    src="/images/co140311.f1.jpeg"
    caption="[Physics of Human Crowds](https://www.annualreviews.org/doi/abs/10.1146/annurev-conmatphys-031620-100450), Corbetta & Toschi. Annual Review of Condensed Matter Physics, vol. 14, 1, p.311-333, 2023"
>}}


Microscopic models further differ based on parameters such as time, space,
modeling approach, and fidelity. Other specific models include:

- **Cellular Automaton (CA)**: Here, systems are divided into cells,
  representing spaces that can be free or occupied by pedestrians. These models
  use space-based rules to determine movement.

{{<
    figure
    src="/images/ca.png"
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
    src="/images/ellipses.png"
    caption="In continuous space models, whether force-based or velocity-based, pedestrians are depicted as two-dimensional figures (like ellipses, circles, etc.). The distance between these figures determines the repulsive interactions among them"
>}}

- **Agent-based Models**: Treat pedestrians as individual agents, using a
  detailed set of parameters to model their behaviors.

In essence, the modeling of pedestrian dynamics is multifaceted, encompassing a
range of approaches that differ based on scale, detail, and the specific
behaviors they aim to capture.

Emphasizing the significance of model validation, this
[paper](https://link.springer.com/chapter/10.1007/978-3-540-79992-4_77) centers
on the fundamental diagram—a key concept linking density to flow or velocity in
crowd dynamics. Despite its importance, diverse sources and experiments present
varying interpretations of this diagram. The paper investigates these variances
and suggests that differences in measurement approaches can yield divergent
results. By analyzing experimental trajectories, the research offers insights
into how these methodologies influence the depiction of the fundamental
diagram.

A comprehensive review and insightful critique of mathematical studies on
modeling and simulating human crowds with an emphasis on behavioral dynamics
can be found in
[Bellomo2023](https://link.springer.com/article/10.1007/s10489-023-04924-7).

These three approaches—simulations, experiments under laboratory conditions,
qualitative observations—complement and intertwine with each other.
Experimental data, whether from controlled or real-life settings, are
increasingly employed to validate and fine-tune simulation models.

## Further reading

For those keen on a deeper exploration of the topic, several review articles
offer extensive insights.

{{<
    figure
    src="/images/reading.jpg"
    caption="[Photo](https://unsplash.com/photos/people-inside-library-1mwPOXb_pB8) by [Benjamin Ashton](https://unsplash.com/@bashton) on [Unsplash](https://unsplash.com)"
>}}

The article by
[Haghani2023](https://www.sciencedirect.com/science/article/pii/S0925753523002345?via%3Dihub)
dives into contemporary challenges related to the Swiss Cheese Model of Crowd
Safety, detailing its layers and the intricacies of its implementation.
Moreover, it promotes the idea of a global Vision Zero target in crowd safety
and accentuates the need for strengthening stakeholder collaboration.

Shifting the lens to the inherent behaviors of human crowds, [Physics of Human
Crowds](https://doi.org/10.1146/annurev-conmatphys-031620-100450) examines the
universality of these behaviors, transcending individual nuances or crowd
densities. The authors channel physics methodologies to unlock a deeper
understanding of pedestrian dynamics, striving for urban environments that
prioritize safety.

In the realm of crowd management, [What Is Crowd
Management?](https://doi.org/10.1007/978-3-030-90012-0_1) presents an
articulate definition, distinguishing the subtleties between management and
control of crowds. The strategies underlined in this piece harmonize the two
imperatives of safety and comfort.

Further enriching this body of knowledge is a
[paper](https://collective-dynamics.eu/index.php/cod/article/view/A141) that
showcases experiments with a sample size nearing 1000 participants. The goal?
To unearth physical and social-psychological theories revolving around
behaviors witnessed at railway stations and the corresponding crowd management
techniques.

For those navigating the academic jargon, an
[article](https://collective-dynamics.eu/index.php/cod/article/view/A19) serves
as a beacon, elucidating terms that find frequent mention in human crowd
research.

Concluding this list, a comprehensive
[review](https://doi.org/10.1007/978-3-030-05129-7_4) marries empirical and
theoretical pedestrian dynamics studies, spotlighting the pivotal role
empirical results play in the calibration and validation of nuanced pedestrian
models.

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


- [Mohcine Chraibi](/authors#MohcineChraibi)
- [Alessandro Corbetta](/authors#AlessandroCorbetta)
- [Claudio Feliciani](/authors#ClaudioFeliciani)
- [Milad Haghani](/authors#MiladHaghani)
- [Enrico Ronchi](/authors#EnricoRonchi)
- [Jette Schumann](/authors#JetteSchumann)
- [Antoine Tordeux](/authors#AntoineTordeux)
- [Ezel Üsten](/authors#EzelÜsten)

