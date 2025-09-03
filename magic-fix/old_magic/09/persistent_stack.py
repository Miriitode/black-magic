from dataclasses import dataclass

@dataclass
class Node[T]:
    value: T
    next: "Node[T] | None" = None


class Stack[T]:
    def __init__(self, sz=0, head=None):
        self.sz = sz
        self.head = head
        super().__init__()

    def push(self, value) -> "Stack[T]":
        return Stack(self.sz + 1, Node(value, self.head))

    def pop(self) -> "tuple[T, Stack[T]]":
        if self.sz == 0:
            raise ValueError
        return (self.head.value, Stack(self.sz - 1, self.head.next))

    def __len__(self):
        return self.sz

stack = Stack()

a = stack.push(0)
a = a.push(1)
a = a.push(3)
a = a.push(7)
