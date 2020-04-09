import sys,codecs,os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import  QApplication, QWidget,QFontDialog

##from PyQt5.QtWidgets import  

from PyQt5.QtCore import  Qt

##from PyQt5.QtGui import QStandardItemModel

from ui_QdataForm import Ui_QdataForm

class QdataForm(QWidget, Ui_QdataForm):

   def __init__(self, parent=None):
       
      super(QdataForm, self).__init__(parent)
      self.setupUi(self) 
      self.setWindowTitle('数据收发栏')
      self.setAttribute(Qt.WA_DeleteOnClose) #MDI子窗口会被自动删除
      self.data1=0

   def __del__(self):   ##析构函数
      print("QdataForm 对象被删除了")
      self.data1=1

##  ==============自定义功能函数============


        
##  ==========由connectSlotsByName() 自动连接的槽函数==================        
        
    
##  =============自定义槽函数===============================        
        
   
##  ============窗体测试程序 ================================
if  __name__ == "__main__":
   app = QApplication(sys.argv)
   form=QdataForm()
   form.show()
   sys.exit(app.exec_())
