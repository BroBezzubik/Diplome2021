import sys
from PyQt6 import QtWidgets

from interface.ui import MainWindow
from interface.app.SettingsWindow import SettingsWindow

import textract
from methods.yake import Yake
from methods.yake import YakeModified
from methods.rake import Rake

from prettytable import PrettyTable

from constants import LITERATURE_DIRECTORY_PATH

class MainWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Устанавливаем внутренний интерфейс
        self.setupUi(self)

        # Установка дополнительных окон
        self.settings_window = SettingsWindow()

        # Установка связей
        self.select_file_button.clicked.connect(self.browse_files)
        self.ExtractButton.clicked.connect(self.run)

        # Дополнительные внутрнение переменые
        self.file = None
        self.methods_checkbox = {
            'yake': self.yake_checkbox,
            'yakemodified': self.yakemodified_checkbox,
        }
        self.methods = {
            'yake': Yake,
            'yakemodified': YakeModified,
        }

    def get_text(self):
        text = self.TextEdit.toPlainText()
        if self.file:
            text = textract.process(self.file)
            # Добавлена заглушка что бы постоянно не генерировать и не вставлять текст
            return text.decode('utf-8')

    def get_settings(self):
        return self.settings_window.get_settings()

    def get_methods(self):
        return {key: self.methods[key] for key, value in self.methods_checkbox.items() if value.isChecked()}

    def setup_methods(self, methods_class, settings):
        methods = {}
        for key, method_class in methods_class.items():
            methods[key] = method_class(**settings[key])
        return methods

    def extract_keywords(self, text, methods):
        result = {}
        for method_name, method in methods.items():
            result[method_name] = method.extract_keywords(text)
        return result

    def display_result(self, result):
        for key, method_data in result.items():
            table = PrettyTable(field_names=['keyword', 'score'])
            for result in method_data:
                table.add_row(result)

            print(table)

    def browse_files(self):
        file_path = QtWidgets.QFileDialog.getOpenFileName(self, directory='/home/bezzubik/Projects/Diplome2021/YRake/Literature')[0]
        self.file_name_label.setText(file_path.rsplit('/', 1)[1])
        self.file = file_path

    def show_settings(self):
        self.settings_window.show()

    def run(self):
        text = self.get_text()
        settings = self.get_settings()
        methods = self.get_methods()
        methods = self.setup_methods(methods, settings)
        result = self.extract_keywords(text, methods)
        self.display_result(result)



