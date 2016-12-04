# -*- coding: utf-8 -*-
import sys
import struct
from PIL import Image

class PakObj():
    def __init__(self, path):
        # http://www.ajisaba.net/python/binary.html
        self._f = open(path, 'rb')
        self._path = path
        self._bin = self._f.read()
    def read_LSB(self, binary, fmt):
        if fmt == 'uint8':
            packfmt = 'B'
            packlen = 1
        elif fmt == 'uint16':
            packfmt = 'H'
            packlen = 2
        elif fmt == 'uint32':
            packfmt = 'I'
            packlen = 4
        else:
            raise

        return [struct.unpack(packfmt, binary[0:packlen]), binary[packlen:]]

def main(path):
    pak = PakObj(path)
    return pak._bin

if __name__ == '__main__':
    print(main(sys.argv[1]))
