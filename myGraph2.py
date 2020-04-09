import sys,codecs,os

from PyQt5.QtWidgets import  QApplication, QWidget,QFontDialog

##from PyQt5.QtWidgets import  

from PyQt5.QtCore import  Qt

##from PyQt5.QtGui import QStandardItemModel

from ui_QGraph2 import Ui_QGraph2

class QGraph2(QWidget, Ui_QGraph2):

   def __init__(self, parent=None):
      super(QGraph2, self).__init__(parent)
      self.setupUi(self) 
      self.setWindowTitle('姿态角绘图栏')
      self.setAttribute(Qt.WA_DeleteOnClose) #MDI子窗口会被自动删除
      
      self.Pyqtgraph_2.clear() # 清空里面的内容，否则会发生重复绘图的结果
      self.plot_angle = self.Pyqtgraph_2.addPlot()  # 把图p加入到窗口中
      self.plot_angle.showGrid(x=True, y=True, alpha=0.3)  # 把X和Y的网格打开
      #self.plot_angle.setRange(xRange=[0, self.heading_length], padding=0)
      self.plot_angle.setLabel(axis='left',text='y/heading')  # 靠左
      self.plot_angle.setLabel(axis='bottom',text='x/point')
      self.plot_angle.setTitle('姿态角信息')  # 表格的名字
      self.draw_angle = self.plot_angle.plot()  # 绘制一个图形,,,测试多线程绘图

   def __del__(self):   ##析构函数
      print("QGraph2 对象被删除了")

##  ==============自定义功能函数============


        
##  ==========由connectSlotsByName() 自动连接的槽函数==================        
        
    
##  =============自定义槽函数===============================        
        
   
##  ============窗体测试程序 ================================
if  __name__ == "__main__":
   app = QApplication(sys.argv)
   form=QGraph2()
   form.show()
   sys.exit(app.exec_())
