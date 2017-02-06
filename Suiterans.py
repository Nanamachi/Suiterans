﻿# -*- coding: utf-8 -*-
import sys
import glob
import os
import argparse
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

        logger.debug('Viewer init start...')

        try:
            super().__init__()

            self.windows = []

            self.ui = wi.Ui_MainWindow()
            self.ui.setupUi(self)

            self.paksuites_model = QG.QStandardItemModel(0,1)
            for ps in core.read_paksuites():
                self.append_paksuite(ps)
            self.ui.folderlist.setModel(self.paksuites_model)

            header_model = QG.QStandardItemModel(0,3)
            header_list = [QG.QStandardItem() for i in range(3)]
            for i, c in enumerate(['type', 'object name', 'file name']):
                header_list[i].setText(c)
            header_model.appendRow(header_list)
            self.ui.paklist.horizontalHeader().setModel(header_model)

            self.ui.folderlist.doubleClicked.connect(
                SLM('Viewer', self.show_paksuite)
            )

            self.ui.actionAdd_Simutrans_pak_folder.triggered.connect(
                SLM('Viewer', self.select_folder)
            )
            self.ui.actionOpen_pak_files.triggered.connect(
                SLM('Viewer', self.select_file)
            )
            self.ui.actionExit.triggered.connect(app.quit)

            self.ui.paklist.clicked.connect(
                SLM('Viewer', self.show_obj)
            )
            self.ui.paklist.doubleClicked.connect(
                SLM('Viewer', self.spawn_ntviewer)
            )
        except Exception as e:
            logger.critical(
                "Unexpected error occured. Program Stop...\n"\
                + "{}: {}"
                .format(type(e), e.args)
            )
            logger.exception(e)
            raise

        else:
            logger.debug('Viewer successfully initialized.')

    def append_paksuite(self, ps):
        Qtps = QG.QStandardItem()
        Qtps.setText(ps.name + ' | ' + str(ps.amount) + ' pak files')
        Qtps.setData(ps)
        self.paksuites_model.appendRow(Qtps)

    def show_paksuite(self,paksuiteIndex):

        self.paksuite = paksuiteIndex.data(0x0101)

        if not hasattr(self.paksuite, 'pak') \
            or self.paksuite.get_amount() != self.paksuite.amount:
            self.paksuite.amount = self.paksuite.get_amount()
            self.ui.progressBar.setMaximum(self.paksuite.amount)
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

                for i in range(3):
                    Qtpf[i].setData(obj)

                paklists_model.appendRow(Qtpf)

        self.ui.paklist.setModel(paklists_model)
        self.ui.progressBar.setValue(0)

        for i in range(3):
            self.ui.paklist.resizeColumnToContents(i)

    def show_obj(self,objIndex):
        obj = objIndex.data(0x0101)

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

    def show_singlepak(self, pakf_path):
        itemModel = QG.QStandardItemModel()
        paksuite = core.SimplePakSuite(pakf_path)
        item = QG.QStandardItem()
        item.setData(paksuite)
        itemModel.appendRow(item)
        itemIndex = item.index()
        self.show_paksuite(itemIndex)

    def select_file(self, _):
        dialog = QW.QFileDialog(self)
        pakfile = dialog.getOpenFileName(
            filter = _translate('InputDialog', "Simutrans pak file (*.pak)")
        )
        if pakfile[0] != '':
            self.show_singlepak(pakfile[0])
        return None

    def select_folder(self, _):
        dialog = QW.QFileDialog(self)
        pakfolder = dialog.getExistingDirectory()
        if pakfolder != '':
            ret = self.input_paksuite_name(pakfolder)
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
    def __init__(self, parent = None, objIndex = None):

        super().__init__(parent)

        self.index = objIndex
        if parent != None:
            self.size = parent.paksuite.size

        self.tvview = tv.Ui_TreeView()
        self.tvview.setupUi(self)
        self.set_model()

        self.tvview.TreeViewer.clicked.connect(
            SLM('TreeViewer', self.show_node)
        )
        self.tvview.buttonNext.clicked.connect(
            SLM('TreeViewer', self.set_next)
        )
        self.tvview.buttonPrev.clicked.connect(
            SLM('TreeViewer', self.set_prev)
        )

    def set_model(self):

        def make_tree(obj):
            ret = QG.QStandardItem()
            ret.setText(obj.type)
            ret.setData(obj)
            ret.setEditable(False)
            for c in obj.child:
                ret.appendRow(make_tree(c))
            return ret

        obj = self.index.data(0x0101)
        self.treeModel = QG.QStandardItemModel()
        self.treeModel.appendRow(make_tree(obj))
        self.tvview.TreeViewer.setModel(self.treeModel)

        self.objectModel = QG.QStandardItemModel(0,2)
        for attr in lib.displayable_node:
            if hasattr(obj, attr):
                Qtpo = [QG.QStandardItem() for i in range(2)]
                Qtpo[0].setText(_translate('parameter', attr))
                Qtpo[1].setText(_translate('parameter', str(getattr(obj, attr))))

                Qtpo[0].setEditable(False)
                Qtpo[1].setEditable(False)
                self.objectModel.appendRow(Qtpo)

        self.tvview.ObjectView.setModel(self.objectModel)

        if obj.type in lib.imaged_obj:
            if self.parent() != None:
                size = self.parent().paksuite.size
            else:
                size = 0
            imgmap = painter.paintobj(obj, size)
            self.tvview.ImageView.setPixmap(QG.QPixmap.fromImage(imgmap))
        else:
            self.tvview.ImageView.setText('NoImage')

        ico = getattr(obj, 'icon', None)
        if ico != None:
            imgmap = painter.paintobj(ico, 32)
            self.tvview.IconView.setPixmap(QG.QPixmap.fromImage(imgmap))
        else:
            self.tvview.IconView.setText('')

        return None

    def set_next(self,*_):
        ix = self.index.sibling(
            self.index.row() + 1,
            self.index.column()
        )
        if not ix.isValid():
            self.index = self.index.sibling(0, self.index.column())
        else:
            self.index = ix

        self.set_model()
        return None

    def set_prev(self,*_):
        ix = self.index.sibling(
            self.index.row() - 1,
            self.index.column()
        )
        if not ix.isValid():
            self.index = self.index.sibling(
                self.index.model().rowCount() - 1,
                self.index.column()
            )
        else:
            self.index = ix

        self.set_model()
        return None

    def show_node(self, objIndex):
        obj = objIndex.data(0x0101)
        if getattr(obj, 'type') == 'IMG':
            imgmap = painter.paintobj(obj,self.size)
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

