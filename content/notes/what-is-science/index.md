---
title: "What is science?"
date: 2026-10-21
summary: We know more today than 300 years ago because we build explanations, test them and replace them with better ones. A small road network shows how, from the Braess paradox to models, experiments, simulation and the limits of what a model can tell us.
math: true
thumbnail: network-shortcut.png
---

{{< callout type="info" icon="none" >}}
**How do we gain scientific knowledge, and how do we recognise a good explanation?** This essay follows one example, a road network in which a new road makes everyone slower, through five steps: **Problem** (sections 1–3) → **Explanation** (4) → **Testing** (5–7) → **Improvement** (8) → **Application** (9). It grew out of the first lecture of *Scientific Working* at the University of Wuppertal in October 2026.
{{< /callout >}}

Why do we know things today that nobody knew 300 years ago? The obvious answers are experiments, better instruments, more data, better technology. More observations alone are not enough, though. We need explanations that we can test critically and improve. The idea goes back to Karl Popper; David Deutsch (*The Beginning of Infinity*, 2011) adds the criterion that good explanations are hard to vary.

A second question goes with the first: how can we understand things that nobody has observed yet? The example at the centre of this essay answers it. Dietrich Braess found the paradox named after him in 1968 in a model, before it was documented on a road.

## 1. Why do we need explanations?

Why does the earth quake? The same observation has had very different explanations. An old story, told in many variants, has the earth resting on a bull. A miniature of 1595 for al-Qazwīnī's cosmography shows an angel carrying the earth; the angel stands on a rock, the rock on a bull, the bull on a fish. In other versions the bull carries the earth on its horns, and the earth quakes when it shifts it from one horn to the other. It is one of many old stories and belongs to no particular culture or religion.

{{< figure src="weltstier_qazwini.jpg" width="300" caption="Miniature for al-Qazwīnī's cosmography (1595): an angel carries the earth, below it a rock, a bull and a fish. Public domain (Wikimedia Commons)." >}}

Modern geology explains earthquakes by the movement of tectonic plates. Plates of the earth's crust move; at their boundaries stresses build up and are released abruptly.

{{< figure src="platten_usgs.png" caption="The tectonic plates. Map: USGS, public domain (Wikimedia Commons)." >}}

Why do we accept plate tectonics and not the bull? The theory made predictions that could have failed. If new ocean floor forms at the mid-ocean ridges and spreads apart, the rock on both sides should record the reversals of the earth's magnetic field as stripes that are symmetric about the ridge, and the floor should get older with distance from it. Both were found in the 1960s (Vine & Matthews 1963). Today GPS measures the plate movements directly, at a few centimetres per year.

Deutsch adds a second criterion: a good explanation is *hard to vary* without losing its explanatory power. Replace the bull with an elephant or a dragon, and the story explains the quake just as well. It fixes almost nothing that could be tested. Plate tectonics cannot be changed at will; it depends on measurable movements, rocks and mechanisms.

{{< callout type="info" >}}
Progress means developing better explanations and testing them critically.
{{< /callout >}}

## 2. A paradox: can a new road make traffic worse?

Take a small road network with four nodes: Start, A, B and Goal. Two routes lead from Start to Goal, an upper one via A and a lower one via B. Each route has one narrow road, where the travel time is \(n\) minutes if \(n\) drivers use it, and one wide road without congestion, where the travel time is a fixed \(C\) minutes. The travel time of a route is the sum of its roads. Every driver wants to reach the goal as fast as possible.

{{< figure src="network.png" width="560" caption="The network. On the narrow roads the travel time grows with the number of drivers *n*; on the wide roads it is a constant *C*." >}}

Take 15 drivers and \(C = 17\). Suppose 10 drive the upper route and 5 the lower one. The upper route then takes \(10 + 17 = 27\) minutes and the lower one \(17 + 5 = 22\). Some drivers on the upper route switch. This goes on until the two routes are nearly balanced: with 7 on top and 8 below, the upper route takes 24 minutes and the lower one 25. A driver who switches from the lower to the upper route would then also need 25 minutes, so nobody can improve by switching alone. This state is a **Nash equilibrium**; in traffic it is called a **Wardrop equilibrium**.

Now the city builds a shortcut from A to B with a travel time of zero. There are three routes: upper, lower, and Start → A → B → Goal. With \(o\) drivers on the upper route, \(u\) on the lower one and \(a\) on the shortcut, the travel times are

