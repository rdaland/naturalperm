
import matplotlib.pyplot as pyplot
from math import pi, cos, sin
from typing import Tuple


# Axis constants
AXIS_MIN = -10
AXIS_MAX = 10

# Numbernode constants
N_LEAST_ELEMENTS = 6
LEAST_RADIUS = 3.0
NODE_RADIUS = 1.0
THETA_OFFSET = pi / 6
NODESEP = LEAST_RADIUS


class Figure1:
    def __init__(self, config: Optional[dict] = None):
        self.config = DEFAULT_CONFIG
        if config:
            self.config.update(config)

        self.fig, self.ax = self.setup()

    def setup(self):
        fig, ax = pyplot.subplots(1, 1, figsize=self.config["figsize"])
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        axis_range = (config["axis_min"], config["axis_max"])
        ax.set_xlim(axis_range)
        ax.set_ylim(axis_range)


    def draw_arrow():
        pass


# TODO: add pyplot.arrow() in elements in their mod groups
# TODO: add pyplot.arrow() for least elements
# TODO: figure out how to color circles so all ones in an orbit are same
# TODO: object-orient this code for modularity and clarity
# TODO: make non-least element nodes smaller? and paler?

def polar2cart(radius: float, radians: float) -> Tuple[float]:
    return (radius * cos(radians), radius * sin(radians))




LEAST_ELEMENT_COORDS = {
    n: polar2cart(LEAST_RADIUS, theta(n))
    for n in range(1, N_LEAST_ELEMENTS + 1)
}



# Graph setup
fig, ax = pyplot.subplots(1, 1, figsize=(10, 10))
ax.axis("off")
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_xlim((AXIS_MIN, AXIS_MAX))
ax.set_ylim((AXIS_MIN, AXIS_MAX))

for n in range(1, 20):
    node_coords = int2coords(n)
    ax.add_patch(pyplot.Circle(node_coords, NODE_RADIUS))
    pyplot.text(node_coords[0], node_coords[1], str(n), fontsize="x-large")


fig.savefig("fig1.png")
