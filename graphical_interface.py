# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphic.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1179, 729)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setGeometry(QtCore.QRect(0, 0, 1171, 731))
        self.tab_widget.setObjectName("tab_widget")
        self.help_tab = QtWidgets.QWidget()
        self.help_tab.setObjectName("help_tab")
        self.help_text = QtWidgets.QTextBrowser(self.help_tab)
        self.help_text.setGeometry(QtCore.QRect(0, 0, 1171, 681))
        self.help_text.setObjectName("help_text")
        self.tab_widget.addTab(self.help_tab, "")
        self.code_tab = QtWidgets.QWidget()
        self.code_tab.setObjectName("code_tab")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.code_tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 1171, 521))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.run_button = QtWidgets.QPushButton(self.code_tab)
        self.run_button.setGeometry(QtCore.QRect(20, 600, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.run_button.setFont(font)
        self.run_button.setAutoRepeatInterval(100)
        self.run_button.setObjectName("run_button")
        self.eax_value = QtWidgets.QTextBrowser(self.code_tab)
        self.eax_value.setGeometry(QtCore.QRect(310, 540, 121, 31))
        self.eax_value.setDocumentTitle("")
        self.eax_value.setObjectName("eax_value")
        self.carry_flag_value = QtWidgets.QTextBrowser(self.code_tab)
        self.carry_flag_value.setGeometry(QtCore.QRect(310, 610, 101, 31))
        self.carry_flag_value.setObjectName("carry_flag_value")
        self.ebx_vlue = QtWidgets.QTextBrowser(self.code_tab)
        self.ebx_vlue.setGeometry(QtCore.QRect(520, 540, 121, 31))
        self.ebx_vlue.setObjectName("ebx_vlue")
        self.zero_flag_value = QtWidgets.QTextBrowser(self.code_tab)
        self.zero_flag_value.setGeometry(QtCore.QRect(550, 610, 101, 31))
        self.zero_flag_value.setObjectName("zero_flag_value")
        self.ecx_value = QtWidgets.QTextBrowser(self.code_tab)
        self.ecx_value.setGeometry(QtCore.QRect(720, 540, 121, 31))
        self.ecx_value.setObjectName("ecx_value")
        self.negative_flag_value = QtWidgets.QTextBrowser(self.code_tab)
        self.negative_flag_value.setGeometry(QtCore.QRect(790, 610, 101, 31))
        self.negative_flag_value.setObjectName("negative_flag_value")
        self.overflow_flag_value = QtWidgets.QTextBrowser(self.code_tab)
        self.overflow_flag_value.setGeometry(QtCore.QRect(1030, 610, 101, 31))
        self.overflow_flag_value.setObjectName("overflow_flag_value")
        self.edx_value = QtWidgets.QTextBrowser(self.code_tab)
        self.edx_value.setGeometry(QtCore.QRect(930, 540, 121, 31))
        self.edx_value.setObjectName("edx_value")
        self.eax_label = QtWidgets.QLabel(self.code_tab)
        self.eax_label.setGeometry(QtCore.QRect(260, 550, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.eax_label.setFont(font)
        self.eax_label.setAlignment(QtCore.Qt.AlignCenter)
        self.eax_label.setObjectName("eax_label")
        self.ebx_label = QtWidgets.QLabel(self.code_tab)
        self.ebx_label.setGeometry(QtCore.QRect(470, 550, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ebx_label.setFont(font)
        self.ebx_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ebx_label.setObjectName("ebx_label")
        self.ecx_label = QtWidgets.QLabel(self.code_tab)
        self.ecx_label.setGeometry(QtCore.QRect(670, 550, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ecx_label.setFont(font)
        self.ecx_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ecx_label.setObjectName("ecx_label")
        self.edx_label = QtWidgets.QLabel(self.code_tab)
        self.edx_label.setGeometry(QtCore.QRect(880, 550, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edx_label.setFont(font)
        self.edx_label.setAlignment(QtCore.Qt.AlignCenter)
        self.edx_label.setObjectName("edx_label")
        self.carry_flag_label = QtWidgets.QLabel(self.code_tab)
        self.carry_flag_label.setGeometry(QtCore.QRect(220, 610, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.carry_flag_label.setFont(font)
        self.carry_flag_label.setAlignment(QtCore.Qt.AlignCenter)
        self.carry_flag_label.setObjectName("carry_flag_label")
        self.overflow_flag_label = QtWidgets.QLabel(self.code_tab)
        self.overflow_flag_label.setGeometry(QtCore.QRect(440, 610, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.overflow_flag_label.setFont(font)
        self.overflow_flag_label.setAlignment(QtCore.Qt.AlignCenter)
        self.overflow_flag_label.setObjectName("overflow_flag_label")
        self.negative_flag_label = QtWidgets.QLabel(self.code_tab)
        self.negative_flag_label.setGeometry(QtCore.QRect(680, 610, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.negative_flag_label.setFont(font)
        self.negative_flag_label.setAlignment(QtCore.Qt.AlignCenter)
        self.negative_flag_label.setObjectName("negative_flag_label")
        self.overflow_flag_label_2 = QtWidgets.QLabel(self.code_tab)
        self.overflow_flag_label_2.setGeometry(QtCore.QRect(920, 610, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.overflow_flag_label_2.setFont(font)
        self.overflow_flag_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.overflow_flag_label_2.setObjectName("overflow_flag_label_2")
        self.read_from_file_button = QtWidgets.QPushButton(self.code_tab)
        self.read_from_file_button.setGeometry(QtCore.QRect(20, 540, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.read_from_file_button.setFont(font)
        self.read_from_file_button.setAutoRepeatInterval(100)
        self.read_from_file_button.setObjectName("read_from_file_button")

        self.read_from_file_button.clicked.connect(self.read_from_file)

        self.tab_widget.addTab(self.code_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.help_text.setPlaceholderText(_translate("MainWindow", "write code !"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.help_tab), _translate("MainWindow", "Help"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "your code ..."))
        self.run_button.setText(_translate("MainWindow", "Run"))
        self.eax_label.setText(_translate("MainWindow", "eax"))
        self.ebx_label.setText(_translate("MainWindow", "ebx"))
        self.ecx_label.setText(_translate("MainWindow", "ecx"))
        self.edx_label.setText(_translate("MainWindow", "edx"))
        self.carry_flag_label.setText(_translate("MainWindow", "Carry Flag"))
        self.overflow_flag_label.setText(_translate("MainWindow", "Overflow Flag"))
        self.negative_flag_label.setText(_translate("MainWindow", "Negative Flag"))
        self.overflow_flag_label_2.setText(_translate("MainWindow", "Overflow Flag"))
        self.read_from_file_button.setText(_translate("MainWindow", "Read from .txt"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.code_tab), _translate("MainWindow", "Code"))

    # my codes :

    def read_from_file(self):
        app.processEvents()
        file_dir = QFileDialog.getOpenFileName(filter="Text files (*.txt)", directory=os.getcwd())[0]
        with open(file_dir, "r") as file:
            extracted_code = file.read()
        self.plainTextEdit.setPlainText(extracted_code)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())