$$
\begin{aligned}
t_\text{upper} &= (o + a) + C,\\
t_\text{lower} &= C + (u + a),\\
t_\text{shortcut} &= (o + a) + (u + a).
\end{aligned}
$$

{{< figure src="network-shortcut.png" width="560" caption="The same network with a shortcut from A to B that takes no time at all." >}}

For each single driver, the shortcut looks attractive: both narrow roads together cost less than one narrow and one wide road. So the drivers move over, and the narrow roads fill up. In the end all 15 use the shortcut, and each needs \(15 + 0 + 15 = 30\) minutes. A driver who goes back to the upper route alone needs \(15 + 17 = 32\) minutes, more than 30. So nobody leaves the shortcut, although without it everyone would arrive sooner. This is again a Nash equilibrium, but a worse one. The old split of 7 and 8 would be better for everyone, but with the shortcut it is no longer an equilibrium.

{{< figure src="result.png" width="640" caption="The two equilibria for 15 drivers and C = 17. Each driver chooses the fastest route, and the result is worse for all." >}}

The choice of \(C\) matters. Here \(C\) is the number of drivers plus 2. With a fixed \(C = 20\) the paradox disappears for fewer than about 14 drivers, and again for 40 or more.

Try it yourself: move the drivers between the routes, switch the shortcut on, and watch where the travel times settle. The box below the bars tells you whether anyone can still gain by switching.

{{< braess-game >}}

### The paradox has a name

This network has exactly the structure of the paper by Dietrich Braess, a mathematician at the University of Münster, published in German in 1968 in *Unternehmensforschung* under the title "Über ein Paradoxon aus der Verkehrsplanung". Braess did not observe the paradox in traffic; he found it in a model. It was theoretical work motivated by traffic planning, basic research. This fits Popper: explanations are not derived from data but conjectured and then criticised. Observations in cities came only later.

The idea travelled. Wardrop stated the equilibrium principle in 1952: in equilibrium, all used routes are equally fast. Braess found the surprising consequence in 1968. Cohen and Horowitz showed the same paradox with springs and strings in 1991. An English translation made the paper widely accessible in 2005. Today it is an argument in traffic planning: more roads do not automatically help.

### What do we actually know now?

Each driver chooses the fastest route, and the result is worse for all. That is what the model predicts. But the model assumes that travel time grows with the number of vehicles, that everyone chooses the fastest route and that the new road takes no time.

Three levels have to be kept apart. The mathematical result is knowledge, but knowledge about the model. Whether real traffic behaves like this is an empirical question. Scientific knowledge means building models, testing their predictions and finding out when a model is useful. When people actually play this game, their result is an observation; the numbers above are the theoretical equilibrium. If the two differ, that is already the first lesson.

## 3. What makes an explanation good?

Here are two explanations for the paradox.

{{< figure src="explanations.png" caption="Two explanations for the same result." >}}

Explanation A sounds plausible but names no mechanism. "Selfish" could explain the opposite result as well, and A does not say under which conditions the paradox occurs. A is the bull of this story: you could put any other word in place of "selfish". Explanation B says which roads fill up and why. No part of B can be swapped without the calculation breaking down, and that is why B makes predictions.

A test: what happens if the shortcut takes 5 minutes instead of none? B predicts that the paradox remains but becomes weaker. With 18 drivers and \(C = 20\), the travel time is then about 34 to 35 minutes instead of 36, compared with 29 without the shortcut. Once the shortcut takes about \(C - N/2\) minutes (\(N\) being the number of drivers; with \(C = N + 2\) that is 11 minutes for 18 drivers, 9 to 10 for 15), nobody uses it any more, and everything is as before. Explanation A cannot even address this question.

{{< callout type="info" >}}
A good explanation cannot be changed at will without ceasing to explain anything. (After David Deutsch, *The Beginning of Infinity*, 2011.)
{{< /callout >}}

Deutsch's criterion says something about the quality of an explanation. It does not replace testing against experience; it complements it.

A good explanation also often reaches beyond the case it was made for. Analogous effects appear in mechanical and electrical networks (Cohen & Horowitz 1991) and have been shown in a laboratory AC power grid (Schäfer et al. 2022). Whether they occur in a given real system has to be checked case by case.

