import unittest

from main import Block, Chain, merge

class SimpleTest(unittest.TestCase):
    
    def simple_test(self):
        zero = Block(0, 0, False, True)
        first = Block(1, 1, False, True)
        second = Block(2, 2, False, False)
        third = Block(3, 3, False, False)

        zero_chain = Chain([zero, first, second])
        first_chain = Chain([zero, third])

        res = merge(zero_chain, first_chain)

unittest.main()
