# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nodetree.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TreeView(object):
    def setupUi(self, TreeView):
        TreeView.setObjectName("TreeView")
        TreeView.resize(504, 338)
        self.horizontalLayoutWidget = QtWidgets.QWidget(TreeView)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 501, 337))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Interpreter = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Interpreter.setMinimumSize(QtCore.QSize(128, 128))
        self.Interpreter.setText("")
        self.Interpreter.setAlignment(QtCore.Qt.AlignCenter)
        self.Interpreter.setObjectName("Interpreter")
        self.gridLayout.addWidget(self.Interpreter, 1, 1, 1, 1)
        self.BinaryBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.BinaryBrowser.setObjectName("BinaryBrowser")
        self.gridLayout.addWidget(self.BinaryBrowser, 0, 1, 1, 1)
        self.TreeViewer = QtWidgets.QTreeView(self.horizontalLayoutWidget)
        self.TreeViewer.setObjectName("TreeViewer")
        self.gridLayout.addWidget(self.TreeViewer, 0, 0, 2, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(TreeView)
        QtCore.QMetaObject.connectSlotsByName(TreeView)

    def retranslateUi(self, TreeView):
        _translate = QtCore.QCoreApplication.translate
        TreeView.setWindowTitle(_translate("TreeView", "Dialog"))

