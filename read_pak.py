# -*- coding: utf-8 -*-
from common_import import *

import lib
from customErr import *
from loginit import *

class PakFile(): #read .pak and extract into PakNode instance
    def __init__(self, path):
        try:
            # http://www.ajisaba.net/python/binary.html
            _fp = open(path, 'rb')
            self.path = path
            self.name = os.path.basename(path)

            for i in range(os.path.getsize(path)):
                b = _fp.read(4)
                _fp.seek(-4,1)
                if b == b'ROOT':
                    break
                else:
                    _fp.seek(1,1)
            else:
                raise NotPakFileError(self.name)

            self.root = ROOTNode(_fp, self)

            _fp.close()
        except Exception as e:
            logger.error('Cannot spawn %s.', self.name)
            logger.exception(e)
            raise

    def __repr__ (self):
        return "<Simutrans Pak File '{}'>".format(self.name)

class PakNode():
    def __init__(self, fp, parent = None): #read data from binary and spawn child Nodes

        [self.type, self.child_count, self.data_len,] \
            = self.read_header(fp)
        self.remain_len = self.data_len
        self.pos = fp.tell()

        self.parent = parent
        if isinstance(parent, PakFile):
            self.pakfile = parent
        elif isinstance(parent, PakNode):
            self.pakfile = parent.pakfile
        else:
            logger.warning('{}Node has invalid parent.'.format(self.type))

        try:
            self.read_data(fp)
        except StreamTooLongError:
            logger.error(
                '{} is too long to read.\n'
                .format(self.__repr__())
                + 'This occured while reading {}.\n'
                .format(self.pakfile)
                + 'Skipping surplus bytes...'
            )
            fp.seek(self.remain_len, 1)

        self.child = []
        for i in range(self.child_count):
            child_type = fp.read(4).decode()
            if child_type[3] == '\0':
                child_type = child_type[0:3]

            child_class = globals()[child_type + 'Node']
            fp.seek(-4, 1) #back 4chars from here

            self.child.append(child_class(fp, parent = self))

        #set name and author from child TEXTNode
        if self.type in lib.named_obj:
            nameNode = self.searchNode('TEXT', pos = 0)
            if isinstance(nameNode, TEXTNode):
                s = nameNode.text if nameNode.text != ''\
                    else '__UnDefined__'
            else:
                s = '__UnDefined__'
            self.name = s

            authorNode = self.searchNode('TEXT', pos = 1)
            if isinstance(authorNode, TEXTNode):
                s = authorNode.text if authorNode.text != ''\
                    else '__UnDefined__'
            else:
                s = '__UnDefined__'
            self.author = s

        elif self.type == 'FACT':
            self.name   = self.searchNode('BUIL').name
            self.author = self.searchNode('BUIL').author

        curs = self.searchNode('CURS')
        if curs != None:
            self.icon = curs.desc(2,1)

        return None

    def __repr__(self):
        if hasattr(self, 'name'):
            return "<Simutrans {0}: {1}>".format(self.type, self.name)
        elif hasattr(self, 'text'):
            return "<Simutrans {0}: {1}>".format(self.type, self.text)
        elif hasattr(self, 'xref'):
            return "<Simutrans {0}: {1}>".format(self.type, self.xref)
        else:
            return "<Simutrans {} Node>".format(self.type)

    def read_LE(self, fp, fmt, rest): #read Little Endian format
        if fmt == 'uint8':
            packfmt = '<B'
            packlen = 1
        elif fmt == 'sint8':
            packfmt = '<b'
            packlen = 1
        elif fmt == 'uint16':
            packfmt = '<H'
            packlen = 2
        elif fmt == 'sint16':
            packfmt = '<h'
            packlen = 2
        elif fmt == 'uint32':
            packfmt = '<I'
            packlen = 4
        elif fmt == 'sint32':
            packfmt = '<i'
            packlen = 4
        elif fmt[0:4] == 'ufix':
            #unsigned fixed point
            #ex.) 'ufix0816' means '0xAB.CD'
            #this func return the value multiplied 100 'cause
            #ufix format usually used percent format.
            packlen = int(fmt[6:8]) >> 3
            shamt = int(fmt[4:6])
            if packlen == 1:
                packfmt = '<B'
            elif packlen == 2:
                packfmt = '<H'
            elif packlen == 4:
                packfmt = '<I'
        else:
            raise FormatError(fmt)

        if rest - packlen < 0:
            raise StreamTooShortError(rest,fmt)

        ret = struct.unpack(packfmt, fp.read(packlen))[0]
        if fmt[0:4] == 'ufix':
            ret = (ret * 100) >> shamt

        return [ret, rest - packlen]

    def read_header(self, fp): #read binary and return headerdata
        typ = fp.read(4).decode()
        if typ[3] == '\0' : #if last char is null (occur in IMG and WAY)
            typ = typ[:3]
        [child_count, _] = self.read_LE(fp, 'uint16', 2)
        [data_len, _] = self.read_LE(fp, 'uint16', 2)
        return [
            typ,
            child_count,
            data_len,
        ]

    def set_intro(self, v_th):
        if hasattr(self, 'intro'):
            if self.version > v_th:
                self.intro_year  = int(self.intro / 12)
                self.intro_month = int(self.intro % 12) + 1
            else:
                self.intro_year  = int(self.intro / 16)
                self.intro_month = int(self.intro % 16) + 1

        return None

    def set_retire(self, v_th):
        if hasattr(self, 'retire'):
            if self.version > v_th:
                self.retire_year  = int(self.retire / 12)
                self.retire_month = int(self.retire % 12) + 1
            else:
                self.retire_year  = int(self.retire / 16)
                self.retire_month = int(self.retire % 16) + 1

        return None

    def read_data(self, fp): #read own data with list defined by lib.py

        #get version
        [dump, self.remain_len] = self.read_LE(fp, 'uint16', self.remain_len)
        self.version = dump & 0x00FF if dump & 0x8000 else 0
        self.experimental = True if dump & 0x4000 else False
        if self.version == 0:
            fp.seek(-2, 1)
            self.remain_len += 2

        #read self param
        for c in getattr(lib, self.type + 'param'):
            param = c(self.version)
            if param != None:
                [val, self.remain_len] = self.read_LE(fp, param[1], self.remain_len)
                if  (param[0] == 'sound')\
                    and (val == -2)\
                    and (self.type == 'CRSS'):
                    [sfile_len, self.remain_len] \
                        = self.read_LE(fp, 'sint8', self.remain_len)
                    self.wav = fp.read(sfile_len).decode()
                    self.remain_len -= sfile_len
                setattr(self, param[0], param[2](val))
        if self.type == 'VHCL' and getattr(self, 'sound', None) == -2:
            [sfile_len, self.remain_len] \
                = self.read_LE(fp, 'sint8', self.remain_len)
            self.wav = fp.read(sfile_len)
            self.remain_len -= sfile_len

        if self.remain_len != 0:
            raise StreamTooLongError(self.remain_len, self.version)

        return None

    def show_tree(self, *number):
        for n in number:
            print(n, end = ' ')
        print(self)
        for i,c in enumerate(self.child):
            c.show_tree(*number, i)

        return None

    def desc(self, *number):
        if len(number) == 0:
            return self
        else:
            try:
                ret = self.child[number[0]].desc(*number[1:])
            except IndexError:
                ret = None
                logger.warning(
                    "{} has no desc {}. \n"
                    .format(self.__repr__(), number)
                    + "{} contains this node."
                    .format(self.pakfile.name)
                )
            return ret

    def searchNode(self, typ, pos = 0):

        def searchChild(obj, typ, pos):

            for c in obj.child:
                if c.type == typ and pos == 0:
                    ret = c
                    break
                elif c.type == typ:
                    pos -= 1
                elif c.child_count != 0:
                    pos = searchChild(c, typ, pos)
                    if type(pos) != int:
                        ret = pos
                        break
            else:
                ret = pos

            return ret

        r = searchChild(self, typ, pos)

        if type(r) == int:
            r = None

        return r