## 4. Models, theories and hypotheses

The road network is a **model**: a simplified image of reality. A lot has been left out of it.

- **People:** not everyone chooses the fastest route.
- **Traffic:** traffic lights, junctions, queues.
- **Roads:** lengths, widths, capacities.
- **Travel time:** why exactly \(n\) minutes? Behind this lies the fundamental diagram.
- **Time:** everyone decides at the same time.
- **Information:** how does everyone know the travel times?

That does not make it a bad model. A model does not have to contain every detail of reality. It has to capture the mechanisms that matter for the question, here the interplay of route choice, traffic load and travel time. With four nodes and five edges it explains something surprising. That is the strength of a model: we simplify reality in order to understand one mechanism.

A model should be as simple as possible, but complex enough for the question. **Ockham's razor** says the same: if two models explain an observation equally well, the simpler one is preferable. A good model captures the relevant mechanisms and gives useful explanations and predictions for its purpose, however few details it contains. Whether we left out the right things is a question for validation (section 7).

Three terms are often mixed up:

- **Assumption:** "Drivers choose the route that is fastest for them." This is an assumption about behaviour. It is assumed within the model; whether people behave this way is a separate, testable question. It is not a theory. The model consists of the network plus this assumption.
- **Theory:** a coherent set of statements built on such assumptions, from which consequences can be derived. Here it is the equilibrium theory of route choice after Wardrop (1952). Its first principle: in equilibrium the travel times on all used routes are equal, and no unused route is faster.
- **Hypothesis:** a concrete prediction that follows from the theory and can fail against data. For example: "If road Y in network X is closed, the mean travel time decreases."

The touchstone for a hypothesis is one question: which observation would refute it? If you cannot say, it is not yet a hypothesis.

### Verify or falsify?

Karl Popper (*Logik der Forschung*, 1934) pointed out that general statements can never be proven conclusively, because nobody has seen all cases. Every white swan confirms the statement "All swans are white", but none proves it. A single black swan refutes it.

The same holds for traffic. A hundred cities in which a new road helped do not prove that new roads always help. One Braess case is enough to refute it, but only because the statement is universal ("always"). Against "mostly", a single counterexample does not help.

In practice a refutation is rarely this clean. A prediction always rests on auxiliary assumptions about instruments, data and conditions. When a prediction fails, one of these may be wrong instead of the theory. This is known as the Duhem–Quine problem, and it is one reason why a single surprising observation rarely settles a dispute.

Popper asks: can the statement fail? Deutsch adds: does it explain why it must be so? Good scientific explanations do both.

Back to the earthquake: which observation could show that plate tectonics is wrong? Magnetic stripes that are not symmetric about the ridges, for example, ocean floor of the same age everywhere, or GPS measurements that show no plate movement. The story of the bull forbids nothing, so no observation can refute it.

One warning about words: in simulation, "verification" means something else, namely checking the program (section 7).

## 5. How do we test explanations?

### Observations from cities

Three cases are often cited for the Braess paradox:

- **Stuttgart 1969:** a new road makes traffic worse. Only when it is closed again does traffic improve.
- **New York 1990:** 42nd Street is closed on Earth Day. Congestion, if anything, decreases.
- **Seoul 2003–2005:** an urban motorway is demolished. At first traffic gets slower, then many people switch to the subway.

As evidence for Braess they are weak: they are observations after an intervention, not controlled experiments. What else changed? In Seoul, trips shifted to the subway over several years (Chung et al. 2012). Seoul is therefore more an example of adaptation than a clean Braess case. In reality many things change at once. An experiment tries to isolate one cause.

### Experiment

Suppose a group of 15 people plays the route game, first without the shortcut and then with it, and they end up slower the second time. Can we conclude that the shortcut caused the difference? Perhaps they decided differently the second time because they already knew the game. Perhaps they were better informed, or understood the rules differently.

A clean comparison has two trials. In trial A everyone chooses between two routes; in trial B the same people choose between three. The number of people, the travel-time rules, the information and as far as possible all other conditions stay the same. Better still: vary the order of the trials between groups, run several rounds and compare.

{{< callout type="info" >}}
An experiment deliberately changes one condition and studies its effect.
{{< /callout >}}

Such a game tests the effect of the shortcut within the model. It is not yet evidence about real road networks.

