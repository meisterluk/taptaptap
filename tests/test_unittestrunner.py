#!/usr/bin/env python

import random
import unittest

from taptaptap.api import UnittestRunner

##     validity: 0
## ok testcases: 3 / 3
##      bailout: no
##       stdout: 1..3
##       stdout: test_shuffle
##       stdout: Running time


class TestSequenceFunctions(unittest.TestCase):
    """Example by `python unittest module`_

    .. _`python unittest module`: http://docs.python.org/2/library/unittest.html
    """

    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main(testRunner=UnittestRunner())
