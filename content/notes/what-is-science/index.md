---
title: "What makes an explanation good? Lessons from a road paradox"
date: 2026-10-21
summary: A good explanation names a mechanism, is hard to vary and can fail a test. A small road network in which a new road makes everyone slower shows how such explanations are built, tested and improved, and what this means for experiments, crowd simulations and the standards that judge them.
math: true
thumbnail: network-shortcut.png
---

{{< callout type="info" icon="none" >}}
**How do we gain scientific knowledge, and how do we recognise a good explanation?** This essay follows one example, a road network in which a new road makes everyone slower, through five steps: Problem (sections 1–2) → Explanation (3–4) → Testing (5–8) → Improvement (9) → Application (10). It was inspired by Armin Seyfried's first lecture of *Scientific Working* at the University of Wuppertal in October 2026.
{{< /callout >}}

We know things today that nobody knew 300 years ago. The obvious reasons are experiments, better instruments, more data, better technology. More observations alone are not enough, though. We need explanations that we can test critically and improve. The idea goes back to Karl Popper (*Conjectures and Refutations*, 1963); David Deutsch (*The Beginning of Infinity*, 2011, ch. 1) adds the criterion that good explanations are hard to vary. The essay follows one example. It describes a way of reasoning; fields differ in the methods they use and the order in which they use them.

A second question is how we can understand things that nobody has observed yet. The example at the centre of this essay answers it. Dietrich Braess found the paradox named after him in 1968 in a model, before it was documented on a road.

## 1. Why do we need explanations?

Take earthquakes. The same observation has had very different explanations. An old story, told in many variants, has the earth resting on a bull. A miniature of 1595 for al-Qazwīnī's cosmography shows an angel carrying the earth; the angel stands on a rock, the rock on a bull, the bull on a fish. In other versions the bull carries the earth on its horns, and the earth quakes when it shifts it from one horn to the other. It is one of many old stories and belongs to no particular culture or religion.

{{< figure src="weltstier_qazwini.jpg" width="300" caption="Miniature for al-Qazwīnī's cosmography (1595): an angel carries the earth, below it a rock, a bull and a fish. Public domain (Wikimedia Commons)." >}}

Modern geology explains earthquakes by the movement of tectonic plates. Plates of the earth's crust move; at their boundaries stresses build up and are released abruptly.

{{< figure src="platten_usgs.png" width="480" caption="The tectonic plates. Map: USGS, public domain (Wikimedia Commons)." >}}

We accept plate tectonics and not the bull because the theory made predictions that could have failed. If new ocean floor forms at the mid-ocean ridges and spreads apart, the rock on both sides should record the reversals of the earth's magnetic field as stripes that are symmetric about the ridge, and the floor should get older with distance from it. Vine and Matthews (1963) proposed this reading of the stripes; both predictions were confirmed later in the 1960s. Today GPS measures the plate movements directly, at a few centimetres per year.

Deutsch adds a second criterion: a good explanation is *hard to vary* without losing its explanatory power. Replace the bull with an elephant or a dragon, and the story explains the quake just as well. It fixes almost nothing that could be tested. Plate tectonics cannot be changed at will; it depends on measurable movements, rocks and mechanisms.

{{< callout type="info" >}}
Progress means developing better explanations and testing them critically.
{{< /callout >}}

## 2. A paradox: can a new road make traffic worse?

Take a small road network with four nodes: Start, A, B and Goal. Two routes lead from Start to Goal, an upper one via A and a lower one via B. Each route has one narrow road, where the travel time is \(n\) minutes if \(n\) drivers use it, and one wide road without congestion, where the travel time is a fixed \(C\) minutes. The travel time of a route is the sum of its roads. Every driver wants to reach the goal as fast as possible.

{{< figure src="network.png" width="560" caption="The network. On the narrow roads the travel time grows with the number of drivers *n*; on the wide roads it is a constant *C*." >}}

Take 15 drivers and \(C = 17\). Suppose 5 drive the upper route and 10 the lower one. The upper route then takes \(5 + 17 = 22\) minutes and the lower one \(17 + 10 = 27\). Some drivers on the lower route switch. This goes on until the two routes are nearly balanced: with 7 on top and 8 below, the upper route takes 24 minutes and the lower one 25. A driver who switches from the lower to the upper route would then also need 25 minutes, so nobody can improve by switching alone. This state is a **Nash equilibrium**.[^wardrop]

Now the city builds a shortcut from A to B with a travel time of zero. There are three routes: upper, lower, and Start → A → B → Goal.

{{< figure src="network-shortcut.png" width="560" caption="The same network with a shortcut from A to B that takes no time at all." >}}

Start from the old split, 7 drivers on the upper route and 8 on the lower one. One driver from the upper route tries the shortcut. The first narrow road still carries 7 drivers, the second now carries 9. This driver needs \(7 + 0 + 9 = 16\) minutes instead of 24, because the 17-minute wide road is replaced by a narrow road that takes 9 minutes. The driver gains 8 minutes, and everyone on the second narrow road loses one.

