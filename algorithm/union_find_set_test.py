import unittest

from algorithm import union_find_set


class IntNode(union_find_set.Node):
    def __init__(self, num):
        self.num = num

    def __hash__(self):
        return self.num


class TestUnionFindSet(unittest.TestCase):
    def test_union_find(self):
        cases = [
            ([(1, 3), (3, 5), (5, 7), (2, 4), (4, 6), (6, 8)], [(3, 7), (4, 6)], [(3, 4), (6, 7)]),
            ([(1, 2), (2, 3), (3, 4), (5, 6), (6, 7), (7, 8)], [(1, 4), (5, 7)], [(1, 5), (3, 7)]),
            ([(1, 2), (2, 3), (4, 5), (5, 6), (7, 8), (8, 7)], [(1, 3), (7, 8)], [(1, 5), (3, 7)]),
        ]
        for case in cases:
            edges, unions, no_unions = case
            ufset = union_find_set.UnionFindSet()
            for edge in edges:
                a, b = edge
                a, b = IntNode(a), IntNode(b)
                ufset.union(a, b)
            print(ufset.parent)
            for edge in unions:
                a, b = edge
                a, b = IntNode(a), IntNode(b)
                self.assertEqual(ufset.find(a), ufset.find(b))
            for edge in no_unions:
                a, b = edge
                a, b = IntNode(a), IntNode(b)
                self.assertNotEqual(ufset.find(a), ufset.find(b))

    def test_get_unions(self):
        cases = [
            ([(1, 3), (3, 5), (5, 7), (2, 4), (4, 6), (6, 8)], 2),
            ([(1, 2), (2, 3), (3, 4), (5, 6), (6, 7), (7, 8)], 2),
            ([(1, 2), (2, 3), (4, 5), (5, 6), (7, 8), (8, 7)], 3),
        ]
        for case in cases:
            edges, n_unions = case
            ufset = union_find_set.UnionFindSet()
            for edge in edges:
                a, b = edge
                a, b = IntNode(a), IntNode(b)
                ufset.union(a, b)
            unions = ufset.get_unions()
            self.assertEqual(len(unions), n_unions)
