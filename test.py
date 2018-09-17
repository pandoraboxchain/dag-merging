import unittest

from main import Block, Chain, merge

class TestSimple(unittest.TestCase):
    
    def test_simple(self):
        zero = Block(0, 0, False, True)
        first = Block(1, 1, False, True)
        second = Block(2, 2, False, False)
        third = Block(3, 3, False, False)

        zero_chain = Chain([zero, first, second])
        first_chain = Chain([zero, third])

        res = merge([zero_chain, first_chain])
        self.assertEqual(res["deterministic_ordering"][0], 0)
        self.assertEqual(res["deterministic_ordering"][1], 1)

        self.assertEqual(len(res["merged_chain"]), 4)
        self.assertEqual(res["merged_chain"][0], zero)
        self.assertEqual(res["merged_chain"][1], first)
        self.assertEqual(res["merged_chain"][2], second)
        self.assertEqual(res["merged_chain"][3], third)

unittest.main()
