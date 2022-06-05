import sys
from PyQt5 import QtWidgets

from interface.ui import MainWindow
from interface.app.SettingsWindow import SettingsWindow

import textract
from methods.yake import Yake
from methods.yake import YakeModified
from methods.rake import Rake
from methods.textrank import TextRank

from prettytable import PrettyTable

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
        self.files = []

        self.methods_checkbox = {
            'yake': self.yake_checkbox,
            'yakemodified': self.yakemodified_checkbox,
            'rake': self.rake_checkbox,
            'textrank': self.textrank_checkbox,
        }
        self.methods = {
            'yake': Yake,
            'yakemodified': YakeModified,
            'rake': Rake,
            'textrank': TextRank
        }

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

    def simpl_result(self, result):
        for key, method_data in result.items():
            print(f"Метод: {key}")
            if key == "rake":
                result_text = ', '.join([str(info[1]) for info in method_data])
            else:
                result_text = ', '.join([str(info[0]) for info in method_data])
            print(result_text)
            print("\n")


    def browse_files(self):
        files = QtWidgets.QFileDialog.getOpenFileNames(self, 'Select files', directory='/www/')[0]
        if len(files) > 1:
            self.file_name_label.setText(f'Выбрано {len(files)}')
        else:
            self.file_name_label.setText(files[0].rsplit('/', 1)[1])
        self.files = files

    

    def get_text(self):
        text = self.TextEdit.toPlainText()
        if text:
            yield text, "Результат из поля ввода"
        for file in self.files:
            yield textract.process(file).decode('utf-8'), file.rsplit('/', 1)[1]

    def show_settings(self):
        self.settings_window.show()

    def run(self):
        settings = self.get_settings()
        methods = self.get_methods()
        methods = self.setup_methods(methods, settings)
        for text, filename in self.get_text():
            result = self.extract_keywords(text, methods)
            print(f"Документ работы: {filename}")
            self.simpl_result(result)
            print("\n\n")


    # Для одиночных запусков
    # def run(self):
    #     text = self.get_text()
    #     settings = self.get_settings()
    #     methods = self.get_methods()
    #     methods = self.setup_methods(methods, settings)
    #     result = self.extract_keywords(text, methods)
    #     self.display_result(result)

    # def get_text(self):
    #     text = self.TextEdit.toPlainText()
    #     if self.file:
    #         text = textract.process(self.file)
    #         # Добавлена заглушка что бы постоянно не генерировать и не вставлять текст
    #         return text.decode('utf-8')
    #     return text
    # def browse_files(self):
    #     file_path = QtWidgets.QFileDialog.getOpenFileName(self, directory='/home/bezzubik/Projects/Diplome2021/YRake/Literature')[0]
    #     self.file_name_label.setText(file_path.rsplit('/', 1)[1])
    #     self.file = file_path