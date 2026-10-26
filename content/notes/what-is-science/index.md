---
title: "What makes an explanation good? Lessons from a road paradox"
date: 2026-10-21
summary: A good explanation makes specific consequences follow from explicit assumptions, and tests show how far those consequences can be trusted. A small road network in which a new road makes everyone slower shows both, and what they mean for crowd simulations and the standards that judge them.
math: true
thumbnail: network-shortcut.png
---

{{< callout type="info" icon="none" >}}
**What makes an explanation good, and how far can we trust it?** This essay follows one example, a road network in which a new road makes everyone slower. It was inspired by Armin Seyfried's first lecture of *Scientific Working* at the University of Wuppertal in October 2026.
{{< /callout >}}

In 1968 the mathematician Dietrich Braess showed, in a model, that a new road can make every driver slower. He found the paradox before the often-cited reports from real road networks. A good explanation of such a result makes specific consequences follow from explicit assumptions. Tests then show how far those consequences hold when the explanation is applied outside the model. The road network shows both steps.

## 1. A road that makes everyone slower

Take a small road network with four nodes: Start, A, B and Goal. Two routes lead from Start to Goal, an upper one via A and a lower one via B. Each route has one narrow road, where the travel time is \(n\) minutes if \(n\) drivers use it, and one wide road without congestion, where the travel time is a fixed \(C\) minutes. The travel time of a route is the sum of its roads. Every driver wants to reach the goal as fast as possible.

{{< figure src="network.png" width="560" caption="The network. On the narrow roads the travel time grows with the number of drivers *n*; on the wide roads it is a constant *C*." >}}

Take 15 drivers and \(C = 17\). Suppose 5 drive the upper route and 10 the lower one. The upper route then takes \(5 + 17 = 22\) minutes and the lower one \(17 + 10 = 27\). Some drivers on the lower route switch. This goes on until the two routes are nearly balanced: with 7 on top and 8 below, the upper route takes 24 minutes and the lower one 25. A driver who switches from the lower to the upper route would then also need 25 minutes, so nobody can improve by switching alone. This state is a **Nash equilibrium**.[^wardrop]

Now the city builds a shortcut from A to B with a travel time of zero. There are three routes: upper, lower, and Start → A → B → Goal.

{{< figure src="network-shortcut.png" width="560" caption="The same network with a shortcut from A to B that takes no time at all." >}}

Start from the old split, 7 drivers on the upper route and 8 on the lower one. One driver from the upper route tries the shortcut. The first narrow road still carries 7 drivers, the second now carries 9. This driver needs \(7 + 0 + 9 = 16\) minutes instead of 24, because the 17-minute wide road is replaced by a narrow road that takes 9 minutes. The driver gains 8 minutes, and everyone on the second narrow road loses one.

Each driver who moves over also gains, though less each time, as long as both narrow roads together cost less than one narrow and one wide road. So the drivers move over, and the narrow roads fill up. In the end all 15 use the shortcut, and each needs \(15 + 0 + 15 = 30\) minutes. A driver who goes back to the upper route alone needs \(15 + 17 = 32\) minutes, more than 30. So nobody leaves the shortcut, although without it everyone would arrive sooner. This is again a Nash equilibrium, but a worse one. The old split of 7 and 8 would be better for everyone, but with the shortcut it is no longer an equilibrium.

{{< figure src="result.png" width="640" caption="The two equilibria for 15 drivers and C = 17: 24 to 25 minutes without the shortcut, 30 minutes with it." >}}

{{< details title="The general case" closed="true" >}}
This box uses the continuous-flow approximation of the footnote: so many drivers that one alone does not change the travel times. With \(o\) drivers on the upper route, \(u\) on the lower one and \(a\) on the shortcut, the travel times are

$$
\begin{aligned}
t_\text{upper} &= (o + a) + C,\\
t_\text{lower} &= C + (u + a),\\
t_\text{shortcut} &= (o + a) + (u + a).
\end{aligned}
$$

