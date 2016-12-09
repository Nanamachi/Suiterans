import glob
import sys
from cx_Freeze import setup, Executable

base = 'Win32GUI' if sys.platform == 'win32' else None

options = {
    'optimize' : 2,
    'includes' : ['sip',],
    'build_exe' : 'Suiterans',
    # 'include_files' :\
    #     "D:\\Program Files\\Python\\Lib\\site-packages"\
    #     + "\\PyQt5\\Qt\\plugins\\platforms\\qwindows.dll"
    'include_files' : "locale/",
}

exe = Executable(script = 'Suiterans.py', base = base)

setup(
    name = "Suiterans",
    version = "0.0.2",
    description = "Suiterans---Simutrans pak management Suite",
    executables = [exe],
    options = {'build_exe' : options},
)
