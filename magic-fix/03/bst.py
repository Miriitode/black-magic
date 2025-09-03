from dataclasses import dataclass


@dataclass
class Node:
    val: int
    l: "Node | None" = None
    r: "Node | None" = None


def _add(node, val):
    # assumes val is not in the tree
    if node is None:
        return Node(val)

    assert val != node.val

    if val < node.val:
        node.l = _add(node.l, val)
        return node
    else:
        assert val > node.val
        node.r = _add(node.r, val)
        return node


def _remove_smallest(node):
    assert node is not None

    if node.l is None:
        return node.val, node.r
    else:
        v, x = _remove_smallest(node.l)
        node.l = x
        return v, node


def _remove(node, val):
    # assumes val is in the tree
    assert node is not None

    if val == node.val:
        if node.r is None:
            return node.l
        else:
            v, x = _remove_smallest(node.r)
            node.r = x
            node.val = v
            return node

    if val < node.val:
        node.l = _remove(node.l, val)
        return node
    else:
        assert val > node.val
        node.r = _remove(node.r, val)
        return node


def add(node, val):
    if contains(node, val):
        return node
    else:
        return _add(node, val)


def remove(node, val):
    if not contains(node, val):
        return node
    else:
        return _remove(node, val)


def contains(node, val):
    if node is None:
        return False

    if val == node.val:
        return True

    if val < node.val:
        return contains(node.l, val)
    else:
        assert val > node.val
        return contains(node.r, val)


def next_larger(node, val):
    if node is None:
        return None

    if val < node.val:
        res = next_larger(node.l, val)
        if res is not None:
            return res
        return node.val
    else:
        assert val >= node.val
        return next_larger(node.r, val)


class OrderedSet:
    def __init__(self):
        self.root = None
        super().__init__()

    def add(self, val):
        self.root = add(self.root, val)

    def remove(self, val):
        self.root = remove(self.root, val)

    def contains(self, val):
        return contains(self.root, val)

    def next_larger(self, val):
        return next_larger(self.root, val)
