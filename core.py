# -*- coding: utf-8 -*-
import sys
import os
import glob
import codecs
import json

import read_pak
from customErr import *
from loginit import *

_op = os.path

class PakSuite():

    def __init__(self, path, name, singleuser):
        self.path_main = path
        self.path_root, self.dirname = _op.split(path)
        self.name = name
        if singleuser:
            self.path_addon = _op.join(
                self.path_root, 'addons', self.dirname
            )
        else:
            self.path_addon = _op.join(
                _op.expanduser('~'),
                'Documents',
                'Simutrans',
                'addons',
                self.dirname
            )
        self.amount = self.get_amount()
        self.size = check_paksuite(self.path_main)

    def get_amount(self):
        amount \
            = len(glob.glob(self.path_main + '\\*.pak')) \
            + len(glob.glob(self.path_addon + '\\*.pak'))

        return amount

    def load_each(self, pakf_path):
        try:
            self.pak.append(read_pak.PakFile(pakf_path))
        except NotPakFileError:
            logger.error(
                'Cannot read %s. Skipping... ',
                _op.basename(pakf_path)
            )

    def __repr__(self):
        return "<Suiterans PakSuite: " +self.path_main+ ">"

def read_paksuites():
    paksuites = []
    configfs = glob.glob('conf/*.conf')
    for configfn in configfs:
        paksuites.append(read_paksuite(configfn))

    return paksuites

def read_paksuite(configfn):
    configf = codecs.open(configfn, 'r', 'utf-8')
    configs = json.load(configf, encoding = 'utf-8')
    configf.close()
    if not 'singleuser' in configs:
        write_paksuite(configs['name'], configs['dir'], True)
        configs['singleuser'] = True
    return PakSuite(configs['dir'], configs['name'], configs['singleuser'])

def write_paksuite(name, path, overwrite = False):
    configfn = _op.join('conf/', name + '.conf')
    if _op.exists(configfn) and not overwrite:
        raise FileExistsError(configfn)
    else:
        path_root, dirname = _op.split(path)

        check_paksuite(path)

        simuconffn = _op.join(path_root, 'config/simuconf.tab')
        simuconff = open(simuconffn)
        for l in simuconff.readlines():
            if l.startswith('singleuser_install'):
                singleuser = bool(l.split('=')[1])
                break
        else:
            singleuser = False
        simuconff.close()

        configf = codecs.open(configfn, 'w', 'utf-8')
        json.dump(
            {'dir':path, 'name':name, 'singleuser':singleuser},
            configf,
            ensure_ascii = False
        )
        configf.close()

    return read_paksuite(configfn)

def delete_paksuite(name):
    configfn = _op.join('conf/', name + '.conf')
    os.remove(configfn)

def check_paksuite(path):
    outsidepath = _op.join(path,'ground.Outside.pak')
    if _op.isfile(outsidepath):
        size = read_pak.PakFile(outsidepath).root.desc(0,2,0,0).width
    else:
        raise NotPakSuiteError(path)

    return size

if __name__ == '__main__':
    pass
