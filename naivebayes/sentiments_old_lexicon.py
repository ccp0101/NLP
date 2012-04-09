
import codecs
import re
import mmseg
import tempfile

class PolarizedSentimentAnalyzer:
    def __init__(self):
        self.lexicons = {}
        self.regexes = {}

    def load_lexicons(self, lexicon_files, weight=1.0):
        # lexicons = [(stm, filepath)]
        files = lexicon_files if isinstance(lexicon_files, list) else [lexicon_files, ]
        for stm, filepath in files:
            assert stm in ["pos", "neg"]
            with codecs.open(filepath, "r", encoding="utf8") as f:
                sign = -1 if stm == "neg" else 1
                for line in f:
                    line = unicode(line.strip())
                    if re.match(u'^[\u4e00-\u9fa5]+$', line):
                        self.lexicons[line] = sign * weight
                    elif re.match(r'^\w+$', line):
                        self.lexicons[line] = sign * weight

    def add_regex(self, regex, weight):
        self.regexes[regex] = weight

    def segment(self, text):
        algor = mmseg.Algorithm(text)
        return [x.text for x in algor]

    def finalize_segmentor(self, tmp_dir=None):
        # Creates a segmentor with loaded lexicons as dictionary
        tmp_path = tempfile.mktemp(dir=tmp_dir, text=True, suffix=".dic")

        mmseg.Dictionary.dictionaries = (
            ("chars", "chars.dic"), 
            ("words", "")
        )

    def segment_and_score(self, sentence):
        segmented = self.segment(sentence)
        lexicon_score = 0
        for word in segmented:
            score += self.lexicons.get(word, 0)

        return segmented, score
