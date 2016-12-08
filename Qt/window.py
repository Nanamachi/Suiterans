# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 380)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.folderlist = QtWidgets.QListView(self.centralWidget)
        self.folderlist.setAcceptDrops(True)
        self.folderlist.setAutoScrollMargin(30)
        self.folderlist.setDragEnabled(True)
        self.folderlist.setObjectName("folderlist")
        self.gridLayout.addWidget(self.folderlist, 1, 0, 5, 1)
        self.imgview = QtWidgets.QGraphicsView(self.centralWidget)
        self.imgview.setObjectName("imgview")
        self.gridLayout.addWidget(self.imgview, 4, 3, 3, 1)
        self.paklist = QtWidgets.QTableView(self.centralWidget)
        self.paklist.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.paklist.setSortingEnabled(True)
        self.paklist.setCornerButtonEnabled(False)
        self.paklist.setObjectName("paklist")
        self.paklist.horizontalHeader().setDefaultSectionSize(250)
        self.paklist.verticalHeader().setDefaultSectionSize(25)
        self.gridLayout.addWidget(self.paklist, 1, 2, 3, 2)
        self.pakinfo = QtWidgets.QTableView(self.centralWidget)
        self.pakinfo.setObjectName("pakinfo")
        self.gridLayout.addWidget(self.pakinfo, 4, 2, 3, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 6, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 638, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuSuiterans_v1_0_0 = QtWidgets.QMenu(self.menuBar)
        self.menuSuiterans_v1_0_0.setObjectName("menuSuiterans_v1_0_0")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_pak_files = QtWidgets.QAction(MainWindow)
        self.actionOpen_pak_files.setObjectName("actionOpen_pak_files")
        self.actionAdd_Simutrans_pak_folder = QtWidgets.QAction(MainWindow)
        self.actionAdd_Simutrans_pak_folder.setObjectName("actionAdd_Simutrans_pak_folder")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuSuiterans_v1_0_0.addAction(self.actionAdd_Simutrans_pak_folder)
        self.menuSuiterans_v1_0_0.addAction(self.actionOpen_pak_files)
        self.menuSuiterans_v1_0_0.addSeparator()
        self.menuSuiterans_v1_0_0.addAction(self.actionExit)
        self.menuBar.addAction(self.menuSuiterans_v1_0_0.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuSuiterans_v1_0_0.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_pak_files.setText(_translate("MainWindow", "Open .pak files"))
        self.actionAdd_Simutrans_pak_folder.setText(_translate("MainWindow", "Add Simutrans .pak folder"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

