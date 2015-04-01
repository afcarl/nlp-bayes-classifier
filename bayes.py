# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
from stats import levenshtein
from operator import itemgetter
from heapq import nlargest

def get_probability_w_given_c(word, dictionary):
  lines = [line.strip() for line in open(dictionary)]
  lines_map = {}
  for line in lines:
    lines_map[line] = levenshtein(unicode(line, "utf-8"), word)

  levenshtein_counters = {}
  for line in lines_map:
    if lines_map[line] not in levenshtein_counters:
      levenshtein_counters[ lines_map[line] ] = 1.
    else:
      levenshtein_counters[ lines_map[line] ] += 1.

  for counter in levenshtein_counters:
    levenshtein_counters[counter] /= len(lines_map)

  return levenshtein_counters

def get_probability_map_w_given_c(mistakes_file):
  lines = [line.strip().split(';') for line in open(mistakes_file)]
  levenshtein_counters = {}
  for line in lines:
    dist = levenshtein(unicode(line[0], "utf-8"), unicode(line[1], "utf-8"))
    if dist not in levenshtein_counters:
      levenshtein_counters[ dist ] = 1.
    else:
      levenshtein_counters[ dist ] += 1.

  for counter in levenshtein_counters:
    levenshtein_counters[counter] /= len(lines)

  return levenshtein_counters

def get_probability_function_c(corpus, dictionary):
  words_in_corpus = 0
  words_counters = {}
  with open(corpus) as f:
    for line in f:
      for word in line.split():
        word2 = word.lower().rstrip('?:!.,;')
        if word2 not in words_counters:
          words_counters[word2] = 1.
        else:
          words_counters[word2] += 1.
        words_in_corpus += 1
  words_in_dictionary = sum(1 for line in open(dictionary))

  for word in words_counters:
    words_counters[word] = (words_counters[word] + 1.) / (words_in_corpus + words_in_dictionary)

  def get_probability_c(fix_word):
    if fix_word in words_counters:
      return words_counters[fix_word]
    else:
      return 1. / (words_in_corpus + words_in_dictionary)

  return get_probability_c

def bayes(word, corpus, dictionary, verbose=False):
  probability_w_given_c = get_probability_map_w_given_c('test/bledy.txt')
  probability_function_c = get_probability_function_c(corpus, dictionary)

  lines = [line.strip() for line in open(dictionary)]
  fixes = {}
  for fix_word in lines:
    levenshtein_distance = levenshtein(unicode(fix_word, "utf-8"), word)
    probability_w = probability_w_given_c[levenshtein_distance] if levenshtein_distance in probability_w_given_c else 0
    probability_c = probability_function_c(fix_word)
    fixes[fix_word] = probability_w**5*probability_c

  if verbose:
    for line, score in nlargest(20, fixes.items(), key=itemgetter(1)):
      print line, " : ", score

  return max(fixes.iteritems(), key=itemgetter(1))[0]


if __name__ == '__main__':
  if len(sys.argv) == 4:
    word = unicode(sys.argv[1], "utf-8")
    corpus = sys.argv[2]
    dictionary = sys.argv[3]

    print bayes(word, corpus, dictionary, verbose=True)

  else:
    print("python stats.py [dictionary] [word2]")