Rapoport and colleagues (2009) ran this experiment in the laboratory. Participants made route choices in an experimental network over many rounds, and their payoff depended on the resulting travel costs. With the additional link they ended up in the worse equilibrium and earned less, even after much practice.

## 6. When explanations fail: Clever Hans

Even careful experiments can miss something decisive. Around 1900 a horse, "Clever Hans", answered arithmetic questions by tapping its hoof, in front of large audiences and mostly correctly. Many experts were convinced, and a commission found no trick in 1904.

{{< figure src="clever_hans.jpg" caption="Clever Hans at a public demonstration, 1904. From K. Krall, *Denkende Tiere* (1912), plate 2. Public domain (Wikimedia Commons)." >}}

His owner, Wilhelm von Osten, a mathematics teacher and follower of phrenology, was convinced that animals can think. The psychologist Oskar Pfungst was not satisfied with this explanation. He worked carefully with Hans and von Osten and changed one factor at a time: whether the questioner knew the answer, whether Hans could see the questioner (using blinkers), how far away the questioner stood.

| Condition | Result |
|---|---|
| The questioner knows the answer | mostly correct |
| The questioner does not know it | many more errors |
| Hans cannot see the questioner | many more errors |

Hans read tiny body signals of the questioner, who relaxed without noticing as soon as the right number was reached. Two explanations competed: "Hans can do arithmetic" and "Hans reads unconscious signals". Both fit the correct answers. Only the second predicts that Hans fails when nobody he can see knows the answer. An experiment that tells two explanations apart produces knowledge. The second explanation wins because it passes the targeted test, whether or not it sounds simpler. Von Osten never accepted the result.

The observation was real; the explanation was wrong, because one influence had been overlooked. An experiment is not automatically a good experiment, and, as with Braess, a correct observation does not guarantee a correct explanation. That many experts were convinced was no argument: knowledge rests on criticism, not on authority.

The episode gave its name to the **Clever Hans effect**: the expectations of observers unconsciously influence the behaviour of those observed. Related are the experimenter effect (Rosenthal) and the interviewer effect in surveys. Today's countermeasures are blinding and control conditions. Science means looking for evidence for one's own explanation and also finding out where one might be wrong, including in one's own experimental design.

## 7. Simulation, verification and validation

The network above has four nodes; you can work it out in your head. A city network has tens of thousands of links, travel times depend nonlinearly on load, and people decide differently. Then you need numerical methods and software, for example SUMO, MATSim, Vissim or, for pedestrians, JuPedSim.

Suppose the fundamental diagram, the relation between density and flow, is well known from experiments. We derive travel times from it, build a network model with route choice and simulate it. Even then the simulation does not necessarily predict the Braess paradox reliably.

If the software reproduces the analytical equilibrium for the Braess network exactly, that shows only that it computes correctly. An important verification test has been passed, but that is not validation. And even with correct software and a well-supported fundamental diagram the predictions can be wrong: people may choose routes differently than assumed, and queues, differences in information or effects over time may be missing. One valid component does not make a valid overall system.

The tempting conclusion is: "The input models are validated and the software passes all tests, so the simulation is realistic." It does not follow. Two questions have to be asked separately: did we implement the model correctly, and did we choose the right model?

{{< figure src="vv.png" caption="Verification compares the program with the model; validation compares the model with reality." >}}

- **Verification:** does the program compute what the model says? Has the model been implemented correctly and solved numerically? This is checked with tests and comparisons with exact solutions, looking for errors in code and numerics.
- **Validation:** does the model describe reality well enough for its intended purpose? This is checked against measured data. A model is always valid for a purpose, never absolutely.

Roache (1998), following Boehm and Blottner, put it briefly: verification means solving the equations right, validation means solving the right equations. A program can be perfectly verified and still not valid. And this "verification" is not Popper's.

For pedestrian simulations the German guideline RiMEA (Richtlinie für Mikroskopische Entfluchtungsanalysen, version 4.1.1, 2025) lists test cases 1 to 16 in its Annex 1. RiMEA uses verification and validation interchangeably, following ISO/TR 13387-8:1999. What it calls "quantitative verification", the comparison with data from evacuation drills, is validation in the AIAA sense (AIAA G-077-1998), and RiMEA itself regards it as not yet possible.

## 8. How scientific knowledge improves

### What moves around what?

