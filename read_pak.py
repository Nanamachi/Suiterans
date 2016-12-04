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
        self.root = PakNode(self._bin[61:])

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

    def __repr__(self):
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

    def read_data(self):
        pass

class BRDGNode(PakNode):
    pass

class BUILNode(PakNode):
    pass

class CCARNode(PakNode):
    pass

class CRSSNode(PakNode):
    pass

class CURSNode(PakNode):
    pass

class FACTNode(PakNode):
    pass

class FFIENode(PakNode):
    pass

class FFCLNode(PakNode):
    pass

class FIELNode(PakNode):
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
    pass

class GOBJNode(PakNode):
    pass

class IMGNode(PakNode):
    pass

class IMG1Node(PakNode):
    pass

class IMG2Node(PakNode):
    pass

class MENUNode(PakNode):
    pass

class MISCNode(PakNode):
    pass

class PASSNode(PakNode):
    pass

class SIGNNode(PakNode):
    pass

class ROOTNode(PakNode):
    pass

class SMOKNode(PakNode):
    pass

class SOUNNode(PakNode):
    pass

class SYMBNode(PakNode):
    pass

class TEXTNode(PakNode):
    pass

class TILENode(PakNode):
    pass

class TREENode(PakNode):
    pass

class TUNLNode(PakNode):
    pass

class VHCLNode(PakNode):
    def read_data(self):
        [dump, next_bin] = self.read_LE(self.data_bin, 'uint16')
        self.version = dump & 0x700F if dump & 0x8000 else 0
        for c in lib.VHCLparam:
            param = c(self.version)
            if param != None:
                [val, next_bin] = self.read_LE(next_bin, param[1])
                setattr(self, param[0], val)

class WAYNode(PakNode):
    pass

class WYOBNode(PakNode):
    pass

class XREFNode(PakNode):
    pass

def main(path):
    pak = PakFile(path)
    return pak.root.child

if __name__ == '__main__':
    print(main(sys.argv[1]))
