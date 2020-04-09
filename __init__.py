import sys, os
import serial
import math
import array
import serial.tools.list_ports
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Ui_uu import Ui_MainWindow
from mydataForm import QdataForm
from mydisplay import Qdisplay
from myGraph1 import QGraph1
from myGraph2 import QGraph2
from myGraph3 import QGraph3
from myGraph4 import QGraph4
from datetime import datetime
import pyqtgraph as pg
import numpy as np
import re

class Pyqt5_Serial(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Pyqt5_Serial, self).__init__()
        pg.setConfigOption('background', '#ffffff')  # 设置背景为白色
        pg.setConfigOption('foreground', 'k')  # 设置前景（包括坐标轴，线条，文本等等）为黑色。
        pg.setConfigOptions(antialias=True) # 使曲线看起来更光滑，而不是锯齿状
        
        self.setupUi(self) 
       
        #数据收发子窗口显示
        self.uidata = QdataForm(self)
        self.mdiArea.addSubWindow(self.uidata)   #文档窗口添加到MDI
        self.uidata.show()    #在单独的窗口中显示
        self.uidata.resize(750, 250)
        
        #实时信息子窗口显示
        self.display = Qdisplay(self)
        self.mdiArea.addSubWindow(self.display)   #文档窗口添加到MDI
        self.display.show()    #在单独的窗口中显示
        
        #绘图1子窗口显示
        self.graph1 = QGraph1(self)
        self.mdiArea.addSubWindow(self.graph1)   #文档窗口添加到MDI
        self.graph1.show()    #在单独的窗口中显示
        
        #绘图2子窗口显示
        self.graph2 = QGraph2(self)
        self.mdiArea.addSubWindow(self.graph2)   #文档窗口添加到MDI
        self.graph2.show()    #在单独的窗口中显示
        
        #绘图3子窗口显示
        self.graph3 = QGraph3(self)
        self.mdiArea.addSubWindow(self.graph3)   #文档窗口添加到MDI
        self.graph3.show()    #在单独的窗口中显示
        
        #绘图4子窗口显示
        self.graph4 = QGraph4(self)
        self.mdiArea.addSubWindow(self.graph4)   #文档窗口添加到MDI
        self.graph4.show()    #在单独的窗口中显示
        
        self.init()
        self.setWindowTitle("Saic Position Manager")
        self.ser = serial.Serial()
        self.port_check()

        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.Receive_LineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.Send_LineEdit.setText(str(self.data_num_sended))
        #暂停按钮、记录数据按钮标志位
        self.suspend_flag=0
        self.log_flag=0        
        #定义记录数据的存储文件名为空
        self.txtname = ''

        #定义开始绘图按钮标志位
        self.draw_flag=0
        
        #定义经纬度绘图参数初始值
        #self.j_step=0 
        self.pos_time_flag=0
        self.lat_list = array.array('d')
        self.lon_list = array.array('d')
        
        #定义姿态角绘图参数初始值
        self.i_step= 0
        self.heading_length = 100  # 姿态角绘图坐标容纳数据长度
        self.angle_heading_list=array.array('d')
        self.angle_time_list=array.array('d') 
        
        #定义车速绘图参数初始值
        self.n_step=0
        self.car_time_flag=0
        self.speed_length = 100  # 车速绘图坐标容纳数据长度
        self.speed_list=array.array('d') 
        self.speed_time_list=array.array('d') 
        
        #定义高度绘图参数初始值
        self.m_step= 0
        self.rtk_time_flag=0
        #self.altitudetest=""
        self.altitude_length = 100  # 高度绘图坐标容纳数据长度
        self.altitude_list=array.array('d') 
        self.altitude_time_list=array.array('d') 
        
        #经纬度绘图坐标设置
        self.graph1.Pyqtgraph_1.clear() # 清空里面的内容，否则会发生重复绘图的结果
        self.plot_position = self.graph1.Pyqtgraph_1.addPlot()  # 把图p加入到窗口中
        self.plot_position.showGrid(x=True, y=True, alpha=0.3)  # 把X和Y的网格打开
        #self.plot_position.setRange(xRange=[0, 10], padding=0)
        self.plot_position.setLabel(axis='left',text='Latitude(degree)')  # y轴  靠左
        self.plot_position.setLabel(axis='bottom',text='Longitude(degree)') # x轴
        self.plot_position.setTitle('经纬度信息')  # 表格的名字
        self.draw_position = self.plot_position.plot()  # 绘制一个图形
        #self.plot_position.plot(self.lon_list, self.lat_list, pen=pg.mkPen(color='r', width=1.5))
        self.vLine = pg.InfiniteLine(angle=90, movable=False,pen=pg.mkPen(color='g', width=1.5))#添加十字光标
        self.hLine = pg.InfiniteLine(angle=0, movable=False,pen=pg.mkPen(color='g', width=1.5))#添加十字光标
        
        #航向角绘图坐标设置
        self.graph2.Pyqtgraph_2.clear() # 清空里面的内容，否则会发生重复绘图的结果
        self.plot_angle = self.graph2.Pyqtgraph_2.addPlot()  # 把图p加入到窗口中
        self.plot_angle.showGrid(x=True, y=True, alpha=0.3)  # 把X和Y的网格打开
        #self.plot_angle.setRange(xRange=[0, 50], padding=0)
        self.plot_angle.setLabel(axis='left',text='Heading(degree)')  # y轴  靠左
        self.plot_angle.setLabel(axis='bottom',text='Time(s)')    # x轴
        self.plot_angle.setTitle('姿态角信息')  # 表格的名字
        self.draw_angle = self.plot_angle.plot()  # 绘制一个图形
        
        #车速绘图坐标设置
        self.graph3.Pyqtgraph_3.clear() # 清空里面的内容，否则会发生重复绘图的结果
        self.plot_speed = self.graph3.Pyqtgraph_3.addPlot()  # 把图p加入到窗口中
        self.plot_speed.showGrid(x=True, y=True, alpha=0.3)  # 把X和Y的网格打开
        #self.plot_speed.setRange(xRange=[0, 50], padding=0)
        self.plot_speed.setLabel(axis='left',text='Speed(m/s)')  # y轴  靠左
        self.plot_speed.setLabel(axis='bottom',text='Time(s)')  # x轴
        self.plot_speed.setTitle('车速信息')  # 表格的名字
        self.draw_speed = self.plot_speed.plot()  # 绘制一个图形
        
        #高度绘图坐标设置
        self.graph4.Pyqtgraph_4.clear() # 清空里面的内容，否则会发生重复绘图的结果
        self.plot_altitude = self.graph4.Pyqtgraph_4.addPlot()  # 把图p加入到窗口中
        self.plot_altitude.showGrid(x=True, y=True, alpha=0.3)  # 把X和Y的网格打开
        #self.plot_altitude.setRange(xRange=[0, 20], padding=0)
        self.plot_altitude.setLabel(axis='left',text='Altitude(m)')  # 靠左
        self.plot_altitude.setLabel(axis='bottom',text='Time(s)')   # x轴
        self.plot_altitude.setTitle('高度信息')  # 表格的名字
        self.draw_altitude = self.plot_altitude.plot()  # 绘制一个图形
        

        
    def init(self):
        # 串口信息检查
        self.Check_Button.clicked.connect(self.port_check)

        # 串口信息显示
        self.Choice_ComboBox.currentTextChanged.connect(self.port_imf)

        # 打开串口按钮
        self.Open_Button.clicked.connect(self.port_open)

        # 关闭串口按钮
        self.Close_Button.clicked.connect(self.port_close)
    
        # 开始绘图按钮
        self.Start_Plot_Button.clicked.connect(self.plot_start)
        
        # 停止绘图按钮
        self.Stop_Plot_Button.clicked.connect(self.plot_stop)

        # 发送数据按钮
        self.uidata.Choice_SendData_Button.clicked.connect(self.data_send)

        # 定时器发送数据
        self.timer_send = QTimer(self)
        self.timer_send.timeout.connect(self.data_send)
        self.uidata.Interval_Time_CheckBox.stateChanged.connect(self.data_send_timer)

        # 定时器接收数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.data_receive)
        
        # 绘图计时器
        self.timer_count = QTimer(self)
        self.timer_count.timeout.connect(self.count_time)
        
        # 定时器按行读取文件
