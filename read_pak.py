# -*- coding: utf-8 -*-
import sys
import struct
import os
import PyQt5.QtCore as QC
import PyQt5.QtGui as QG
import PyQt5.QtWidgets as QW

import lib
from customErr import *

class PakFile(): #read .pak and extract into PakNode instance
    def __init__(self, path):
        # http://www.ajisaba.net/python/binary.html
        _fp = open(path, 'rb')
        self.path = path
        self.name = os.path.basename(path)
        while True:
            if _fp.read(4) == b'ROOT':
                break
            else:
                _fp.seek(-3,1)

        _fp.seek(-4, 1) #back 4chars from here
        self.root = ROOTNode(_fp)
        _fp.close()

    def __repr__ (self):
        return "<Simutrans Pak File '{}'>".format(self.path)

class PakNode():
    def __init__(self, fp): #read data from binary and spawn child Nodes
        [self.type, self.child_count, self.data_len,] \
            = self.read_header(fp)

        self.read_data(fp)

        self.child = []
        for i in range(self.child_count):
            child_type = fp.read(4).decode()
            if child_type[3] == '\0':
                child_type = child_type[0:3]

            child_class = globals()[child_type + 'Node']
            fp.seek(-4, 1) #back 4chars from here

            self.child.append(child_class(fp))

        #set name and author from child TEXTNode
        if self.type in lib.named_obj:
            for c in self.child:
                if type(c) == CURSNode:
                    _name_node   = c.child[0]
                    _author_node = c.child[1]
                    break
            else:
                _name_node   = self.child[0]
                _author_node = self.child[1]

            self.name = _name_node.text
            if (type(_author_node) == TEXTNode):
                self.author = _author_node.text
            if not getattr(self, 'author', ''):
                self.author = '__UnDefined__'

        elif self.type == 'FACT':
            self.name   = self.child[0].name
            self.author = self.child[0].author

        return None

    def __repr__(self):
        if hasattr(self, 'name'):
            return "<Simutrans {0}: {1}>".format(self.type, self.name)
        elif hasattr(self, 'text'):
            return "<Simutrans {0}: {1}>".format(self.type, self.text)
        elif hasattr(self, 'xref'):
            return "<Simutrans {0}: {1}>".format(self.type, self.xref)
        else:
            return "<Simutrans {} Node>".format(self.type)

    def read_LE(self, fp, fmt, rest): #read Liettle Endian format
        if fmt == 'uint8':
            packfmt = '<B'
            packlen = 1
        elif fmt == 'sint8':
            packfmt = '<b'
            packlen = 1
        elif fmt == 'uint16':
            packfmt = '<H'
            packlen = 2
        elif fmt == 'sint16':
            packfmt = '<h'
            packlen = 2
        elif fmt == 'uint32':
            packfmt = '<I'
            packlen = 4
        elif fmt == 'sint32':
            packfmt = '<i'
            packlen = 4
        elif fmt[0:4] == 'ufix':
            #unsigned fixed point
            #ex.) 'ufix0816' means '0xAB.CD'
            #this func return the value multiplied 100 'cause
            #ufix format mostly used percent format.
            packlen = int(fmt[6:8]) >> 3
            shamt = int(fmt[4:6])
            if packlen == 1:
                packfmt = '<B'
            elif packlen == 2:
                packfmt = '<H'
            elif packlen == 4:
                packfmt = '<I'
        else:
            raise FormatError(fmt)

        if rest - packlen < 0:
            raise StreamTooShortError(rest,fmt)

        ret = struct.unpack(packfmt, fp.read(packlen))[0]
        if fmt[0:4] == 'ufix':
            ret = (ret * 100) >> shamt

        return [ret, rest - packlen]

    def read_header(self, fp): #read binary and return headerdata
        typ = fp.read(4).decode()
        if typ[3] == '\0' : #if last char is null (occur in IMG and WAY)
            typ = typ[:3]
        [child_count, _] = self.read_LE(fp, 'uint16', 2)
        [data_len, _] = self.read_LE(fp, 'uint16', 2)
        return [
            typ,
            child_count,
            data_len,
        ]

    def set_intro(self, v_th):
        if self.version > v_th:
            self.intro_year  = int(self.intro / 12)
            self.intro_month = int(self.intro % 12) + 1
        else:
            self.intro_year  = int(self.intro / 16)
            self.intro_month = int(self.intro % 16) + 1

        return None

    def set_retire(self, v_th):
        if self.version > v_th:
            self.retire_year  = int(self.retire / 12)
            self.retire_month = int(self.retire % 12) + 1
        else:
            self.retire_year  = int(self.retire / 16)
            self.retire_month = int(self.retire % 16) + 1

        return None

    def read_data(self, fp): #read own data with list defined by lib.py

        #get version
        [dump, self.data_len] = self.read_LE(fp, 'uint16', self.data_len)
        self.version = dump & 0x7FFF if dump & 0x8000 else 0
        if self.version == 0:
            fp.seek(-2, 1)
            self.data_len += 2

        #read self param
        for c in getattr(lib, self.type + 'param'):
            param = c(self.version)
            if param != None:
                [val, self.data_len] = self.read_LE(fp, param[1], self.data_len)
                if  (param[0] == 'sound')\
                    and (val == -2)\
                    and (self.type == 'CRSS'):
                    [sfile_len, self.data_len] \
                        = self.read_LE(fp, 'sint8', self.data_len)
                    self.wav = fp.read(sfile_len).decode()
                    self.data_len -= sfile_len
                setattr(self, param[0], param[2](val))
        if self.type == 'VHCL' and getattr(self, 'sound', None) == -2:
            [sfile_len, self.data_len] \
                = self.read_LE(fp, 'sint8', self.data_len)
            self.wav = fp.read(sfile_len)
            self.data_len -= sfile_len

        if self.data_len != 0:
            raise StreamTooLongError(self.data_len, self.version)

        return None

    def show_tree(self, *number):
        for n in number:
            print(n, end = ' ')
        print(self)
        for i,c in enumerate(self.child):
            c.show_tree(*number, i)

        return None

    def desc(self, *number):
        if len(number) == 0:
            return self
        else:
            try:
                ret = self.child[number[0]].desc(*number[1:])
            except IndexError:
                ret = None
            return ret

    def searchNode(self, obj, typ, pos = 0):
        for c in obj.child:
            if c.type == typ and pos == 0:
                break
            elif c.type == typ:
                pos -= 1
            elif c.child_count != 0:
                try:
                    c = self.searchNode(c, typ)
                    break
                except NodeNotFoundError:
                    pass
        else:
            raise NodeNotFoundError(self, typ)

        return c

