#!env python
import sys
import struct
from PIL import Image

class PakObj():

    def __init__(self, path):
        self._f = open(path, 'rb')
        self._path = path
        self._read()

    def _read(self):
        # http://www.ajisaba.net/python/binary.html
        self._bin = self._f.read()

if __name__ == '__main__':
    pak = PakObj(sys.argv[1])
