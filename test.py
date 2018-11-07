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

    def test_another_simple(self):
        zero = Block(0, 0, False, True)
        first = Block(1, 1, False, True)
        second = Block(2, 2, False, False)
        third = Block(3, 3, False, False)

        zero_chain = Chain([zero, first, third])
        first_chain = Chain([zero, second])

        res = merge([zero_chain, first_chain])
        self.assertEqual(res["deterministic_ordering"][0], 0)
        self.assertEqual(res["deterministic_ordering"][1], 1)

        self.assertEqual(len(res["merged_chain"]), 4)
        self.assertEqual(res["merged_chain"][0], zero)
        self.assertEqual(res["merged_chain"][1], first)
        self.assertEqual(res["merged_chain"][2], third)
        self.assertEqual(res["merged_chain"][3], second)

    def test_3_with_im(self):

        zero = Block(0, 0, False, True)
        first = Block(1, 1, False, False)
        second = Block(2, 2, False, False)

        zero_chain = Chain([
            zero,
            first,
            Block(2, 3, True, False),
            Block(3, 4, False, False),
            Block(4, 5, False, False),
            Block(5, 6, True, False),
            Block(6, 7, False, False),
            Block(7, 8, True, False),
            Block(8, 9, True, False),
            Block(9, 10, False, False),
        ])

        first_chain = Chain([
            zero,
            first,
            second,
            Block(3, 11, True, False),
            Block(4, 12, True, False),
            Block(5, 13, False, False),
            Block(6, 14, True, False),
            Block(7, 15, True, False),
            Block(8, 16, True, False),
            Block(9, 17, True, False),
        ])

        first_im = Block(first.timeslot, first.identifier, 
            first.is_empty, True)
        second_im = Block(second.timeslot, second.identifier, 
            second.is_empty, True)

        second_chain = Chain([
            zero,
            first_im,
            second_im,
            Block(3, 18, True, True),
            Block(4, 19, True, True),
            Block(5, 20, True, True),
            Block(6, 21, True, True),
            Block(7, 22, False, False),
            Block(8, 23, False, False),
            Block(9, 24, True, False),
        ])

        res = merge([zero_chain, first_chain, second_chain])

        self.assertEqual(res["merged_chain"][0].timeslot, 0)
        self.assertEqual(res["merged_chain"][1].timeslot, 1)
        self.assertEqual(res["merged_chain"][2].timeslot, 2)
        self.assertEqual(res["merged_chain"][3].timeslot, 3)
        self.assertEqual(res["merged_chain"][4].timeslot, 4)
        self.assertEqual(res["merged_chain"][5].timeslot, 6)
        self.assertEqual(res["merged_chain"][6].timeslot, 9)
        self.assertEqual(res["merged_chain"][7].timeslot, 7)
        self.assertEqual(res["merged_chain"][8].timeslot, 8)
        self.assertEqual(res["merged_chain"][9].timeslot, 5)

unittest.main()