def main():

    global _translate
    global app
    global programFolder

    argparser = argparse.ArgumentParser(
        description = "Simutrans PakFile Viewer & Manager."
    )
    argparser.add_argument('-d', '--debug',
        help = "Select debug level. "\
        + "1:DEBUG | 2:INFO | 3:WARNING(default) | 4:ERROR | 5:CRITICAL",
        type = int,
        choices = range(1,6)
    )
    argparser.add_argument('fname',
        help = "pak file or config file to open.",
        type = str,
        nargs = '?'
    )

    args = argparser.parse_args()

    programFolder = sys.path[0]

    if args.debug != None:
        handler.setLevel(args.debug * 10)
        logger.setLevel(args.debug * 10)

    if not _op.isdir(_op.join(sys.path[0], 'conf/')):
        os.mkdir(_op.join(sys.path[0], 'conf/'))

    _translate = QC.QCoreApplication.translate
    translator = QC.QTranslator()
    translator.load(_op.join(sys.path[0], 'locale/Suiterans_ja'))
    app = QW.QApplication(sys.argv)
    app.installTranslator(translator)
    app.setWindowIcon(QG.QIcon(_op.join(sys.path[0],'resources/Suiterans.ico')))

    logger.debug('--------Suiterans: Simutrans pak manager--------')

    vwr = Viewer()
    if args.fname == None:
        pass
    elif args.fname.endswith('.pak'):
        vwr.show_singlepak(args.fname)

    # elif args.fname.endswith('.conf'):
    #     pass
    else:
        raise NotPakFileError(args.fname)

    vwr.show()
    app.exec_()

try:
    _op = os.path
    main()
except Exception as e:
    logger.critical(
        "Unexpected error occured. Program Stop...\n"\
        + "{}: {}"
        .format(type(e), e.args)
    )
    logger.exception(e)
    raise
else:
    logger.debug('--------Suiterans was successfully closed.--------\n')
    sys.exit()
