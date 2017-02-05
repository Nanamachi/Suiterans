# -*- coding: utf-8 -*-
from loginit import *

class FormatError(Exception):
    def __init__(self, fmt):
        self._fmt = fmt
        self.message = "Cannot recognize {} format.".format(self._fmt)

        super().__init__(self.message)

    def __repr__(self):
        return "FormatError: " + self.message

class StreamTooShortError(Exception):
    def __init__(self, rest, fmt):
        self._rest = rest
        self._fmt  = fmt
        self.message =\
            "Stream size {} is too short to read {}."\
            .format(self._rest, self._fmt)

        super().__init__(self.__repr__())

    def __repr__(self):
        return "StreamTooShortError: "\

class StreamTooLongError(Exception):
    def __init__(self, diff, v):
        self._diff = diff
        self._v  = v
        self.message = \
            "Given byte-len doesn't match with known byte-len.\n"\
            + "Maybe the version {} is too new to read.\n"\
            + "Diff to known byte-len is {}"\
            .format(str(self._v), str(self._diff))

        super().__init__(self.__repr__())

    def __repr__(self):
        return "StreamTooLongError: " + self.message

class NotPakSuiteError(Exception):
    def __init__(self, dirname):
        self._dirname = dirname
        self.message = \
            "{} doesn't seem to be a Simutrans pak folder."\
            .format(self._dirname)

        super().__init__(self.__repr__())

    def __repr__(self):
        return "NotPakSuiteError: " + self.message

class NotPakFileError(Exception):
    def __init__(self, filename):
        self._filename = filename
        self.message = \
            "{} is not proper Simutrans pak file."\
            .format(self._filename)

        super().__init__(self.__repr__())

    def __repr__(self):
        return "NotPakFileError: " + self.message

class NodeNotFoundError(Exception):
    def __init__(self, obj, typ):
        self._obj = obj
        self._typ = typ
        self.message = "{} doesn't have {}Node.".format(self._obj, self._typ)

        super().__init__(self.__repr__())

    def __repr__(self):
        return "NodeNotFoundError: " + self.message
