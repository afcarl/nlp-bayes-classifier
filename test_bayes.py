# -*- coding: utf-8 -*-
#!/usr/bin/env python

import unittest
from bayes import get_probability_w_given_c, get_probability_function_c, bayes, get_probability_map_w_given_c


class TestLogger(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_get_probability_w_given_c(self):
    self.assertDictEqual(
      {0.0: 0.1, 4.25: 0.1, 2.0: 0.1, 4.0: 0.2, 5.0: 0.2, 6.0: 0.3},
      get_probability_w_given_c(u'abcd', 'test/dictionary.txt') )

  def test_get_probability_w_given_c2(self):
    self.assertDictEqual(
      {1.25: 0.13539445628997868, 1.0: 0.28251599147121537, 2.0: 0.1652452025586354, 3.0: 0.046908315565031986, 4.0: 0.013859275053304905, 5.0: 0.005330490405117271, 2.25: 0.03624733475479744, 7.0: 0.0010660980810234541, 0.0: 0.0010660980810234541, 0.75: 0.008528784648187633, 2.5: 0.014925373134328358, 4.25: 0.0031982942430703624, 1.75: 0.0042643923240938165, 2.75: 0.0021321961620469083, 6.0: 0.0010660980810234541, 0.5: 0.11513859275053305, 1.5: 0.03091684434968017, 3.25: 0.008528784648187633, 0.25: 0.12366737739872068},
      get_probability_map_w_given_c('test/bledy.txt'))

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
