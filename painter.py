# -*- coding: utf-8 -*-
import sys

import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
import PyQt5.QtWidgets as QW

import lib

def show_img(imgnode):

    app = QW.QApplication(sys.argv)

    label = QW.QLabel()
    imgmap = QG.QImage(128, 128, QG.QImage.Format_RGB555)
    bgcol = QG.QColor(123, 170, 57)
    imgmap.fill(bgcol)
    paint(imgmap, imgnode)
    label.setPixmap(QG.QPixmap.fromImage(imgmap))
    label.show()

    app.exec_()

def paint(qimg, imgnode):

    status = 'blank'
    penpos = QC.QPoint(
        imgnode.x if imgnode.version == 3 else 0,
        imgnode.y
    )
    print(imgnode.version)

    for i in range(imgnode.length):
        data = imgnode.img[2*i] + imgnode.img[2*i+1] * 256

        if status == 'blank': #if number of transparent cell
            if imgnode.version == 3 and data == 0 and penpos.x() != imgnode.x:
                penpos += QC.QPoint(0,1)
                penpos.setX(imgnode.x)
                status = 'blank'
            else:
                penpos += QC.QPoint(data,0)
                status = 'colored'
        elif status == 'colored': #if number of colored cell
            if data == 0:
                status = 'newline'
            else:
                status = data
        elif status == 'newline':
            penpos += QC.QPoint(0,1)
            penpos.setX(0)
            status = 'blank'
        else:
            if data >= 0x8000: #if special color
                color_index = data & 0x1F
                color = QG.QColor(lib.special_color[color_index])
            else:
                colorR = (data >> 10) << 3
                colorG = ((data >> 5) & 0x1F) << 3
                colorB = (data & 0x1F) << 3
                color = QG.QColor(colorR, colorG, colorB)
            qimg.setPixelColor(penpos, color)

            penpos += QC.QPoint(1,0)
            status -= 1
            if status == 0:
                status = 'blank'