class BRDGNode(PakNode):
    def read_data(self, fp):
        super().read_data(fp)

        if hasattr(self, 'intro'):
            self.set_intro(4)
            self.set_retire(4)

class BUILNode(PakNode):
    def read_data(self, fp):
        super().read_data(fp)

        if hasattr(self, 'intro'):
            self.set_intro(1)
            self.set_retire(1)

class CCARNode(PakNode):
    def read_data(self, fp):
        super().read_data(fp)

        if hasattr(self, 'intro'):
            self.set_intro(1)
            self.set_retire(1)

class CRSSNode(PakNode):
    def read_data(self, fp):
        super().read_data(fp)

        if hasattr(self, 'intro'):
            self.set_intro(1)
            self.set_retire(1)

class CURSNode(PakNode):
    def read_data(self, fp):
        pass

class FACTNode(PakNode):
    pass

class FFIENode(PakNode):
    pass

class FFCLNode(PakNode):
    pass

class FIELNode(PakNode):
    def read_data(self, fp):
        pass

class FPRONode(PakNode):
    pass

class FSMONode(PakNode):
    pass

class FSUPNode(PakNode):
    pass

class GOODNode(PakNode):
    pass

class GRNDNode(PakNode):
    def read_data(self, fp):
        pass

class GOBJNode(PakNode):
    pass

class IMGNode(PakNode):

    def read_data(self, fp):
        fp.seek(6,1)
        [self.version, _] = self.read_LE(fp, 'uint8', self.data_len)
        fp.seek(-7,1)
        for c in getattr(lib, self.type + 'param'):
            param = c(self.version)
            if param != None:
                [val, self.data_len] = self.read_LE(fp, param[1], self.data_len)
                setattr(self, param[0], param[2](val))

        if self.version == 3:
            self.length = int(self.data_len / 2)

        self.img = fp.read(self.length * 2)
        self.data_len -= self.length * 2

        if self.data_len != 0:
            raise StreamTooLongError(self.data_len, self.version)

        return None

class IMG1Node(PakNode):
    def read_data(self, fp):
        self.version = 0

        for c in getattr(lib, self.type + 'param'):
            param = c(self.version)
            if param != None:
                [val, self.data_len] = self.read_LE(fp, param[1], self.data_len)
                setattr(self, param[0], param[2](val))

        if self.data_len != 0:
            raise StreamTooLongError(self.data_len, self.version)

class IMG2Node(PakNode):
    def read_data(self, fp):
        self.version = 0

        for c in getattr(lib, self.type + 'param'):
            param = c(self.version)
            if param != None:
                [val, self.data_len] = self.read_LE(fp, param[1], self.data_len)
                setattr(self, param[0], param[2](val))

        if self.data_len != 0:
            raise StreamTooLongError(self.data_len, self.version)

class MENUNode(PakNode):
    def read_data(self, fp):
        pass

class MISCNode(PakNode):
    def read_data(self, fp):
        pass

class PASSNode(PakNode):
    pass

class SIGNNode(PakNode):
    def read_data(self, fp):
        super().read_data(fp)

        self.set_intro(2)
        self.set_retire(2)

class ROOTNode(PakNode):
    def read_data(self, fp):
        pass

class SMOKNode(PakNode):
    def read_data(self, fp):
        pass

class SOUNNode(PakNode):
    def read_data(self, fp):
        pass

class SYMBNode(PakNode):
    def read_data(self, fp):
        pass

class TEXTNode(PakNode):
    def read_data(self, fp):
        self.text = fp.read(self.data_len).decode('sjis', errors = 'ignore')[:-1]

class TILENode(PakNode):
    pass

class TREENode(PakNode):
    pass

class TUNLNode(PakNode):
    def read_data(self, fp):
        super().read_data(fp)

        self.set_intro(0)
        self.set_retire(0)

class VHCLNode(PakNode):
    def read_data(self, fp):
        super().read_data(fp)

        if hasattr(self, 'intro'):
            self.set_intro(4)
        if hasattr(self, 'retire'):
            self.set_retire(4)

class WAYNode(PakNode):
    def read_data(self, fp):
        super().read_data(fp)

        self.set_intro(1)
        self.set_retire(1)

class WYOBNode(PakNode):
    def read_data(self, fp):
        super().read_data(fp)

        self.set_intro(0)
        self.set_retire(0)

class XREFNode(PakNode):
    def read_data(self, fp):
        self.xref = fp.read(self.data_len).decode('sjis', errors = 'ignore')

def main(path):
    pak = PakFile(path)
    return pak.root.child

if __name__ == '__main__':
    pass
