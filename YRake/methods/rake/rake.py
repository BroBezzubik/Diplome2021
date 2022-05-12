import RAKE
import io

class Rake(RAKE.Rake):
    def __init__(self, stopwords=None):
        if stopwords is None:
            stopwords = "/home/bezzubik/Projects/Diplome2021/YRake/methods/yake/StopwordsList/stopwords_ru.txt"
            with open(stopwords, 'r', encoding='utf8') as f:
                text = f.read()
                stopwords = text.split('\n')
        super(Rake, self).__init__(stop_words=stopwords)

    def extract_keywords(self, text):
        settings = {
            "minFrequency": 0.5,
            "maxWords": 5
        }
        return self.run(text, **settings)
