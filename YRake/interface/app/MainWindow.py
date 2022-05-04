import sys
from PyQt6 import QtWidgets

from interface.ui import MainWindow

from .ResultWindow import ResultWindow

import textract
from methods.yake import Yake
from methods.yake import YakeModified

class MainWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # TODO Переписать на добавление методов по имени с помощью sys
        self.methods = {
            'yake': Yake(),
            'yakemodified': YakeModified(),
            # 'rakeyake': None,
        }

        self.active_methods = {
            'yake': False,
            'rake': False,
            'rakeyake': False
        }

        # Установка связей
        self.SelectFileButton.clicked.connect(self.browse_files)
        self.ExtractButton.clicked.connect(self.run)

        # Дополнительные внутрнение переменые
        self.file = None

    def browse_files(self):
        pass

    def run(self):
        text = self.TextEdit.toPlainText()

        print(text)
        if self.file:
            text = textract.process(self.file)

        result = {}
        for key, method in self.methods.items():
            result[key] = method.extract_keywords(text)

        result_widget = ResultWindow(self, result)
        result_widget.show()

        print(result)


