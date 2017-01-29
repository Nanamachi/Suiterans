# -*- coding: utf-8 -*-
import sys
import glob
import os
import PyQt5.QtWidgets as QW
import PyQt5.QtCore as QC
import PyQt5.QtGui as QG

import Qt.mainwindow as wi
import Qt.treeviewer as tv
import core
import lib
import painter
import binaryViewer
from customErr import *
from loginit import *

class Viewer(QW.QMainWindow):

    def __init__(self):
        super().__init__()

        self.windows = []

        self.ui = wi.Ui_MainWindow()
        self.ui.setupUi(self)

        self.paksuites_model = QG.QStandardItemModel(0,1)
        for ps in core.read_paksuites():
            self.append_paksuite(ps)
        self.ui.folderlist.setModel(self.paksuites_model)
        self.ui.folderlist.doubleClicked.connect(
            SLM('Viewer', self.show_paksuite)
        )

        self.ui.actionAdd_Simutrans_pak_folder.triggered.connect(
            self.select_folder
            # SLM('Viewer', self.select_folder)
        )
        self.ui.actionExit.triggered.connect(app.quit)

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
        self.ui.paklist.horizontalHeader().setModel(header_model)

        self.ui.progressBar.setMaximum(self.paksuite.amount)
        if not hasattr(self.paksuite, 'pak') \
            or self.paksuite.get_amount() != self.paksuite.amount:
            self.paksuite.amount = self.paksuite.get_amount()
            self.paksuite.pak = []
            for i, pakf_path in\
                enumerate(glob.glob(self.paksuite.path_main + '\\*.pak')):
                self.paksuite.load_each(pakf_path)
                self.ui.progressBar.setValue(i)
            for j, pakf_path in\
                enumerate(glob.glob(self.paksuite.path_addon + '\\*.pak')):
                self.paksuite.load_each(pakf_path)
                self.ui.progressBar.setValue(i+j)

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

        self.ui.paklist.setModel(paklists_model)
        self.ui.progressBar.setValue(0)

        self.ui.paklist.clicked.connect(
            SLM('Viewer', self.show_obj)
        )
        self.ui.paklist.doubleClicked.connect(
            SLM('Viewer', self.spawn_ntviewer)
        )

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

        self.ui.pakinfo.setModel(obj_model)

        if obj.type in lib.imaged_obj:
            imgmap = painter.paintobj(obj, self.paksuite.size)
            self.ui.ImgViewer.setPixmap(QG.QPixmap.fromImage(imgmap))
        else:
            self.ui.ImgViewer.setText('NoImage')

    def select_folder(self, status):
        dialog = QW.QFileDialog(self)
        pakfolder = dialog.getExistingDirectory()
        if pakfolder != '':
            ret = self.input_paksuite_name(pakfolder)
        else:
            ret = QW.QMessageBox(self)
            ret.setText(_translate(
                "InputDialog",
                "Adding PakSuite is cancelled"
            ))

        ret.show()

        return None

    def input_paksuite_name(self, pakfolder):
        statusdiag = QW.QMessageBox(self)
        name = os.path.basename(pakfolder)
        dialog = QW.QInputDialog(self)
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
                logger.info('PakSuite name duplicates.')
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
                logger.info('Selected folder is not a PakSuite folder.')
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
        NodeTreeViewer(self, objIndex).show()

class NodeTreeViewer(QW.QMainWindow):
    def __init__(self, parent, objIndex):

        super().__init__(parent)

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

        self.tvview = tv.Ui_TreeView()
        self.tvview.setupUi(self)
        self.tvview.TreeViewer.setModel(model)
        self.setSizePolicy(QW.QSizePolicy(
            QW.QSizePolicy.Preferred,
            QW.QSizePolicy.Preferred
        ))

        self.tvview.TreeViewer.clicked.connect(
            SLM('TreeViewer', self.show_node)
        )

    def show_node(self, objIndex):
        obj = objIndex.model().itemFromIndex(objIndex).data()
        if getattr(obj, 'type') == 'IMG':
            imgmap = painter.paintobj(obj,128)
            self.tvview.Interpreter.setPixmap(QG.QPixmap.fromImage(imgmap))
        elif getattr(obj, 'type') == 'TEXT':
            self.tvview.Interpreter.setText(obj.text)
        elif getattr(obj, 'type') == 'XREF':
            self.tvview.Interpreter.setText(obj.xref)
        else:
            self.tvview.Interpreter.setText(str(obj))
        self.tvview.BinaryBrowser.setPlainText(
            binaryViewer.ReadableBinary(obj).bin()
        )

_translate = QC.QCoreApplication.translate
translator = QC.QTranslator()
translator.load('locale/Suiterans_ja')
app = QW.QApplication(sys.argv)
app.installTranslator(translator)

if __name__ == '__main__':
    logger.debug('--------Suiterans: Simutrans pak manager--------')
    vwr = Viewer()
    vwr.show()
    sys.exit(app.exec_())
