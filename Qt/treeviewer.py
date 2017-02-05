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
        TreeView.resize(696, 467)
        TreeView.setAutoFillBackground(False)
        TreeView.setDocumentMode(False)
        TreeView.setDockNestingEnabled(False)
        TreeView.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(TreeView)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.buttonPrev = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPrev.setEnabled(True)
        self.buttonPrev.setObjectName("buttonPrev")
        self.gridLayout_3.addWidget(self.buttonPrev, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 1, 1, 1)
        self.buttonNext = QtWidgets.QPushButton(self.centralwidget)
        self.buttonNext.setObjectName("buttonNext")
        self.gridLayout_3.addWidget(self.buttonNext, 2, 3, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabObjectView = QtWidgets.QWidget()
        self.tabObjectView.setObjectName("tabObjectView")
        self.gridLayout = QtWidgets.QGridLayout(self.tabObjectView)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ImageView = QtWidgets.QLabel(self.tabObjectView)
        self.ImageView.setMinimumSize(QtCore.QSize(256, 0))
        self.ImageView.setText("")
        self.ImageView.setAlignment(QtCore.Qt.AlignCenter)
        self.ImageView.setObjectName("ImageView")
        self.gridLayout.addWidget(self.ImageView, 1, 1, 1, 1)
        self.IconView = QtWidgets.QLabel(self.tabObjectView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconView.sizePolicy().hasHeightForWidth())
        self.IconView.setSizePolicy(sizePolicy)
        self.IconView.setMinimumSize(QtCore.QSize(32, 64))
        self.IconView.setText("")
        self.IconView.setAlignment(QtCore.Qt.AlignCenter)
        self.IconView.setObjectName("IconView")
        self.gridLayout.addWidget(self.IconView, 0, 1, 1, 1)
        self.tableView = QtWidgets.QTableView(self.tabObjectView)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 0, 0, 2, 1)
        self.tabWidget.addTab(self.tabObjectView, "")
        self.tabNodeTreeView = QtWidgets.QWidget()
        self.tabNodeTreeView.setObjectName("tabNodeTreeView")
        self.gridLayout1 = QtWidgets.QGridLayout(self.tabNodeTreeView)
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout1.setObjectName("gridLayout1")
        self.TreeViewer = QtWidgets.QTreeView(self.tabNodeTreeView)
        self.TreeViewer.setStyleSheet("")
        self.TreeViewer.setObjectName("TreeViewer")
        self.gridLayout1.addWidget(self.TreeViewer, 0, 0, 2, 1)
        self.BinaryBrowser = QtWidgets.QPlainTextEdit(self.tabNodeTreeView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BinaryBrowser.sizePolicy().hasHeightForWidth())
        self.BinaryBrowser.setSizePolicy(sizePolicy)
        self.BinaryBrowser.setMinimumSize(QtCore.QSize(375, 0))
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
        self.gridLayout1.addWidget(self.BinaryBrowser, 0, 1, 1, 1)
        self.Interpreter = QtWidgets.QLabel(self.tabNodeTreeView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Interpreter.sizePolicy().hasHeightForWidth())
        self.Interpreter.setSizePolicy(sizePolicy)
        self.Interpreter.setMinimumSize(QtCore.QSize(128, 128))
        self.Interpreter.setText("")
        self.Interpreter.setAlignment(QtCore.Qt.AlignCenter)
        self.Interpreter.setObjectName("Interpreter")
        self.gridLayout1.addWidget(self.Interpreter, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tabNodeTreeView, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 4)
        TreeView.setCentralWidget(self.centralwidget)

        self.retranslateUi(TreeView)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TreeView)
        TreeView.setTabOrder(self.tabWidget, self.TreeViewer)
        TreeView.setTabOrder(self.TreeViewer, self.BinaryBrowser)
        TreeView.setTabOrder(self.BinaryBrowser, self.buttonPrev)
        TreeView.setTabOrder(self.buttonPrev, self.buttonNext)

    def retranslateUi(self, TreeView):
        _translate = QtCore.QCoreApplication.translate
        TreeView.setWindowTitle(_translate("TreeView", "Suiterans Tree Viewer"))
        self.buttonPrev.setText(_translate("TreeView", "Prev"))
        self.buttonPrev.setShortcut(_translate("TreeView", "Ctrl+B"))
        self.buttonNext.setText(_translate("TreeView", "Next"))
        self.buttonNext.setShortcut(_translate("TreeView", "Ctrl+N"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabObjectView), _translate("TreeView", "ObjectView"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabNodeTreeView), _translate("TreeView", "NodeTreeView"))

