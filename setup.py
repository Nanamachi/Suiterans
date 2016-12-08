from distutils.core import setup
import py2exe
import glob

options = {
    'compressed' : True,
    'optimize' : 2,
    'bundle_files': 1,
    'includes' : ['sip',],
    'dist_dir' : 'Suiterans',
}
setup(
    windows = ['GUI.py'],
    options = {'py2exe' : options},
    data_files = [("platforms",glob.glob(
        "D:\\Program Files (x86)\\Python\\Lib\\site-packages\\PyQt5\\plugins\\platforms\\qwindows.dll"
    ))]
)