Each driver who moves over also gains, though less each time, as long as both narrow roads together cost less than one narrow and one wide road. So the drivers move over, and the narrow roads fill up. In the end all 15 use the shortcut, and each needs \(15 + 0 + 15 = 30\) minutes. A driver who goes back to the upper route alone needs \(15 + 17 = 32\) minutes, more than 30. So nobody leaves the shortcut, although without it everyone would arrive sooner. This is again a Nash equilibrium, but a worse one. The old split of 7 and 8 would be better for everyone, but with the shortcut it is no longer an equilibrium.

{{< figure src="result.png" width="640" caption="The two equilibria for 15 drivers and C = 17. Each driver chooses the fastest route, and the result is worse for all." >}}

{{< details title="The general case" closed="true" >}}
With \(o\) drivers on the upper route, \(u\) on the lower one and \(a\) on the shortcut, the travel times are

$$
\begin{aligned}
t_\text{upper} &= (o + a) + C,\\
t_\text{lower} &= C + (u + a),\\
t_\text{shortcut} &= (o + a) + (u + a).
\end{aligned}
$$

With \(N\) drivers and no shortcut, the equilibrium travel time is about \(N/2 + C\). With the shortcut it is \(2N\) if \(N \le C\) and \(2C\) if \(C \le N \le 2C\); for \(N \ge 2C\) the shortcut stays empty and the time stays \(N/2 + C\). The paradox therefore occurs when \(N/2 < C < 3N/2\). Here \(N = 15\) and \(C = 17\). With \(C = 20\), the paradox disappears for fewer than about 14 drivers, and again for 40 or more.
{{< /details >}}

Try it yourself. The game keeps \(C = N + 2\), so \(C\) changes with the number of drivers. Move the drivers between the routes, switch the shortcut on, and watch where the travel times settle. The box below the bars tells you whether anyone can still gain by switching.

{{< braess-game >}}

### The paradox has a name

This network has exactly the structure of the paper by Dietrich Braess, a mathematician at the University of Münster, published in German in 1968 in *Unternehmensforschung* under the title "Über ein Paradoxon aus der Verkehrsplanung". Braess did not observe the paradox in traffic; he found it in a model. It was theoretical work motivated by traffic planning, basic research. This fits Popper: explanations start as conjectures, which are then criticised. Observations in cities came only later.

The idea travelled. Wardrop stated the equilibrium principle in 1952: in equilibrium, all used routes are equally fast. Braess found the surprising consequence in 1968. Cohen and Horowitz showed the same paradox with springs and strings in 1991. An English translation made the paper widely accessible in 2005. Today it is an argument in traffic planning: more roads do not automatically help.

### What we know now

Each driver chooses the fastest route, and the result is worse for all. That is what the model predicts. But the model assumes that travel time grows with the number of vehicles, that everyone chooses the fastest route and that the new road takes no time.

Three levels have to be kept apart. The mathematical result is knowledge, but knowledge about the model. Whether real traffic behaves like this is an empirical question. Scientific knowledge means building models, testing their predictions and finding out when a model is useful. When people play this game, their result is an observation; the numbers above are the theoretical equilibrium. If the two differ, that is already the first lesson.

## 3. What makes an explanation good?

Here are two explanations for the paradox.

{{< figure src="explanations.png" caption="Two explanations for the same result." >}}

Explanation A sounds plausible but names no mechanism. "Selfish" could explain the opposite result as well, and A does not say under which conditions the paradox occurs. A is the bull of this story: you could put any other word in place of "selfish". Explanation B says which roads fill up and why. B connects assumptions to consequences. We can change an assumption, for example the travel time of the shortcut, but then the model fixes what follows, so B cannot be adjusted to fit any outcome. That is why B makes predictions.

A test: what happens if the shortcut takes 5 minutes instead of none? B predicts that the paradox remains but becomes weaker. With the same 15 drivers, the drivers need 27 to 29 minutes, depending on the split, instead of 30, compared with 24 to 25 without the shortcut. Once the shortcut takes 9 minutes or more (about \(C - N/2\) for \(N\) drivers in general), nobody uses it any more, and everything is as before. Explanation A cannot even address this question.

{{< callout type="info" >}}
A good explanation cannot be changed at will without ceasing to explain anything. (After David Deutsch, *The Beginning of Infinity*, 2011, ch. 1.)
{{< /callout >}}

Deutsch's criterion says something about the quality of an explanation. Testing against experience is still needed.

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

A model should be as simple as possible, but complex enough for the question. **Ockham's razor** says the same: if two models explain an observation equally well, the simpler one is preferable. A good model captures the relevant mechanisms and gives useful explanations and predictions for its purpose, however few details it contains. Box (1976) wrote: "Since all models are wrong the scientist must be alert to what is importantly wrong." In the road network, the colour of the cars does not matter; the assumptions about route choice and congestion are the mechanism itself. Whether we left out the right things is a question for validation (section 7).

Three terms are often mixed up:

