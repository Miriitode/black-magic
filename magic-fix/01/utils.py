from dataclasses import dataclass

@dataclass(order=True)
class Edge:
    cost: int
    i: int
    j: int
