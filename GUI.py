# -*- coding: utf-8 -*-
import sys
import glob
import PyQt5.QtWidgets as QW
import PyQt5.QtCore as QC
import PyQt5.QtGui as QG

import Qt.window as wi
import core
import lib

app = QW.QApplication(sys.argv)
window = QW.QMainWindow()
ui = wi.Ui_MainWindow()
ui.setupUi(window)

def call_main():

    ui.actionExit.triggered.connect(app.quit)

    paksuites_model = QG.QStandardItemModel(0,1)
    paksuites = core.read_paksuites()
    for ps in paksuites:
        Qtps = QG.QStandardItem()
        Qtps.setText(ps.name + ' | ' + str(ps.amount) + ' pak files')
        Qtps.setData(ps)
        Qtps.setEditable(False)
        paksuites_model.appendRow(Qtps)
    ui.folderlist.setModel(paksuites_model)
    ui.folderlist.doubleClicked.connect(show_paksuite)

    window.show()
    sys.exit(app.exec_())

def show_paksuite(paksuiteIndex):

    header_model = QG.QStandardItemModel(0,3)
    header_list = [QG.QStandardItem() for i in range(3)]
    for i, c in enumerate(['type', 'object name', 'file name']):
        header_list[i].setText(c)

    header_model.appendRow(header_list)
    ui.paklist.horizontalHeader().setModel(header_model)

    paksuite = paksuiteIndex.model().item(paksuiteIndex.row()).data()
    ui.progressBar.setMaximum(paksuite.amount)
    if not hasattr(paksuite, 'pak') or paksuite.get_amount() != paksuite.amount:
        paksuite.amount = paksuite.get_amount()
        paksuite.pak = []
        for i, pakf_path in\
            enumerate(glob.glob(paksuite.path_main + '\\*.pak')):
            paksuite.load_each(pakf_path)
            ui.progressBar.setValue(i)
        for j, pakf_path in\
            enumerate(glob.glob(paksuite.path_addon + '\\*.pak')):
            paksuite.load_each(pakf_path)
            ui.progressBar.setValue(i+j)

    paklists_model = QG.QStandardItemModel(0,3)

    for pakfile in paksuite.pak:
        for obj in pakfile.root.child:
            Qtpf = [QG.QStandardItem() for i in range(3)]
            Qtpf[0].setText(obj.type)
            if hasattr(obj, 'name'):
                Qtpf[1].setText(obj.name)
            Qtpf[2].setText(pakfile.name)

            Qtpf[0].setData(obj)
            Qtpf[1].setData(obj)
            Qtpf[2].setData(obj)

            Qtpf[0].setEditable(False)
            Qtpf[1].setEditable(False)
            Qtpf[2].setEditable(False)
            paklists_model.appendRow(Qtpf)

    ui.paklist.setModel(paklists_model)
    ui.progressBar.setValue(0)

    ui.paklist.clicked.connect(show_obj)

def show_obj(objIndex):
    obj = objIndex.model().item(objIndex.row()).data()

    obj_model = QG.QStandardItemModel(0,2)
    for attr in lib.displayable_node:
        if hasattr(obj, attr):
            Qtpo = [QG.QStandardItem() for i in range(2)]
            Qtpo[0].setText(attr)
            Qtpo[1].setText(str(getattr(obj, attr)))

            Qtpo[0].setEditable(False)
            Qtpo[1].setEditable(False)
            obj_model.appendRow(Qtpo)

    ui.pakinfo.setModel(obj_model)

if __name__ == '__main__':
    call_main()