- **Assumption:** "Drivers choose the route that is fastest for them." This is an assumption about behaviour. It is assumed within the model; whether people behave this way is a separate, testable question. It is not a theory. The model consists of the network plus this assumption.
- **Theory:** a coherent set of statements built on such assumptions, from which consequences can be derived. Here it is the equilibrium theory of route choice after Wardrop (1952). Its first principle: in equilibrium the travel times on all used routes are equal, and no unused route is faster.
- **Hypothesis:** a concrete prediction that follows from the theory and can fail against data. For example: "If road Y in network X is closed, the mean travel time decreases."

The touchstone for a hypothesis is one question: which observation would refute it? If you cannot say, it is not yet a hypothesis.

### Verify or falsify?

Karl Popper (*Logik der Forschung*, 1934; *Conjectures and Refutations*, 1963, ch. 1) pointed out that general statements can never be proven conclusively, because nobody has seen all cases. Every white swan confirms the statement "All swans are white", but none proves it. A single black swan refutes it.

The same holds for traffic. A hundred cities in which a new road helped do not prove that new roads always help. One Braess case is enough to refute it, but only because the statement is universal ("always"). Against "mostly", a single counterexample does not help.

In practice a refutation is rarely this clean. A prediction always rests on auxiliary assumptions about instruments, data and conditions. When a prediction fails, something in this group of assumptions is wrong, but the failure does not say which part (Duhem 1954, part II, ch. 6); it may be an auxiliary assumption instead of the theory. This is known as the Duhem–Quine problem, and it is one reason why a single surprising observation rarely settles a dispute.

Popper asks: can the statement fail? Deutsch adds: does it explain why it must be so? Good scientific explanations do both.

Back to the earthquake: which observation could show that plate tectonics is wrong? Magnetic stripes that are not symmetric about the ridges, for example, ocean floor of the same age everywhere, or GPS measurements that show no plate movement. The story of the bull forbids nothing, so no observation can refute it.

One warning about words: in simulation, "verification" means something else, namely checking the program (section 7).

## 5. How do we test explanations?

### Observations from cities

Three cases are often cited for the Braess paradox:

- **Stuttgart 1969:** a new road makes traffic worse. Only when it is closed again does traffic improve (Knödel 1969, as reported by Rapoport et al. 2009).
- **New York 1990:** 42nd Street is closed on Earth Day. Congestion, if anything, decreases (Kolata 1990).
- **Seoul 2003–2005:** an urban motorway is demolished. At first traffic gets slower, while many people switch to the subway.

As evidence for Braess they are weak (Rapoport et al. 2009, p. 539, call them "sketchy and mostly anecdotal"): they are observations after an intervention, not controlled experiments. What else changed? In Seoul, trips shifted to the subway over several years (Chung et al. 2012). The shift to the subway may be part of the response to the demolition, or it may have other causes; the observations alone do not tell. In reality many things change at once. An experiment tries to isolate one cause.

### Experiment

Suppose a group of 15 people plays the route game, first without the shortcut and then with it, and they end up slower the second time. That does not yet show that the shortcut caused the difference. Perhaps they decided differently the second time because they already knew the game. Perhaps they were better informed, or understood the rules differently.

A clean comparison has two trials. In trial A everyone chooses between two routes; in trial B the same people choose between three. The number of people, the travel-time rules, the information and as far as possible all other conditions stay the same. Better still: vary the order of the trials between groups, run several rounds and compare.

{{< callout type="info" >}}
An experiment deliberately changes one condition and studies its effect.
{{< /callout >}}

Such a game tests the effect of the shortcut within the model. It is not yet evidence about real road networks.

Rapoport and colleagues (2009) ran this game in the laboratory with groups of 18 students, paid according to their travel costs, for 40 rounds without and 40 rounds with the shortcut. Reversing the order made no difference. In a network with the same structure as ours, the groups moved to the shortcut route, and their payoff per round fell from about 95 to about 40 points. In a larger network with five routes, choices moved the same way, but after 80 rounds some players still used the old routes.

## 6. When explanations fail: Clever Hans

Even careful experiments can miss something decisive. Around 1900 a horse, "Clever Hans", answered arithmetic questions by tapping its hoof, in front of large audiences and mostly correctly. Many experts were convinced, and a commission found no trick in 1904.

{{< figure src="clever_hans.jpg" caption="Clever Hans at a public demonstration, 1904. From K. Krall, *Denkende Tiere* (1912), plate 2. Public domain (Wikimedia Commons)." >}}

His owner, Wilhelm von Osten, a mathematics teacher and follower of phrenology, was convinced that animals can think. The psychologist Oskar Pfungst was not satisfied with this explanation. He worked carefully with Hans and von Osten and changed one factor at a time: whether the questioner knew the answer, whether Hans could see the questioner (using blinkers), how far away the questioner stood (Pfungst 1907).

| Condition | Result |
|---|---|
| The questioner knows the answer | mostly correct |
| The questioner does not know it | many more errors |
| Hans cannot see the questioner | many more errors |

