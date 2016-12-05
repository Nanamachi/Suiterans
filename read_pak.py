# -*- coding: utf-8 -*-
import sys
import struct
from PIL import Image

import lib

class PakFile(): #read .pak and extract into PakNode instance
    def __init__(self, path):
    # http://www.ajisaba.net/python/binary.html
        self._f = open(path, 'rb')
        self._path = path
        self._bin = self._f.read()

        i = 0
        while self._bin[i : i+4] != b'ROOT':
            i += 1

        self.root = ROOTNode(self._bin[i:])

    def __repr__ (self):
        return "<Simutrans Pak File '{}'>".format(self._path)

class PakNode():
    def __init__(self, binary): #read data from binary and generate child Nodes
        [
            self.type,
            self.child_count,
            self.data_len,
            self.data_bin,
            self.next_bin,
        ] \
        = self.read_header(binary)

        self.child = []
        for i in range(self.child_count):
            child_type = self.next_bin[0:4].decode()
            if child_type[3] == '\0':
                child_type = child_type[0:3]

            child_class = globals()[child_type + 'Node']

            self.child.append(child_class(self.next_bin))
            self.next_bin = self.child[i].next_bin
            del self.child[i].next_bin #to reduce memory

        self.read_data()

        if self.type in lib.named_obj:
            for i,c in enumerate(self.child):
                if type(c) == CURSNode:
                    self.name   = self.child[i].child[0].data_bin[:-1].decode()
                    self.author = self.child[i].child[1].data_bin[:-1].decode()
                    break
            else:
                self.name   = self.child[0].data_bin[:-1].decode()
                self.author = self.child[1].data_bin[:-1].decode()

        elif self.type == 'FACT':
            self.name   = self.child[0].name
            self.author = self.child[0].author

    def __repr__(self):
        if self.type in lib.named_obj:
            return "<Simutrans {0}: {1}>".format(self.type, self.name)
        else:
            return "<Simutrans {} Node>".format(self.type)

    def read_LE(self, binary, fmt):
        if fmt == 'uint8':
            packfmt = '<B'
            packlen = 1
        elif fmt == 'sint8':
            packfmt = '<b'
            packlen = 1
        elif fmt == 'uint16':
            packfmt = '<H'
            packlen = 2
        elif fmt == 'uint32':
            packfmt = '<I'
            packlen = 4
        elif fmt == 'sint32':
            packfmt = '<i'
            packlen = 4
        else:
            raise

        return [struct.unpack(packfmt, binary[0:packlen])[0], binary[packlen:]]

    def read_header(self, binary): #read binary and return headerdata
        typ = binary[0:4].decode()
        if typ[3] == '\0' : #if last char is null (occur in IMG and WAY)
            typ = typ[:3]
        [child_count, _] = self.read_LE(binary[4:6], 'uint16')
        [data_len, _] = self.read_LE(binary[6:8], 'uint16')
        data_bin = binary[8:8 + data_len]
        child_bin = binary[8 + data_len:]
        return [
            typ,
            child_count,
            data_len,
            data_bin,
            child_bin,
        ]

    def set_intro(self, v_th):
        if self.version > v_th:
            self.intro_year  = int(self.intro / 12)
            self.intro_month = int(self.intro % 12) + 1
        else:
            self.intro_year  = int(self.intro / 16)
            self.intro_year  = int(self.intro % 16) + 1

    def set_retire(self, v_th):
        if self.version > v_th:
            self.retire_year  = int(self.retire / 12)
            self.retire_month = int(self.retire % 12) + 1
        else:
            self.retire_year  = int(self.retire / 16)
            self.retire_year  = int(self.retire % 16) + 1

    def read_data(self):
        [dump, next_bin] = self.read_LE(self.data_bin, 'uint16')
        self.version = dump & 0x7FFF if dump & 0x8000 else 0
        if self.version == 0:
            raise
        for c in getattr(lib, self.type + 'param'):
            param = c(self.version)
            if param != None:
                [val, next_bin] = self.read_LE(next_bin, param[1])
                setattr(self, param[0], param[2](val))

class BRDGNode(PakNode):
    def read_data(self):
        super().read_data()

        if self.version > 4:
            self.set_intro(4)
            self.set_retire(4)

class BUILNode(PakNode):
    def read_data(self):
        super().read_data()

        if self.version > 1:
            self.set_intro(1)
            self.set_retire(1)

class CCARNode(PakNode):
    def read_data(self):
        super().read_data()

        if self.version > 1:
            self.set_intro(1)
            self.set_retire(1)

class CRSSNode(PakNode):
    def read_data(self):
        pass

class CURSNode(PakNode):
    def read_data(self):
        pass

class FACTNode(PakNode):
    def read_data(self):
        pass

class FFIENode(PakNode):
    def read_data(self):
        pass

class FFCLNode(PakNode):
    def read_data(self):
        pass

class FIELNode(PakNode):
    def read_data(self):
        pass

class FPRONode(PakNode):
    def read_data(self):
        pass

class FSMONode(PakNode):
    def read_data(self):
        pass

class FSUPNode(PakNode):
    def read_data(self):
        pass

class GOODNode(PakNode):
    def read_data(self):
        pass

class GRNDNode(PakNode):
    def read_data(self):
        pass

class GOBJNode(PakNode):
    def read_data(self):
        pass

class IMGNode(PakNode):
    def read_data(self):
        pass

class IMG1Node(PakNode):
    def read_data(self):
        pass

class IMG2Node(PakNode):
    def read_data(self):
        pass

class MENUNode(PakNode):
    def read_data(self):
        pass

class MISCNode(PakNode):
    def read_data(self):
        pass

class PASSNode(PakNode):
    def read_data(self):
        pass

class SIGNNode(PakNode):
    def read_data(self):
        pass

class ROOTNode(PakNode):
    def read_data(self):
        pass

class SMOKNode(PakNode):
    def read_data(self):
        pass

class SOUNNode(PakNode):
    def read_data(self):
        pass

class SYMBNode(PakNode):
    def read_data(self):
        pass

class TEXTNode(PakNode):
    def read_data(self):
        pass

class TILENode(PakNode):
    def read_data(self):
        pass

class TREENode(PakNode):
    def read_data(self):
        pass

class TUNLNode(PakNode):
    def read_data(self):
        pass

class VHCLNode(PakNode):
    def read_data(self):
        super().read_data()

        self.set_intro(4)
        if self.version > 2:
            self.set_retire(4)

class WAYNode(PakNode):
    def read_data(self):
        pass

class WYOBNode(PakNode):
    def read_data(self):
        pass

class XREFNode(PakNode):
    def read_data(self):
        pass

def main(path):
    pak = PakFile(path)
    return pak.root.child

if __name__ == '__main__':
    print(main(sys.argv[1]))
