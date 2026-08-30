---
title: Collision Free Speed Model
math: true
---

## Introduction to collision-free speed model

The collision-free speed model [[1]](#Tordeux2015) is a
mathematical approach designed for pedestrian dynamics, emphasizing the
prevention of collisions among agents.

The direction in which an agent moves is determined through an isotropic
combination of exponential repulsion from nearby agents. The strength of this
repulsion is influenced by the proximity to others within their surroundings,
treating all directions equally in terms of influence.

Agents adjust their speed according to the nearest neighbor in their headway,
allowing them to navigate through congested areas without overlapping or
obstructing each other. The collision-free speed model takes into account the
length of the agent, which determines the required space for movement, and the
maximum achievable speed of the agent.

The model is simple and computationally efficient.

## Mathematical description

Models that establish a relationship between speed and spacing, known as the OV
function, were originally introduced in traffic flow studies. They have since
been adapted for pedestrian modeling, offering a straightforward way to control
the fundamental diagram. The collision-free speed model is mathematically
represented as a derivative equation for the velocity of each pedestrian.
Typically, this can be expressed as

$$\dot{\mathbf{x}}_i=V_i\big(s_i(\mathbf{x}_i,\mathbf{x}_j,\ldots)\big)\times\mathbf e_i(\mathbf{x}_i,\mathbf{x}_j,\ldots)$$

where $x_i$ represents the position of pedestrian $i$ and $V_i$ represents
their speed.

The speed function $V_i$ regulates the overall speed of the pedestrian, while
the direction function $\textbf{e}_i$ determines the direction in which the
pedestrian moves.

### Direction function

The direction function is governed by a weighted sum of exponential repulsion
from neighboring pedestrians, which is calibrated by the repulsion rate and
distance.

{{< figure src="figure1.png" caption="Calculation of the movement direction" >}}

$$\mathbf e_i(\mathbf x_i,\mathbf x_j,\ldots)=\frac{1}{N}\left(\mathbf e_0+\sum_j R(s_{i,j})\right)$$

with $\mathbf e_0$ the desired direction, $N$ a normalization constant such
that $\|\mathbf e_i\|=1$ and $R(s)=a\,\exp\big((l-s)/D\big)$ the repulsion
function calibrated by the coefficient $a>0$ and distance $D>0$.

{{< figure src="figure2.png" caption="Repulsive influence in the direction" >}}

### Speed function

The velocity is calculated by multiplying two functions: A speed function $V_i$
and a direction function $\textbf{e}_i$.

Inspired from car-following models, the speed function only depends on the distance to the nearest pedestrian or obstacle in front through an Optimal Velocity (OV) function.

The set $J_i$ of pedestrians and obstacles in front is given by

$$J_i=\big\\{j,\\;\mathbf e_i\cdot \mathbf e_{ij}\le 0\\;\text{and}\\;|\mathbf e_i^\perp\cdot\mathbf e_{ij}|\le l/s_{ij}\big\\}.$$

The distance to the nearest pedestrian or obstacle in front is then the minimum
$$s_i=\min_{j\in J_i}s_{ij}.$$

In the following, the OV function is the piecewise linear
$$V(s)=\min\big\\{v_0,\max\\{0,(s-l)/T\\}\big\\},$$

satisfies

$$\begin{align*}V(s)&\gt0\quad\forall s\gt l\\\\ V(s)&=0\quad\forall s\le\ell\end{align*}$$

{{< figure src="figure3.png" caption="OV speed function vs fundamental diagram" >}}

The spacing is calculated along the direction of motion and is defined as the
spacing to the nearest neighbor that may collide with the agent. See following
picture:

{{< figure src="figure4.png" caption="Calculation of the minimal speed in the direction of motion" >}}

### Parameters


The collision-free speed model depends on five parameters:
- Pedestrian diameter ($l \ge 0$)
- Desired speed ($v_0 > 0$)
- Time gap ($T > 0$)
- Repulsion rate and distance ($a>0$ and $D>0$)

## Limitations of the collision-free speed model

The collision-free speed model has some limitations:

- The model rests on simple assumptions. In particular, representing agents as
  circles cannot capture many details of real pedestrian behavior.
- It neglects response time and visual perception.
- Stop-and-go waves and gridlocks are not well reproduced, except in confined
  circular bottlenecks.
- Obstacles and environmental conditions that influence pedestrian movement
  are not part of the model.

Several studies extended the model to address these limitations. Xu
[[2]](#Xu2019) proposed a generalized velocity model that includes wall
influence, uses velocity-based ellipses for distance calculations, and
smooths changes of direction. Further refinements of the direction function
were introduced in [[3]](#Rzezonka2022), [[4]](#Zhang2021), and
[[5]](#Xu2021).


## Challenges in Implementing Collision Free Speed Models

Numerical solution of the first-order ordinary differential equation defined
by the model is solved as follows:

{{< figure src="figure5.png" caption="Update algorithm" >}}

Implementing the model raises several practical questions. The original model
does not define agent-wall interactions; extensions such as Xu's generalized
velocity model fill this gap. Calibrating the parameters of the speed and
direction functions is another difficulty, and in some symmetrical scenarios
the direction function is not well defined.

### Isotropical direction influence

The direction model is uniform, meaning it does not differentiate between
various directions of influence. The model treats all directions equally and
does not consider specific pedestrian preferences or biases in their movement.
This may lead to certain unrealistic situations where the agent's direction is
influenced by agents from behind them.

### Balancing Collision Avoidance with Performance: Selecting the Appropriate Time-Step

The continuous model is provably collision-free in any situation. Its
discretisation, however, can introduce collisions. When solving the ordinary
differential equation with an Euler scheme, the time step must be small
enough. The model is collision-free in discrete time if

$$\delta t \le \min\left\\{\frac T2,\frac{l(\sqrt2-1)}{v_0\sqrt2}\right\\}$$

The condition for collision-free dynamics is determined solely by the
parameters of the speed model. For example, if we use parameter values of $T=1$
s, $v_0=1.2$ m/s and $l$, with a smallness condition on the time step
approximate to $\delta t \le0.072$ s for explicit Euler schemes and circular
pedestrian shape.

### Parameter calibration

The repulsion rate and distance in the direction model are hard to calibrate,
since suitable values vary with the environment and the crowd.



## References

- <a name="Tordeux2015"></a>[1] Tordeux, A., Chraibi, M., Seyfried, A. (2016).
  Collision-Free Speed Model for Pedestrian Dynamics. In: Knoop, V., Daamen, W.
  (eds) Traffic and Granular Flow '15.
  <br/>https://doi.org/10.1007/978-3-319-33482-0_29

- <a name="Xu2019"></a>[2] Xu, Q., Chraibi, M., Tordeux, M., Zhang (2019).
  Generalized collision-free velocity model for pedestrian dynamics. Physica A:
  Statistical Mechanics and its Applications, Volume 535.
  <br/>https://doi.org/10.1016/j.physa.2019.122521

- <a name="Rzezonka2022"></a>[3] Rzezonka, J., Chraibi, M., Seyfried, A., Hein,
  B., Schadschneider, A. (2022). An attempt to distinguish physical and
  socio-psychological influences on pedestrian bottleneck. Royal Society Open
  Science. <br/>https://royalsocietypublishing.org/doi/10.1098/rsos.211822

- <a name="Zhang2021"></a>[4] Zhang, S., Zhang, J., Chraibi, M., Song, W.
  (2021). A speed-based model for crowd simulation considering walking
  preferences. Communications in Nonlinear Science and Numerical Simulation,
  Volume 95. <br/>https://doi.org/10.1016/j.cnsns.2020.105624

- <a name="Xu2021"></a>[5] Xu, Q., Chraibi, M., Seyfried, A. (2021).
  Anticipation in a velocity-based model for pedestrian dynamics.
  Transportation Research Part C: Emerging Technologies, Volume 133.
  <br/>https://doi.org/10.1016/j.trc.2021.103464

- <a name="Xu2021"></a>[6] Tordeux, A. talk in TGF15, Delft.
<br/>[Slides.](https://www.vzu.uni-wuppertal.de/fileadmin/site/vzu/Pres_1st_order_models.pdf)