Hans read tiny body signals of the questioner, who relaxed without noticing as soon as the right number was reached. Two explanations competed: "Hans can do arithmetic" and "Hans reads unconscious signals". Both fit the correct answers. Only the second predicts that Hans fails when nobody he can see knows the answer. An experiment that tells two explanations apart produces knowledge. The second explanation wins because it passes the targeted test, whether or not it sounds simpler. Von Osten never accepted the result.

The observation was real; the explanation was wrong, because one influence had been overlooked. An experiment is not automatically a good experiment, and, as with Braess, a correct observation does not guarantee a correct explanation. That many experts were convinced was no argument; knowledge rests on criticism.

The episode gave its name to the **Clever Hans effect**: the expectations of observers unconsciously influence the behaviour of those observed. Related are the experimenter effect (Rosenthal 1966) and the interviewer effect in surveys. Today's countermeasures are blinding and control conditions. Science means looking for evidence for one's own explanation and also finding out where one might be wrong, including in one's own experimental design.

### Criticism as a shared practice

Pfungst found the error because he could work with the horse, change the conditions one at a time and publish what he did. Science relies on this kind of access more than on the objectivity of individual scientists, a point Popper made in *The Open Society and Its Enemies* (1945). A result comes with its methods and data, so that others can check the calculations, repeat the measurements, collect new observations and test alternative explanations. An error that survives one investigation can show up in the next. This works only when methods and data are shared and the checks are done; publication alone does not do it (see National Academies 2019 on transparency and replication).

An expert's reputation does not make a claim correct. That does not put every opinion on the same level either. The useful questions are what evidence supports a claim and how well it has held up under informed, independent checks. Oreskes (2019) argues that trust in science rests on this collective, critical scrutiny within diverse expert communities.

## 7. Simulation, verification and validation

The network above has four nodes; you can work it out in your head. A city network has tens of thousands of links, travel times depend nonlinearly on load, and people decide differently. Then you need numerical methods and software, for example SUMO, MATSim, Vissim or, for pedestrians, JuPedSim.

Suppose the fundamental diagram, the relation between density and flow, is well known from experiments. We derive travel times from it, build a network model with route choice and simulate it. Even then the simulation does not necessarily predict the Braess paradox reliably.

If the software reproduces the analytical equilibrium for the Braess network exactly, that shows only that it computes correctly. An important verification test has been passed, but that is not validation. And even with correct software and a well-supported fundamental diagram the predictions can be wrong: people may choose routes differently than assumed, and queues, differences in information or effects over time may be missing. One valid component does not make a valid overall system.

The tempting conclusion is: "The input models are validated and the software passes all tests, so the simulation is realistic." It does not follow. Two questions have to be asked separately: did we implement the model correctly, and did we choose the right model?

{{< figure src="vv.png" caption="Verification compares the program with the model; validation compares the model with reality." >}}

- **Verification:** does the program compute what the model says? Has the model been implemented correctly and solved numerically? This is checked with tests and comparisons with exact solutions, looking for errors in code and numerics.
- **Validation:** does the model describe reality well enough for its intended purpose? This is checked against measured data. A model is always valid for a purpose, never absolutely.

Roache (1998), following Boehm and Blottner, put it briefly: verification means solving the equations right, validation means solving the right equations. A program can be perfectly verified and still not valid. And this "verification" is not Popper's.

{{< details title="A note on standards" closed="true" >}}
For pedestrian simulations the German guideline RiMEA (Richtlinie für Mikroskopische Entfluchtungsanalysen, version 4.1.1, 2025) lists test cases 1 to 16 in its Annex 1. RiMEA uses verification and validation interchangeably; its four forms of verification follow ISO/TR 13387-8:1999 (Annex 1, A 1). What it calls "quantitative verification", the comparison with data from evacuation drills, is validation in the AIAA sense (AIAA G-077-1998), and RiMEA itself regards the data as insufficient for it (A 5). The NIST report on evacuation models makes the same correction for the IMO guidelines (Ronchi et al. 2013).
{{< /details >}}

## 8. Models, experiments and observations of crowds

In pedestrian dynamics these questions are part of our daily work. We build models, run experiments with hundreds of participants and observe people at stations, stadiums and events. Each method draws criticism. Models simplify behaviour. Participants in an experiment know that they are in an experiment. Observations in public spaces are limited by privacy, and their conditions cannot be controlled. Simulations are still used to plan buildings and events, and decisions about evacuation have to be made with the evidence available.

The criticism is often general: "models are just models", "people don't behave like that", "experiments are not reality". Each points to a real problem, but none says which conclusion is affected. The terms of this essay turn them into questions that can be checked:

| Objection | Question to ask |
|---|---|
| "Models are just models." | Which simplification could change the result we are using? |
| "People don't behave like that." | Which behaviour is missing, for which people and situation, and which prediction does it affect? |
| "Experiments are not reality." | Which findings carry over to the target situation, and which depend on the experimental setting? |
| "Field observations are too messy." | What can be measured reliably, and which influences can be told apart? |
| "We ran thousands of simulations." | Which uncertainty did the runs reduce, and which assumptions stayed untested? |

