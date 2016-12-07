# -*- coding: utf-8 -*-
import sys
import PyQt5.QtWidgets as QW
import PyQt5.QtCore as QC
import PyQt5.QtGui as QG

import Qt.window as wi
import main

app = QW.QApplication(sys.argv)
window = QW.QMainWindow()
ui = wi.Ui_MainWindow()
ui.setupUi(window)

def call_main():

    ui.actionExit.triggered.connect(app.quit)

    paksuites_model = QG.QStandardItemModel(0,1)
    paksuites = main.read_paksuites()
    for ps in paksuites:
        Qtps = QG.QStandardItem()
        Qtps.setText(ps['name'])
        Qtps.setData(ps['dir'])
        Qtps.setEditable(False)
        paksuites_model.appendRow(Qtps)
    ui.folderlist.setModel(paksuites_model)
    ui.folderlist.doubleClicked.connect(show_paksuite)

    window.show()
    sys.exit(app.exec_())

def show_paksuite(paksuiteIndex):
    paklists_model = QG.QStandardItemModel(0,1)

    for pakfile in \
        main.PakSuite(\
            paksuiteIndex.model().item(paksuiteIndex.row()).data()
        ).pak:

        paksuite = QG.QStandardItem()
        paksuite.setText(pakfile.name)
        paksuite.setData(pakfile)
        paklists_model.appendRow(paksuite)

    ui.paklist.setModel(paklists_model)

if __name__ == '__main__':
    call_main()
