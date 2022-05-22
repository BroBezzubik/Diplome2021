from pke.unsupervised import TextRank

class TextRank(TextRank):
    def __init__(self, top=20, language="ru", window=3):
        super(TextRank, self).__init__()

        self.language = language
        self.top = top
        self.window = window

    def extract_keywords(self, text):
        self.load_document(text, language=self.language)
        self.candidate_selection()
        self.candidate_weighting(window=self.window)
        result = self.get_n_best(n=self.top)
        return result

