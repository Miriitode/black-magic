from dataclasses import dataclass
from random import Random

rand = Random()


@dataclass
class Node:
    val: int
    priority: int
    l: "Node | None" = None
    r: "Node | None" = None


def split(node, val):
    if node is None:
        return None, None, None

    if val == node.val:
        return node.l, node, node.r

    if val < node.val:
        l, m, r = split(node.l, val)
        node.l = r
        return l, m, node
    else:
        l, m, r = split(node.r, val)
        node.r = l
        return node, m, r


def merge(l, r):
    if l is None:
        return r
    if r is None:
        return l

    if l.priority < r.priority:
        # r must be the root
        r.l = merge(l, r.l)
        return r
    else:
        # l must be the root
        l.r = merge(l.r, r)
        return l


def _add(node, val):
    # assumes val is not in the tree
    l, m, r = split(node, val)
    assert m is None
    m = Node(val, priority=rand.getrandbits(64))
    return merge(merge(l, m), r)


def _remove(node, val):
    # assumes val is in the tree
    l, m, r = split(node, val)
    assert m is not None and m.val == val
    return merge(l, r)


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
