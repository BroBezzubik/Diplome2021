from keybert import KeyBERT


class Bert(KeyBERT):

    def __init__(self, min_n=1, max_n=3, top=20, **kwargs):
        super(Bert, self).__init__()
        self.min_n = min_n
        self.max_n = max_n
        self.top = top


    def extract_keywords(self, text):
        result = super(Bert, self).extract_keywords(text, top_n=self.top, keyphrase_ngram_range=(self.min_n, self.max_n))
        return result
