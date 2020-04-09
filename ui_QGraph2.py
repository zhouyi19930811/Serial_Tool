# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QGraph2.Ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QGraph2(object):
    def setupUi(self, QGraph2):
        QGraph2.setObjectName("QGraph2")
        QGraph2.resize(348, 288)
        QGraph2.setMinimumSize(QtCore.QSize(330, 270))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/images/18.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QGraph2.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(QGraph2)
        self.gridLayout.setObjectName("gridLayout")
        self.Pyqtgraph_2 = GraphicsLayoutWidget(QGraph2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pyqtgraph_2.sizePolicy().hasHeightForWidth())
        self.Pyqtgraph_2.setSizePolicy(sizePolicy)
        self.Pyqtgraph_2.setMinimumSize(QtCore.QSize(330, 270))
        self.Pyqtgraph_2.setObjectName("Pyqtgraph_2")
        self.gridLayout.addWidget(self.Pyqtgraph_2, 0, 0, 1, 1)

        self.retranslateUi(QGraph2)
        QtCore.QMetaObject.connectSlotsByName(QGraph2)

    def retranslateUi(self, QGraph2):
        _translate = QtCore.QCoreApplication.translate
        QGraph2.setWindowTitle(_translate("QGraph2", "Form"))

from pyqtgraph import GraphicsLayoutWidget
import apprcc_rc
