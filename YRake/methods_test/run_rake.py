from methods.rake import Rake
from RAKE.RAKE import Rake
from constants import DEFAULT_TEXT

from prettytable import PrettyTable

stopwords_file = '/home/bezzubik/Projects/Diplome2021/YRake/methods/yake/StopwordsList/stopwords_ru.txt'
stopwords = open(stopwords_file, 'r', encoding='utf8').read().split('\n')
rake = Rake(stop_words=stopwords)
result = dict(rake.run(text=DEFAULT_TEXT, minFrequency=3))


prettyTable = PrettyTable(field_names=('words', 'coefficent'))
for w, c in result.items():
    prettyTable.add_row((w, c))

print(prettyTable)