class BRDGNode(PakNode):
    def read_data(self, fp):
        super().read_data(fp)

        self.set_intro(4)
        self.set_retire(4)

class BUILNode(PakNode):
    def read_data(self, fp):
        super().read_data(fp)

        self.set_intro(1)
        self.set_retire(1)

class CCARNode(PakNode):
    def read_data(self, fp):
        super().read_data(fp)

        self.set_intro(1)
        self.set_retire(1)

class CRSSNode(PakNode):
    def read_data(self, fp):
        super().read_data(fp)

        self.set_intro(1)
        self.set_retire(1)

class CURSNode(PakNode):
    def read_data(self, fp):
        pass

class FACTNode(PakNode):
    pass

class FFIENode(PakNode):
    pass

class FFCLNode(PakNode):
    pass

class FIELNode(PakNode):
    def read_data(self, fp):
        pass

class FPRONode(PakNode):
    pass

class FSMONode(PakNode):
    pass

class FSUPNode(PakNode):
    pass

class GOODNode(PakNode):
    pass

class GRNDNode(PakNode):
    def read_data(self, fp):
        pass

class GOBJNode(PakNode):
    pass

class IMGNode(PakNode):

    def read_data(self, fp):
        fp.seek(6,1)
        [self.version, _] = self.read_LE(fp, 'uint8', self.remain_len)
        fp.seek(-7,1)
        for c in getattr(lib, 'IMGparam'):
            param = c(self.version)
            if param != None:
                [val, self.remain_len] = self.read_LE(fp, param[1], self.remain_len)
                setattr(self, param[0], param[2](val))

        if self.version == 3:
            self.length = int(self.remain_len / 2)

        self.img = fp.read(self.length * 2)
        self.remain_len -= self.length * 2

        if self.remain_len != 0:
            raise StreamTooLongError(self.remain_len, self.version)

        return None