Even a wrong or limited model can describe observations quite well. Ptolemy's geocentric model predicted planetary positions usefully for centuries and was refined mathematically again and again. Copernicus' heliocentric model (1543) was at first not more accurate in every respect; it still used circular orbits.

{{< figure src="cellarius_ptolemaeus.jpg" width="520" caption="The geocentric world view: the earth at the centre. Andreas Cellarius, *Harmonia Macrocosmica* (1660). Public domain (Wikimedia Commons)." >}}

{{< figure src="cellarius_kopernikus.jpg" width="520" caption="The heliocentric world view: the earth moves around the sun. Andreas Cellarius, *Harmonia Macrocosmica* (1660). Public domain (Wikimedia Commons)." >}}

Only Kepler's elliptical orbits (*Astronomia nova*, 1609), Galileo's observations with the telescope (1610, among them the phases of Venus) and later Newton's theory of gravitation (1687) made it the much more convincing explanation. The geocentric model was replaced step by step, between 1543 and 1687. Knowledge grows this way, by improving and replacing models.

It follows that a model that reproduces the data has not yet shown that its mechanism is right. Ptolemy, too, fitted the data. This leads to the question of what really caused a result.

### Causality

Causality means: A causes B. In the route game the chain is clear. The road does not change the travel time directly; it changes behaviour, and behaviour changes the travel time. This can be shown because the game compares with and without the road while everything else stays the same.

{{< figure src="causality.png" caption="In the controlled game the causal chain can be shown. In Seoul it cannot: without a comparison, a sequence in time is a correlation, not a cause." >}}

Seoul is harder. After the urban motorway was demolished, traffic first got slower, but not worse in the long run. Was the demolition the cause, or the switch to the subway, driving behaviour, the economy? Without a comparison this is a correlation in time, not proof of a cause. And a falsification in Popper's sense needs a reliable observation, which is exactly what is uncertain in the city cases.

### Interaction

The causal chain has a catch: drivers also react to each other. Interaction means that two quantities influence each other in a feedback loop. In the route game my route choice changes your travel time, your travel time changes your route choice, and that changes mine again.

{{< figure src="interaction.png" width="560" caption="Everyone influences everyone." >}}

So one cannot simply say that the road is the cause. The result emerges from the interplay. This holds for almost everything in traffic and pedestrian dynamics.

## 9. What science can and cannot tell us

### From basic research to application

Basic research wants to understand, without a direct use in view. Applied research wants to solve a problem. The boundary is open. Braess' paper was mathematics in 1968; today the argument is part of traffic planning. Peter Grünberg at Forschungszentrum Jülich discovered giant magnetoresistance, at the same time as Albert Fert; it led to read heads for hard disks, and both received the Nobel Prize in 2007. GPS works only with corrections from the theory of relativity. Applied research often ends up in standards and guidelines (DIN, FGSV, VDI), which should rest on well-founded knowledge.

### The same questions, a different theory

The questions from the traffic example apply far beyond traffic. Gustave Le Bon (*The Crowd*, 1895) still shapes the popular image of "mass panic". In his words, individuals in a crowd are changed because "the fact that they have been transformed into a crowd puts them in possession of a sort of collective mind" (English translation of 1896).

A thought experiment: you are a Dortmund fan in the Bayern Munich block, and Dortmund scores in the last minute. What do you feel?

What exactly does the "collective mind" explain? Which mechanism lies behind it? Which observation would refute it? It is supposed to explain aggressive crowds as well as peaceful ones. Can it be adapted so freely that it explains everything, and therefore nothing? Further reading: Clarke (2002), Drury, Novelli and Stott (2013), Haghani et al. (2019).

### How to evaluate a claim

The questions used throughout this essay work for any claim, in a newspaper, a report or one's own thesis:

1. What exactly is explained, and what is the mechanism?
2. Could the explanation be changed at will and still "explain" the same thing?
3. Which observation would refute it?
4. Is there a controlled comparison, with and without, or only a sequence in time?
5. Was a model checked against reality, and for which purpose is it valid?

An example of how a question becomes testable: "A bottleneck 3 m wide and 1 m long, or 1 m wide and 3 m long: which is better?" As it stands, this is not yet a scientific question. One has to fix the walking direction (the width across the direction of walking matters most, but the length of the bottleneck also affects the flow; Liddle et al. 2009), the geometry, and what "better" means: higher flow, shorter evacuation time or lower density in front of the bottleneck. Only then does an intuitive question become a testable hypothesis. As with Braess, one changes the geometry and asks what happens to the flow.

