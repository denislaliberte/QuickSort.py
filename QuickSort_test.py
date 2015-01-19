import unittest
from QuickSort import *


class sort_test(unittest.TestCase):
  def test_return_empty_list(self):
    self.assertEqual(sort([]),[])
  def test_return_one_element_list(self):
    self.assertEqual(sort([1]),[1])
  def test_sort_three_items(self):
    self.assertEqual(sort([3,2,1]),[1,2,3])
    self.assertEqual(sort([-1,2,3]),[-1,2,3])
  def test_sort_more_items(self):
    self.assertEqual(sort([3,2,1,4]),[1,2,3,4])
    self.assertEqual(sort([5,3,2,1,4]),[1,2,3,4,5])
  def test_middle_index(self):
    self.assertEqual(middle_value([1,2,3]),2)
