import sys
from PyQt6 import QtWidgets

from interface.ui import MainWindow

import textract
from methods import Yake

class MainWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Получения списка всех
        # TODO Переписать на автообновление чекбоксов с помощь чтения dir()
        self.methods_checkbox_list = [
            self.YakeMethod,
            self.RakeMethod,
            self.RakeYakeMethod,
            self.KeaMethod,
        ]

        # TODO Переписать на добавление методов по имени с помощью sys
        self.methods = {
            'yake': Yake,
            'rake': None,
            'rakeyake': None,
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
        if file:
            text = textract.process(self.file)

        result = {}
        for checkbox in self.methods_checkbox_list:
            if checkbox.isChecked():
                method = self.methods[checkbox.text().lower()]
                result[]method.extract_keywords(text)

