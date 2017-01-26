# -*- coding: utf-8 -*-

class FormatError(Exception):
    def __init__(self, fmt):
        self._fmt = fmt

    def __repr__(self):
        return "FormatError: Cannot recognize " + self._fmt + " format."

class StreamTooShortError(Exception):
    def __init__(self, rest, fmt):
        self._rest = rest
        self._fmt  = fmt

    def __repr__(self):
        return "StreamTooShortError: "\
            + "Stream size " + str(rest) + " is too short to read " + fmt

class StreamTooLongError(Exception):
    def __init__(self, diff, v):
        self._diff = diff
        self._v  = v

    def __repr__(self):
        return "StreamTooLongError: "\
            + "Given byte-len doesn't match with known byte-len."\
            + "Maybe the version " + str(self._v) + " is too new to read."\
            + "Diff to known byte-len is " + str(self._diff)

class NotPakSuiteError(Exception):
    def __init__(self, dirname):
        self._dirname = dirname

    def __repr__(self):
        return "NotPakSuiteError: "\
        + dirname + " doesn't seem to be a Simutrans pak folder."

class NodeNotFoundError(Exception):
    def __init__(self, obj, typ):
        self._obj = obj
        self._typ = typ

    def __repr__(self):
        return "NodeNotFoundError: "\
        + str(self._obj) + " doesn't have " + self._typ + 'Node.'
