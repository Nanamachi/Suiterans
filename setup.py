import glob
import sys
from cx_Freeze import setup, Executable

import lib

base = 'Win32GUI' if sys.platform == 'win32' else None

options = {
    'optimize' : 2,
    'includes' : [
        'sip',
        'PyQt5'
    ],
    'build_exe' : 'Suiterans',
    'include_files' : ["locale/", "resources/"],
}

exe = Executable(
    script = 'Suiterans.py',
    base = base,
    icon = 'resources/Suiterans.ico'
)

setup(
    name = "Suiterans",
    version = lib.VERSION,
    description = "Suiterans---Simutrans pak management Suite",
    executables = [exe],
    options = {'build_exe' : options},
)