With \(N\) drivers and no shortcut, the equilibrium travel time is \(N/2 + C\). With the shortcut it is \(2N\) if \(N \le C\) and \(2C\) if \(C \le N \le 2C\); for \(N \ge 2C\) the shortcut stays empty and the time stays \(N/2 + C\). The paradox therefore occurs when \(N/2 < C < 3N/2\). Here \(N = 15\) and \(C = 17\). With \(C = 20\), the paradox disappears for fewer than about 14 drivers, and again for 40 or more.
{{< /details >}}

Try it yourself. The game keeps \(C = N + 2\), so \(C\) changes with the number of drivers. Move the drivers between the routes, switch the shortcut on, and watch where the travel times settle. The box below the bars tells you whether anyone can still gain by switching.

{{< braess-game >}}

This network has the structure of Braess' paper, published in German in 1968 in *Unternehmensforschung* under the title "Über ein Paradoxon aus der Verkehrsplanung" and in English translation in 2005 (Braess et al. 2005). It builds on Wardrop's equilibrium principle of 1952. In the terms of Karl Popper (*Conjectures and Refutations*, 1963), the explanation started as a conjecture. Today it is an argument in traffic planning: more roads do not automatically help.

## 2. What explains the result?

Here are two explanations for the paradox.

{{< figure src="explanations.png" caption="Explanation A blames selfish drivers. Explanation B says which route is cheapest for each driver and how its load grows." >}}

Explanation A sounds plausible but names no mechanism. "Selfish" could explain the opposite result as well, and A does not say under which conditions the paradox occurs. Explanation B says which roads fill up and why. B connects assumptions to consequences. We can change an assumption, for example the travel time of the shortcut, but then the model fixes what follows, so B cannot be adjusted to fit any outcome. That is why B makes predictions.

B also shows how the road acts. The road does not change the travel time directly; it changes behaviour, and behaviour changes the travel time. The drivers also react to each other: my route choice changes your travel time, your travel time changes your route choice, and that changes mine again.

{{< figure src="interaction.png" width="560" caption="The feedback loop in the route game: my route changes your travel time, your travel time changes your route, and your route changes my travel time." >}}

In this model the new road changes the outcome through the drivers' responses to each other. The road is a cause, and it acts through this feedback. Such feedback is the rule in traffic and pedestrian dynamics.

A test: what happens if the shortcut takes 5 minutes instead of none? B predicts that the paradox remains but becomes weaker. With the same 15 drivers, the drivers need 27 to 29 minutes, depending on the split, instead of 30, compared with 24 to 25 without the shortcut. Once the shortcut takes 10 minutes or more (more than \(C - N/2\) in the continuous approximation), nobody uses it any more, and everything is as before. Explanation A cannot even address this question.

{{< callout type="info" >}}
A good explanation cannot be changed at will without ceasing to explain anything. (After David Deutsch, *The Beginning of Infinity*, 2011, ch. 1.)
{{< /callout >}}

The contrast is old. A story told in many variants has the earth resting on a bull, and the earth quakes when the bull shifts it from one horn to the other. Replace the bull with an elephant or a dragon, and the story explains the quake just as well; it fixes almost nothing that could be tested. Explanation A is the bull of the road network: any other word could replace "selfish". Modern geology explains earthquakes by the movement of tectonic plates: plates of the earth's crust move, and at their boundaries stresses build up and are released abruptly. This explanation made predictions that could have failed. If new ocean floor forms at the mid-ocean ridges and spreads apart, the rock on both sides should record the reversals of the earth's magnetic field as stripes that are symmetric about the ridge, and the floor should get older with distance from it. Vine and Matthews (1963) proposed this reading of the stripes; both predictions were confirmed later in the 1960s, and today GPS measures the plate movements directly, at a few centimetres per year.

{{< figure src="weltstier_qazwini.jpg" width="300" caption="Miniature for al-Qazwīnī's cosmography (1595): an angel carries the earth, below it a rock, a bull and a fish. Public domain (Wikimedia Commons)." >}}

A good explanation also often reaches beyond the case it was made for. Analogous effects appear in mechanical and electrical networks (Cohen & Horowitz 1991) and have been shown in a laboratory AC power grid (Schäfer et al. 2022). Whether they occur in a given real system has to be checked case by case.

## 3. What the model claims