A common argument is that a simulation deserves more trust than an experiment, because it can be run thousands of times and an experiment cannot. Repeated runs of a stochastic model are useful. They show when the mean evacuation time, its spread and the shape of the evacuation curve stop changing (Ronchi et al. 2014). If a model assumes that everyone knows all exits and takes the fastest route, a million runs with different random seeds will never produce a person who does not know the way. Models have to make such assumptions about behaviour, often without data to support them (Kuligowski 2013). Convergence shows how precisely we know the model's answer; only data show whether that answer describes these people (section 7).

{{< figure src="convergence.png" caption="Illustration with synthetic data: the running mean of a stochastic model settles on the model's own value as the runs accumulate, while a measured drill value stays where it is. ([Script](convergence.py))" >}}

The same care applies to experiments. An experiment observes real people, in a particular situation. A bottleneck experiment with instructed participants supports conclusions about movement under those instructions, densities and geometries. Whether they hold for another population, a different motivation or an emergency is a separate question. Field observations have the opposite problem: they are closer to the target situation, but many factors vary at once, and being natural does not make them valid (Haghani 2023).

The methods check different parts of an explanation. An experiment can isolate a mechanism, an observation can check whether it transfers, and a simulation works out the consequences under conditions that cannot be tested directly. These methods help each other because their weaknesses differ; several sources that share a weakness would not.

Human behaviour is varied, so a model can support only narrow claims. "Our model reproduces human behaviour" is too broad to test. "Our model estimates the flow through this exit, for this population and these conditions, with this uncertainty" can be tested. Estimating the flow through a given exit is also a different task from predicting which exit people choose. The second rests on assumptions about behaviour that movement data do not test.

We ran into this in our own work. In a [calibration study]({{< relref "/notes/dakota-calibration" >}}) we fitted JuPedSim's Collision Free Speed model to a bottleneck experiment. The calibrated model matched flow, density and speed in front of the opening mostly within ten percent, also at two widths left out of the fit. Two optimizer starts gave two parameter sets that fit almost equally well but differ by factors of two to four, so a good fit did not pin down the parameters. Hydrologists call this equifinality: different parameter sets, and even different models, can fit the same data acceptably well (Beven 2006). These data cannot tell them apart; the difference can show when the model is used somewhere else. In the [second part]({{< relref "/notes/dakota-validation" >}}) the same parameters went, without refitting, to a half-metre gate and an entrance without guiding barriers. At the gate one set stalls and the other is 20 to 40 % too fast; at the entrance every set empties the crowd two to three times faster than the people did. A model calibrated for one situation was not valid for the next.

Guidelines such as RiMEA list test cases for simulation software. Such tests catch errors and make results easier to compare. Their results can also be used for claims they cannot support. "The software passes the RiMEA tests" can become "the software is validated", then "the results of this project are reliable" and finally "this design is safe". Each step is a new claim and needs its own evidence. RiMEA does not set pass limits for most of its tests (RiMEA 2025, Annex 1, A 2). The first test checks, by design, only that a person with a given walking speed crosses a corridor in the expected time. Whether that speed fits the people in the building, or whether they find the exits, is outside its scope.

RiMEA warns against this itself. Its preamble calls a simulation "an idealized case" in which people move as the user specifies, and it states that there are not enough reliable data from evacuation drills for a thorough quantitative comparison. Until such data exist, it regards its other tests as sufficient (Annex 1, A 5). This sentence is a translation from the IMO guidelines for passenger ships (IMO 2002), and it has stayed unchanged since then, in later IMO versions (IMO 2016) as in RiMEA, while laboratory data have appeared that RiMEA itself now uses. IMO, RiMEA, the NIST report (Ronchi et al. 2013) and ISO 20414 share many of their tests, and most of these come from the same IMO list. In my view their agreement therefore counts only once. RiMEA's later tests compare models with laboratory data, mostly for trends or the spread of the data, and the user may vary the parameters. Once software is tuned to pass a test, passing it says less about anything outside the test (Goodhart 1984; Strathern 1997). ISO 20414 (2020) asks for more: the field of application must be stated, validation against one data set does not necessarily carry over to other scenarios, and validation runs must also use default or generally representative settings, not only settings tuned to the data. The tests themselves should be tested. We need to know which errors that would change a safety conclusion they can reveal, and which wrong predictions still pass them. The same applies to our own software. Passing a standard is one part of the argument for trusting a simulation. The rest has to come from evidence about the people, the building and the purpose.

A useful criticism names an omission and says why it matters. For example: "The model does not include groups who wait for each other. This matters here, because the predicted benefit of the second exit depends on people spreading out independently." Such a criticism can be checked, and it may be strong enough to rule out one particular use of the model.

For practical projects the question becomes: what evidence is enough for this model to support this decision? "Layout A gives a shorter mean evacuation time in this simulation", "Layout A is faster under every behavioural assumption we tested" and "Layout A is safer for the people who will use it" are three different claims, and each needs more evidence than the one before. The third also needs a safety criterion, for example that everyone is out before conditions become untenable (ASET > RSET); a layout can be faster on average and worse for the last people out. Sometimes the answer is that the evidence does not support the proposed safety claim.

