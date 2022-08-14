#MIT License

#Copyright (c) 2022 Caplitero

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import asyncio
from asyncore import loop
from time import sleep
from PySide6 import QtCore, QtGui, QtWidgets
import pyautogui
import re

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.thread_manager = \
            QtCore.QThreadPool()
        self.setupUi()
        
    
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget =QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.exit =QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(500, 380, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(50, 20, 680, 281))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 678, 279))
        self.scrollAreaWidgetContentssetObjectName("scrollAreaWidgetContents")
        self.textEdit = QtWidgets. QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(0, 40, 681, 241))
        self.textEdit.setObjectName("textEdit")
        self.scrollArea.setWidget (self.scrollAreaWidgetContents)
        self.StartButt = QtWidgets.QPushButton(self.centralwidget)
        self.StartButt.setGeometry(QtCore.QRect(70, 380, 191, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.StartButt.setFont(font)
        self.StartButt.setObjectName("StartButt")
        self.StopButt = QtWidgets.QPushButton(self.centralwidget)
        self.StopButt.setGeometry(QtCore.QRect(290, 380, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.StopButt.setFont(font)
        self.StopButt.setObjectName("StopButt")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        
        self.retranslateUi(self)
        self.StartButt.clicked.connect(Start)
        self.exit.clicked.connect(self.close) # type: ignore
        
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.StartButt.setText(_translate("MainWindow", "Start"))
        self.StopButt.setText(_translate("MainWindow", "Stop"))


def Write(ToWrite:str):
     pyautogui.write(ToWrite,0.025)

def Start():
    Text = MainWindow.textEdit.toPlainText()
    Text = re.sub(r"\t","",Text)
    sleep(2)
    MainWindow.thread_manager.start(Write(Text),1)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec())