#        self.timer_read_data = QTimer(self)
#        self.timer_read_data.timeout.connect(self.readline_data)
#
#
        # 清除发送窗口
        self.uidata.Clear_SendData_Button.clicked.connect(self.send_data_clear)
#
        # 清除接收窗口
        self.uidata.Clear_ReceiveData_Button.clicked.connect(self.receive_data_clear)
        
        # 点击按钮，开始发送虚拟数据
        #self.uidata.FalseData_Send_Button.clicked.connect(self.false_data_send)
        
        # 点击按钮，停止发送虚拟数据
        #self.uidata.FalseData_Stop_Button.clicked.connect(self.false_data_stop)
        
        # 导入杆臂向量数值
        self.Setting_Button.clicked.connect(self.setting_ganbi)
        
    # 串口检测
    def port_check(self):
        # 检测所有存在的串口，将信息存储在字典中
        self.Com_Dict = {}
        port_list = list(serial.tools.list_ports.comports())
        self.Choice_ComboBox.clear()
        for port in port_list:
            self.Com_Dict["%s" % port[0]] = "%s" % port[1]
            self.Choice_ComboBox.addItem(port[0])
        if len(self.Com_Dict) == 0:
            self.State_Label.setText(" 无串口")

    # 串口信息
    def port_imf(self):
        # 显示选定的串口的详细信息
        imf_s = self.Choice_ComboBox.currentText()
        if imf_s != "":
            self.State_Label.setText(self.Com_Dict[self.Choice_ComboBox.currentText()])

    # 打开串口
    def port_open(self):
        self.ser.port = self.Choice_ComboBox.currentText()
        self.ser.baudrate = int(self.Baudrate_ComboBox.currentText())
        self.ser.bytesize = int(self.Bytesize_ComboBox.currentText())
        self.ser.stopbits = int(self.Stopbits_ComboBox.currentText())
        self.ser.parity = self.Parity_ComboBox.currentText()
        try:
            self.ser.open()
        except:
            QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
            return None

        # 打开串口接收定时器，采样间隔周期为2ms
        self.timer.start(2)

        if self.ser.isOpen():
            self.Open_Button.setEnabled(False)
            self.Close_Button.setEnabled(True)
            self.actionStart.setEnabled(False)
            self.actionStop.setEnabled(True)
            self.Serial_GroupBox.setTitle("串口状态（已开启）")

            
    # 关闭串口
    def port_close(self):
        self.timer.stop()
        self.timer_send.stop()
        
        try:
            self.ser.close()
        except:
            pass
        self.Open_Button.setEnabled(True)
        self.Close_Button.setEnabled(False)
        self.actionStart.setEnabled(True)
        self.actionStop.setEnabled(False)
        self.uidata.Interval_Time_LineEdit.setEnabled(True)
        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.Receive_LineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.Send_LineEdit.setText(str(self.data_num_sended))
        self.Serial_GroupBox.setTitle("串口状态（已关闭）")

    # 发送数据
    def data_send(self):
        if self.ser.isOpen():
            input_s = self.uidata.Send_Data_Text.toPlainText()
            if input_s != "":
                # 非空字符串
                # ascii发送
                #input_s = (input_s).encode('utf-8')
                input_s = (input_s + '\r\n').encode('utf-8')
                num = self.ser.write(input_s)
                self.data_num_sended += num
                self.Send_LineEdit.setText(str(self.data_num_sended))
        else:
            pass
            
    # 导入杆臂向量数值
    def setting_ganbi(self):
        try:
            lever_arm=str(self.X_LineEdit.text())+","+str(self.Y_LineEdit.text())+","+str(self.Z_LineEdit.text())+","
            if lever_arm != "":
                # 非空字符串
                # ascii发送
                lever_arm = (lever_arm + '\r\n').encode('utf-8')
                num = self.ser.write(lever_arm)
                self.data_num_sended += num
                self.Send_LineEdit.setText(str(self.data_num_sended))
        except:
            QMessageBox.critical(self, "Port Error", "请先打开串口，再导入杆臂向量数值！")
            return None

    # 接收数据
    def data_receive(self):
        try:
            num = self.ser.inWaiting()
        except:
            self.port_close()
            return None
        if(num > 0):
            data = self.ser.read(num)#self.ser.read(num)
            # 串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去
            list_1=data.decode('utf-8')#编码方式utf-8，iso-8859-1
            self.uidata.Receive_Data_Text.insertPlainText(list_1)
            #print("list_1=", list_1)
            if(self.log_flag==1):
                with open(self.txtname, 'a+',encoding="utf-8") as data_write:
                    data_write.writelines(list_1)
            
            # 提取g报文数据并显示
            try:
                found1 = re.search('g(.+?)\r\n', list_1).group(1)
            except AttributeError:
                found1 = '' # 如果报错则赋值为空
            found1="g" + found1
            header_row1=found1.split(',')# 将字符串转化为list
            first_data= header_row1[0]# 取第一个值
            if(first_data=='g' ):#Imudata&&Pos_fusion，19/16位数据,and len(header_row1)==16
                try:
                    lat=header_row1[14]
                    lon=header_row1[15]
                    east=header_row1[10]
                    north=header_row1[11]
                    utc_time=header_row1[13]
                    heading=header_row1[12]
                    stamp_time=header_row1[1]
                    #heading=(float(heading)+math.pi)/(math.pi)*180
                    #heading=float('%.5f' % heading)
                    heading=float(heading)
                    self.display.Latitude_Text.setText(lat)
                    self.display.Longitude_Text.setText(lon)
                    self.display.East_Text.setText(east)
                    self.display.North_Text.setText(north)
                    self.display.UTC_Text.setText(utc_time)
                    self.display.Heading_Text.setText(str(heading)+"°")
                    lat=float(lat)
                    lon=float(lon)
                    stamp_time=float(stamp_time)
                    if(self.draw_flag==1):
                        if(self.pos_time_flag!=stamp_time):#用时间戳判断
                            self.pos_time_flag=stamp_time
                            self.lat_list.append(lat)
                            self.lon_list.append(lon)
                            self.draw_position.setData(self.lon_list,self.lat_list, pen=pg.mkPen(color='r', width=1.5))# 经纬度绘图
                            self.vLine.setPos(self.lon_list[-1])#添加十字光标
                            self.hLine.setPos(self.lat_list[-1])#添加十字光标
                            # 首先判断航向角坐标长度，如果在长度之内则不断添加；如果超出长度，则按位移动，先进先出。
                            if self.i_step < self.heading_length:
                                self.angle_heading_list.append(heading)
                                self.angle_time_list.append(self.count_time_show)#此处self.count_time_show由计时器累加
                            else:
                                self.angle_heading_list[:-1] = self.angle_heading_list[1:]# 按位移动，先进先出
                                self.angle_heading_list[-1] = heading
                                self.angle_time_list[:-1] = self.angle_time_list[1:]# 按位移动，先进先出
                                self.angle_time_list[-1] = self.count_time_show
                            self.i_step = self.i_step + 1 # 步长累加
                            #print("self.angle_timelist", self.angle_timelist)
                            self.draw_angle.setData(self.angle_time_list, self.angle_heading_list, pen=pg.mkPen(color='r', width=1.5))# 航向角绘图
                except:
                    pass

            # 提取a报文数据并显示
            try:
                found2 = re.search('a(.+?)\r\n', list_1).group(1)
            except AttributeError:
                found2 = '' # 如果报错则赋值为空
            found2="a" + found2
            header_row2=found2.split(',')# 此处list备用
            
            # 提取s报文数据并显示
            try:
                found3 = re.search('s(.+?)\r\n', list_1).group(1)
            except AttributeError:
                found3 = '' # 如果报错则赋值为空
            found3="s" + found3
            header_row3=found3.split(',')
            first_data= header_row3[0]
            if(first_data=='s'):#Car,and len(header_row3)==8
                try:
                    car_left_non=float(header_row3[2])
                    car_right_non=float(header_row3[3])
                    car_time=float(header_row3[1])
                    car_speed=0.5*(car_left_non+car_right_non)/3.6*1.014
                    car_speed=float('%.5f' % car_speed)
                    #print(math.pi)
                    self.display.Speed_Text.setText(str(car_speed)+"m/s")
                    speed=car_speed
                    #print("car_time=", car_time)
                    if(self.draw_flag==1):
                        if(self.car_time_flag!=car_time):#用时间戳判断
                            self.car_time_flag=car_time
                            # 首先判断速度坐标长度，如果在长度之内则不断添加；如果超出长度，则按位移动，先进先出。
                            if self.n_step < self.speed_length:
                                self.speed_list.append(speed)
                                self.speed_time_list.append(self.count_time_show)
                            else:
                                self.speed_list[:-1] = self.speed_list[1:]
                                self.speed_list[-1] = speed
                                self.speed_time_list[:-1] = self.speed_time_list[1:]
                                self.speed_time_list[-1] = self.count_time_show
                            self.n_step = self.n_step + 1 # 步长累加
                            #print("self.speedlist=", self.speedlist)
                            self.draw_speed.setData(self.speed_time_list, self.speed_list, pen=pg.mkPen(color='b', width=1.5)) # 速度绘图
                except:
                    pass
            
            # 提取r报文数据并显示
            try:
                found4 = re.search('r(.+?)\r\n', list_1).group(1)
            except AttributeError:
                found4 = '' # 如果报错则赋值为空
            found4="r" + found4
            header_row4=found4.split(',')
            first_data= header_row4[0]
            if(first_data=='r'):#RTK,and len(header_row4)==14
                try:
                    altitude=header_row4[4]
                    #print(self.altitude)
                    rtk_state=header_row4[7]
                    rtk_heading_flag=header_row4[9]
                    rtk_time=header_row4[1]
                    self.display.Altitude_Text.setText(altitude+"m")
                    self.display.RTK_State_Text.setText(rtk_state)
                    self.display.RTK_Heading_Flag_Text.setText(rtk_heading_flag)
                    altitude=float(altitude)
                    rtk_time=float(rtk_time)
                    if(self.draw_flag==1):
                        if(self.rtk_time_flag!=rtk_time):#用时间戳判断
                            self.rtk_time_flag=rtk_time
                            # 首先判断高度坐标长度，如果在长度之内则不断添加；如果超出长度，则按位移动，先进先出。
                            if self.m_step < self.altitude_length:
                                self.altitude_list.append(altitude)
                                self.altitude_time_list.append(self.count_time_show)
                            else:
                                self.altitude_list[:-1] = self.altitude_list[1:]
                                self.altitude_list[-1] = altitude
                                self.altitude_time_list[:-1] = self.altitude_time_list[1:]
                                self.altitude_time_list[-1] = self.count_time_show
                            self.m_step = self.m_step + 1 # 步长累加
                            self.draw_altitude.setData(self.altitude_time_list, self.altitude_list, pen=pg.mkPen(color='b', width=1.5))# 高度绘图
                except:
                    pass
            
            
            # 统计接收字符的数量
            self.data_num_received += num
            self.Receive_LineEdit.setText(str(self.data_num_received))

            # 获取到text光标
            textCursor = self.uidata.Receive_Data_Text.textCursor()
            # 滚动到底部
            textCursor.movePosition(textCursor.End)
            # 设置光标到text中去
            self.uidata.Receive_Data_Text.setTextCursor(textCursor)
        else:
            pass
            
    # 定时发送数据
    def data_send_timer(self):
        if self.uidata.Interval_Time_CheckBox.isChecked():
            self.timer_send.start(int(self.Interval_Time_LineEdit.text()))
            self.uidata.Interval_Time_LineEdit.setEnabled(False)
        else:
            self.timer_send.stop()
            self.uidata.Interval_Time_LineEdit.setEnabled(True)

    # 清除发送的数据显示
    def send_data_clear(self):
        self.uidata.Send_Data_Text.setText("")

    # 清除接收的数据显示
    def receive_data_clear(self):
        self.uidata.Receive_Data_Text.setText("")
        
