from PyQt6 import QtCore, QtGui, QtWidgets

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
        }

    def get_yake_settings(self):
        return {
            'lan': self.lang.currentText(),
            'dedupLim': self.yake_dedup_lim.value(),
            'dedupFunc': self.yake_dedup_func.currentText(),
            'n': self.yake_ngram_size.value(),
            'windowsSize': self.yake_window_size.value(),
        }

    def get_yakemodified_settings(self):
        return {
            'lan': self.lang.currentText(),
            'dedupLim': self.yakemodified_dedup_lim.value(),
            'dedupFunc': self.yakemodified_dedup_func.currentText(),
            'n': self.yakemodified_ngram_size.value(),
            'windowsSize': self.yakemodified_window_size.value()
        }


    def accept(self):
        self.close()

    def reject(self):
        self.close()