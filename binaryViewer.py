# -*- coding: utf-8 -*-
import read_pak as rpk
import binascii

class ReadableBinary():
    def __init__(self, paknode):
        if not isinstance(paknode, rpk.PakNode):
            raise TypeError(
                "{} is not PakNode. ReadableBinary can't accept it."\
                .format(type(paknode))
            )
        self._node = paknode

    def bin(self):
        fp = open(self._node.pakfile.path, mode = 'rb')
        fp.seek(self._node.pos)
        ret = ""

        for i in range(self._node.data_len):
            b = fp.read(1)
            ret += b.hex().upper() + " "
            if i%16 == 15:
                ret += "\n"

        fp.close

        return ret

    def __repr__(self):
        return "<Readble Binary: {} in {}>".format(
            self._node,
            self._node.pakfile
        )
