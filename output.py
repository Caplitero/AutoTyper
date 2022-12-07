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


import threading
from PySide6.QtWidgets import  QStatusBar, QMenuBar, QTextEdit, QScrollArea, QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide6.QtCore import QObject, QMetaObject,QCoreApplication,  QRunnable, Slot, QThreadPool, QRect, QThread
from PySide6.QtGui import QFont
import pyautogui
import re
import ctypes
      

class Ui_MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.thread_manager = QThreadPool()
        self.setupUi()
        
    def setupUi(self):
        
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget  = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.exit = QPushButton(self.centralwidget)
        self.exit.setGeometry(QRect(500, 380, 200, 100))
        font = QFont()
        font.setPointSize(20)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QRect(50, 20, 680, 281))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 678, 279))
        self.textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QRect(0, 40, 681, 241))
        self.textEdit.setObjectName("textEdit")
        self.scrollArea.setWidget (self.scrollAreaWidgetContents)
        self.StartButt = QPushButton(self.centralwidget)
        self.StartButt.setGeometry(QRect(70, 380, 191, 101))
        font = QFont()
        font.setPointSize(20)
        self.StartButt.setFont(font)
        self.StartButt.setObjectName("StartButt")
        self.StopButt = QPushButton(self.centralwidget)
        self.StopButt.setGeometry(QRect(290, 380, 181, 101))
        self.StopButt.setDisabled(True)
        font = QFont()
        font.setPointSize(20)
        self.StopButt.setFont(font)
        self.StopButt.setObjectName("StopButt")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
       
        self.retranslateUi(self)
        self.StartButt.clicked.connect(self.Start_Writing)
        self.StopButt.clicked.connect(self.Stop_Writing)
        self.exit.clicked.connect(self.close) # type: ignore
        self.threadpool = QThreadPool()
        QMetaObject.connectSlotsByName(self)
     
    
    def retranslateUi(self,MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.StartButt.setText(_translate("MainWindow", "Start"))
        self.StopButt.setText(_translate("MainWindow", "Stop"))
    
    def Start_Writing(self ):
        Text = MainWindow.textEdit.toPlainText()
        Text = re.sub(r"\t","",Text)
        
        self.StartButt.setDisabled(True)
        self.StopButt.setDisabled(False)
        self.newthread = CAP_Thread(Text, 2, self)
        self.newthread.start()
        
        
    
    def Stop_Writing(self):
        self.StartButt.setDisabled(False)
        self.StopButt.setDisabled(True)
        self.newthread.raise_exception()
        print("Stopped")
        
class CAP_Thread(threading.Thread):
    def __init__(self, Data : str , Delay: int , Window : Ui_MainWindow ):
        threading.Thread.__init__(self)
        self.data = Data
        self.delay = Delay
        self.MyWindow= Window   
             
    def run(self):
      print("Thread starting")
      print("Delay : ",self.delay,"s",sep = "")    
      pyautogui.sleep(self.delay)
      pyautogui.write(self.data ,0.025)
      print("Thread done")
      self.MyWindow.StartButt.setDisabled(False)
      self.MyWindow.StopButt.setDisabled(True)
          
    def get_id(self):
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
  
    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
              ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
  
          


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec())