Each driver chooses the fastest route, and the result is worse for all. That is what the model predicts. But the model assumes that travel time grows with the number of vehicles, that everyone chooses the fastest route and that the new road takes no time.

The road network is a **model**: a simplified image of reality. A lot has been left out of it.

- **People:** drivers who do not choose the fastest route.
- **Traffic:** traffic lights, junctions, queues.
- **Roads:** lengths, widths, capacities.
- **Travel time:** where the rule of \(n\) minutes comes from; behind it lies the fundamental diagram.
- **Time:** how route choices change from day to day, and whether traffic settles into the equilibrium at all; the model only states the equilibrium.
- **Information:** how drivers learn the travel times; in the model everyone knows them.

A model does not have to contain every detail of reality. It has to capture the mechanisms that matter for the question, here the link between route choice, traffic load and travel time. With four nodes and five edges it explains something surprising.

A model should be as simple as possible, but complex enough for the question. **Ockham's razor** covers the first half: if two models explain an observation equally well, the simpler one is preferable. A good model captures the relevant mechanisms and gives useful explanations and predictions for its purpose, however few details it contains. Box (1976) wrote: "Since all models are wrong the scientist must be alert to what is importantly wrong." In the road network, the colour of the cars does not matter; the assumptions about route choice and congestion are the mechanism itself. Whether we left out the right things is a question for validation (section 5).

Four terms are often mixed up:

- **Assumption:** "Drivers choose the route that is fastest for them." This is an assumption about behaviour. It is assumed within the model; whether people behave this way is a separate, testable question. It is not a theory. The model consists of the network plus this assumption.
- **Theory:** a coherent set of statements built on such assumptions, from which consequences can be derived. Here it is the equilibrium theory of route choice after Wardrop (1952). Its first principle: in equilibrium the travel times on all used routes are equal, and no unused route is faster.
- **Hypothesis:** a proposed explanation that can be tested. For example: drivers respond to their own travel times in a way that concentrates traffic on the two narrow roads.
- **Prediction:** an observable consequence of the hypothesis under stated conditions, which can fail against data. For example: "If the shortcut in this network is closed, the mean travel time decreases."

Following Popper, ask which observation would refute a prediction. If you cannot name one, the claim is not yet empirically testable.

An example of how a question becomes testable: "A bottleneck 3 m wide and 1 m long, or 1 m wide and 3 m long: which is better?" As it stands, this is not yet a scientific question. One has to fix the walking direction,[^bottleneck] the geometry, and what "better" means: higher flow, shorter evacuation time or lower density in front of the bottleneck. Only then does an intuitive question become a testable prediction.

### Verify or falsify?

Karl Popper (*Logik der Forschung*, 1934; *Conjectures and Refutations*, 1963, ch. 1) pointed out that general statements can never be proven conclusively, because nobody has seen all cases. A hundred cities in which a new road helped do not prove that new roads always help. One Braess case is enough to refute it, but only because the statement is universal ("always"). Against "mostly", a single counterexample does not help.

In practice a refutation is rarely this clean. A prediction always rests on auxiliary assumptions about instruments, data and conditions. When a prediction fails, something in this group of assumptions is wrong, but the failure does not say which part (Duhem 1954, part II, ch. 6); it may be an auxiliary assumption instead of the theory. This is known as the Duhem–Quine problem, and it is one reason why a single surprising observation rarely settles a dispute.

Popper asks: can the statement fail? Deutsch adds: does it explain why the result follows from the stated assumptions?

One warning about words: in simulation, "verification" means something else, namely checking the program (section 5).

Three levels have to be kept apart: the model, people playing the route game, and real traffic. The mathematical result is knowledge about the model. When people play the game, their result is an observation about these players under these rules. Whether real traffic behaves like either is a further empirical question. If players and model differ, the next step is to find out which assumption the players did not meet.

## 4. Testing competing explanations

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

