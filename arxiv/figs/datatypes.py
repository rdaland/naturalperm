from dataclasses import dataclass
from enum import Enum

@dataclass
class FigureConfig:
    """Figure width/height on screen"""
    size: tuple[float, float] = (10.0, 10.0)


@dataclass
class AxisConfig:
    """Axis coordinates for canvas"""
    amin: float = -10.0
    amax: float = 10.0


@dataclass
class NodeConfig:
    """Properties shared by generic nodes"""
    radius: float = 1.0
    fontsize: str = "x-large"
    nodesep: float = 3.0
    text_offset_x: float = 0.20
    text_offset_y: float = 0.20


@dataclass
class LeastElementsConfig:
    """Number of least elements and arrangement on circle"""
    theta_offset: float
    dist_from_origin: float = 3.0


@dataclass
class ConFig:
    fig: FigureConfig
    axis: AxisConfig
    node: NodeConfig
    least_elements: LeastElementsConfig


@dataclass
class Node:
    label: str
    coords: tuple[float, float]
    radius: float
    fontsize: str


@dataclass
class Edge:
    from_coords: tuple[float, float]
    to_coords: tuple[float, float]
