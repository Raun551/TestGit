#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def basic_test(self):
        testcase = "Dhankher, Naveen"
        expected = "Naveen Dhankher"
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
     
    def test_second(self):
        testcase = "Malik Raunaq"
        expected = "Raunaq Malik"
        self.assertEqual(rearrange_name(testcase) , expected)
    
    def test_one(self):
        testcase = "Raja"
        expected = "Raja"
        self.assertEqual(rearrange_name(testcase) , expected)
    
        
unittest.main()
