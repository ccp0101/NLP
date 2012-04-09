
# http://hetland.org/coding/python/nbayes.py

from __future__ import division

class NaiveBayesClassifier:
    
    """
    A naive Bayesian classifier. The observation vectors can be
    arbitrary iterable objecs with hashable values. The classes should
    also be hashable.
    """

    def __init__(self):
        self.prior = {}  # Frequency of each class
        self.total = {}  # Frequency of each (class, value)-tuple
        self.count = 0   # Number of observations
        self.vocabs = {}

    def add(self, cls, obs):
        'Adds an observation to the classifier'
        self.prior[cls] = self.prior.get(cls, 0) + 1
        for idx, val in enumerate(obs):
            key = cls, val
            self.total[key] = self.total.get(key, 0) + 1
            self.vocabs[val] = self.vocabs.get(val, 0) + 1
        self.count += 1

    def discr(self, cls, obs):
        'Bayesian discriminant. Proportional to posterior probability'
        result = self.prior[cls]/self.count
        for idx, val in enumerate(obs):
            freq = self.total.get((cls, val), 0) + 1
            result *= freq/(self.prior[cls] + len(self.vocabs))
        return result

    def classify(self, obs):
        'Classifies an observation'
        candidates = [(self.discr(c, obs), c) for c in self.prior]
        return max(candidates)[1]

    def score(self, obs):
        candidates = [(self.discr(c, obs), c) for c in self.prior]
        return candidates

    def train(self, generator):
        'Train observations from generator function yielding (cls, obs)'
        for cls, obs in generator:
            self.add(cls, obs)

