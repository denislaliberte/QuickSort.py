import unittest
from QuickSort import sort


class sort_test(unittest.TestCase):
  def test_return_empty_list(self):
    self.assertEqual(sort([]),[])
  def test_return_one_element_list(self):
    self.assertEqual(sort([1]),[1])
  def test_sort_three_items(self):
    self.assertEqual(sort([3,2,1]),[1,2,3])
