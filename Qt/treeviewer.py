# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treeviewer.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TreeView(object):
    def setupUi(self, TreeView):
        TreeView.setObjectName("TreeView")
        TreeView.setWindowModality(QtCore.Qt.NonModal)
        TreeView.resize(604, 393)
        TreeView.setAutoFillBackground(False)
        TreeView.setDocumentMode(False)
        TreeView.setDockNestingEnabled(False)
        TreeView.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(TreeView)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.TreeViewer = QtWidgets.QTreeView(self.centralwidget)
        self.TreeViewer.setStyleSheet("")
        self.TreeViewer.setObjectName("TreeViewer")
        self.gridLayout.addWidget(self.TreeViewer, 2, 0, 2, 1)
        self.Interpreter = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Interpreter.sizePolicy().hasHeightForWidth())
        self.Interpreter.setSizePolicy(sizePolicy)
        self.Interpreter.setMinimumSize(QtCore.QSize(128, 128))
        self.Interpreter.setText("")
        self.Interpreter.setAlignment(QtCore.Qt.AlignCenter)
        self.Interpreter.setObjectName("Interpreter")
        self.gridLayout.addWidget(self.Interpreter, 3, 1, 1, 1)
        self.BinaryBrowser = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BinaryBrowser.sizePolicy().hasHeightForWidth())
        self.BinaryBrowser.setSizePolicy(sizePolicy)
        self.BinaryBrowser.setMinimumSize(QtCore.QSize(375, 240))
        font = QtGui.QFont()
        font.setFamily("Consolas,Courier New,Courier,Monaco,monospace")
        font.setPointSize(9)
        font.setKerning(True)
        self.BinaryBrowser.setFont(font)
        self.BinaryBrowser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.BinaryBrowser.setAcceptDrops(False)
        self.BinaryBrowser.setStyleSheet("font-family: Consolas, \'Courier New\', Courier, Monaco, monospace;")
        self.BinaryBrowser.setReadOnly(True)
        self.BinaryBrowser.setObjectName("BinaryBrowser")
        self.gridLayout.addWidget(self.BinaryBrowser, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        TreeView.setCentralWidget(self.centralwidget)

        self.retranslateUi(TreeView)
        QtCore.QMetaObject.connectSlotsByName(TreeView)

    def retranslateUi(self, TreeView):
        _translate = QtCore.QCoreApplication.translate
        TreeView.setWindowTitle(_translate("TreeView", "Suiterans Tree Viewer"))

