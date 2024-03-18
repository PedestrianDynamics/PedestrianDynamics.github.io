---
title: Social Force Model
math: true
---

## Introduction to Social Force Model

The Social Force Model [[1]](#Helbing2000) is a force-based model that defines the movement of pedestrians by the combination of different social forces affecting an individual. 

There are three basic forces that affect an individual. The driving force represents a person's desire to move in a certain direction, independent of other people and obstacles. The agent force is caused by the interaction between the individuals and causes them to avoid each other in order to avoid collisions. The obstacle force acts in a similar way to the person force to avoid collisions with obstacles in the environment.

## Driving force
The driving force defines the force that propels pedestrians towards their intended destinations:

$$ \overrightarrow{F_i^{\mathrm{drv}}}=\frac{v_i^0\overrightarrow{e_i^0} - \overrightarrow{v_i}}{\tau}$$
* $v_i^0$ is the desired speed
* $\overrightarrow{e_i^0}$ is the desired direction
* $v_i$ is the currect velocity
* $\tau$ is the reaction time

{{< figure src="Driving_Force.png" width="500">}}

In the figure above, the black dot represents an agent. Its radius is represented by the gray circle around it. The desired direction is towards the target, which is indicated by an X.

## Agent force
The agents exert a repulsive force on each other, which increases exponentially with their proximity. When they collide the pushing forces are increased additionally. When colliding, a frictional force also occurs, which acts orthogonally to the repulsive force in the direction of the speed difference. 

$$ \overrightarrow{F\_i^{\mathrm{ped}}} = \sum_{j} \overrightarrow{f_{ij}}$$

$$\overrightarrow{f_{ij}} = [A_i exp[(r_{ij} - d_{ij})/B_i] + kg(r_{ij} - d_{ij})] \overrightarrow{n_{ij}} + \kappa g(r_{ij} - d_{ij}) \Delta v\_{ji}^t \overrightarrow{t_{ij}}$$

$$\phantom{......}\fbox{\phantom{...................} pushing \phantom{...................}} \fbox{\phantom{......} sliding \phantom{......}}$$

* $j$ is another agent
* $r_{ij} = r_i + r_j$ is the combined radius of $i$ and $j$
* $d_{ij}$ is the distance between $i$ an $j$ them. 
* $A_i$, $B_i$, $k$ and $\kappa$ are constants 
  -  $A_i$ agent scale
  -  $B_i$ force distance
  -  $k$ body force
  -  $\kappa$ friction
* $g$ is a function with $g(x) =  \begin{cases}
                                      x \text{ if } x < 0 \\
                                      \text{ else } 0
                                  \end{cases}$
* $ \overrightarrow{n_{ij}} = (n\_{ij}^1, n\_{ij}^2) = (\overrightarrow{pos\_i} - \overrightarrow{pos\_j})/d\_{ij} $ is the normalised vector from $j$ to $i$ 
* $ \overrightarrow{t_{ij}} = (- n\_{ij}^2, n\_{ij}^1)$ is the tangent of $\overrightarrow{n_{ij}}$ which is perpendicular to it, rotated counterclockwise
* $\Delta v\_{ji}^t = (\overrightarrow{v\_j} - \overrightarrow{v\_i}) \cdot \overrightarrow{t_{ij}}$ is the tangential velocity difference of $i$ and $j$

{{< figure src="Pushing_Agents.png" caption="Direction of repulsive forces acting on an agent" width="500">}}

The repulsive force of the agents acts from the originating agent towards the agent on which the forces act. When their distance greater than their combined radius no other forces apply

{{< figure src="Sliding_Agent_Forces.png" caption="Direction of the pushing and frictional forces acting on colliding agents">}}

If the distance between two agents is smaller than their combined radius, the agents collide and a frictional force also occurs. This frictional force acts orthogonally to the repulsive force in the direction of the velocity difference of the two agents.

## Obstacle force
Obstacles exert a force on the agent similar to a static agent.
The repulsive force is increases exponentially with decreasing distance. When the Obstacle collides with the agent the pushing forces are increased additionally. When colliding, a frictional force also occurs, which acts orthogonally to the repulsive force in the direction of the speed of the agent.

$$ \overrightarrow{F\_i^{\mathrm{obst}}} = \sum_{W} \overrightarrow{f_{iW}}$$

$$\overrightarrow{f_{iW}} = [A_i exp[(r_{i} - d_{iW})/B_i] + kg(r_{i} - d_{iW})] \overrightarrow{n_{iW}} + \kappa g(r_{i} - d_{iW}) (\overrightarrow{v\_{i}}\cdot\overrightarrow{t_{iW}}) \overrightarrow{t_{iW}}$$

$$\phantom{.........}\fbox{\phantom{.....................} pushing \phantom{...................}} \fbox{\phantom{...........} sliding \phantom{...........}}$$

* $W$ is a wall segment
* $r_i$ is the radius agent $i$
* $d_{iW}$ is distance from closest point on the wall segement to $i$
* $\overrightarrow{n_{iW}} = (n\_{iW}^1, n\_{iW}^2) = (\overrightarrow{pos\_i} - \overrightarrow{pos\_W})/d\_{iW}$ the direction from $\overrightarrow{pos\_W}$ the closest point on the wall  to $i$
* $ \overrightarrow{t_{iW}} = (- n\_{iW}^2, n\_{iW}^1)$ is the tangent of $\overrightarrow{n_{iW}}$ which is perpendicular to it, rotated counterclockwise
* $v\_i$ is the velocity of $i$
* $A_i$, $B_i$, $k$ and $\kappa$ are constants 
  -  $A_i$ obstacle scale
  -  $B_i$ force distance
  -  $k$ body force
  -  $\kappa$ friction
* $g$ is a function with $g(x) =  \begin{cases}
                                      x \text{ if } x < 0 \\
                                      \text{ else } 0
                                  \end{cases}$


{{< figure src="Pushing_Obstacle_Force.png" caption="Direction of repulsive forces acting on an agent" width="650">}}

the repulsive force originating from a wall segment acts from the point on the wall segment that is closest to the agent. This point is marked in magenta in the illustration above.

{{< figure src="Sliding_Obstacle_Force.png" caption="Direction of the pushing and frictional forces acting on agents colliding with a wall"  width="800">}}

If the minimal distance to a wallsegment is smaller than the radius of an agent an additional frictional force occurs. This frictional force acts orthogonally to the repulsive force in the direction of the speed difference of the two agents.

## Calculating new velocity and new position from forces
With the definition of the forces affecting an individual, it is possible to calculate its new speed and position.

$$ \overrightarrow{v\_{new}} = \overrightarrow{v\_i} + [\overrightarrow{F\_i^{\mathrm{drv}}} + \frac{\overrightarrow{F\_i^{\mathrm{ped}}} + \overrightarrow{F\_i^{\mathrm{obst}}}}{m\_i}] \cdot \delta T$$

$$ \overrightarrow{pos\_{new}} = \overrightarrow{pos\_i} +  \overrightarrow{v\_{new}} \cdot \delta T$$

Here $m\_i$  denotes the mass of $i$ and $\delta T$ denotes the length one simulation iteration.

## Default values
| Parameter | Value    | Unit     |
|-----------|----------|----------|
| $A_i$     | 2\_000   | N        |
| $B_i$     | 0.08     | m        |
| $k$       | 120\_000 | $\mathrm{\frac{kg}{s^2}}$
| $\kappa$  | 240\_000 | $\mathrm{\frac{kg}{m \cdot s}}$
| $r_i$     |  0.3     | m        |
| $\tau$    | 0.5      | s        |
| $v_i^0$   | 0.8      | $\mathrm{\frac{m}{s}}$
| $m$       | 80       | kg       |


## References
- <a name="Helbing2000"></a>[1] Helbing, D., Farkas, I., Vicsek, T. (2000).
  Simulating dynamical features of escape panic. In: Nature
  <br/>https://doi.org/10.1038/35035023