---
title: Anticipation Velocity Model
math: true
---

## Introduction to anticipation velocity model

The anticipation velocity model (AVM) [1](#Xu2021) is a mathematical approach designed for pedestrian dynamics. It represents a further development of the collision-free speed model [2](#Tordeux2015), extending its framework by incorporating pedestrian anticipation. 
This anticipation process is structured into three components: perception of the current situation, prediction of a future situation, and selection of a strategy that leads to action.

Similar to the Collision-Free Speed Model, the direction in which an agent moves is determined through an **anisotropic** combination of exponential repulsion from nearby agents within its vision field. However, the strength of this repulsion is influenced by the predicted distance to others in the surroundings, rather than the actual distance used in the Collision-Free Speed Model.

The calculation of the speed is completely the same as the collision-free speed model. Agents adjust their speed according to the nearest neighbor in their headway, allowing them to navigate through congested areas without overlapping or obstructing each other. 

The anticipation mechanism incorporated in the AVM enables it to reproduce lane formation in bidirectional flow scenarios more realistically than the Collision-Free Speed Model. Additionally, the AVM is more effective in preventing jamming in such scenarios and offers improved accuracy in reproducing the fundamental diagram.

## Mathematical description
In AVM, an agent is represented as a disk with a constant radius $r$. The position and velocity of agent $i$ are denoted by $\vec{x}_i$ and $\vec{v}_i$, respectively, where $\vec{v}_i=\dot{\vec{x}}_i$. Furthermore, $\vec{v}_i=\vec{e}_i\cdot v_i$, where $\vec{e}_i$ and $v_i$ denote the direction of movement and the speed of agent $i$, respectively.


### Direction function
The desired direction of agent $i$ is denoted by $\vec{e}_i^{~0}$, a unit vector pointing towards its target.
Then the process of operational navigation to avoid collisions and obstructions can be divided into three parts.

a. Perception of the actual situation: 
To consider restrictions using visual perception, it is assumed that only agents located in the union of two half-planes, where $i$ is moving or intends to move, affect its direction. The set containing all agents who have an impact on $i$'s direction of movement is

$$N_i(t)=\bigg\{j,~\vec{e}_i(t) \cdot \vec{e}_{i,j}(t)>0\ \text{or}\  \vec{e}_i^{\ 0}(t) \cdot \vec{e}_{i,j}(t)>0\bigg\},$$

where $\vec{e}_{i,j}$ denotes the unit vector from $i$ to $j$.


{{< figure src="figure1.png" caption="The agents who are located in the gray area have an impact" >}}

b. Prediction of a future situation: 
To consider the prediction, it is assumed that the strength of $j$'s impact on $i$ is a function of the predicted distance between these two agents at a particular time point. Given a time constant $t^\text{a}$, which can be interpreted as the prediction time, the predicted distance is defined as 

$${s}^\text{a}_{i,j}(t+t^\text{a})=\max \bigg\{2r,~\Big(\vec{x}^\text{a}_j(t+t^\text{a})-\vec{x}^\text{a}_i(t+t^\text{a})\Big) \cdot \vec{e}_{i,j}(t) \bigg\},$$
 
where $\vec{x}^\text{a}_i(t+t^\text{a})=\vec{x}_i(t)+\vec{v}_i(t)\cdot t^\text{a}$.

{{< figure src="figure2.png" caption="The agents who are located in the gray area have an impact" >}}


c. Selection of a strategy leading to an action: 
After the introduction of the predicted distance, the strength of the impact from agent $j$ on the direction of movement of agent $i$ is defined as

$$ R_{i,j}(t)= \alpha_{i,j}(t) \cdot \exp 
    \bigg( \frac{2 r-s^\text{a}_{i,j}(t+t^\text{a})}{D} \bigg),$$

where $D>0$ is a constant parameter used to calibrate the range of the impact from neighbors and $\alpha_{i,j}$ is a directional dependency used to vary the strength of impact from different neighbors.

$$\alpha_{i,j}(t)=k \Big(1+ \frac{1- \vec{e}_i^{~0}(t) \cdot \vec{e}_j(t)}{2}\Big),\; k>0 ,$$

where $\alpha_{i,j}$ is minimal ($k$) when both vectors $\vec{e}_i^{~0}$ and $\vec{e}_j$ are aligned and is maximum ($2 k$) when they are anti-aligned, which means that agents influence each other's direction strongly in bidirectional scenarios. Here, $\alpha_{i,j}$ means agents have a high tendency to follow the agents who move in the same direction. When this strategy is used, the probability of further conflicts is reduced. 

The direction of the impact from agent $j$ on $i$'s direction of the movement is defined as

$$\vec{n}_{i,j}(t) =-\text{sgn}\bigg(\vec{e}^{~\text{a}}_{i,j}(t+t^\text{a}) \cdot \vec{e}_i^{~0\bot}(t)\bigg) \cdot\vec{e}_i^{~0\bot}(t),$$

where $\vec{e}^{~\text{a}}_{i,j}(t+t^\text{a})= \vec{x}^\text{a}_j(t+t^\text{a})- \vec{x}_i(t)$. The direction of $\vec{n}_{i,j}$ depends on the predicted position of agent $j$ after a period of time $t^\text{a}$. Note that when this predicted position is aligned with the desired direction of $i$, the direction of $\vec{n}_{i,j}(t)$ is chosen randomly as $\vec{e}_i^{~0\bot}$ or $-\vec{e}_i^{~0\bot}$. This rule prevents agents from moving in the opposite direction to the desired direction.

{{< figure src="figure3.png" caption="The agents who are located in the gray area have an impact" >}}

Finally, the optimal direction of agent $i$ is obtained as

$$ \vec{e}_i^{~\text{d}}(t)=u \bigg(\vec{e}_i^{~0}(t)+\sum_{j\in N_i(t)} R_{j,i}(t)\cdot \vec{n}_{j,i}(t)\bigg),$$ 

where $u$ is a normalization constant such that $\lVert\vec{e}_i^{~\text{d}}\rVert=1$. Then, the direction of movement of agent $i$ is updated as

$$\frac{d\vec{e}_i(t)}{dt} = \frac{ \vec{e}_i^{~\text{d}}(t)-\vec{e}_{i}(t)}{\tau},$$

where $\tau$ is a relaxation parameter adjusting the rate of the turning process from the current direction $\vec{e}_i$ to the optimal direction $\vec{e}_i^{~d}$.


### Speed function
After obtaining the new direction of the movement, the set of neighbors that are imminently colliding with $i$ is defined as

$$J_i=\Big\{j,~\vec{e}_i \cdot \vec{e}_{i,j} \ge 0\ \text{and}\ \left|\vec{e}_i^{~\bot} \cdot \vec{e}_{i,j}\right| \leq \frac{2 r}{s_{i,j}}\Big\},$$

where $s_{i,j}$ is the current distance between $i$ and $j$. Therefore, the maximum distance that agent $i$ can move in the direction without overlapping other agents is

$$s_i=\min_{j\in J_i}s_{i,j}-2r.$$

{{< figure src="figure4.png" caption="Calculation of the speed in the direction of movement" >}}

Finally, the speed of agent $i$ in the new direction is

$$v_i=\min\Big\{v_i^0,~\max\big\{0,\frac{s_{i}}{T}\big\}\Big\},$$

where $v_i^0$ is the free speed of agent $i$, and $T>0$ is the slope of the speed-headway relationship.


### Parameters


The anticipation velocity model depends on seven parameters: 
- Pedestrian radius ($r>0$)
- Free speed ($v^0>0$)
- Time gap ($T>0$)
- Repulsion rate and distance ($k>0$ and $D>0$)
- Rate of turning process ($\tau>0$) 
- Prediction time ($t^\text{a}$>0)

## Limitations of the anticipation velocity model

Despite the AVM demonstrating superior performance in bidirectional flow scenarios compared to traditional models such as the collision-free speed model (CSM), there are still notable limitations:

**Realism Gap:** Although the AVM represents an improvement over the CSM, it does not fully capture real-world pedestrian behavior. While the model incorporates anticipation, it overlooks key aspects of human interactions, such as cooperation, pushing, and waiting, which are prevalent in high-density crowds. Consequently, the AVM faces challenges in accurately representing extreme crowd dynamics. For instance, in scenarios with very high pedestrian densities and multidirectional flows, gridlock can still occur.

-**Model Robustness**: The robustness of the AVM is limited when compared to the CSM. A key difference is that the AVM excludes backward movement, which is often observed in real-world crowds. While backward movement in the CSM is not directly modeled, it still occures and contributes to solving conflicts between agents. By removing this behavior, the AVM becomes less adaptable to certain crowd configurations, particularly when faced with complex interactions.

**Parameter Sensitivity:** Some parameter values in the AVM are scenario-dependent. In particular, the anticipation parameter plays a significant role in sparse densities, where agents can effectively anticipate new avoidance opportunities. However, in high-density situations, the limited space for avoidance reduces the usefulness of anticipation and can even lead to numerical issues in the simulation.


## Challenges in implementing anticipation velocity model

In the original publication of the AVM, walls are implemented as static agents, with interactions based on the nearest point on the wall to an agent. In high-density scenarios, this approach can lead to imbalances, where agents are pushed towards walls by others, but the walls are unable to exert sufficient repulsive influence to push them back. A common solution to this issue involves calibrating wall parameters to make the repulsion strong enough to counteract the influence of surrounding agents.

However, in the JuPedSim implementation, wall interactions are designed differently. Walls are treated as gliding surfaces, meaning agents adjust their movement to avoid collisions while maintaining smooth trajectories along wall boundaries. The influence of walls on an agent's movement is determined by the agent's distance to the wall and their movement direction.

{{< youtube iY_mQdB0fdE >}}    

Importantly, walls do not affect the speed of agents—only their direction. Agents glide along walls by subtly adjusting their trajectory while preserving their intended movement as much as possible. This influence transitions smoothly as agents move closer to or farther from the wall, ensuring realistic and continuous behavior near boundaries.

## Using the anticipation velocity model with JuPedSim 
The anticipation velocity model has also been implemented and tested using the JuPedSim software platform (`VelocityModelBuilder`). 
Following table summarize the parameters of the model and their naming.

| Parameter Description                     | Variable Name |
| ----------------------------------------- | ------------- |
| Pedestrian size                           | `radius`      |
| Desired speed                             | `v0`          |
| Time gap                                  | `time_gap`    |
| Repulsion rate for agents interaction     | `strength_neighbor_repulsion`|
| Repulsion distance for agents interaction |`range_neighbor_repulsion`|
| Rate of turning process                   | `reaction_time`  |
| Prediction time                           | `anticipation_time` |


To determine the desired direction vector, a designated exit or waypoint must be defined as a polygon. The unit vector, denoted as $\vec{e}_i^{~0}$, is then calculated by pointing from the current position of the pedestrian towards the specified exit or waypoint.


> **_NOTE:_**  Given that the target is always a polygon, the objective would be the polygon's center.


## The anticipation velocity model in the literature

The following map shows works from the literature connected to the anticipation velocity model.

<figure style="text-align: center;">
    <img src="https://iffmd.fz-juelich.de/uploads/upload_3eaaacd3f58f94267004de892f6f8c87.png" alt="crowd" width="600"/>
    <figcaption style="text-align: right;">
        <small>
This is not necessary although nice!
        </small>
    </figcaption>
</figure>

{{< figure src="figure5.png" caption="Linking the AVM Paper to 18 Key Publications" >}}

## References: 

- <a name="Xu2021"></a>[1] Xu, Q., Chraibi, M., Seyfried, A. (2021). Anticipation in a velocity-based model for pedestrian dynamics. Transportation Research Part C: Emerging Technologies, Volume 133. https://doi.org/10.1016/j.trc.2021.103464


- <a name="Tordeux2015"></a>[2] Tordeux, A., Chraibi, M., Seyfried, A. (2016). Collision-Free Speed Model for Pedestrian Dynamics. In: Knoop, V., Daamen, W. (eds) Traffic and Granular Flow '15. 
<br>
<a href="https://doi.org/10.1007/978-3-319-33482-0_29" target="_blank">
    <i class="fas fa-file-alt"></i> DOI Link
</a> 
&nbsp; | &nbsp;
<a href="https://pedestriandynamics.org/models/collision_free_speed_model/" target="_blank">
    <i class="fas fa-external-link-alt"></i> Model Description
</a>

