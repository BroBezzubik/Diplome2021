from rake_nltk import Rake


class Rake(Rake):
    def __init__(self, stopwords=None, top=20, **kwargs):
        if stopwords is None:
            stopwords = "/home/nbarsukov/projects/Diplome2021/YRake/methods/yake/StopwordsList/stopwords_ru.txt"
            with open(stopwords, 'r', encoding='utf8') as f:
                text = f.read()
                stopwords = text.split('\n')
        super(Rake, self).__init__(stopwords=stopwords, **kwargs)

        self.top = top

    def extract_keywords(self, text):
        self.extract_keywords_from_text(text)
        result = self.get_ranked_phrases_with_scores()
        if len(result) > self.top:
            result = result[:self.top]
        return result
