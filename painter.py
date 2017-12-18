# -*- coding: utf-8 -*-
from common_import import *

import lib
from loginit import *

def show_img(imgnode):

    app = QW.QApplication(sys.argv)

    label = QW.QLabel()
    imgmap = QG.QImage(128, 128, QG.QImage.Format_RGB555)
    bgcol = QG.QColor(123, 170, 57)
    imgmap.fill(bgcol)
    paint(imgmap, imgnode, QC.QPoint(0,0))
    label.setPixmap(QG.QPixmap.fromImage(imgmap))
    label.show()

    app.exec_()

def size_estimate(obj):
    i = 0
    s = 0
    while obj.searchNode('IMG', i) != None:
        imgnode = obj.searchNode('IMG', i)
        s = max(
            imgnode.x + imgnode.width,
            imgnode.y + imgnode.height,
            s
        )
        s = math.ceil(s/32) * 32
        i += 1
    return s

def paintobj(obj, size = 0):

    if size == 0:
        size = size_estimate(obj)

    if obj.type == 'BUIL':
        qimg = QG.QImage(
            size + (obj.size_x + obj.size_y - 2) * size / 2,
            size + (obj.size_x - 1 + obj.size_y - 1) * size / 4,
            QG.QImage.Format_RGB555
        )
    else:
        qimg = QG.QImage(size, size, QG.QImage.Format_RGB555)
    bgcol = QG.QColor(123, 170, 57)
    qimg.fill(bgcol)

    if   obj.type == 'CRSS':
        paint(qimg, obj.searchNode('IMG1',0).desc(0), QC.QPoint(0,0))
        paint(qimg, obj.searchNode('IMG1',2).desc(0), QC.QPoint(0,0))
    elif obj.type == 'BRDG':
        paint(qimg, obj.searchNode('IMG1',0).desc(3), QC.QPoint(0,0))
        paint(qimg, obj.searchNode('IMG1',1).desc(3), QC.QPoint(0,0))
    elif obj.type == 'TUNL':
        paint(qimg, obj.searchNode('IMG1',0).desc(0), QC.QPoint(0,0))
        paint(qimg, obj.searchNode('IMG1',1).desc(0), QC.QPoint(0,0))
    elif obj.type == 'WYOB':
        paint(qimg, obj.searchNode('IMG1',1).desc(5), QC.QPoint(0,0))
        paint(qimg, obj.searchNode('IMG1',0).desc(5), QC.QPoint(0,0))
    elif obj.type == 'WAY' :
        paint(qimg, obj.searchNode('IMG1',0).desc(5), QC.QPoint(0,0))
        frontimg = obj.searchNode('IMG1',7)
        if frontimg != None:
            paint(qimg, frontimg.desc(5), QC.QPoint(0,0))

    elif obj.type == 'BUIL':
        for i in range(obj.size_y):
            for j in range(obj.size_x):
                tile = obj.searchNode('TILE', i*obj.size_x + j)
                origpos = QC.QPoint(
                    size / 2 * (obj.size_y - i + j - 1),
                    size / 4 * (i + j)
                )
                paint(qimg, tile.desc(0,0,0), origpos)
                if obj.u_type in [33,34]:
                    paint(qimg, tile.desc(1,0,0), origpos)
    elif obj.type == 'FACT':
        qimg = paintobj(obj.searchNode('BUIL'), size)

    elif obj.type == 'IMG':
        qimg = paint(qimg, obj, QC.QPoint(0,0))
    else:
        paint(qimg, obj.searchNode('IMG'), QC.QPoint(0,0))

    return qimg

def paint(qimg, imgnode, origpos):

    if hasattr(imgnode, 'img'):

        status = 'blank'
        penpos = QC.QPoint(
            imgnode.x if imgnode.version > 2 else 0,
            imgnode.y
        ) + origpos

        for i in range(imgnode.length):
            data = imgnode.img[2*i] + imgnode.img[2*i+1] * 256

            if status == 'blank': #if number of transparent cell
                if data == 0 and penpos.x() != imgnode.x + origpos.x():
                    penpos += QC.QPoint(0,1)
                    if imgnode.version > 2:
                        penpos.setX(imgnode.x + origpos.x())
                    else:
                        penpos.setX(origpos.x())
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
                if imgnode.version > 2:
                    penpos.setX(imgnode.x + origpos.x())
                else:
                    penpos.setX(origpos.x())
                status = 'blank'
            else:
                if data >= 0x8000: #if special color
                    color_index = data & 0x1F
                    color = QG.QColor(lib.specialColor[color_index])
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

    return qimg
