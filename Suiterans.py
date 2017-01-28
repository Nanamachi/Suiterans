# -*- coding: utf-8 -*-
import sys
import glob
import os
import PyQt5.QtWidgets as QW
import PyQt5.QtCore as QC
import PyQt5.QtGui as QG

import Qt.mainwindow as wi
import Qt.nodetree as nt
import core
import lib
import painter
from customErr import *

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
        self.windows = []

        self.paksuites_model = QG.QStandardItemModel(0,1)
        for ps in core.read_paksuites():
            self.append_paksuite(ps)
        ui.folderlist.setModel(self.paksuites_model)
        ui.folderlist.doubleClicked.connect(self.show_paksuite)

        ui.actionAdd_Simutrans_pak_folder.triggered.connect(self.select_folder)

    def append_paksuite(self, ps):
        Qtps = QG.QStandardItem()
        Qtps.setText(ps.name + ' | ' + str(ps.amount) + ' pak files')
        Qtps.setData(ps)
        Qtps.setEditable(False)
        self.paksuites_model.appendRow(Qtps)

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
        ui.paklist.doubleClicked.connect(self.spawn_ntviewer)

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
            ret = self.input_paksuite_name(pakfolder)
        else:
            ret = QW.QMessageBox()
            ret.setText(_translate(
                "InputDialog",
                "Adding PakSuite is cancelled"
            ))

        ret.show()
        self.windows.append(ret)

        return None

    def input_paksuite_name(self, pakfolder):
        statusdiag = QW.QMessageBox()
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
            try:
                newps = core.write_paksuite(name, pakfolder)
                self.append_paksuite(newps)
                status = 'success'
            except FileExistsError:
                a = statusdiag.question(
                    statusdiag,
                    _translate('InputDialog', 'PakSuite already exists'),
                    _translate(
                        'InputDialog',
                        "PakSuite '{}' already exists. Overwrite?"
                    ).format(name),
                    QW.QMessageBox.Cancel |
                    QW.QMessageBox.Yes |
                    QW.QMessageBox.No
                )
                if a == QW.QMessageBox.Yes:
                    newps = core.write_paksuite(name, pakfolder, True)
                    self.append_paksuite(newps)
                    status = 'success'
                elif a == QW.QMessageBox.No:
                    status = 'inherit'
                    statusdiag = self.input_paksuite_name(pakfolder)
                else:
                    status = 'cancel'

            except NotPakSuiteError:
                status = 'NotPS'
        else:
            status = 'cancel'

        if status == 'cancel':
            statusdiag.setText(_translate(
                "InputDialog",
                "Adding PakSuite is cancelled"
            ))
        elif status == 'success':
            statusdiag.setText(_translate(
                "InputDialog",
                'PakSuite was successfully added.'
            ))
        elif status == 'NotPS':
            statusdiag.setText(_translate(
                "InputDialog",
                "Folder {} is not Simutrans PakSuite Folder."
            ).format(name))

        return statusdiag

    def spawn_ntviewer(self, objIndex):
        self.windows.append(NodeTreeViewer(objIndex))

class NodeTreeViewer():
    def __init__(self, objIndex):

        def make_tree(obj):
            ret = QG.QStandardItem()
            ret.setText(obj.type)
            ret.setData(obj)
            ret.setEditable(False)
            for c in obj.child:
                ret.appendRow(make_tree(c))
            return ret

        obj = objIndex.model().item(objIndex.row()).data()
        model = QG.QStandardItemModel()
        model.appendRow(make_tree(obj))

        self.dialog = QW.QDialog()
        self.ntview = nt.Ui_Dialog()
        self.ntview.setupUi(self.dialog)
        self.ntview.treeView.setModel(model)
        self.dialog.setSizePolicy(QW.QSizePolicy(
            QW.QSizePolicy.Preferred,
            QW.QSizePolicy.Preferred
        ))

        self.ntview.treeView.clicked.connect(self.show_node)
        self.dialog.show()

    def show_node(self, objIndex):
        obj = objIndex.model().itemFromIndex(objIndex).data()
        if getattr(obj, 'type') == 'IMG':
            imgmap = painter.paintobj(obj,128)
            self.ntview.label.setPixmap(QG.QPixmap.fromImage(imgmap))
        elif getattr(obj, 'type') == 'TEXT':
            self.ntview.label.setText(obj.text)
        elif getattr(obj, 'type') == 'XREF':
            self.ntview.label.setText(obj.xref)

call_main()
