# -*- coding: utf-8 -*-
import sys
import os
import glob
import codecs
import json

import GUI
import read_pak

class PakSuite():
    def __init__(self,path):
        _op = os.path
        self.path_main = path
        self.path_root, self.pakset = _op.split(path)
        self.path_addon \
        = _op.join(self.path_root, 'addons', self.pakset)
        self.pak = []
        for fname in glob.glob(self.path_main + '\\*.pak'):
            print(fname)
            self.pak.append(read_pak.PakFile(fname))

def main():
    config = codecs.open('conf/pak.conf', 'r', 'utf-8')
    confs = json.load(config, encoding = 'utf-8')
    ps = PakSuite(confs['dir'])

if __name__ == '__main__':
    main()
