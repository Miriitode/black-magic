from random import Random

import list_set
import bst
import treap

oset_classes = (
    list_set.OrderedSet,
    bst.OrderedSet,
    treap.OrderedSet,
)


def process_queries(OrderedSet, queries):
    s = OrderedSet()

    for query in queries:
        match query:
            case ['add', val]:
                s.add(val)
            case ['remove', val]:
                s.remove(val)
            case ['contains', val]:
                yield s.contains(val)
            case ['next_larger', val]:
                yield s.next_larger(val)
            case _:
                raise Exception


def main():
    rand = Random(33)

    t = 10**7
    for cas in range(t):
        q = rand.randint(1, rand.choice([3, 11, 31, 111, 1111]))
        V = rand.randint(1, rand.choice([3, 11, 31, 111, 10**9]))
        def randval():
            return rand.randint(-V, V)

        def make_query():
            match rand.choice(('add', 'remove', 'contains', 'next_larger')):
                case 'add':
                    return 'add', randval()
                case 'remove':
                    return 'remove', randval()
                case 'contains':
                    return 'contains', randval()
                case 'next_larger':
                    return 'next_larger', randval()
                case _:
                    raise Exception

        queries = [make_query() for _ in range(q)]

        answers = [[*process_queries(oset_class, queries)]
            for oset_class in oset_classes
        ]

        answer = answers[0]

        print(f"Case {cas} of {t}: {q=} {V=}")
        # print(f"Case {cas} of {t}: {q=} {V=} {answer=}")

        assert all(ans == answer for ans in answers)


if __name__ == '__main__':
    main()