#  ==============自定义功能函数========================#

    def __openByIODevice(self,fileName):  # 用QFile打开文件         
        fileDevice=QFile(fileName)
        if not fileDevice.exists():  #判断文件是否存在
            return False

        if not fileDevice.open(QIODevice.ReadOnly | QIODevice.Text):
            return False

        try:
            self.uidata.Receive_Data_Text.clear()
            while not fileDevice.atEnd():
                qtBytes = fileDevice.readAll()  # 返回QByteArray类型
                pyBytes=bytes(qtBytes.data())    # QByteArray转换为bytes类型
                lineStr=pyBytes.decode("utf-8")  #bytes转换为str型
                lineStr=lineStr.strip()          #去除结尾增加的空行
                self.uidata.Receive_Data_Text.insertPlainText(lineStr)
        finally:
            fileDevice.close()
        return True
       
    def __saveByIODevice(self,fileName):  # 用QFile保存文件
        fileDevice=QFile(fileName)
        if not fileDevice.open(QIODevice.WriteOnly | QIODevice.Text):
            return False
        try:
            text=self.uidata.Receive_Data_Text.toPlainText()  #返回str类型
            strBytes=text.encode("utf-8")        # str转换为bytes类型
            fileDevice.write(strBytes)           #写入文件
        finally:
            fileDevice.close()
        return  True

