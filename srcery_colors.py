#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 16:04:40 2020

@author: Oliver C. Sandli

Srcery color theme mappings for PyQt and Matplotlib
"""

from PyQt5.QtGui import QColor


class SrceryColors:
    """A convenience class for accessing the colors of the Srcery theme.
    Credit to https://github.com/srcery-colors
    """

    def __init__(self):
        """init"""
        pass

    class qt:
        """PyQt compatible colors"""

        def _h2t(hv):
            """convert hexadecimal color to 0-1 RGB tuple in a QColor method"""
            hv = hex(hv)[2:]
            r = int(hv[:2], 16)
            g = int(hv[2:4], 16)
            b = int(hv[4:8], 16)
            return QColor(r, g, b)

        # standard colors
        black = _h2t(0x1C1B19)
        red = _h2t(0xEF2F27)
        green = _h2t(0x519F50)
        yellow = _h2t(0xFBB829)
        blue = _h2t(0x2C78BF)
        magenta = _h2t(0xE02C6D)
        cyan = _h2t(0x0AAEB3)
        white = _h2t(0xD0BFA1)
        brightblack = _h2t(0x918175)
        brightred = _h2t(0xF75341)
        brightgreen = _h2t(0x98BC37)
        brightyellow = _h2t(0xFED06E)
        brightblue = _h2t(0x68A8E4)
        brightmagenta = _h2t(0xFF5C8F)
        brightcyan = _h2t(0x53FDE9)
        brightwhite = _h2t(0xFCE8C3)

        # xterm 256 colors
        orange = _h2t(0xFF5F00)
        brightorange = _h2t(0xFF8700)
        hardblack = _h2t(0x121212)
        xgray1 = _h2t(0x262626)
        xgray2 = _h2t(0x303030)
        xgray3 = _h2t(0x3A3A3A)
        xgray4 = _h2t(0x444444)
        xgray5 = _h2t(0x4E4E4E)
        xgray6 = _h2t(0x585858)

    class mpl:
        """Matplotlib compatible colors"""

        def _h2t(hv):
            """convert hexadecimal color to 0-1 RGB tuple"""
            hv = hex(hv)[2:]
            r = int(hv[:2], 16) / 255
            g = int(hv[2:4], 16) / 255
            b = int(hv[4:8], 16) / 255
            return (r, g, b)

        # standard colors
        black = _h2t(0x1C1B19)
        red = _h2t(0xEF2F27)
        green = _h2t(0x519F50)
        yellow = _h2t(0xFBB829)
        blue = _h2t(0x2C78BF)
        magenta = _h2t(0xE02C6D)
        cyan = _h2t(0x0AAEB3)
        white = _h2t(0xD0BFA1)
        brightblack = _h2t(0x918175)
        brightred = _h2t(0xF75341)
        brightgreen = _h2t(0x98BC37)
        brightyellow = _h2t(0xFED06E)
        brightblue = _h2t(0x68A8E4)
        brightmagenta = _h2t(0xFF5C8F)
        brightcyan = _h2t(0x53FDE9)
        brightwhite = _h2t(0xFCE8C3)

        # xterm 256 colors
        orange = _h2t(0xFF5F00)
        brightorange = _h2t(0xFF8700)
        hardblack = _h2t(0x121212)
        xgray1 = _h2t(0x262626)
        xgray2 = _h2t(0x303030)
        xgray3 = _h2t(0x3A3A3A)
        xgray4 = _h2t(0x444444)
        xgray5 = _h2t(0x4E4E4E)
        xgray6 = _h2t(0x585858)
