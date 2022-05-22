import sys

from PyQt5 import QtWidgets

from interface.app.MainWindow import MainWindow



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