#  ==========由connectSlotsByName()自动连接的槽函数============
    @pyqtSlot()   #用QFile 打开文件
    def on_actionOpen_File_triggered(self):
        curPath=QDir.currentPath()    #获取系统当前目录
        title="打开一个文件"    #对话框标题
        #filt="程序文件(*.h *.cpp *.py);;文本文件(*.txt);;所有文件(*.*)"   #文件过滤器
        filt="所有文件(*.*)"   #文件过滤器
        fileName,flt=QFileDialog.getOpenFileName(self,title,curPath,filt)
        if (fileName == ""):
            return

        if self.__openByIODevice(fileName):
            self.statusBar.showMessage(fileName)
        else:
            QMessageBox.critical(self,"错误","打开文件失败")
            
    @pyqtSlot()   #用QFile 另存文件
    def on_actionSave_triggered(self):
        curPath=QDir.currentPath()    #获取系统当前目录
        title="另存为一个文件"        #对话框标题
        filt="所有文件(*.*)"  #文件过滤器
        fileName,flt=QFileDialog.getSaveFileName(self,title,curPath,filt)
        if (fileName==""):
            return
        if self.__saveByIODevice(fileName):
            self.statusBar.showMessage(fileName)
        else:
            QMessageBox.critical(self,"错误","保存文件失败")
        
    @pyqtSlot()   #用actionSuspend暂停数据接收
    def on_actionSuspend_triggered(self):
        if(self.suspend_flag==0):
            self.timer.stop()
            self.suspend_flag=1
        elif(self.suspend_flag==1):
            self.timer.start(2)
            self.suspend_flag=0
            
    @pyqtSlot()   # 清除接收的数据显示
    def on_actionClear_triggered(self):
        self.uidata.Receive_Data_Text.setText("")
        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.Receive_LineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.Send_LineEdit.setText(str(self.data_num_sended))
        # 实时显示信息清除
        self.display.Latitude_Text.setText("")
        self.display.Longitude_Text.setText("")
        self.display.East_Text.setText("")
        self.display.North_Text.setText("")
        self.display.UTC_Text.setText("")
        self.display.Heading_Text.setText(" "+"°")
        self.display.Speed_Text.setText(str(" "+"m/s"))
        self.display.Altitude_Text.setText(str(" "+"m"))
        self.display.RTK_State_Text.setText("")
        self.display.RTK_Heading_Flag_Text.setText("")
        #绘图数据清除
        self.lat_list = array.array('d')
        self.lon_list = array.array('d')
        self.angle_heading_list=array.array('d')
        self.angle_time_list=array.array('d') 
        self.speed_list=array.array('d') 
        self.speed_time_list=array.array('d') 
        self.altitude_list=array.array('d') 
        self.altitude_time_list=array.array('d') 

    @pyqtSlot()   #用actionLog存储数据
    def on_actionLog_triggered(self):
        try:
            if(self.log_flag==0):
                self.txtname = datetime.now().strftime("%Y%m%d_%H%M%S") #获取当前时间
                self.log_flag=1 
                self.statusBar.showMessage("开始记录数据！")
            elif(self.log_flag==1):
                self.log_flag=0
                self.statusBar.showMessage(self.txtname+"文件保存成功！")
        except:
            QMessageBox.critical(self, "Port Error", "请先打开串口，再记录数据！")
            return None
            
    @pyqtSlot()   #用actionTile使子窗口平铺
    def on_actionTile_triggered(self):
        self.mdiArea.tileSubWindows()
        
    @pyqtSlot()   #用actionCascade使子窗口折叠
    def on_actionCascade_triggered(self):
        self.mdiArea.cascadeSubWindows()
    
    @pyqtSlot()   #用actionData_Show_View使子窗口显示
    def on_actionData_Show_View_triggered(self):
        if (self.uidata.data1==1):
            self.uidata = QdataForm(self)
            self.mdiArea.addSubWindow(self.uidata)   #文档窗口添加到MDI
            self.uidata.show()    #在单独的窗口中显示
        
    @pyqtSlot()   #用actionReal_Time_Information使子窗口显示
    def on_actionReal_Time_Information_triggered(self):
        self.display.show()
     
    #绘图计时器
    def count_time(self):
        self.count_time_show += 0.02
            
    #开始绘制
    def plot_start(self):
        self.Start_Plot_Button.setEnabled(False)
        self.plot_position.addItem(self.vLine, ignoreBounds=True)
        self.plot_position.addItem(self.hLine, ignoreBounds=True)
        
        self.i_step= 0
        #self.j_step= 0
        self.n_step= 0
        self.m_step= 0
        self.lat_list = array.array('d')
        self.lon_list = array.array('d')
        self.angle_heading_list=array.array('d')
        self.angle_time_list=array.array('d') 
        self.speed_list=array.array('d') 
        self.speed_time_list=array.array('d') 
        self.altitude_list=array.array('d') 
        self.altitude_time_list=array.array('d') 
        try:
            if(self.draw_flag==0):
                self.draw_flag=1 
                self.statusBar.showMessage("开始绘图！")
        except:
            return None
        self.count_time_show=0 # 计时器归零
        self.timer_count.start(20) # 计时器开始计时，间隔20ms

    def plot_stop(self):
        try:
            if(self.draw_flag==1):
                self.draw_flag=0 
                self.statusBar.showMessage("停止绘图！")
        except:
            return None
        self.Start_Plot_Button.setEnabled(True)
        self.timer_count.stop() # 计时器停止