Rapoport and colleagues (2009) ran this game in the laboratory with groups of 18 students, paid according to their travel costs, for 40 rounds without and 40 rounds with the shortcut. Reversing the order made no difference. In a network with the same structure as ours, the groups moved to the shortcut route, and their payoff per round fell from about 95 to about 40 points. In a larger network with five routes, choices moved the same way, but after 80 rounds some players still used the old routes. Such a comparison shows the effect of adding the shortcut under these conditions. It is not yet evidence about real road networks. Whether the players reached the result through the feedback of section 2 is a separate question; it would need data on whether each player switched in response to their own previous travel times.

### When an experiment misses something: Clever Hans

Even careful experiments can miss something decisive. Around 1900 a horse, "Clever Hans", answered arithmetic questions by tapping its hoof, in front of large audiences and mostly correctly. Many experts were convinced, and a commission found no trick in 1904.

{{< figure src="clever_hans.jpg" caption="Clever Hans at a public demonstration, 1904. From K. Krall, *Denkende Tiere* (1912), plate 2. Public domain (Wikimedia Commons)." >}}

His owner, Wilhelm von Osten, a mathematics teacher, was convinced that animals can think. The psychologist Oskar Pfungst was not satisfied with this explanation. He worked carefully with Hans and von Osten and changed one factor at a time: whether the questioner knew the answer, whether Hans could see the questioner (using blinkers), how far away the questioner stood (Pfungst 1907).

| Condition | Result |
|---|---|
| The questioner knows the answer | mostly correct |
| The questioner does not know it | many more errors |
| Hans cannot see the questioner | many more errors |

Hans read tiny body signals of the questioner, who relaxed without noticing as soon as the right number was reached. Two explanations competed: "Hans can do arithmetic" and "Hans reads unconscious signals". Both fit the correct answers. Only the second predicts that Hans fails when nobody he can see knows the answer. Pfungst's conditions tested this prediction, and Hans failed as it predicted. Von Osten never accepted the result. The correct answers were real, but the commission had overlooked the influence that produced them.

The episode gave its name to the **Clever Hans effect**: the expectations of observers unconsciously influence the behaviour of those observed. Today's countermeasures are blinding and control conditions.

### Criticism as a shared practice

Pfungst found the error because he could work with the horse, change the conditions one at a time and publish what he did. Science relies on this kind of access more than on the objectivity of individual scientists, a point Popper made in *The Open Society and Its Enemies* (1945). A result comes with its methods and data, so that others can check the calculations, repeat the measurements, collect new observations and test alternative explanations. An error that survives one investigation can show up in the next. This works only when methods and data are shared and the checks are done; publication alone does not do it (see National Academies 2019 on transparency and replication).

An expert's reputation does not make a claim correct. That does not put every opinion on the same level either. The useful questions are what evidence supports a claim and how well it has held up under informed, independent checks. Oreskes (2019) argues that trust in science rests on this collective, critical scrutiny within diverse expert communities.

## 5. From a model to a simulation

Sections 1 to 3 explained the paradox inside a model, and section 4 tested it with players in a laboratory. Applying the explanation to a real road network or a real crowd needs a different kind of evidence: something has to establish that it holds outside the model.

The network above has four nodes; you can work it out in your head. A city network has tens of thousands of links, travel times depend nonlinearly on load, and people decide differently. Then you need numerical methods and software, for example MATSim or, for pedestrians, JuPedSim.

Suppose the fundamental diagram, the relation between density and flow, is well known from experiments. We derive travel times from it, build a network model with route choice and simulate it. Even then the simulation does not necessarily predict the Braess paradox reliably.

If the software reproduces the analytical equilibrium for the Braess network exactly, that shows that it computes correctly for this test case. A verification test has been passed, but that is not validation. And even with correct software and a well-supported fundamental diagram the predictions can be wrong: people may choose routes differently than assumed, and queues, differences in information or effects over time may be missing.

The tempting conclusion is: "The input models are validated and the software passes all tests, so the simulation is realistic." Two questions have to be asked separately: did we implement the model correctly, and did we choose the right model?

{{< figure src="vv.png" caption="Verification compares the program with the model; validation compares the model with reality." >}}

- **Verification:** does the program compute what the model says? Has the model been implemented correctly and solved numerically? This is checked with tests and comparisons with exact solutions, looking for errors in code and numerics.
- **Validation:** does the model describe reality well enough for its intended purpose? This is checked against measured data. A model is always valid for a purpose, never absolutely.

