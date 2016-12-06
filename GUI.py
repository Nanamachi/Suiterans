# -*- coding: utf-8 -*-

import sys
import Qt.window as wi
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
ui = wi.Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
