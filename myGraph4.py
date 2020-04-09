import sys,codecs,os

from PyQt5.QtWidgets import  QApplication, QWidget,QFontDialog

##from PyQt5.QtWidgets import  

from PyQt5.QtCore import  Qt

##from PyQt5.QtGui import QStandardItemModel

from ui_QGraph4 import Ui_QGraph4

class QGraph4(QWidget, Ui_QGraph4):

   def __init__(self, parent=None):
      super(QGraph4, self).__init__(parent)
      self.setupUi(self) 
      self.setWindowTitle('高度绘图栏')
      self.setAttribute(Qt.WA_DeleteOnClose) #MDI子窗口会被自动删除

   def __del__(self):   ##析构函数
      print("QGraph4 对象被删除了")

##  ==============自定义功能函数============


        
##  ==========由connectSlotsByName() 自动连接的槽函数==================        
        
    
##  =============自定义槽函数===============================        
        
   
##  ============窗体测试程序 ================================
if  __name__ == "__main__":
   app = QApplication(sys.argv)
   form=QGraph4()
   form.show()
   sys.exit(app.exec_())
