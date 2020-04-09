import sys,codecs,os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import  QApplication, QWidget,QFontDialog

##from PyQt5.QtWidgets import  

from PyQt5.QtCore import  Qt

##from PyQt5.QtGui import QStandardItemModel

from ui_QGraph1 import Ui_QGraph1

import pyqtgraph as pg

class QGraph1(QWidget, Ui_QGraph1):

   def __init__(self, parent=None):
      super(QGraph1, self).__init__(parent)
      self.setupUi(self) 
      self.setWindowTitle('经纬度绘图栏')
      self.setAttribute(Qt.WA_DeleteOnClose) #MDI子窗口会被自动删除

   def __del__(self):   ##析构函数
      print("QGraph1 对象被删除了")
      

##  ==============自定义功能函数============


        
##  ==========由connectSlotsByName() 自动连接的槽函数==================        
        
    
##  =============自定义槽函数===============================        
        
   
##  ============窗体测试程序 ================================
if  __name__ == "__main__":
   app = QApplication(sys.argv)
   form=QGraph1()
   form.show()
   sys.exit(app.exec_())
