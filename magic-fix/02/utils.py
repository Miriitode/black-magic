from dataclasses import dataclass

@dataclass(order=True)
class Edge:
    cost: int
    i: int
    j: int

    def __iter__(self):
        yield self.i
        yield self.j
        yield self.cost
