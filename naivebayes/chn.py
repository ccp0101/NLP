#coding=utf8
import sys
from sentiments import PolarizedSentimentAnalyzer

analyzer = PolarizedSentimentAnalyzer("/Library/Python/2.7/site-packages/pymmseg_cpp-1.0.0-py2.7-macosx-10.7-intel.egg/mmseg/data/chars.dic", 
                                      "/Users/ccp/Dropbox/src/nlp/naivebayes/hownet/hownet_only.words.chn.dic")
analyzer.load_lexicons([("pos", u"hownet/pos_sentiments_chn.txt"), 
                        ("pos", u"hownet/pos_judgements_chn.txt"),
                        ("neg", u"hownet/neg_sentiments_chn.txt"), 
                        ("neg", u"hownet/neg_judgements_chn.txt"),])

import pymongo
conn = pymongo.Connection()
db = conn.eastmoney

for row in db.page_extracted.find():
    article = row["article"]
    title = row["title"]
    segmented,score = analyzer.segment_and_score(article)
    if score < 80:
        print u"[%d] %s" % (score, title)