### Summary

1. We want to understand the world.
2. We discover something surprising.
3. We look for an explanation.
4. We test whether our explanation holds.
5. We improve our knowledge and apply it.

Scientific knowledge is provisional, testable, methodically grounded and correctable. We know more today than 300 years ago because we form explanations, criticise them and improve them, instead of only collecting observations: the bull and plate tectonics, Ptolemy and Kepler and Newton, whose *Principia* appeared in 1687, almost 340 years ago.

{{< callout type="info" >}}
Science means developing explanations, finding their errors and replacing them with better ones. It has no final answers.
{{< /callout >}}

## Further material

- [Slides of the lecture](/teaching/scientific-working-2026/) ([PDF](/teaching/scientific-working-2026/What_is_science_slides.pdf))
- [Companion text of the lecture](/teaching/scientific-working-2026/What_is_science_companion.pdf) (PDF)

## References

- Braess, D. (1968): Über ein Paradoxon aus der Verkehrsplanung. *Unternehmensforschung* 12, 258–268.
- Braess, D., Nagurney, A., Wakolbinger, T. (2005): On a Paradox of Traffic Planning. *Transportation Science* 39(4), 446–450.
- AIAA (1998): *Guide for the Verification and Validation of Computational Fluid Dynamics Simulations*. AIAA G-077-1998.
- Chung, J.-H., Hwang, K. Y., Bae, Y. K. (2012): The loss of road capacity and self-compliance: Lessons from the Cheonggyecheon stream restoration. *Transport Policy* 21, 165–178.
- Clarke, L. (2002): Panic: Myth or Reality? *Contexts* 1(3).
- Cohen, J. E., Horowitz, P. (1991): Paradoxical behaviour of mechanical and electrical networks. *Nature* 352, 699–701.
- Deutsch, D. (2011): *The Beginning of Infinity*. London: Allen Lane.
- Drury, J., Novelli, D., Stott, C. (2013): Psychological disaster myths in the perception and management of mass emergencies. *Journal of Applied Social Psychology* 43(11), 2259–2270.
- Haghani, M., Cristiani, E., Bode, N. W. F., Boltes, M., Corbetta, A. (2019): Panic, Irrationality, and Herding: Three Ambiguous Terms in Crowd Dynamics Research. *Journal of Advanced Transportation*, 9267643.
- Kolata, G. (1990). *New York Times*, 25 December 1990.
- Le Bon, G. (1895): *Psychologie des foules*. English: *The Crowd: A Study of the Popular Mind* (1896).
- Liddle, J., Seyfried, A., Klingsch, W., Rupprecht, T., Schadschneider, A., Winkens, A. (2009): An Experimental Study of Pedestrian Congestions: Influence of Bottleneck Width and Length. arXiv:0911.4350.
- Pfungst, O. (1907): *Das Pferd des Herrn von Osten (Der Kluge Hans)*. Leipzig: Barth.
- Popper, K. (1934): *Logik der Forschung*. Wien: Springer.
- Rapoport, A., Kugler, T., Dugar, S., Gisches, E. J. (2009): Choice of routes in congested traffic networks: Experimental tests of the Braess Paradox. *Games and Economic Behavior* 65(2), 538–571.
- RiMEA (2025): Richtlinie für Mikroskopische Entfluchtungsanalysen, version 4.1.1.
- Roache, P. J. (1998): Verification of codes and calculations. *AIAA Journal* 36(5), 696–702.
- Schäfer, B. et al. (2022): Understanding Braess' Paradox in power grids. *Nature Communications* 13, 5396.
- Vine, F. J., Matthews, D. H. (1963): Magnetic anomalies over oceanic ridges. *Nature* 199, 947–949.
- Wardrop, J. G. (1952): Some Theoretical Aspects of Road Traffic Research. *Proceedings of the Institution of Civil Engineers* Part II 1(3).

Stuttgart case: after Knödel (1969), cited in the German Wikipedia article "Braess-Paradoxon".

{{< icon "pencil-alt" >}} By: [Mohcine Chraibi]({{< relref "/authors#MohcineChraibi" >}}) and [Armin Seyfried]({{< relref "/authors#ArminSeyfried" >}})
