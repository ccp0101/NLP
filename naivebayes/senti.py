#coding=utf8
from naivebayes import NaiveBayesClassifier
import os
import re
import codecs
from segmentor import Segmentor

def corpus_generator(segmentor):
    for corpus in map(lambda x: "sentiment_corpus/" + x, ["Ctrip_htl_ba_4000", "Dangdang_Book_4000", "Jingdong_NB_4000"]):
        classes = filter(lambda x: x[0] != ".", os.listdir(corpus))
        for cls in classes:
            print "Enumerating for '%s/%s' reviews." % (corpus, cls)
            cls_dir = os.path.join(corpus, cls)
            files = filter(lambda x: x.endswith(".txt"), os.listdir(cls_dir))
            for filename in files:
                with codecs.open(os.path.join(cls_dir, filename), "r", encoding="utf8") as file:
                    for line in file:
                        if not line.strip():
                            continue
                        words = segmentor(line.strip())
                        yield (cls, words)

segmentor = Segmentor()
generator = corpus_generator(segmentor)
classifier = NaiveBayesClassifier()
classifier.train(generator)

print classifier.classify(segmentor(u"这一地区生鲜奶收购价持续在低位徘徊，导致很多奶户入不敷出，被迫“砍牛”（杀牛或卖牛）。 近期，双鸭山市多地奶农联名向记者反映"))

# print classifier.classify("This is awesome but still I don't like it thisisaweirdwordneveroccurs. ".split(" "))
# print classifier.classify("iqbvajkkjbarjta".split(" "))
# print classifier.classify("I don't recommend.".split(" "))