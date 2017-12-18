# -*- coding: utf-8 -*-
from common_import import *

import read_pak
import lib
from customErr import *
from loginit import *

_op = os.path

class PakSuite():

    def __init__(self, **configs):
        for confn in configs:
            setattr(self, confn, configs[confn])
        self.path_root, self.dirname = _op.split(configs['path_main'])
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

    def getSize(self, force = False):
        if not hasattr(self, 'size') or force:
            outsidepath = _op.join(
                self.path_main,
                'ground.Outside.pak'
            )
            ret = read_pak.PakFile(outsidepath).root.desc(0,2,0,0).width
            self.size = ret
        return self.size

    def isValid(self):
        outsidepath = _op.join(
            self.path_main,
            'ground.Outside.pak'
        )

        ret = False
        if _op.isfile(outsidepath):
            try:
                size = read_pak.PakFile(outsidepath).root.desc(0,2,0,0).width
            except Exception as e:
                pass
            else:
                ret = True

        return ret

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
        self._paksuites = {}
        configfs = glob.glob(_op.join(sys.path[0], 'conf/*.conf'))
        for configfn in configfs:
            self.loadPakSuite(configfn)

        return None

    def loadPakSuite(self, configfn):
        configf = codecs.open(configfn, 'r', 'utf-8')
        configs = json.load(configf, encoding = 'utf-8')
        configf.close()
        ps = PakSuite(**configs)
        if not ps.isValid():
            raise NotPakSuiteError(ps.path_main)
        else:
            ps.getSize()

        self.refreshPakSuite(ps)

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
        self._writePakSuiteConf(
            path_main = path,
            name = name,
            singleuser = singleuser,
            isHalfSlope = None
        )
        self.loadPakSuite(configfn)

        return None

    def setPakSuiteConf(self, name, **configs):
        configs['name'] = name
        self._writePakSuiteConf(**configs)
        ps = self._paksuites[name]
        for key in configs:
            setattr(ps, key, configs[key])
        self.refreshPakSuite(ps)

    def refreshPakSuite(self, ps):
        self._paksuites[ps.name] = ps

    def _writePakSuiteConf(self, **configs):
        configfn = _op.join(sys.path[0], 'conf/', configs['name'] + '.conf')

        if configs['name'] not in self._paksuites:
            ps = PakSuite(**configs)

            if not ps.isValid():
                del ps
                raise NotPakSuiteError(configs['path_main'])

        else:
            ps = self._paksuites[configs['name']]
            for s in lib.paksuite_param:
                if s in configs:
                    setattr(self._paksuites[configs['name']], s, configs[s])
                else:
                    configs[s] = getattr(self._paksuites[configs['name']], s)

        configf = codecs.open(configfn, 'w', 'utf-8')
        json.dump(
            configs,
            configf,
            ensure_ascii = False
        )
        configf.close()

        return None

    def removePakSuite(self, name):
        configfn = _op.join(sys.path[0], 'conf/', name + '.conf')
        os.remove(configfn)
        del self.paksuites[name]

if __name__ == '__main__':
    pass
