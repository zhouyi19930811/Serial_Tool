# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QGraph3.Ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QGraph3(object):
    def setupUi(self, QGraph3):
        QGraph3.setObjectName("QGraph3")
        QGraph3.resize(348, 288)
        QGraph3.setMinimumSize(QtCore.QSize(330, 270))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/images/18.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QGraph3.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(QGraph3)
        self.gridLayout.setObjectName("gridLayout")
        self.Pyqtgraph_3 = GraphicsLayoutWidget(QGraph3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pyqtgraph_3.sizePolicy().hasHeightForWidth())
        self.Pyqtgraph_3.setSizePolicy(sizePolicy)
        self.Pyqtgraph_3.setMinimumSize(QtCore.QSize(330, 270))
        self.Pyqtgraph_3.setObjectName("Pyqtgraph_3")
        self.gridLayout.addWidget(self.Pyqtgraph_3, 0, 0, 1, 1)

        self.retranslateUi(QGraph3)
        QtCore.QMetaObject.connectSlotsByName(QGraph3)

    def retranslateUi(self, QGraph3):
        _translate = QtCore.QCoreApplication.translate
        QGraph3.setWindowTitle(_translate("QGraph3", "Form"))

from pyqtgraph import GraphicsLayoutWidget
import apprcc_rc
