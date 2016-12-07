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
        self.imgview = QtWidgets.QGraphicsView(self.centralWidget)
        self.imgview.setObjectName("imgview")
        self.gridLayout.addWidget(self.imgview, 2, 2, 1, 1)
        self.paklist = QtWidgets.QTableView(self.centralWidget)
        self.paklist.setObjectName("paklist")
        self.gridLayout.addWidget(self.paklist, 0, 1, 1, 2)
        self.pakinfo = QtWidgets.QTableView(self.centralWidget)
        self.pakinfo.setObjectName("pakinfo")
        self.gridLayout.addWidget(self.pakinfo, 2, 1, 1, 1)
        self.folderlist = QtWidgets.QListView(self.centralWidget)
        self.folderlist.setObjectName("folderlist")
        self.gridLayout.addWidget(self.folderlist, 0, 0, 4, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 2)
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
        self.pushButton.setText(_translate("MainWindow", "Push ME!"))
        self.menuSuiterans_v1_0_0.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_pak_files.setText(_translate("MainWindow", "Open .pak files"))
        self.actionAdd_Simutrans_pak_folder.setText(_translate("MainWindow", "Add Simutrans .pak folder"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

