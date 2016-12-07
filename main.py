# -*- coding: utf-8 -*-
import sys
import os
import glob
import codecs
import json
import pdb

import GUI
import read_pak

class PakSuite():
    def __init__(self,path):
        _op = os.path
        self.path_main = path
        self.path_root, self.pakset_name = _op.split(path)
        self.path_addon \
        = _op.join(self.path_root, 'addons', self.pakset_name)
        self.pak = []
        for fname in glob.glob(self.path_main + '\\*.pak'):
            self.pak.append(read_pak.PakFile(fname))
        for fname in glob.glob(self.path_addon + '\\*.pak'):
            self.pak.append(read_pak.PakFile(fname))

    def __repr__(self):
        return "<Suiterans PakSuite: " +self.path_main+ ">"

def read_paksuites():
    paksuites = []
    configfs = glob.glob('conf/*.conf')
    for configfn in configfs:
        configf = codecs.open(configfn, 'r', 'utf-8')
        confs = json.load(configf, encoding = 'utf-8')
        paksuites.append(PakSuite(confs['dir']))
        configf.close()

    return paksuites

if __name__ == '__main__':
    pass
