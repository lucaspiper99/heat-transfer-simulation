# Heat Transfer Simulation
## Exercise 2: Simulating and visualising temperature distribution in a material

### Description

The goal of this exercise is to simulate and visualize the temperature distribution in a material retrieved from Neal Wagner's "The Distillation of Human Knowledge" cartoon (Wagner, 1978). Considering the geometry and the boundary conditions specified in the cartoon, the simulation consists of a continuous application of a two-dimensional Laplace equation using finite differences.

The material was discretized into a mesh of quadrangular elements with customizable size (`resolution`) uniform temperature. Initially all the interior elements have the same costumizable temperature (`init_temp`). Furthermore, the simulation ends when the sum of temperature differences between same elements of consecutive iterations reaches a pre-determined value (`threshold`). The following values were assigned:

- `init_temp = 90`
- `resolution = 13`
- `threshold = 10`

### How to Run

In order to access the visualization, it's necessary to have Python installed with all the modules specified in the [requirements file](requirements.txt). Afterwards, the visualization can be launched by running `simulation.py`.

On Windows:

> `pip install -r requirements.txt`

> `python simulation.py`

### References

- Wagner, N. (1978) The Distillation of Human Knowledge. In Kaufman, R. E., *A FORTRAN Coloring Book*. MIT Press.