## 9. How scientific knowledge improves

### What moves around what?

Even a wrong or limited model can describe observations quite well. Ptolemy's geocentric model predicted planetary positions usefully for centuries and was refined mathematically again and again. Copernicus' heliocentric model (1543) was at first not more accurate in every respect; it still used circular orbits.

{{< figure src="cellarius_ptolemaeus.jpg" width="520" caption="The geocentric world view: the earth at the centre. Andreas Cellarius, *Harmonia Macrocosmica* (1660). Public domain (Wikimedia Commons)." >}}

{{< figure src="cellarius_kopernikus.jpg" width="520" caption="The heliocentric world view: the earth moves around the sun. Andreas Cellarius, *Harmonia Macrocosmica* (1660). Public domain (Wikimedia Commons)." >}}

Only Kepler's elliptical orbits (*Astronomia nova*, 1609), Galileo's observations with the telescope (1610, among them the phases of Venus) and later Newton's theory of gravitation (1687) made it the much more convincing explanation. The geocentric model was replaced step by step, between 1543 and 1687. Knowledge grows this way, by improving and replacing models.

It follows that a model that reproduces the data has not yet shown that its mechanism is right. Ptolemy, too, fitted the data. This leads to the question of what really caused a result.

### Causality

Causality means: A causes B. In the route game the chain is clear. The road does not change the travel time directly; it changes behaviour, and behaviour changes the travel time. This can be shown because the game compares with and without the road while everything else stays the same.

{{< figure src="causality.png" caption="In the controlled game the causal chain can be shown. In Seoul it cannot: without a comparison, a sequence in time is only a correlation." >}}

Seoul is harder. After the urban motorway was demolished, traffic first got slower, and many trips moved to the subway (Chung et al. 2012). Whether the demolition was the cause stays open. Without a comparison this is only a correlation in time. And a falsification in Popper's sense needs a reliable observation, which is exactly what is uncertain in the city cases.

### Interaction

The causal chain has a catch: drivers also react to each other. Interaction means that two quantities influence each other in a feedback loop. In the route game my route choice changes your travel time, your travel time changes your route choice, and that changes mine again.

{{< figure src="interaction.png" width="560" caption="Everyone influences everyone." >}}

In this model the new road changes the outcome through the drivers' responses to each other. The road is a cause, and it acts through this feedback. Identifying a cause does not mean that it acts alone. Such feedback is the rule in traffic and pedestrian dynamics.

## 10. What science can and cannot tell us

### From basic research to application

Basic research wants to understand, without a direct use in view. Applied research wants to solve a problem. The boundary is open. Braess' paper was mathematics in 1968; today the argument is part of traffic planning. Peter Grünberg at Forschungszentrum Jülich discovered giant magnetoresistance, at the same time as Albert Fert; it led to read heads for hard disks, and both received the Nobel Prize in 2007. GPS works only with corrections from the theory of relativity. Applied research often ends up in standards and guidelines (DIN, FGSV, VDI), which should rest on well-founded knowledge.

### The same questions, a different theory

The questions from the traffic example apply far beyond traffic. Gustave Le Bon (*The Crowd*, 1895) still shapes the popular image of "mass panic". In his words, individuals in a crowd are changed because "the fact that they have been transformed into a crowd puts them in possession of a sort of collective mind" (English translation of 1896).

A thought experiment: you are a Dortmund fan in the Bayern Munich block, and Dortmund scores in the last minute. What do you feel?

The questions from section 3 apply to the "collective mind": what exactly it explains, which mechanism lies behind it and which observation would refute it. It is supposed to explain aggressive crowds as well as peaceful ones. If it can be adapted this freely, it explains everything, and therefore nothing. Further reading: Clarke (2002), Drury, Novelli and Stott (2013), Haghani et al. (2019).

### Predictions and decisions

Suppose a well-tested model predicts that closing a road reduces the mean travel time. The prediction alone does not decide whether the road should be closed. Some travellers gain and others lose, and access to particular places, costs and safety count as well. Weighing them requires stating what we want to achieve. Science can say what is likely to happen under each option; which outcome to prefer is a decision about goals. Values also enter the science itself, for example when deciding how much evidence is enough to accept a claim, given the consequences of being wrong (Douglas 2009, ch. 5).

### How to evaluate a claim

The questions used throughout this essay work for any claim, in a newspaper, a report or one's own thesis:

1. What exactly is explained, and what is the mechanism?
2. Could the explanation be changed at will and still "explain" the same thing?
3. Which observation would refute it?
4. What evidence separates the explanation from plausible alternatives: a controlled comparison, independent observations that agree, or only a sequence in time?
5. Was a model checked against reality, and for which purpose is it valid?

Controlled experiments are one way to answer question 4. Where they are impossible, as for earthquakes or planetary orbits, independent observations can do this, when they test predictions that the alternatives get wrong.