#    #开始模拟数据发送，按行读取txt文件数据，采样间隔周期为2ms    
#    def false_data_send(self):
#        self.falsedata_txt = "20191030_141707.txt" #获取文件名称
#        self.fileDevice=QFile(self.falsedata_txt)
#        if not self.fileDevice.open(QIODevice.ReadOnly | QIODevice.Text):
#            return False
#        self.uidata.Send_Data_Text.clear()
#        self.timer_read_data.start(2)
#       
#    # 停止模拟数据发送
#    def false_data_stop(self):
#        self.timer_read_data.stop()
#    
#    # 按行读取数据并写入串口
#    def readline_data(self):
#        try:
#            if not self.fileDevice.atEnd():
#                qtBytes = self.fileDevice.readLine()  # 返回QByteArray类型
#                pyBytes=bytes(qtBytes.data())    # QByteArray转换为bytes类型
#                lineStr=pyBytes.decode("utf-8")  #bytes转换为str型
#                lineStr=lineStr.strip()          #去除结尾增加的空行
#                #print("lineStr=", lineStr)
#                self.uidata.Send_Data_Text.insertPlainText(lineStr+"\n")
#                lineStr = (lineStr + '\r\n').encode('utf-8')
#                num = self.ser.write(lineStr)
#                self.data_num_sended += num
#                self.Send_LineEdit.setText(str(self.data_num_sended))
#                # 获取到text光标
#                textCursor = self.uidata.Send_Data_Text.textCursor()
#                # 滚动到底部
#                textCursor.movePosition(textCursor.End)
#                # 设置光标到text中去
#                self.uidata.Send_Data_Text.setTextCursor(textCursor)
#            else:
#                self.fileDevice.close()
#        except:
#            self.port_close()
#            self.timer_read_data.stop()
#            return None

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = Pyqt5_Serial()
    myshow.show()
    sys.exit(app.exec_())
