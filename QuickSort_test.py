import unittest
from QuickSort import sort


class sort_test(unittest.TestCase):
  def test(self):
    self.assertEqual(sort([]),[])
