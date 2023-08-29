
# import matplotlib
# matplotlib.use("QtAgg")

import matplotlib.pyplot as pyplot
from math import pi, cos, sin

# Axis constants
AXIS_MIN = -10
AXIS_MAX = 10

# Numbernode constants
N_LEAST_ELEMENTS = 6
LEAST_RADIUS = 3.0
NODE_RADIUS = 1.0

# Graph setup
fig, ax = pyplot.subplots(1, 1, figsize=(10, 10))
ax.axis("off")
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_xlim((AXIS_MIN, AXIS_MAX))
ax.set_ylim((AXIS_MIN, AXIS_MAX))


def polar2cart(radius: float, radians: float):
    return (radius * cos(radians), radius * sin(radians))


for n in range(N_LEAST_ELEMENTS):
    node_coords = polar2cart(LEAST_RADIUS, 2*n*pi / N_LEAST_ELEMENTS)
    ax.add_patch(pyplot.Circle(node_coords, NODE_RADIUS))

fig.savefig("fig1.png")
