import yake


class Yake(yake.KeywordExtractor):
    def __init__(self, *args, **kwargs):
        super(Yake, self).__init__(args, kwargs)
