#-------------------------------------------------
#
# Project created by QtCreator 2016-12-06T09:52:10
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = Suiterans
TEMPLATE = app

lupdate_only{
SOURCES +=\
    ../Suiterans.py\
    ../lib.py
}
HEADERS  +=
FORMS    += mainwindow.ui \
    nodetree.ui

TRANSLATIONS += Suiterans_ja.ts

DISTFILES +=
