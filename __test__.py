from typing import List
import unittest

import ListF
import sorting

class UnitTestListF(unittest.TestCase):
    def test_sorted(self):
        self.assertEqual(ListF.listIsSorted([]), True)
        self.assertEqual(ListF.listIsSorted([1]), True)
        self.assertEqual(ListF.listIsSorted([1, 1]), True)
        self.assertEqual(ListF.listIsSorted([0, 1]), True)
        self.assertEqual(ListF.listIsSorted([1, 0]), False)
        self.assertEqual(ListF.listIsSorted([0, 1, 5, 7, 8, 12]), True)
        self.assertEqual(ListF.listIsSorted([0, 1, 5, 8, 7, 12]), False)

class UnitTestSorting(unittest.TestCase):
    def test_sorting(self):
        unsorted = ListF.randomIntList(100)
        sorted = unsorted.copy()
        sorting.selection(sorted)
    
    def test_edge_cases(self):
        Lists: List[list] = [
            [],
            [1],
            [1, 0],
            [1, 2, 3],
            [0, 12, 4],
            ['abc','123','bacon','apple']
        ]

        for l in Lists:
            c = l.copy()
            sorting.selection(c)
            self.assertTrue(ListF.listIsSorted(c))

if __name__ == '__main__':
    unittest.main()