Roache (1998), following Boehm and Blottner, put it briefly: verification means solving the equations right, validation means solving the right equations.

## 6. How far does a successful model travel?

In pedestrian dynamics these questions are part of our daily work. We build models, run experiments with hundreds of participants and observe people at stations, stadiums and events. Each method draws criticism. Models simplify behaviour. Participants in an experiment know that they are in an experiment. Observations in public spaces are limited by privacy, and their conditions cannot be controlled. Simulations are still used to plan buildings and events, and decisions about evacuation have to be made with the evidence available.

The criticism is often general: "models are just models", "people don't behave like that", "experiments are not reality". Each points to a real problem, but none says which conclusion is affected. The terms of this essay turn them into questions that can be checked:

| Objection | Question to ask |
|---|---|
| "Models are just models." | Which simplification could change the result we are using? |
| "People don't behave like that." | Which behaviour is missing, for which people and situation, and which prediction does it affect? |
| "Experiments are not reality." | Which findings carry over to the target situation, and which depend on the experimental setting? |
| "Field observations are too messy." | What can be measured reliably, and which influences can be told apart? |
| "We ran thousands of simulations." | Which uncertainty did the runs reduce, and which assumptions stayed untested? |

A useful criticism names an omission and says why it matters. For example: "The model does not include groups who wait for each other. This matters here, because the predicted benefit of the second exit depends on people spreading out independently." Such a criticism can be checked, and it may be strong enough to rule out one particular use of the model.

Being able to run a simulation thousands of times does not make it more trustworthy than an experiment. Repeated runs of a stochastic model are useful. They show when the mean evacuation time, its spread and the shape of the evacuation curve stop changing (Ronchi et al. 2014). If a model assumes that everyone knows all exits and takes the fastest route, a million runs with different random seeds will never produce a person who does not know the way. Models have to make such assumptions about behaviour, often without data to support them (Kuligowski 2013). Convergence shows how precisely we know the model's answer; only data show whether that answer describes these people (section 5).

{{< figure src="convergence.png" caption="Illustration with synthetic data: the running mean of a stochastic model settles on the model's own value as the runs accumulate, while a measured drill value stays where it is. ([Script](convergence.py))" >}}

An experiment observes real people, but in a particular situation. A bottleneck experiment with instructed participants supports conclusions about movement under those instructions, densities and geometries. Whether they hold for another population, a different motivation or an emergency is a separate question. Field observations have the opposite problem: they are closer to the target situation, but many factors vary at once, and being natural does not make them valid (Haghani 2023).

The methods overlap, but each is better at checking some parts of an explanation than others: experiments at isolating a mechanism, observations at checking whether it transfers, simulations at working out the consequences under conditions that cannot be tested directly. These methods help each other because their weaknesses differ; sources that share a weakness can still add evidence, but they cannot resolve that weakness.

Claims about a model of human behaviour have to be specific to be tested. "Our model reproduces human behaviour" is too broad to test. "Our model estimates the flow through this exit, for this population and these conditions, with this uncertainty" can be tested. Estimating the flow through a given exit is also a different task from predicting which exit people choose. The second rests on assumptions about behaviour that bottleneck flow measurements do not test.

A good fit in one situation also does not show that a model transfers to the next. We ran into this in our own work. In a [calibration study]({{< relref "/notes/dakota-calibration" >}}) we fitted JuPedSim's Collision Free Speed model to a bottleneck experiment. The calibrated model matched flow, density and speed in front of the opening mostly within ten percent, also at two widths left out of the fit. Two optimizer starts gave two parameter sets that fit almost equally well but differ by factors of two to four, so a good fit did not pin down the parameters. Hydrologists call this equifinality: different parameter sets, and even different models, can fit the same data acceptably well (Beven 2006). These data cannot tell them apart; the difference can show when the model is used somewhere else.

In the [second part]({{< relref "/notes/dakota-validation" >}}) the same parameters went, without refitting, to a half-metre gate and an entrance without guiding barriers. At the gate one set stalls and the other is 20 to 40 % too fast; at the entrance every set empties the crowd two to three times faster than the people did. A model calibrated for one situation was not valid for the next.

