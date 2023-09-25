
import matplotlib.pyplot as pyplot
from math import pi, cos, sin, sqrt
from typing import Dict, Optional, Tuple


from datatypes import (
    FigureConfig,
    AxisConfig,
    NodeConfig,
    LeastElementsConfig,
    ConFig,
    Node,
    Edge,
)

class Figure(object):
    def __init__(self, n_total_elements: int, n_least_elements: int):
        self.n = n_total_elements
        self.N = n_least_elements
        self.config = ConFig(
            fig=FigureConfig(),
            axis=AxisConfig(),
            node=NodeConfig(),
            least_elements=LeastElementsConfig(theta_offset=pi/self.N),
        )

        self.least_element_coords = self.get_least_elements_coords()
        self.fig, self.ax = self.setup_figure()
        self.node_registry = self.setup_nodes()
        self.edge_registry = set()

    def get_least_elements_coords(self) -> Dict[int, Tuple[float, float]]:
        return {
            k: self.polar2cart(self.config.least_elements.dist_from_origin, self.theta(k))
            for k in range(1, self.N + 1)
        }

    @staticmethod
    def polar2cart(radius: float, radians: float) -> Tuple[float, float]:
        return radius * cos(radians), radius * sin(radians)

    def theta(self, k: int) -> float:
        """
        Returns the angle in radians for least_element (mod N_LEAST_ELEMENTS)

        The goal is to have all N_LEAST_ELEMENT elements be equally distributed
        around the unit circle.
        """
        if self.is_least_element(k):
            return 2*(k-1)*pi / self.N + self.config.least_elements.theta_offset
        else:
            raise ValueError(f"Argument k={k} should be an integer between 1 and {self.N}")

    def is_least_element(self, k: int):
        return isinstance(k, int) and 1 <= k and k <= self.N

    def setup_figure(self):
        fig, ax = pyplot.subplots(1, 1, figsize=self.config.fig.size)
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        axis_range = (self.config.axis.amin, self.config.axis.amax)
        ax.set_xlim(axis_range)
        ax.set_ylim(axis_range)
        return fig, ax

    def setup_nodes(self):
        return {
            k: Node(
                label=str(k),
                coords=self.node_coords(k),
                radius=self.config.node.radius,
                fontsize=self.config.node.fontsize,
            )
            for k in range(1, self.n + 1)
        }

    def node_coords(self, k: int) -> Tuple[float, float]:
        """
        Sets node coordinates so that elements of [k]_modN are in a line to [k] itself

        The least elements are the canonical representatives of their orbit. These are
        arranged around the "unit" circle at equal angles (although the canvas radius
        may be greater than 1, this scale is not exposed; it may as well be a unit circle).

        Non-least elements are arranged in a line that "points" toward their least element.
        For example, if N=6, the least element [1] has non-least elements 7, 13, 20, ...
        This function takes the divisor and modulus of the input k. The modulus is used
        to determine the least element. And the divisor is used to determine distance from
        the least element. The angle of the line is chosen to generate a semi-spiral look.
        """
        if self.is_least_element(k):
            return self.least_element_coords[k]
        else:
            mult, rem = (k - 1) // self.N, ((k - 1) % self.N) + 1
            x0, y0 = self.least_element_coords[rem]
            dx, dy = self.polar2cart(
                mult * self.config.node.nodesep,
                self.theta(rem) + self.config.least_elements.theta_offset
            )
            return x0 + dx, y0 + dy

    def register_strand(self, least_element: int, decreasing_order: bool):
        if not self.is_least_element(least_element):
            raise ValueError(f"Value {least_element} is not a least element")
        node_indices = sorted(
            [k for k in self.node_registry if ((k - 1) % self.N) + 1 == least_element],
            reverse=decreasing_order
        )
        for i in range(len(node_indices) - 1):
            self.edge_registry.add((node_indices[i], node_indices[i+1]))

    def render(self):
        for node in self.node_registry.values():
            self.draw_node(node)
        for from_node_index, to_node_index in self.edge_registry:
            self.draw_edge(from_node_index, to_node_index)

    def savefig(self, filename: str):
        self.fig.savefig(filename)

    def draw_node(self, node: Node):
        # nodes ae automatically drawn within axis boundaries
        self.ax.add_patch(pyplot.Circle(node.coords, node.radius))
        x = node.coords[0] - self.config.node.text_offset_x
        y = node.coords[1] - self.config.node.text_offset_y
        if self.within_axes(x, y):
            self.ax.text(x, y, node.label, fontsize=node.fontsize)

    def within_axes(self, x: float, y: float) -> bool:
        return not any([
            x < self.config.axis.amin,
            x > self.config.axis.amax,
            y < self.config.axis.amin,
            y > self.config.axis.amax,
        ])

    def draw_edge(self, from_node_index: int, to_node_index: int):
        from_coords = self.node_registry[from_node_index].coords
        to_coords = self.node_registry[to_node_index].coords
        delta_x, delta_y = to_coords[0] - from_coords[0], to_coords[1] - from_coords[1]
        Delta = sqrt(delta_x * delta_x + delta_y * delta_y)
        node_proportion = self.config.node.radius / Delta
        node_offset = node_proportion * delta_x, node_proportion * delta_y
        arrow_end = (to_coords[0] - node_offset[0], to_coords[1] - node_offset[1])
        arrow_start = (from_coords[0] + node_offset[0], from_coords[1] + node_offset[1])
        if self.within_axes(arrow_start[0], arrow_start[1]) and self.within_axes(arrow_end[0], arrow_end[1]):
            self.ax.annotate("", xy=arrow_end, xytext=arrow_start, arrowprops=dict(arrowstyle="->"))
