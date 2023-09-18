# Collision-free speed model

## Introduction to collision-free speed model
The collision-free speed model [1](#Tordeux2015) is a mathematical framework that prioritizes the avoidance of collisions in pedestrian dynamics. It achieves this by calculating the optimal velocity for each individual agent, taking into account factors such as agent size and maximum attainable speed. The direction in which an agent moves is determined through a combination of exponential repulsion from nearby agents, with the strength of repulsion influenced by proximity to others within their surroundings. The main idea behind the collision-free speed model is to replicate real-world phenomena in pedestrian dynamics using a simplified and computationally efficient approach.

## Basic Principles of collision-free speed model

The fundamental principle of collision-free speed models is to enable pedestrians to move without colliding with one another. The collision-free speed model in pedestrian dynamics focuses on avoiding collisions by determining the velocity of agents based on their interactions with neighboring agents. In this model, agents adjust their speed according to the nearest neighbor in their headway, allowing them to navigate through congested areas without overlapping or obstructing each other.  The collision-free speed model takes into account the length of the agent, which determines the required space for movement, and the maximum achievable speed of the agent. 

## Mathematical description

Models that establish a relationship between speed and spacing, known as the OV function, were originally introduced in traffic flow studies. They have since been adapted for pedestrian modeling, offering a straightforward way to control the fundamental diagram.
The collision-free speed model is mathematically represented as a derivative equation for the velocity of each pedestrian. Typically, this can be expressed as 

$$\dot{\mathbf{x}}_i=V_i\big(s_i(\mathbf{x}_i,\mathbf{x}_j,\ldots)\big)\times\mathbf e_i(\mathbf{x}_i,\mathbf{x}_j,\ldots)$$

where $x_i$ represents the position of pedestrian $i$ and $V_i$ represents their position. 

The speed function $V_i$ regulates the overall speed of the pedestrian, while the direction function $\textbf{e}_i$ determines the direction in which the pedestrian moves.


### Speed function
The velocity is calculated by multiplying two functions: A speed function $V_i$ and a direction function $\textbf{e}_i$.

In the following, the OV function is the piecewise linear 
$$V(s)=\min\{v_0,\max\{0,(s-l)/T\}\},$$

satisfies

$$V(s)\ge0\quad\mbox{for all $s$}\qquad\mbox{and}\qquad V(s)=0\quad\mbox{for all $s\le\ell$}.
$$

<figure style="text-align: center;">
    <img src="https://iffmd.fz-juelich.de/uploads/upload_fc66a3b89c6c0c6771b28e5051896d30.png" alt="crowd" width="600"/>
    <figcaption style="text-align: right;">
        <small>
    OV speed function vs fundamental diagram.
        </small>
    </figcaption>
</figure>



The spacing is calculated along the direction of motion and is defined as the spacing to the nearest neighbor that may collide with the agent. See following picture:
<figure style="text-align: center;">
    <img src="
https://iffmd.fz-juelich.de/uploads/upload_7e0ff84e88b92da135ed1672ddb41b53.png
" alt="crowd" width="400"/>
    <figcaption style="text-align: right;">
        <small>
Calculation of the minimal speed in the direction of motion        </small>
    </figcaption>
 
</figure>

### Direction function
The direction function is governed by a weighted sum of exponential repulsion from neighboring pedestrians, which is calibrated by the repulsion rate and distance. This mathematical representation ensures that the pedestrians are able to adjust their speed and direction based on their interactions with neighboring agents, ultimately resulting in a collision-free movement. 


$$\mathbf e_i(\mathbf{x}_i,\mathbf{x}_j,\ldots)=\frac{1}{N}\left(\mathbf e_0+\sum_j R(s_{i,j})\,\mathbf e_{i,j}\right)
$$

with $\mathbf e_0$ the desired direction, $N$ a normalization constant such that $\|\mathbf e_i\|=1$ and 
$R(s)=a\,\exp\big((l-s)/D\big)$ the repulsion function calibrated by the coefficient $a>0$ and distance $D>0$. 


<figure style="text-align: center;">
    <img src="https://iffmd.fz-juelich.de/uploads/upload_307ad7bbcbf1f539475d3deea9ee5e4c.png
" alt="crowd" width="400"/>
    <figcaption style="text-align: right;">
        <small>
Repulsive influence in the direction.
        </small>
    </figcaption>
 
</figure>







The collision-free speed model depends on five parameters: 
- Pedestrian size ($l$)
- Desired speed ($v_0$)
- Time gap ($T$)
- Repulsion rate and distance ($a$ and $D$)

## Limitations of the collision-free speed model

Despite its ability to simulate pedestrian dynamics and replicate real-world phenomena, the collision-free speed model has some limitations that should be acknowledged. First, the model is based on simplified assumptions and may not fully capture the complexity of actual pedestrian behavior. For instance, it assumes agents have a circular shape and does not consider factors such as reaction time or visual perception. Additionally, stop-and-go phenomena in congested areas and gridlock situations are not adequately accounted for unless they occur in narrow bottlenecks with circular shapes. Furthermore, external influences like obstacles or environmental conditions that can impact pedestrian movement are not taken into consideration by this model.

Numerous studies have presented different enhancements to the collision-free speed-based pedestrian model with the aim of addressing its limitations and improving the accuracy of pedestrian simulations. For instance, Xu ([2](#Xu2019)) proposed a comprehensive velocity model that takes into account wall influence and incorporates velocity-based ellipses for accurate distance calculations. Moreover, improvements were made to the direction function in order to ensure seamless changes in pedestrian directions during simulation. Similarly, other researchers such as [3](#Rzezonka2022), [4](#Zhang2021), and [5](#Xu2021) introduced additional refinements to enhance the direction function further.


## Challenges in Implementing Collision Free Speed Models
Numerical solution of the first-order ordinary differentiial equation defined by the model is solved as follows:
<figure style="text-align: center;">
    <img src="https://iffmd.fz-juelich.de/uploads/upload_6e68d9c3212b7d48aff1a7e32ef7534a.png" alt="crowd" width="800"/>
    <figcaption style="text-align: right;">
        <small>
Update algorithm.
        </small>
    </figcaption>
</figure>


The implementation of collision-free speed models presents several challenges. One challenge is the lack of definition for agent-wall interactions in the original model. However, this issue has been tackled by proposed enhancements to the model, such as Xu's generalized velocity model. Another challenge lies in accurately calibrating the parameters in both the speed and direction models. In certain symmetrical scenarios, determining a well-defined direction function can be difficult. 

### Isotropical direction influence 
The direction model is uniform, meaning it does not differentiate between various directions of influence. The model treats all directions equally and does not consider specific pedestrian preferences or biases in their movement. This may lead to certain unrealistic situations where the agent's direction is influenced by agents from behind them. 

### On time-steps: Collision-freeness vs performance
The continuous definition of the model is proved to be collision-free in any situation.
However, the discretisation of the model, as often required for computational efficiency, can introduce potential collision problems.
While the speed model has a fast and efficient implementation, it is crucial to select a sufficiently small time step when solving the ordinary differential equation with Euler scheme in order to ensure that the model remains collision-free.
Therefore, the model is collision-free in discrete time if 
$$
\delta t \le \min\left\{\frac T2,\frac{l(\sqrt2-1)}{v_0\sqrt2}\right\}.
$$

The condition for collision-free dynamics is determined solely by the parameters of the speed model. 
For exampl, if we use parameter values of $T=1$ s, $v_0=1.2$ m/s and $l$, with a smallness condition on the time step approximate to $\delta t \le0.072$ s for explicit Euler schemes and circular pedestrian shape.

### Parameter calibration 
Additionally, accurately calibrating the repulsion rate and distance in the direction model can prove challenging due to variation based on specific environmental conditions and crowd dynamics.

## Using the collision-free speed model with JuPedSim 
The collision-free speed model has also been implemented and tested using the JuPedSim software platform (`VelocityModelBuilder`). 
Following table summarize the parameters of the model and their naming.

| Parameter Description                          | Variable Name      |
|------------------------------------------------|---------------|
| Pedestrian size                                | `radius`      |
| Desired speed                                  | `v0`          |
| Time gap                         | `time_gap`    |
| Repulsion rate for agents interaction         | `a_ped`       |
| Repulsion distance for agents interaction     | `d_ped`       |
| Repulsive rate for wall interaction            | `a_wall`      |
| Repulsive distance for wall interaction       | `d_wall`      |


To determine the desired direction vector, a designated exit or waypoint must be defined as a polygon. 
The unit vector, denoted as $\textbf{e}_0$, is then calculated by pointing from the current position of the pedestrian towards the specified exit or waypoint.

> **_NOTE:_**  Given that the target is always a polygon, the objective would be the polygon's center.

The continuous definition of the model is proved to be collision-free in any situation.
However the discretisation of the model, as often required for computational efficiency, can introduce potential collision problems.
While the speed model has a fast and efficient implementation, it is crucial to select a sufficiently small time step when solving the ordinary differential equation with Euler scheme in order to ensure that the model remains collision-free.
Therefore the model is collision-free in discrete time if 
$$
\delta t \le \min\left\{\frac T2,\frac{\ell(\sqrt2-1)}{v_0\sqrt2}\right\}.
$$

The condition for collision-free dynamics is determined solely by the parameters of the speed model. In this paper, we use parameter values of $T=1$ s, $v_0=1.2$ m/s and $\ell$, with a smallness condition on the time step approximate to $\delta t \le0.072$ s for explicit Euler schemes and circular pedestrian shape.


## The collision-free speed model in the literature

The following map shows works from the literature connected to the collision-free speed model.
<figure style="text-align: center;">
    <img src="https://iffmd.fz-juelich.de/uploads/upload_443961e85c3dcdd69565bc8a5504c0c5.png" alt="crowd" width="600"/>
    <figcaption style="text-align: right;">
        <small>
Das ist evtl. ueberfluessig
        </small>
    </figcaption>
</figure>




## References: 

- <a name="Tordeux2015"></a>[1] Tordeux, A., Chraibi, M., Seyfried, A. (2016). Collision-Free Speed Model for Pedestrian Dynamics. In: Knoop, V., Daamen, W. (eds) Traffic and Granular Flow '15. 
https://doi.org/10.1007/978-3-319-33482-0_29

- <a name="Xu2019"></a>[2] Xu, Q., Chraibi, M., Tordeux, M., Zhang (2019). Generalized collision-free velocity model for pedestrian dynamics. Physica A: Statistical Mechanics and its Applications, Volume 535.
https://doi.org/10.1016/j.physa.2019.122521

- <a name="Rzezonka2022"></a>[3] Rzezonka, J., Chraibi, M., Seyfried, A., Hein, B., Schadschneider, A. (2022). An attempt to distinguish physical and socio-psychological influences on pedestrian bottleneck. Royal Society Open Science.
https://royalsocietypublishing.org/doi/10.1098/rsos.211822

- <a name="Zhang2021"></a>[4] Zhang, S., Zhang, J., Chraibi, M., Song, W. (2021). A speed-based model for crowd simulation considering walking preferences. Communications in Nonlinear Science and Numerical Simulation, Volume 95.
https://doi.org/10.1016/j.cnsns.2020.105624

- <a name="Xu2021"></a>[5] Xu, Q., Chraibi, M., Seyfried, A. (2021). Anticipation in a velocity-based model for pedestrian dynamics. Transportation Research Part C: Emerging Technologies, Volume 133.
https://doi.org/10.1016/j.trc.2021.103464

- <a name="Xu2021"></a>[6] Tordeux, A. talk in TGF15, Delft. [Slides.](https://www.vzu.uni-wuppertal.de/fileadmin/site/vzu/Pres_1st_order_models.pdf)

---- 
###### tags: `pedestriandynamics`