## 7. What passing a standard establishes

Guidelines such as RiMEA list test cases for simulation software. Such tests catch errors and make results easier to compare. Their results can also be used for claims they cannot support. "The software passes the RiMEA tests" can become "the software is validated", then "the results of this project are reliable" and finally "this design is safe". Each step is a new claim and needs its own evidence. RiMEA does not set pass limits for most of its tests (RiMEA 2025, Annex 1, A 2). The first test checks, by design, only that a person with a given walking speed crosses a corridor in the expected time. Whether that speed fits the people in the building, or whether they find the exits, is outside its scope.

RiMEA warns against this itself. Its preamble calls a simulation "an idealized case" in which people move as the user specifies, and it states that there are not enough reliable data from evacuation drills for a thorough quantitative comparison. Until such data exist, it regards its other tests as sufficient (Annex 1, A 5). This sentence is a translation from the IMO guidelines for passenger ships (IMO 2002), and it has stayed unchanged since then, in later IMO versions (IMO 2016) as in RiMEA, while laboratory data have appeared that RiMEA itself now uses.

IMO, RiMEA, the NIST report (Ronchi et al. 2013) and ISO 20414 share many of their tests, and most of these come from the same IMO list. Passing the same inherited test under several standards is therefore one piece of evidence, not several.

RiMEA's later tests compare models with laboratory data, mostly for trends or the spread of the data, and the user may vary the parameters. Once software is tuned to pass a test, passing it says less about anything outside the test (Goodhart 1984; Strathern 1997). ISO 20414 (2020) asks for more: the field of application must be stated, validation against one data set does not necessarily carry over to other scenarios, and validation runs must also use default or generally representative settings, not only settings tuned to the data.

The tests themselves should be tested. We need to know which errors that would change a safety conclusion they can reveal, and which wrong predictions still pass them. The same applies to our own software. Passing a standard is one part of the argument for trusting a simulation. The rest has to come from evidence about the people, the building and the purpose.

{{< details title="A note on standards" closed="true" >}}
For pedestrian simulations the German guideline RiMEA (Richtlinie für Mikroskopische Entfluchtungsanalysen, version 4.1.1, 2025) lists test cases 1 to 16 in its Annex 1. RiMEA uses verification and validation interchangeably; its four forms of verification follow ISO/TR 13387-8:1999 (Annex 1, A 1). What it calls "quantitative verification", the comparison with data from evacuation drills, is validation in the AIAA sense (AIAA G-077-1998), and RiMEA itself regards the data as insufficient for it (A 5). The NIST report on evacuation models makes the same correction for the IMO guidelines (Ronchi et al. 2013).
{{< /details >}}

## 8. Using an explanation to make a decision

For practical projects the question becomes: what evidence is enough for this model to support this decision? A claim that a layout is safer needs a safety criterion, for example that everyone is out before conditions become untenable (ASET > RSET); a layout can be faster on average and worse for the last people out. Sometimes the answer is that the evidence does not support the proposed safety claim.

Suppose a well-tested model predicts that closing a road reduces the mean travel time. The prediction alone does not decide whether the road should be closed. Some travellers gain and others lose, and access to particular places, costs and safety count as well. Weighing them requires stating what we want to achieve. Science can say what is likely to happen under each option; which outcome to prefer is a decision about goals. Values also enter the science itself, for example when deciding how much evidence is enough to accept a claim, given the consequences of being wrong (Douglas 2009, ch. 5).

## What makes an explanation good

A good explanation names a mechanism that turns explicit assumptions into specific consequences. It cannot be adjusted to fit any outcome, so a test can show it wrong. Explanation B does this; "selfish drivers" does not. How far to trust such an explanation is a separate question, and each kind of test answers part of it: the arithmetic holds within the model, the laboratory game shows the effect for its players, a simulation's validation covers its stated purpose, and the city cases are too weak to show the paradox in real networks. Scientific knowledge can be revised, and its parts are uncertain to very different degrees. What counts is how well an explanation has survived attempts to find its weaknesses, what evidence supports it and where its limits lie.

