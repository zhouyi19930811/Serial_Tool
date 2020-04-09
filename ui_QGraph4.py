# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QGraph4.Ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QGraph4(object):
    def setupUi(self, QGraph4):
        QGraph4.setObjectName("QGraph4")
        QGraph4.resize(348, 288)
        QGraph4.setMinimumSize(QtCore.QSize(330, 270))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/images/19.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QGraph4.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(QGraph4)
        self.gridLayout.setObjectName("gridLayout")
        self.Pyqtgraph_4 = GraphicsLayoutWidget(QGraph4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pyqtgraph_4.sizePolicy().hasHeightForWidth())
        self.Pyqtgraph_4.setSizePolicy(sizePolicy)
        self.Pyqtgraph_4.setMinimumSize(QtCore.QSize(330, 270))
        self.Pyqtgraph_4.setObjectName("Pyqtgraph_4")
        self.gridLayout.addWidget(self.Pyqtgraph_4, 0, 0, 1, 1)

        self.retranslateUi(QGraph4)
        QtCore.QMetaObject.connectSlotsByName(QGraph4)

    def retranslateUi(self, QGraph4):
        _translate = QtCore.QCoreApplication.translate
        QGraph4.setWindowTitle(_translate("QGraph4", "Form"))

from pyqtgraph import GraphicsLayoutWidget
import apprcc_rc
