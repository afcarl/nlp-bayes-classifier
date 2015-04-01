Natural Language Processing - Bayes classifier
============

P(c|w) = (P(w|c) * P(c)) / P(w)

where:

c - the best fix for entered word
w - entered word

Run:
~~~
pip install -r requirements.txt
python -m test_stats
python -m test_bayes
python stats.py żołnież rzołnież
python bayes.py alamakoty test/dramat.iso.utf8 test/dictionary2.txt
~~~
