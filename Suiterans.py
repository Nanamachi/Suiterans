﻿# -*- coding: utf-8 -*-
import sys
import glob
import os
import argparse
import PyQt5.QtWidgets as QW
import PyQt5.QtCore as QC
import PyQt5.QtGui as QG
import PyQt5 as Qt

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

        super().__init__()

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

        self.ui.actionAdd_Simutrans_pak_folder.triggered.connect(
            SLM('Viewer', self.select_folder)
        )
        self.ui.actionOpen_pak_files.triggered.connect(
            SLM('Viewer', self.select_file)
        )
        self.ui.actionExit.triggered.connect(app.quit)

        actionHighlight = QW.QActionGroup(self)
        actionHighlight.addAction(self.ui.action_None)
        actionHighlight.addAction(self.ui.actionConflicting)
        actionHighlight.addAction(self.ui.actionDuplicating)
        self.ui.action_None.triggered.connect(
            SLM('Viewer', self.setHighlight, 'None')
        )
        self.ui.actionConflicting.triggered.connect(
            SLM('Viewer', self.setHighlight, 'Conflicting')
        )
        self.ui.actionDuplicating.triggered.connect(
            SLM('Viewer', self.setHighlight, 'Duplicating')
        )
        self.setHighlight('None')
        self.ui.action_None.setChecked(True)

        self.ui.folderlist.doubleClicked.connect(
        SLM('Viewer', self.show_paksuite)
        )

        self.ui.paklist.clicked.connect(
            SLM('Viewer', self.show_obj)
        )
        self.ui.paklist.doubleClicked.connect(
            SLM('Viewer', self.spawn_ntviewer)
        )

        logger.debug('Viewer successfully initialized.')

    def append_paksuite(self, ps):
        Qtps = QG.QStandardItem()
        Qtps.setText(ps.name + ' | ' + str(ps.amount) + ' pak files')
        Qtps.setData(ps)
        self.paksuites_model.appendRow(Qtps)

    def show_paksuite(self,paksuiteIndex):

        self.paksuite = paksuiteIndex.data(QC.Qt.UserRole | 0x01)

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
                item = []
                for s in [obj.type, obj.name, pakfile.name]:
                    item.append(QG.QStandardItem(s))
                    item[-1].setData(obj)

                paklists_model.appendRow(item)

        self.ui.paklist.setModel(paklists_model)
        self.draw_highlight()
        self.ui.progressBar.setValue(0)

        for i in range(3):
            self.ui.paklist.resizeColumnToContents(i)

    def show_obj(self,objIndex):
        obj = objIndex.data(QC.Qt.UserRole | 0x01)

        obj_model = QG.QStandardItemModel(0,2)
        for attr in lib.displayable_node:
            if hasattr(obj, attr):
                row = [QG.QStandardItem() for i in range(2)]
                row[0].setText(_tr('parameter', attr))
                row[1].setText(_tr('parameter', str(getattr(obj, attr))))

                row[0].setEditable(False)
                row[1].setEditable(False)
                obj_model.appendRow(row)

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
            filter = _tr('InputDialog', "Simutrans pak file (*.pak)")
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
            _tr("InputDialog", 'Add New pak Suite...'),
            _tr("InputDialog", 'Please write new pak Suite name'),
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
                    _tr('InputDialog', 'PakSuite already exists'),
                    _tr(
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
            statusdiag.setText(_tr(
                "InputDialog",
                "Adding PakSuite is cancelled"
            ))
        elif status == 'success':
            statusdiag.setText(_tr(
                "InputDialog",
                'PakSuite was successfully added.'
            ))
        elif status == 'NotPS':
            statusdiag.setText(_tr(
                "InputDialog",
                "Folder {} is not Simutrans PakSuite Folder."
            ).format(name))

        return statusdiag

    def spawn_ntviewer(self, objIndex):
        NodeTreeViewer(self, objIndex).show()

    def setHighlight(self, mode, *_):
        self._highlight = mode
        if hasattr(self, 'paksuite'):
            self.draw_highlight()

    def draw_highlight(self):
        m = self.ui.paklist.model()

        if self._highlight == 'Duplicating':
            for i in range(m.rowCount()):
                index = m.index(i, 1)
                searchres = m.match(
                    index,
                    0,
                    m.data(index),
                    hits = -1,
                    flags = QC.Qt.MatchExactly,
                )
                for j,r1 in enumerate(searchres[:-1]):
                    for r2 in searchres[j+1:]:
                        idxes1 = [r1.sibling(r1.row(), k) for k in range(3)]
                        idxes2 = [r1.sibling(r2.row(), k) for k in range(3)]
                        if  idxes1[0].data()\
                            == idxes2[0].data():
                            for k in idxes1:
                                m.itemFromIndex(k).setBackground(
                                    QG.QBrush(QG.QColor(0xffccff))
                                )
                            for k in idxes2:
                                m.itemFromIndex(k).setBackground(
                                    QG.QBrush(QG.QColor(0xffccff))
                                )

        elif self._highlight == 'None':
            for i in range(m.rowCount()):
                index = [m.index(i,j) for j in range(3)]
                for j in index:
                    m.itemFromIndex(j).setBackground(
                        QG.QBrush(QG.QColor('white'))
                    )

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

        obj = self.index.data(QC.Qt.UserRole | 0x01)
        self.treeModel = QG.QStandardItemModel()
        self.treeModel.appendRow(make_tree(obj))
        self.tvview.TreeViewer.setModel(self.treeModel)

        self.objectModel = QG.QStandardItemModel(0,2)
        for attr in lib.displayable_node:
            if hasattr(obj, attr):
                Qtpo = [QG.QStandardItem() for i in range(2)]
                Qtpo[0].setText(_tr('parameter', attr))
                Qtpo[1].setText(_tr('parameter', str(getattr(obj, attr))))

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
            self.tvview.IconView.setText(' ')

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
        obj = objIndex.data(QC.Qt.UserRole | 0x01)
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

    global _tr
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

    _tr = QC.QCoreApplication.translate
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
    logger.debug('--------Suiterans was crashed.--------\n')
    raise
else:
    logger.debug('--------Suiterans was successfully closed.--------\n')
    sys.exit()
