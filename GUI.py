# -*- coding: utf-8 -*-
import sys
import Qt.window as wi
from PyQt5.QtWidgets import QApplication, QMainWindow

def call_main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = wi.Ui_MainWindow()
    ui.setupUi(window)

    ui.actionExit.triggered.connect(app.quit)

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    call_main()
