from PyQt6 import QtCore, QtGui, QtWidgets

class ResultWindow(QtWidgets.QWidget):
    def __init__(self, parent, results):
        super(ResultWindow, self).__init__(parent=parent)

        self.label = QtWidgets.QLabel("Hello world", parent=self)