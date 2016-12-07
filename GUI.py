# -*- coding: utf-8 -*-
import sys
import PyQt5.QtWidgets as QW
import PyQt5.QtCore as QC
import PyQt5.QtGui as QG

import Qt.window as wi
import main

def call_main():
    app = QW.QApplication(sys.argv)
    window = QW.QMainWindow()
    ui = wi.Ui_MainWindow()
    ui.setupUi(window)

    ui.actionExit.triggered.connect(app.quit)

    model = QC.QStringListModel(main.read_paksuites())
    ui.folderlist.setModel(model)

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    call_main()
