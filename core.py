# -*- coding: utf-8 -*-
import sys
import os
import glob
import codecs
import json
from collections import OrderedDict

import read_pak
from customErr import *
from loginit import *

_op = os.path

class PakSuite():

    def __init__(self, **configs):
        self.path_main = configs['dir']
        self.path_root, self.dirname = _op.split(configs['dir'])
        self.name = configs['name']
        if configs['singleuser']:
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

class SimplePakSuite(PakSuite):
    def __init__(self, pakf_path):
        self.amount = 1
        self.pak = []
        self.load_each(pakf_path)
        self.size = 0

    def get_amount(self):
        return 1

class PakSuiteManager():

    def __init__(self):
        self._paksuites = OrderedDict()
        configfs = glob.glob(_op.join(sys.path[0], 'conf/*.conf'))
        for configfn in configfs:
            self.addPakSuite(configfn)

        return None

    def addPakSuite(self, configfn):
        configf = codecs.open(configfn, 'r', 'utf-8')
        configs = json.load(configf, encoding = 'utf-8')
        configf.close()
        ps = PakSuite(**configs)
        if not self.isPakSuiteValid(ps):
            raise NotPakSuiteError(ps.path_main)
        else:
            ps.size = self.isPakSuiteValid(ps, getsize = True)
            self._paksuites[ps.name] = ps

        return None

    def addNewPakSuite(self, name, path, overwrite = False):
        configfn = _op.join(sys.path[0], 'conf/', name + '.conf')
        if _op.exists(configfn) and not overwrite:
            raise FileExistsError(configfn)

        path_root, dirname = _op.split(path)

        simuconffn = _op.join(path_root, 'config/simuconf.tab')
        try:
            simuconff = open(simuconffn)
        except FileNotFoundError:
            raise NotPakSuiteError(path)

        for l in simuconff.readlines():
            if l.startswith('singleuser_install'):
                singleuser = bool(l.split('=')[1])
                break
            else:
                singleuser = False
                simuconff.close()

        configs = {'dir':path, 'name':name, 'singleuser':singleuser}
        ps = PakSuite(**configs)

        if not self.isPakSuiteValid(ps):
            raise NotPakSuiteError(path)

        configf = codecs.open(configfn, 'w', 'utf-8')
        json.dump(
            configs,
            configf,
            ensure_ascii = False
        )
        configf.close()

        self.addPakSuite(configfn)

        return None

    def removePakSuite(self, name):
        configfn = _op.join(sys.path[0], 'conf/', name + '.conf')
        os.remove(configfn)
        del self.paksuites[name]

    def isPakSuiteValid(self, arg, getsize = False):
        if isinstance(arg, str):
            outsidepath = _op.join(
                self._paksuites[arg].path_main,
                'ground.Outside.pak'
            )
        elif isinstance(arg, PakSuite):
            outsidepath = _op.join(
                arg.path_main,
                'ground.Outside.pak'
            )
        else:
            raise TypeError('isPakSuiteValid needs str or PakSuite. Not {}'
                .format(type(arg)))

        ret = False
        if _op.isfile(outsidepath):
            try:
                size = read_pak.PakFile(outsidepath).root.desc(0,2,0,0).width
            except Exception as e:
                pass
            else:
                if getsize:
                    ret = size
                else:
                    ret = True
        else:
            logger.debug(outsidepath)

        return ret

if __name__ == '__main__':
    pass
