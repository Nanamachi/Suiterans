# -*- coding: utf-8 -*-
import sys
import struct
from PIL import Image

class PakFile():
    def __init__(self, path):
    # http://www.ajisaba.net/python/binary.html
        self._f = open(path, 'rb')
        self._path = path
        self._bin = self._f.read()
        self.root = PakNode(self._bin[61:])

class PakNode():
    def __init__(self, binary): #read .pak and extract into _bin
        [
            self.type,
            self.child_count,
            self.data_len,
            self.data_bin,
            self.child_bin,
        ] = self.read_header(binary)

    def read_LE(self, binary, fmt):
        if fmt == 'uint8':
            packfmt = '<B'
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

    def read_header(self, binary):
        typ = binary[0:4]
        [child_count, _] = self.read_LE(binary[4:6], 'uint16')
        [data_len, _] = self.read_LE(binary[6:8], 'uint16')
        data_bin = binary[8:8 + data_len]
        child_bin = binary[8 + data_len:]
        return [typ, child_count, data_len, data_bin, child_bin]

def main(path):
    pak = PakNode(path)
    return pak._bin

if __name__ == '__main__':
    print(main(sys.argv[1]))