An example of how a question becomes testable: "A bottleneck 3 m wide and 1 m long, or 1 m wide and 3 m long: which is better?" As it stands, this is not yet a scientific question. One has to fix the walking direction (the width across the direction of walking matters most; in one experiment the length made little difference between 2 and 4 m, and only an opening a few centimetres deep let noticeably more people through; Liddle et al. 2009, 2022), the geometry, and what "better" means: higher flow, shorter evacuation time or lower density in front of the bottleneck. Only then does an intuitive question become a testable hypothesis. As with Braess, one changes the geometry and asks what happens to the flow.

### How much confidence a result deserves

Scientific knowledge can be revised, and its parts are uncertain to very different degrees. A new conjecture and an explanation that has passed many independent tests do not have the same standing. Plate tectonics has passed tests from magnetic stripes, the age of the ocean floor and GPS; the story of the bull has passed none. The question to ask is how well an explanation has survived attempts to find its weaknesses, what evidence supports it and where its limits lie.

The road network shows the same gradation. That all 15 drivers end up at 30 minutes follows from the rules of the model, and anyone can check the arithmetic. Whether a real city behaves this way depends on further questions: how people choose routes, how travel times vary and whether the model contains the effects that matter. Confidence in the calculation and confidence in its application are two different things.

### Summary

1. Problem: we meet something surprising that we want to understand.
2. Explanation: we look for a mechanism that is hard to vary.
3. Testing: we check whether the explanation holds.
4. Improvement: we replace it when a better one survives the tests.
5. Application: we use it, within the limits the tests have shown.

Scientific knowledge is provisional, testable, methodically grounded and correctable. We know more today than 300 years ago because we form explanations, criticise them and improve them, instead of only collecting observations: the bull and plate tectonics, Ptolemy and Kepler and Newton, whose *Principia* appeared in 1687, almost 340 years ago.

{{< callout type="info" >}}
Science means developing explanations, finding their errors and replacing them with better ones. It has no final answers, but some of its answers have survived far more tests than others.
{{< /callout >}}

## Further reading

