import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import score


class TestSeverity(unittest.TestCase):
    def test_max_is_p1(self):
        self.assertEqual(score(5, 5), "P1")

    def test_mid_is_p2(self):
        self.assertEqual(score(4, 3), "P2")

    def test_low_is_p4(self):
        self.assertEqual(score(1, 1), "P4")