The same questions work for any claim, in a newspaper, a report or one's own thesis:

1. What exactly is explained, and what is the mechanism?
2. Could the explanation be changed at will and still "explain" the same thing?
3. Which observation would refute it?
4. What evidence separates the explanation from plausible alternatives: a controlled comparison, independent observations that test predictions the alternatives get wrong, or only a sequence in time?
5. Was a model checked against reality, and for which purpose is it valid?


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
- Cohen, J. E., Horowitz, P. (1991): Paradoxical behaviour of mechanical and electrical networks. *Nature* 352, 699–701.
- Deutsch, D. (2011): *The Beginning of Infinity: Explanations That Transform the World*. London: Allen Lane.
- Douglas, H. E. (2009): *Science, Policy, and the Value-Free Ideal*. Pittsburgh: University of Pittsburgh Press.
- Duhem, P. (1954): *The Aim and Structure of Physical Theory*. Translated by P. P. Wiener. Princeton: Princeton University Press.
- Goodhart, C. A. E. (1984): Problems of monetary management: the U.K. experience. In: *Monetary Theory and Practice: The UK Experience*. London: Macmillan, 91–121. doi:10.1007/978-1-349-17295-5_4.
- Haghani, M. (2023): The notion of validity in experimental crowd dynamics. *International Journal of Disaster Risk Reduction* 93, 103750.
- IMO (2002): *Interim Guidelines for Evacuation Analyses for New and Existing Passenger Ships*. MSC/Circ.1033. London: International Maritime Organization.
- IMO (2016): *Revised Guidelines on Evacuation Analysis for New and Existing Passenger Ships*. MSC.1/Circ.1533. London: International Maritime Organization.
- ISO/TR 13387-8 (1999): *Fire safety engineering — Part 8: Life safety — Occupant behaviour, location and condition*. Geneva: ISO (withdrawn).
- ISO 20414 (2020): *Fire safety engineering — Verification and validation protocol for building fire evacuation models*. Geneva: ISO.
- Knödel, W. (1969): *Graphentheoretische Methoden und ihre Anwendungen*. Berlin: Springer.
- Kolata, G. (1990): What if They Closed 42d Street and Nobody Noticed? *New York Times*, 25 December 1990. Free summary: ["42nd Street: Braess's Paradox"](https://blogs.cornell.edu/info2040/2016/09/14/42nd-street-braess-paradox/), Cornell course blog *Networks*, 2016.
- Kuligowski, E. (2013): Predicting Human Behavior During Fires. *Fire Technology* 49(1), 101–120.
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
- Schäfer, B. et al. (2022): Understanding Braess' Paradox in power grids. *Nature Communications* 13, 5396.
- Strathern, M. (1997): 'Improving ratings': audit in the British University system. *European Review* 5(3), 305–321.
- Vine, F. J., Matthews, D. H. (1963): Magnetic anomalies over oceanic ridges. *Nature* 199, 947–949.
- Wardrop, J. G. (1952): Some Theoretical Aspects of Road Traffic Research. *Proceedings of the Institution of Civil Engineers* Part II 1(3).

[^wardrop]: Traffic research uses the related **Wardrop equilibrium** (Wardrop 1952): the travel times on all used routes are equal, and no unused route is faster. It is usually stated for so many drivers that a single one does not change the travel times. With 15 drivers, one driver changes a narrow road by a whole minute, so in a Nash equilibrium the used routes can differ by one minute, here 24 and 25.

[^bottleneck]: The width across the direction of walking matters most. In one experiment the length made little difference between 2 and 4 m, and only an opening a few centimetres deep let noticeably more people through (Liddle et al. 2009, 2022).

*Disclosure:* The author's group develops JuPedSim, simulation software to which such tests apply. Some of the laboratory data that RiMEA uses in its tests, and the bottleneck studies cited above (Liddle et al. 2009, 2022), come from Armin Seyfried and colleagues at Forschungszentrum Jülich, where the author works.

{{< icon "pencil-alt" >}} By: [Mohcine Chraibi]({{< relref "/authors#MohcineChraibi" >}})
