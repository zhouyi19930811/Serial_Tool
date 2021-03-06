# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QdataForm.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QdataForm(object):
    def setupUi(self, QdataForm):
        QdataForm.setObjectName("QdataForm")
        QdataForm.setWindowModality(QtCore.Qt.WindowModal)
        QdataForm.resize(1100, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QdataForm.sizePolicy().hasHeightForWidth())
        QdataForm.setSizePolicy(sizePolicy)
        QdataForm.setMinimumSize(QtCore.QSize(1100, 1000))
        QdataForm.setMaximumSize(QtCore.QSize(1100, 1500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/images/14.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QdataForm.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(QdataForm)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 420, 793, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Interval_Time_CheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.Interval_Time_CheckBox.setObjectName("Interval_Time_CheckBox")
        self.horizontalLayout_6.addWidget(self.Interval_Time_CheckBox)
        spacerItem = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.Interval_Time_LineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(10)
        self.Interval_Time_LineEdit.setFont(font)
        self.Interval_Time_LineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Interval_Time_LineEdit.setObjectName("Interval_Time_LineEdit")
        self.horizontalLayout_6.addWidget(self.Interval_Time_LineEdit)
        self.Dw = QtWidgets.QLabel(self.layoutWidget)
        self.Dw.setObjectName("Dw")
        self.horizontalLayout_6.addWidget(self.Dw)
        spacerItem1 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 1)
        self.horizontalLayout_6.setStretch(3, 1)
        self.horizontalLayout_6.setStretch(6, 1)
        self.layoutWidget1 = QtWidgets.QWidget(QdataForm)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 10, 921, 271))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Receive_Data_Text = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.Receive_Data_Text.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.Receive_Data_Text.setObjectName("Receive_Data_Text")
        self.horizontalLayout.addWidget(self.Receive_Data_Text)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Receive_CheckBox_ = QtWidgets.QCheckBox(self.layoutWidget1)
        self.Receive_CheckBox_.setObjectName("Receive_CheckBox_")
        self.verticalLayout_2.addWidget(self.Receive_CheckBox_)
        self.Clear_ReceiveData_Button = QtWidgets.QPushButton(self.layoutWidget1)
        self.Clear_ReceiveData_Button.setObjectName("Clear_ReceiveData_Button")
        self.verticalLayout_2.addWidget(self.Clear_ReceiveData_Button)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.layoutWidget2 = QtWidgets.QWidget(QdataForm)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 300, 921, 111))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Send_Data_Text = QtWidgets.QTextEdit(self.layoutWidget2)
        self.Send_Data_Text.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.Send_Data_Text.setObjectName("Send_Data_Text")
        self.horizontalLayout_2.addWidget(self.Send_Data_Text)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Send_CheckBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.Send_CheckBox.setObjectName("Send_CheckBox")
        self.verticalLayout.addWidget(self.Send_CheckBox)
        self.Choice_SendData_Button = QtWidgets.QPushButton(self.layoutWidget2)
        self.Choice_SendData_Button.setObjectName("Choice_SendData_Button")
        self.verticalLayout.addWidget(self.Choice_SendData_Button)
        self.Clear_SendData_Button = QtWidgets.QPushButton(self.layoutWidget2)
        self.Clear_SendData_Button.setObjectName("Clear_SendData_Button")
        self.verticalLayout.addWidget(self.Clear_SendData_Button)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(QdataForm)
        QtCore.QMetaObject.connectSlotsByName(QdataForm)

    def retranslateUi(self, QdataForm):
        _translate = QtCore.QCoreApplication.translate
        QdataForm.setWindowTitle(_translate("QdataForm", "Form"))
        self.Interval_Time_CheckBox.setText(_translate("QdataForm", "定时发送"))
        self.Interval_Time_LineEdit.setText(_translate("QdataForm", "1000"))
        self.Dw.setText(_translate("QdataForm", "ms/次"))
        self.Receive_CheckBox_.setText(_translate("QdataForm", "Hex"))
        self.Clear_ReceiveData_Button.setText(_translate("QdataForm", "清除"))
        self.Send_Data_Text.setHtml(_translate("QdataForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">123456</span></p></body></html>"))
        self.Send_CheckBox.setText(_translate("QdataForm", "Hex"))
        self.Choice_SendData_Button.setText(_translate("QdataForm", "发送"))
        self.Clear_SendData_Button.setText(_translate("QdataForm", "清除"))

import apprcc_rc
