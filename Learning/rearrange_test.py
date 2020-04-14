#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def basic_test(self):
        test_case = "Dhankher, Naveen"
        expected = "Naveen Dhankher"
        self.assertEqual(rearrange_name(test_case), expected)

unittest.main()
