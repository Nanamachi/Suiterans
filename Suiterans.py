# -*- coding: utf-8 -*-
import sys
import glob
import os
import PyQt5.QtWidgets as QW
import PyQt5.QtCore as QC
import PyQt5.QtGui as QG

import Qt.mainwindow as wi
import core
import lib
import painter

_translate = QC.QCoreApplication.translate
translator = QC.QTranslator()
translator.load('locale/Suiterans_ja')
app = QW.QApplication(sys.argv)
app.installTranslator(translator)
window = QW.QMainWindow()
ui = wi.Ui_MainWindow()
ui.setupUi(window)

def call_main():

    ui.actionExit.triggered.connect(app.quit)

    vwr = Viewer()

    window.show()
    sys.exit(app.exec_())

class Viewer():

    def __init__(self):
        self.show_paksuiteList()

    def show_paksuiteList(self):

        paksuites_model = QG.QStandardItemModel(0,1)
        paksuites = core.read_paksuites()
        for ps in paksuites:
            Qtps = QG.QStandardItem()
            Qtps.setText(ps.name + ' | ' + str(ps.amount) + ' pak files')
            Qtps.setData(ps)
            Qtps.setEditable(False)
            paksuites_model.appendRow(Qtps)
        ui.folderlist.setModel(paksuites_model)
        ui.folderlist.doubleClicked.connect(self.show_paksuite)

        ui.actionAdd_Simutrans_pak_folder.triggered.connect(self.select_folder)

        return len(paksuites)

    def show_paksuite(self,paksuiteIndex):

        self.paksuite = paksuiteIndex.model().item(paksuiteIndex.row()).data()

        header_model = QG.QStandardItemModel(0,3)
        header_list = [QG.QStandardItem() for i in range(3)]
        for i, c in enumerate(['type', 'object name', 'file name']):
            header_list[i].setText(c)

        header_model.appendRow(header_list)
        ui.paklist.horizontalHeader().setModel(header_model)

        ui.progressBar.setMaximum(self.paksuite.amount)
        if not hasattr(self.paksuite, 'pak') \
            or self.paksuite.get_amount() != self.paksuite.amount:
            self.paksuite.amount = self.paksuite.get_amount()
            self.paksuite.pak = []
            for i, pakf_path in\
                enumerate(glob.glob(self.paksuite.path_main + '\\*.pak')):
                self.paksuite.load_each(pakf_path)
                ui.progressBar.setValue(i)
            for j, pakf_path in\
                enumerate(glob.glob(self.paksuite.path_addon + '\\*.pak')):
                self.paksuite.load_each(pakf_path)
                ui.progressBar.setValue(i+j)

        paklists_model = QG.QStandardItemModel(0,3)

        for pakfile in self.paksuite.pak:
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

        ui.paklist.clicked.connect(self.show_obj)

    def show_obj(self,objIndex):
        obj = objIndex.model().item(objIndex.row()).data()

        obj_model = QG.QStandardItemModel(0,2)
        for attr in lib.displayable_node:
            if hasattr(obj, attr):
                Qtpo = [QG.QStandardItem() for i in range(2)]
                Qtpo[0].setText(_translate('parameter', attr))
                Qtpo[1].setText(_translate('parameter', str(getattr(obj, attr))))

                Qtpo[0].setEditable(False)
                Qtpo[1].setEditable(False)
                obj_model.appendRow(Qtpo)

        ui.pakinfo.setModel(obj_model)

        if obj.type in lib.imaged_obj:
            imgmap = painter.paintobj(obj, self.paksuite.size)
            ui.label.setPixmap(QG.QPixmap.fromImage(imgmap))
        else:
            ui.label.setText('NoImage')

    def select_folder(self):
        dialog = QW.QFileDialog()
        pakfolder = dialog.getExistingDirectory()

        if pakfolder != '':
            name = os.path.basename(pakfolder)
            dialog = QW.QInputDialog()
            name, isAdd = dialog.getText(
                dialog,
                _translate("InputDialog", 'Add New pak Suite...'),
                _translate("InputDialog", 'Please write new pak Suite name'),
                QW.QLineEdit.Normal,
                name
            )
            if isAdd:
                core.write_paksuite(name, pakfolder)
            self.show_paksuiteList()

        return None

call_main()
