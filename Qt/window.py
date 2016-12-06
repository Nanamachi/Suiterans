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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listView = QtWidgets.QListView(self.centralWidget)
        self.listView.setObjectName("listView")
        self.horizontalLayout_2.addWidget(self.listView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.centralWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
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
