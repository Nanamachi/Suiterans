# -*- coding: utf-8 -*-
import read_pak as rpk
import painter as ptr

def spawn(filename):
    return rpk.PakFile(filename).root
