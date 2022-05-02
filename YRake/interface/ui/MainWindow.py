# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(962, 628)
        self.CentralWidget = QtWidgets.QWidget(MainWindow)
        self.CentralWidget.setObjectName("CentralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.CentralWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.MethodsBox = QtWidgets.QGroupBox(self.CentralWidget)
        self.MethodsBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MethodsBox.sizePolicy().hasHeightForWidth())
        self.MethodsBox.setSizePolicy(sizePolicy)
        self.MethodsBox.setMaximumSize(QtCore.QSize(800, 800))
        self.MethodsBox.setObjectName("MethodsBox")
        self.gridLayout = QtWidgets.QGridLayout(self.MethodsBox)
        self.gridLayout.setContentsMargins(9, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.YakeMethod = QtWidgets.QCheckBox(self.MethodsBox)
        self.YakeMethod.setObjectName("YakeMethod")
        self.gridLayout.addWidget(self.YakeMethod, 0, 0, 1, 1)
        self.RakeYakeMethod = QtWidgets.QCheckBox(self.MethodsBox)
        self.RakeYakeMethod.setObjectName("RakeYakeMethod")
        self.gridLayout.addWidget(self.RakeYakeMethod, 2, 0, 1, 1)
        self.RakeMethod = QtWidgets.QCheckBox(self.MethodsBox)
        self.RakeMethod.setObjectName("RakeMethod")
        self.gridLayout.addWidget(self.RakeMethod, 1, 0, 1, 1)
        self.KeaMethod = QtWidgets.QCheckBox(self.MethodsBox)
        self.KeaMethod.setObjectName("KeaMethod")
        self.gridLayout.addWidget(self.KeaMethod, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.MethodsBox, 1, 0, 1, 1)
        self.FileBox = QtWidgets.QGroupBox(self.CentralWidget)
        self.FileBox.setObjectName("FileBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.FileBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FileName = QtWidgets.QLabel(self.FileBox)
        self.FileName.setObjectName("FileName")
        self.horizontalLayout.addWidget(self.FileName)
        self.SelectFileButton = QtWidgets.QPushButton(self.FileBox)
        self.SelectFileButton.setObjectName("SelectFileButton")
        self.horizontalLayout.addWidget(self.SelectFileButton)
        self.gridLayout_2.addWidget(self.FileBox, 1, 1, 1, 1)
        self.ExtractButton = QtWidgets.QPushButton(self.CentralWidget)
        self.ExtractButton.setObjectName("ExtractButton")
        self.gridLayout_2.addWidget(self.ExtractButton, 2, 0, 1, 2)
        self.TextEdit = QtWidgets.QTextEdit(self.CentralWidget)
        self.TextEdit.setObjectName("TextEdit")
        self.gridLayout_2.addWidget(self.TextEdit, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.CentralWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 962, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MethodsBox.setTitle(_translate("MainWindow", "Методы извлечения ключевых слов"))
        self.YakeMethod.setText(_translate("MainWindow", "Yake"))
        self.RakeYakeMethod.setText(_translate("MainWindow", "Yake + Rake"))
        self.RakeMethod.setText(_translate("MainWindow", "Rake"))
        self.KeaMethod.setText(_translate("MainWindow", "Kea"))
        self.FileBox.setTitle(_translate("MainWindow", "Выбор файла"))
        self.FileName.setText(_translate("MainWindow", "Имя файла"))
        self.SelectFileButton.setText(_translate("MainWindow", "Выбрать файл"))
        self.ExtractButton.setText(_translate("MainWindow", "Извлечь"))