- David Deutsch, *The Beginning of Infinity* (2011), chapter 1, "The Reach of Explanations". A shorter text by him: ["Why It's Good To Be Wrong"](https://nautil.us/why-its-good-to-be-wrong-234374/), *Nautilus*, 23 May 2013.
- Karl Popper, *Conjectures and Refutations* (1963), chapter 1, "Science: Conjectures and Refutations".
- Naomi Oreskes, *Why Trust Science?* (2019).
- Peter Godfrey-Smith, *Theory and Reality: An Introduction to the Philosophy of Science* (2nd edition, University of Chicago Press, 2021), an introduction to the philosophy of science that compares several views.

## Further material

- [Slides of the lecture](/teaching/scientific-working-2026/) ([PDF](/teaching/scientific-working-2026/What_is_science_slides.pdf))
- [Companion text of the lecture](/teaching/scientific-working-2026/What_is_science_companion.pdf) (PDF)

## References

- AIAA (1998): *Guide for the Verification and Validation of Computational Fluid Dynamics Simulations*. AIAA G-077-1998.
- Beven, K. (2006): A manifesto for the equifinality thesis. *Journal of Hydrology* 320(1–2), 18–36. doi:10.1016/j.jhydrol.2005.07.007.
- Box, G. E. P. (1976): Science and Statistics. *Journal of the American Statistical Association* 71(356), 791–799. doi:10.1080/01621459.1976.10480949.
- Braess, D. (1968): Über ein Paradoxon aus der Verkehrsplanung. *Unternehmensforschung* 12, 258–268.
- Braess, D., Nagurney, A., Wakolbinger, T. (2005): On a Paradox of Traffic Planning. *Transportation Science* 39(4), 446–450.
- Chung, J.-H., Hwang, K. Y., Bae, Y. K. (2012): The loss of road capacity and self-compliance: Lessons from the Cheonggyecheon stream restoration. *Transport Policy* 21, 165–178.
- Clarke, L. (2002): Panic: Myth or Reality? *Contexts* 1(3).
- Cohen, J. E., Horowitz, P. (1991): Paradoxical behaviour of mechanical and electrical networks. *Nature* 352, 699–701.
- Deutsch, D. (2011): *The Beginning of Infinity: Explanations That Transform the World*. London: Allen Lane.
- Douglas, H. E. (2009): *Science, Policy, and the Value-Free Ideal*. Pittsburgh: University of Pittsburgh Press.
- Drury, J., Novelli, D., Stott, C. (2013): Psychological disaster myths in the perception and management of mass emergencies. *Journal of Applied Social Psychology* 43(11), 2259–2270.
- Duhem, P. (1954): *The Aim and Structure of Physical Theory*. Translated by P. P. Wiener. Princeton: Princeton University Press.
- Goodhart, C. A. E. (1984): Problems of monetary management: the U.K. experience. In: *Monetary Theory and Practice: The UK Experience*. London: Macmillan, 91–121. doi:10.1007/978-1-349-17295-5_4.
- Haghani, M. (2023): The notion of validity in experimental crowd dynamics. *International Journal of Disaster Risk Reduction* 93, 103750.
- Haghani, M., Cristiani, E., Bode, N. W. F., Boltes, M., Corbetta, A. (2019): Panic, Irrationality, and Herding: Three Ambiguous Terms in Crowd Dynamics Research. *Journal of Advanced Transportation*, 9267643.
- IMO (2002): *Interim Guidelines for Evacuation Analyses for New and Existing Passenger Ships*. MSC/Circ.1033. London: International Maritime Organization.
- IMO (2016): *Revised Guidelines on Evacuation Analysis for New and Existing Passenger Ships*. MSC.1/Circ.1533. London: International Maritime Organization.
- ISO/TR 13387-8 (1999): *Fire safety engineering — Part 8: Life safety — Occupant behaviour, location and condition*. Geneva: ISO (withdrawn).
- ISO 20414 (2020): *Fire safety engineering — Verification and validation protocol for building fire evacuation models*. Geneva: ISO.
- Knödel, W. (1969): *Graphentheoretische Methoden und ihre Anwendungen*. Berlin: Springer.
- Kolata, G. (1990): What if They Closed 42d Street and Nobody Noticed? *New York Times*, 25 December 1990. Free summary: ["42nd Street: Braess's Paradox"](https://blogs.cornell.edu/info2040/2016/09/14/42nd-street-braess-paradox/), Cornell course blog *Networks*, 2016.
- Kuligowski, E. (2013): Predicting Human Behavior During Fires. *Fire Technology* 49(1), 101–120.
- Le Bon, G. (1895): *Psychologie des foules*. English: *The Crowd: A Study of the Popular Mind* (1896).
- Liddle, J., Seyfried, A., Klingsch, W., Rupprecht, T., Schadschneider, A., Winkens, A. (2009): An Experimental Study of Pedestrian Congestions: Influence of Bottleneck Width and Length. arXiv:0911.4350.
- Liddle, J., Seyfried, A., Steffen, B., Klingsch, W., Rupprecht, T., Winkens, A., Boltes, M. (2022): Microscopic insights into pedestrian motion through a bottleneck, resolving spatial and temporal variations. *Collective Dynamics* 7, A139, 1–23. doi:10.17815/CD.2022.139.
- National Academies of Sciences, Engineering, and Medicine (2019): *Reproducibility and Replicability in Science*. Washington, DC: The National Academies Press. doi:10.17226/25303.
- Oreskes, N. (2019): *Why Trust Science?* Princeton: Princeton University Press.
- Pfungst, O. (1907): *Das Pferd des Herrn von Osten (Der Kluge Hans)*. Leipzig: Barth.
- Popper, K. (1934): *Logik der Forschung*. Wien: Springer.
- Popper, K. (1945): *The Open Society and Its Enemies*. London: Routledge.
- Popper, K. (1963): *Conjectures and Refutations: The Growth of Scientific Knowledge*. London: Routledge & Kegan Paul.
- Rapoport, A., Kugler, T., Dugar, S., Gisches, E. J. (2009): Choice of routes in congested traffic networks: Experimental tests of the Braess Paradox. *Games and Economic Behavior* 65(2), 538–571.
- RiMEA (2025): Richtlinie für Mikroskopische Entfluchtungsanalysen, version 4.1.1.
- Roache, P. J. (1998): Verification of codes and calculations. *AIAA Journal* 36(5), 696–702.
- Ronchi, E., Kuligowski, E. D., Reneke, P. A., Peacock, R. D., Nilsson, D. (2013): *The Process of Verification and Validation of Building Fire Evacuation Models*. NIST Technical Note 1822.
- Ronchi, E., Reneke, P. A., Peacock, R. D. (2014): A method for the analysis of behavioural uncertainty in evacuation modelling. *Fire Technology* 50(6), 1545–1571.
- Rosenthal, R. (1966): *Experimenter Effects in Behavioral Research*. New York: Appleton-Century-Crofts.
- Schäfer, B. et al. (2022): Understanding Braess' Paradox in power grids. *Nature Communications* 13, 5396.
- Strathern, M. (1997): 'Improving ratings': audit in the British University system. *European Review* 5(3), 305–321.
- Vine, F. J., Matthews, D. H. (1963): Magnetic anomalies over oceanic ridges. *Nature* 199, 947–949.
- Wardrop, J. G. (1952): Some Theoretical Aspects of Road Traffic Research. *Proceedings of the Institution of Civil Engineers* Part II 1(3).

[^wardrop]: Traffic research uses the related **Wardrop equilibrium** (Wardrop 1952): the travel times on all used routes are equal, and no unused route is faster. It is usually stated for so many drivers that a single one does not change the travel times. With 15 drivers, one driver changes a narrow road by a whole minute, so in a Nash equilibrium the used routes can differ by one minute, here 24 and 25.

*Disclosure:* The author's group develops JuPedSim, simulation software to which such tests apply. Some of the laboratory data that RiMEA uses in its tests, and the bottleneck studies cited above (Liddle et al. 2009, 2022), come from Armin Seyfried and colleagues at Forschungszentrum Jülich, where the author works.

{{< icon "pencil-alt" >}} By: [Mohcine Chraibi]({{< relref "/authors#MohcineChraibi" >}})
