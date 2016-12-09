# -*- coding: utf-8 -*-
import sys
import os
import glob
import codecs
import json

import read_pak
from customErr import *

_op = os.path

class PakSuite():

    def __init__(self, path):
        self.path_main = path
        self.path_root, self.name = _op.split(path)
        self.path_addon = _op.join(self.path_root, 'addons', self.name)
        self.amount = self.get_amount()

    def get_amount(self):
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

def write_paksuite(name, path, overwrite = False):
    configfn = os.path.join('conf/', name + '.conf')
    if (os.path.exist(configfn)) and not overwrite:
        raise FileExistsError(configfn)
    else:
        configf = codecs.open(configfn, 'w', 'utf-8')
        json.dump(
            {'dir':path, 'name':name},
            configf,
            ensure_ascii = False
        )

if __name__ == '__main__':
    pass
