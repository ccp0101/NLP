import tornado.ioloop
import tornado.web
import pickle
import json
import math
from segmentor import Segmentor

with open("simple_classifier.pickle") as f:
    print "Loading classifier..."
    classifier = pickle.load(f)
    print "Finished loading classifier. "

segmentor = Segmentor()

class SimpleSentimentAnalysis(tornado.web.RequestHandler):
    def post(self):
        self.process()
    def get(self):
        self.process()
    def process(self):
        data = self.get_argument("data")
        segmented = segmentor(data)
        candidates = classifier.score(segmented)
        best = max(candidates)
        result = {'class':best[1], 'score' : {}, 'data' : data}
        result['tokens'] = segmented
        for x in candidates:
            result['score'][x[1]] = x[0]
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(result, indent=4))
        self.finish()

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/sentiment/analyze/simple", SimpleSentimentAnalysis),
    ])
    application.listen(8888, '127.0.0.1')
    tornado.ioloop.IOLoop.instance().start()