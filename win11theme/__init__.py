


from PySide2.QtGui import QColor
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QDialog

from .qframelesswindow import StandardTitleBar, AcrylicWindow, FramelessWindow

from .calendarpaint import Calendar

from darkdetect import isDark as checkDark

from .accent import get_accent_color

import sys

__all__ = ['Calendar', 'DARK', 'DEFAULT', 'FX_ACRYLIC', 'FX_AERO', 'FX_MICA', 'FX_NONE', 'LIGHT', 'Win11Layout', 'Win11FXWindow', 'isDark']

isDark = checkDark()

LIGHT = 'light'
DARK = 'dark'
DEFAULT = 'default'
FX_MICA = 'fx_mica'
FX_AERO = 'fx_aero'
FX_ACRYLIC = 'fx_acylic'
FX_NONE = 'none'



if sys.platform != 'win32':
    raise SystemExit(f'Bad platform: {sys.platform}!')

if isDark:
    from .dark import Win11Layout

else:
    from .light import Win11Layout

r, g, b, hexa  = get_accent_color()
accent = f'rgb({r}, {g}, {b})'



class _DarkTitleBar(StandardTitleBar):
    """ Dark Custom title bar """

    def __init__(self, parent):
        super().__init__(parent)

        # use qss to customize title bar button
        self.minBtn.setNormalColor(QColor(200, 200, 200, 200))
        self.minBtn.setNormalBackgroundColor(Qt.transparent)
        self.minBtn.setHoverColor(QColor(200, 200, 200, 200))
        self.minBtn.setHoverBackgroundColor(QColor(r, g, b, 50))
        self.minBtn.setPressedColor(Qt.white)
        self.minBtn.setPressedBackgroundColor(QColor(54, 57, 65))

        self.maxBtn.setNormalColor(QColor(200, 200, 200, 200))
        self.maxBtn.setNormalBackgroundColor(Qt.transparent)
        self.maxBtn.setHoverColor(QColor(200, 200, 200, 200))
        self.maxBtn.setHoverBackgroundColor(QColor(r, g, b, 50))
        self.maxBtn.setPressedColor(Qt.white)
        self.maxBtn.setPressedBackgroundColor(QColor(54, 57, 65))

        self.closeBtn.setNormalColor(QColor(200, 200, 200, 200))
        self.closeBtn.setNormalBackgroundColor(Qt.transparent)
        self.closeBtn.setHoverColor(Qt.white)
        self.closeBtn.setHoverBackgroundColor(QColor(180, 50, 50, 255))
        self.closeBtn.setPressedColor(Qt.white)
        self.closeBtn.setPressedBackgroundColor(QColor(200, 50, 50, 255))

class _LightTitleBar(StandardTitleBar):
    """ Light Custom title bar """

    def __init__(self, parent):
        super().__init__(parent)

        # use qss to customize title bar button
        self.minBtn.setNormalColor(QColor(20, 20, 20, 250))
        self.minBtn.setNormalBackgroundColor(Qt.transparent)
        self.minBtn.setHoverColor(QColor(100, 100, 100, 200))
        self.minBtn.setHoverBackgroundColor(QColor(r, g, b, 50))
        self.minBtn.setPressedColor(Qt.white)
        self.minBtn.setPressedBackgroundColor(QColor(54, 57, 65))

        self.maxBtn.setNormalColor(QColor(20, 20, 20, 250))
        self.maxBtn.setNormalBackgroundColor(Qt.transparent)
        self.maxBtn.setHoverColor(QColor(100, 100, 100, 200))
        self.maxBtn.setHoverBackgroundColor(QColor(r, g, b, 50))
        self.maxBtn.setPressedColor(Qt.white)
        self.maxBtn.setPressedBackgroundColor(QColor(54, 57, 65))

        self.closeBtn.setNormalColor(QColor(20, 20, 20, 250))
        self.closeBtn.setNormalBackgroundColor(Qt.transparent)
        self.closeBtn.setHoverColor(Qt.white)
        self.closeBtn.setHoverBackgroundColor(QColor(180, 50, 50, 255))
        self.closeBtn.setPressedColor(Qt.white)
        self.closeBtn.setPressedBackgroundColor(QColor(200, 50, 50, 255))

class Win11FXWindow(AcrylicWindow):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent)
        self.default_kwargs = {'fx' : FX_MICA,
                          'win11': True,
                          'default_bar': DEFAULT,
                          }
        self.kwcommands = {'fx' : lambda fx: self._setFx(fx),
                           'win11': lambda b: self._setWin11Layout() if b else None,
                           'default_bar' : lambda b: self._setDefaultTitleBar() if b == DEFAULT else self.setCustomTitleBar(b)}

        self.kwargs = {**self.default_kwargs, **kwargs}

        for key in list(self.kwargs.keys()):
            self.kwcommands[key](self.kwargs[key])
    
    def __setitem__(self, key, value):
        self.kwargs[key] = value
        self.kwcommands[key](value)

    def __getitem__(self, key):
        return self.kwargs[key]

    def __str__(self):
        return f"win11Window(FX: {self['fx']}, MODE: {DARK if isDark else LIGHT})"

    def __repr__(self):
        return self.__str__()

    def setCustomTitleBar(self, value):
        if value == DARK:
            bar = _DarkTitleBar(self)
        elif value == LIGHT:
            bar = _LightTitleBar(self)
        else:
            raise ValueError(f'No title bar named {value}')
        self.setTitleBar(bar)

    def _setDefaultTitleBar(self):
        if isDark:
            bar = _DarkTitleBar(self)
        else:
            bar = _LightTitleBar(self)
        self.setTitleBar(bar)

    def _setWin11Layout(self):
        Win11Layout(self)

    def _setFx(self, fx):
        id = self.winId()
        self.windowEffect.removeBackgroundEffect(id)
        if fx == FX_AERO:
            self.windowEffect.setAeroEffect(id)
        elif fx == FX_ACRYLIC:
            self.windowEffect.setAcrylicEffect(id, gradientColor="2F2F2FBB" if isDark else "F2F2F2BB")
        elif fx == FX_MICA:
            self.windowEffect.setMicaEffect(id, isDark)
        elif fx == FX_NONE:
            self.windowEffect.removeBackgroundEffect(id)
        else:
            raise ValueError(f"No fx found: {fx}")