class IMG1Node(PakNode):
    def read_data(self, fp):
        self.version = 0

        for c in getattr(lib, self.type + 'param'):
            param = c(self.version)
            if param != None:
                [val, self.remain_len] = self.read_LE(fp, param[1], self.remain_len)
                setattr(self, param[0], param[2](val))

        if self.remain_len != 0:
            raise StreamTooLongError(self.remain_len, self.version)

class IMG2Node(PakNode):
    def read_data(self, fp):
        self.version = 0

        for c in getattr(lib, self.type + 'param'):
            param = c(self.version)
            if param != None:
                [val, self.remain_len] = self.read_LE(fp, param[1], self.remain_len)
                setattr(self, param[0], param[2](val))

        if self.remain_len != 0:
            raise StreamTooLongError(self.remain_len, self.version)

class MENUNode(PakNode):
    def read_data(self, fp):
        pass

class MISCNode(PakNode):
    def read_data(self, fp):
        pass

class PASSNode(PakNode):
    pass

class SIGNNode(PakNode):
    def read_data(self, fp):
        super().read_data(fp)

        self.set_intro(2)
        self.set_retire(2)

class ROOTNode(PakNode):
    def read_data(self, fp):
        pass

class SMOKNode(PakNode):
    def read_data(self, fp):
        pass

class SOUNNode(PakNode):
    def read_data(self, fp):
        pass

class SYMBNode(PakNode):
    def read_data(self, fp):
        pass

class TEXTNode(PakNode):
    def read_data(self, fp):
        self.text = fp.read(self.remain_len).decode('sjis', errors = 'ignore')[:-1]

class TILENode(PakNode):
    pass

class TREENode(PakNode):
    pass

class TUNLNode(PakNode):
    def read_data(self, fp):
        super().read_data(fp)

        self.set_intro(0)
        self.set_retire(0)

class VHCLNode(PakNode):
    def read_data(self, fp):
        super().read_data(fp)

        self.set_intro(4)
        self.set_retire(4)

class WAYNode(PakNode):
    def read_data(self, fp):
        super().read_data(fp)

        self.set_intro(1)
        self.set_retire(1)

class WYOBNode(PakNode):
    def read_data(self, fp):
        super().read_data(fp)

        self.set_intro(0)
        self.set_retire(0)

class XREFNode(PakNode):
    def read_data(self, fp):
        self.xref = fp.read(self.remain_len).decode('sjis', errors = 'ignore')

def main(path):
    pak = PakFile(path)
    return pak.root.child

if __name__ == '__main__':
    pass
