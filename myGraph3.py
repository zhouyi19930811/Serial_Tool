import sys,codecs,os

from PyQt5.QtWidgets import  QApplication, QWidget,QFontDialog

##from PyQt5.QtWidgets import  

from PyQt5.QtCore import  Qt

##from PyQt5.QtGui import QStandardItemModel

from ui_QGraph3 import Ui_QGraph3

class QGraph3(QWidget, Ui_QGraph3):

   def __init__(self, parent=None):
      super(QGraph3, self).__init__(parent)
      self.setupUi(self) 
      self.setWindowTitle('车速绘图栏')
      self.setAttribute(Qt.WA_DeleteOnClose) #MDI子窗口会被自动删除

   def __del__(self):   ##析构函数
      print("QGraph3 对象被删除了")

##  ==============自定义功能函数============


        
##  ==========由connectSlotsByName() 自动连接的槽函数==================        
        
    
##  =============自定义槽函数===============================        
        
   
##  ============窗体测试程序 ================================
if  __name__ == "__main__":
   app = QApplication(sys.argv)
   form=QGraph3()
   form.show()
   sys.exit(app.exec_())
