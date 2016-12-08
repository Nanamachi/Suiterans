# -*- coding: utf-8 -*-
import sys
import os
import glob
import codecs
import json

import read_pak

_op = os.path

class PakSuite():

    def __init__(self, path):
        self.path_main = path
        self.path_root, self.name = _op.split(path)
        self.amount = self.get_amount()

    def get_amount(self):
        self.path_addon \
            = _op.join(self.path_root, 'addons', self.name)
        amount \
            = len(glob.glob(self.path_main + '\\*.pak')) \
            + len(glob.glob(self.path_addon + '\\*.pak'))

        return amount

    def load_each(self, pakf_path):
        self.pak.append(read_pak.PakFile(pakf_path))

    def __repr__(self):
        return "<Suiterans PakSuite: " +self.path_main+ ">"

def read_paksuites():
    paksuites = []
    configfs = glob.glob('conf/*.conf')
    for configfn in configfs:
        configf = codecs.open(configfn, 'r', 'utf-8')
        configs = json.load(configf, encoding = 'utf-8')
        paksuites.append(PakSuite(configs['dir']))
        configf.close()

    return paksuites

if __name__ == '__main__':
    pass
