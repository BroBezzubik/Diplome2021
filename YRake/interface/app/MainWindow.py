import sys
from PyQt6 import QtWidgets

from interface.ui import MainWindow

from .ResultWindow import ResultWindow

import textract
from methods.yake import Yake
from methods.yake import YakeModified
from methods.rake import Rake

from prettytable import PrettyTable


class MainWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Устанавливаем внутренний интерфейс
        self.setupUi(self)

        # Установка связей
        self.SelectFileButton.clicked.connect(self.browse_files)
        self.ExtractButton.clicked.connect(self.run)

        # Дополнительные внутрнение переменые
        self.file = None

    def get_text(self):
        test = self.TextEdit.toPlainText()
        if self.file:
            text = textract.process(self.file)
            # Добавлена заглушка что бы постоянно не генерировать и не вставлять текст
            text = textract.process(
                '/home/bezzubik/Projects/Diplome2021/YRake/Literature/3420-7350-1-SM.pdf',
            )
            return text.decode('utf-8')

    def get_settings(self):
        pass

    def get_methods(self):
        pass

    def extract_keywords(self, methods, settings):
        pass



    def browse_files(self):
        pass

    def run(self):
        text = self.get_text()
        settings = self.get_settings()
        result = self.extract_keywords()
        # text = self.TextEdit.toPlainText()
        #
        # if self.file:
        #     text = textract.process(self.file)
        #
        # text = textract.process(
        #     '/home/bezzubik/Projects/Diplome2021/YRake/Literature/3420-7350-1-SM.pdf',
        # )
        #
        # text = text.decode('utf-8')
        #
        # result = {}
        # for key, method in self.methods.items():
        #     result[key] = method.extract_keywords(text)
        #
        # for key, method_data in result.items():
        #     table = PrettyTable()
        #     for result in method_data:
        #         table.add_row(result)
        #
        #     print(table)


