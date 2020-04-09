# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QGraph1.Ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QGraph1(object):
    def setupUi(self, QGraph1):
        QGraph1.setObjectName("QGraph1")
        QGraph1.resize(348, 319)
        QGraph1.setMinimumSize(QtCore.QSize(330, 270))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/images/16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QGraph1.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(QGraph1)
        self.gridLayout.setObjectName("gridLayout")
        self.Pyqtgraph_1 = GraphicsLayoutWidget(QGraph1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pyqtgraph_1.sizePolicy().hasHeightForWidth())
        self.Pyqtgraph_1.setSizePolicy(sizePolicy)
        self.Pyqtgraph_1.setMinimumSize(QtCore.QSize(330, 270))
        self.Pyqtgraph_1.setObjectName("Pyqtgraph_1")
        self.gridLayout.addWidget(self.Pyqtgraph_1, 0, 0, 1, 1)

        self.retranslateUi(QGraph1)
        QtCore.QMetaObject.connectSlotsByName(QGraph1)

    def retranslateUi(self, QGraph1):
        _translate = QtCore.QCoreApplication.translate
        QGraph1.setWindowTitle(_translate("QGraph1", "Form"))

from pyqtgraph import GraphicsLayoutWidget
import apprcc_rc
