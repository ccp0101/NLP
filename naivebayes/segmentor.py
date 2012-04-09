import re
import mmseg

class Segmentor:
    def __init__(self):
        mmseg.dict_load_defaults()
    def __call__(self, text, must_chinese=True):
        algor = mmseg.Algorithm(text)
        words = [unicode(x.text) for x in algor]
        if must_chinese:
            words = filter(lambda x: re.match(u'^[\u4e00-\u9fa5]+$', x), words)
        return words