from dataclasses import dataclass

@dataclass(order=True)
class Edge:
    i: int
    j: int
