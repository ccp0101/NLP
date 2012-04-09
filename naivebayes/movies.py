from naivebayes import NaiveBayesClassifier
import os
import re

def review_generator(dir):
    classes = os.listdir(dir)
    for cls in classes:
        print "Enumerating for '%s' reviews." % cls
        cls_dir = os.path.join(dir, cls)
        files = filter(lambda x: x.endswith(".txt"), os.listdir(cls_dir))
        for filename in files:
            with open(os.path.join(cls_dir, filename), "r") as file:
                for line in file:
                    words = line.split()
                    words = filter(lambda x: re.match(r'^\w{3,}$', x), words)
                    yield (cls, words)

generator = review_generator("txt_sentoken")
classifier = NaiveBayesClassifier()
classifier.train(generator)

print classifier.classify("This is awesome but still I don't like it thisisaweirdwordneveroccurs. ".split(" "))
print classifier.classify("iqbvajkkjbarjta".split(" "))
print classifier.classify("".split(" "))