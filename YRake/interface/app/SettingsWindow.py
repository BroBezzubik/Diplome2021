from PyQt5 import QtCore, QtGui, QtWidgets

from interface.ui import SettingsWindow

from methods.settings import YAKE_SETTINGS, YAKEMODIFIED_SETTINGS

class SettingsWindow(QtWidgets.QWidget, SettingsWindow.Ui_Settings):
    def __init__(self):
        super(SettingsWindow, self).__init__()

        # Устанавливаем UI
        self.setupUi(self)

    def get_settings(self):
        return {
            'yake': self.get_yake_settings(),
            'yakemodified': self.get_yakemodified_settings(),
            'rake': self.get_rake_settings(),
            'textrank': self.get_textrank_settings()
        }

    def get_yake_settings(self):
        return {
            'lan': self.lang.currentText(),
            'dedupLim': self.yake_dedup_lim.value(),
            'dedupFunc': self.yake_dedup_func.currentText(),
            'n': 1,
            'windowsSize': self.yake_window_size.value(),
            'top': self.yake_top.value()
        }

    def get_yakemodified_settings(self):
        return {
            'lan': self.lang.currentText(),
            'dedupLim': self.yakemodified_dedup_lim.value(),
            'dedupFunc': self.yakemodified_dedup_func.currentText(),
            'n': self.yakemodified_ngram_size.value(),
            'windowsSize': self.yakemodified_window_size.value(),
            'top': self.yakemodified_top.value()
        }

    def get_rake_settings(self):
        return {
            'max_length': self.rake_max_n.value(),
            'min_length': self.rake_min_n.value(),
            'top': self.rake_top.value()
        }

    def get_textrank_settings(self):
        return {
            'window': self.textrank_window_size.value(),
            'top': self.textrank_window_size.value(),
            'language': self.lang.currentText()
        }

    def accept(self):
        self.close()

    def reject(self):
        self.close()
