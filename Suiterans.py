# -*- coding: utf-8 -*-

#     Suiterans --- Simutrans add-on manager
#
#     Copyright (C) 2017 Nanamachi
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#     contact: town7.haruki@gmail.com or twitter:@town7_haruki

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

class QPakMan(QG.QStandardItemModel, core.PakSuiteManager):
    def __init__(self):
        super().__init__()

        for name in self._paksuites:
            ps = self._paksuites[name]
            Qtps = QG.QStandardItem()
            if hasattr(ps, 'icon'):
                icopath = _op.join(
                    sys.path[0],
                    'resources/'+ ps.icon +'.png'
                )
            elif ps.size in [64, 128]:
                icopath = _op.join(
                    sys.path[0],
                    'resources/pak'+ str(ps.size) +'n.png'
                )
            else:
                icopath = _op.join(
                    sys.path[0],
                    'resources/paketcn.png'
                )
            Qtps.setIcon(QG.QIcon(icopath))
            Qtps.setText(
                ps.name + ' - ' + str(ps.amount) + ' pak files\n'
                + ps.path_main
            )
            Qtps.setData(ps)
            self.appendRow(Qtps)

    def addNewPakSuite(self, name, path, overwrite = False):
        super().addNewPakSuite(name, path, overwrite)
        ps = self._paksuites[name]
        Qtps = QG.QStandardItem()
        Qtps.setText(
            ps.name + ' - ' + str(ps.amount) + ' pak files\n'
            + ps.path_main
        )
        Qtps.setData(ps)
        self.appendRow(Qtps)

class Viewer(QW.QMainWindow):

    def __init__(self):

        logger.debug('Viewer init start...')

        super().__init__()

        self.ui = wi.Ui_MainWindow()
        self.ui.setupUi(self)

        self.pakman = QPakMan()
        self.ui.folderlist.setIconSize(QC.QSize(48,48))
        self.ui.folderlist.setModel(self.pakman)

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

                item[1].isDuplicate = False
                searchres = paklists_model.match(
                    paklists_model.index(0, 1),
                    0,
                    obj.name,
                    hits = 2,
                    flags = QC.Qt.MatchExactly,
                )

                if len(searchres) > 1:
                    r1 = searchres[0]
                    r2 = item[1].index()
                    if r1.sibling(r1.row(), 0).data()\
                        == r1.sibling(r2.row(), 0).data():
                        paklists_model.itemFromIndex(r1).isDuplicate = True
                        paklists_model.itemFromIndex(r2).isDuplicate = True


        self.ui.paklist.setModel(paklists_model)
        for i in range(3):
            self.ui.paklist.resizeColumnToContents(i)
        self.draw_highlight()
        self.ui.progressBar.setValue(0)

    def show_obj(self,objIndex):
        obj = objIndex.data(QC.Qt.UserRole | 0x01)

        obj_model = QG.QStandardItemModel(0,2)
        for attr in lib.displayable_node:
            if hasattr(obj, attr):
                row = [QG.QStandardItem() for i in range(2)]
                row[0].setText(_translate('parameter', attr))
                row[1].setText(_translate('parameter', str(getattr(obj, attr))))

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
                newps = self.pakman.addNewPakSuite(name, pakfolder)
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
                    newps = self.pakman.addNewPakSuite(name, pakfolder, True)
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

    def setHighlight(self, mode, *_):
        self._highlight = mode
        if hasattr(self, 'paksuite'):
            self.draw_highlight()

    def draw_highlight(self):
        m = self.ui.paklist.model()

        for i in range(m.rowCount()):
            index = [m.index(i,j) for j in range(3)]
            for j in index:
                if self._highlight == 'Duplicating'\
                    and m.itemFromIndex(index[1]).isDuplicate:
                    m.itemFromIndex(j).setBackground(
                        QG.QBrush(QG.QColor(0xffccff))
                    )
                else:
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
    logger.debug('--------Suiterans was crashed.--------\n')
    raise
else:
    logger.debug('--------Suiterans was successfully closed.--------\n')
    sys.exit()
