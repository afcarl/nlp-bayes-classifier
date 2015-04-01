# -*- coding: utf-8 -*-
#!/usr/bin/env python

import unittest
from bayes import get_probability_w_given_c, get_probability_function_c, bayes


class TestLogger(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_get_probability_w_given_c(self):
    self.assertDictEqual(
      {0.0: 0.1, 4.25: 0.1, 2.0: 0.1, 4.0: 0.2, 5.0: 0.2, 6.0: 0.3},
      get_probability_w_given_c(u'abcd', 'test/dictionary.txt') )

  def test_get_c(self):
    probability_function_c = get_probability_function_c('test/dramat.iso.utf8', 'test/dictionary.txt')
    print probability_function_c(u'asdf')
    print probability_function_c(u'qwertyuiopzxcv')
    print probability_function_c(u'widocznie')
    print probability_function_c(u'a')

  def test_bayes(self):
    print bayes(u'abcd', 'test/dictionary.txt', 'test/dictionary.txt')

if __name__ == '__main__':
  unittest.main()
