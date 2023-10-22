---
title: Generalized Centrifugal Force Model
math: true
---

## Introduction to Generalized Centrifugal Force Model

The Generalized Centrifugal Force Model [[1]](#Chraibi2010) is a force-based
model that defines the movement of pedestrians through the combination of
small-range forces. This model represents the spatial requirement of
pedestrians, including their body asymmetry, in an elliptical shape with two
axes dependent on speed. The semi-axis representing the dynamic space
requirement in the direction of motion increases proportionally as speed
increases. Conversely, the semi-axis along the shoulder direction decreases
with higher velocities.

## Basic Principles of Generalized Centrifugal Force Model

GCFM belongs to the class of force-based pedestrian models, which view
pedestrian movement as the result of forces acting on an individual at any
given moment. These so-called acceleration-based models calculate the
acceleration of agents by superposing the forces acting on them.

The movement of pedestrians is influenced by three main forces in the
Generalized Centrifugal Force Model: the destination driving force, the
obstacle repulsive force, and the repulsive force between pedestrians. The
destination driving force propels individuals towards their intended
destinations, taking into account factors such as distance and desired walking
speed. On the other hand, the obstacle-repulsive force pushes pedestrians away
from obstacles to maintain a safe distance from walls or other objects. Lastly,
the repulsive force between pedestrians prevents collisions among them
[[1]](#Chraibi2010).

The model considers both the distance between pedestrians and their relative
velocities. Using an elliptical volume exclusion instead of a circular one has
several advantages. Circular symmetry is inconsistent with the asymmetric space
requirements of pedestrians in terms of their motion direction and transverse
to it. As a force-based model, GCFM describes the temporal changes in
pedestrian movement through the combination of short-range forces acting on
them simultaneously.


## Mathematical description

### Elliptical volume exclusion of agents

The Generalized Centrifugal Force Model incorporates an elliptical volume
exclusion of pedestrians. This means that pedestrians are represented as
elliptical disks with two semi-axes, which depend on their speed. The semi-axis
representing the dynamic space requirement in the direction of motion ($a$)
increases proportionally as speed increases, while the semi-axis along the
shoulder direction decreases with higher speed values ($b$).

{{< figure src="figure1.png" caption="The distance between the borders of the ellipses along a line connecting their centers." >}}

The mathematical description of the elliptical volume exclusion in GCFM is as follows

$$a=a_{\min }+\tau_a v_i$$

and

$$b=b_{\max }-\left(b_{\max }-b_{\min }\right) \frac{v_i}{v_i^0},$$

where $v_i$ is the speed and $v_i^0$ the desired speed of agent $i$.

### Equation of motion

The behavior of agents in motion is influenced by the presence of others,
causing them to deviate from a straight path. Drawing parallels to Newtonian
mechanics, such deviations or accelerations are attributed to a force. Hence,
the equation of motion can be written as:

$$\vec{\ddot x}\_i=\overrightarrow{F\_i^{\mathrm{drv}}}+\sum\_{j \in \mathcal{N}\_{i}} \overrightarrow{F\_{i j}^{\mathrm{rep}}}+\sum\_{w \in \mathcal{W}\_{i}} \overrightarrow{F\_{i w}^{\mathrm{rep}}}.$$


#### Driving force

The driving force in the Generalized Centrifugal Force Model is defined as the
force that propels pedestrians towards their intended destinations:

$$\vec{F}_i^{\mathrm{drv}}=m_i \frac{\overrightarrow{v_i^0}-\overrightarrow{v_i}}{\tau}.$$

#### Pedestrian-pedestrian repulsive force

The pedestrian-pedestrian repulsive force in the Generalized Centrifugal Force
Model is defined as the force that prevents collisions between pedestrians. By
considering the repulsive force between pedestrians, the Generalized
Centrifugal Force Model ensures that individuals maintain a safe distance from
each other.

$${\overrightarrow{F\_{i,j}}}\_{\text {rep }}=-m_i k\_{i j} \frac{\left(\eta\left\|\overrightarrow{v\_i^0}\right\|+v\_{i j}\right)^2}{d\_{i j}} \overrightarrow{e\_{i j}},$$

with the relative speed

$$v_{i j}=\frac{1}{2}\left[\left(\overrightarrow{v_i}-\overrightarrow{v_j}\right) \cdot \overrightarrow{e_{i j}}+\left|\left(\overrightarrow{v_i}-\overrightarrow{v_j}\right) \cdot \overrightarrow{e_{i j}}\right|\right],$$

and a reduction of the influence range to $180^\circ$ by:

$$k_{i j}=\frac{1}{2} \frac{\overrightarrow{v_i} \cdot \overrightarrow{e_{i j}}+\left|\overrightarrow{v_i} \cdot \overrightarrow{e_{i j}}\right|}{v_i}.$$

{{< figure src="figure2.png" caption="The interpolation of the repulsive force between pedestrians." >}}

#### Pedestrian-wall repulsive force

In the Generalized Centrifugal Force Model, the repulsive force between
pedestrians and walls represents the force that propels pedestrians away from
walls and other fixed structures. For a pedestrian labeled as $i$, this
repulsive force is nullified when $i$ moves parallel to the wall. However,
while this force behavior is accurate, it results in minimal repulsion when the
pedestrian's trajectory is nearly aligned with the wall.

For this reason, we characterize in this model walls by three-point masses
acting on pedestrians within a certain interaction range.

{{< figure src="figure2.png" caption="Each wall is modeled as three static point masses acting on pedestrians." >}}

## Limitations of the GCFM

As a force-based model, the GCFM suffers from several drawbacks typical for
force-based models, namely the duality problem of overlapping and oscillations.

It is possible to reduce the amount of overlapping among agents, by increasing
the strength of the repulsive forces. However, this leads inevitably to an
increase of oscillations in the movements of agents, which in turn can only be
mitigated by decreasing the strength of the repulsive forces.  See
[[2]](#Chraibi203) for a more in-depth analysis of this issue.

## Challenges in Implementing GCFM

The computational cost of the GCFM is high, as it requires continuous
calculations to determine the forces and interactions between pedestrians. This
includes calculating distances between ellipses, such as the closest approach
distance. Additionally, while the strength of repulsive force decreases with
increasing distance between pedestrians, it currently has an infinite range,
which is unrealistic for pedestrian interactions. To address this, we propose
introducing a cutoff radius for the force to limit interactions only to
adjacent pedestrians. However, implementing this cutoff radius requires a
two-sided Hermite-interpolation of the repulsive force and further increases
computational complexity. Furthermore, finding appropriate values for model
parameters that are independent of neighborhood properties and reduce
overlapping and oscillation is challenging.

## References:

- <a name="Chraibi2010"></a>[1] Chraibi, M., Seyfried, A., Schadschneider, A.
  (2010). Generalized centrifugal-force model for pedestrian dynamics, Physical
  Review E, 82, 4
  <br/>https://link.aps.org/doi/10.1103/PhysRevE.82.046111
- <a name="Chraibi2013"></a>[2] Chraibi, M., Schadschneider, A., Seyfried, A.
  (2013). On Force-Based Modeling of Pedestrian Dynamics.
  <br/>https://doi.org/10.1007/978-1-4614-8483-7_2
