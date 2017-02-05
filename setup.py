import glob
import sys
from cx_Freeze import setup, Executable

import lib

base = 'Win32GUI' if sys.platform == 'win32' else None

options = {
    'optimize' : 2,
    'includes' : ['sip',],
    'build_exe' : 'Suiterans',
    'include_files' : "locale/",
}

exe = Executable(script = 'Suiterans.py', base = base)

setup(
    name = "Suiterans",
    version = lib.VERSION,
    description = "Suiterans---Simutrans pak management Suite",
    executables = [exe],
    options = {'build_exe' : options},
)
