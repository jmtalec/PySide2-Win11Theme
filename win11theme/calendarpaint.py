from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from .accent import get_accent_color
from darkdetect import isDark as checkDark

isDark = checkDark()

if isDark:
    from .dark import *
else:
    from .light import *


r, g, b, hexa = get_accent_color()


class Calendar(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__(self, parent)

        self.setVerticalHeaderFormat(self.NoVerticalHeader)
        self.setHorizontalHeaderFormat(self.ShortDayNames)

        if isDark:
            for d in (QtCore.Qt.Saturday, QtCore.Qt.Sunday):
                fmt = self.weekdayTextFormat(d)
                fmt.setForeground(QtCore.Qt.white)
                self.setWeekdayTextFormat(d, fmt)
        else:
            for d in (QtCore.Qt.Saturday, QtCore.Qt.Sunday):
                fmt = self.weekdayTextFormat(d)
                fmt.setForeground(QtCore.Qt.black)
                self.setWeekdayTextFormat(d, fmt)

    if isDark:
        def paintCell(self, painter, rect, date):
            if date == date.currentDate():
                painter.save()
                painter.fillRect(rect, QtGui.QColor("transparent"))
                painter.setPen(QtCore.Qt.NoPen)
                painter.setBrush(QtGui.QColor(hexa))
                r = QtCore.QRect(QtCore.QPoint(), min(rect.width(), rect.height())*QtCore.QSize(1, 1))
                r.moveCenter(rect.center())
                painter.drawEllipse(r)
                painter.setPen(QtGui.QPen(QtGui.QColor("black")))
                painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))
                painter.restore()
            else:
                month = "{0}-{1}".format(str(self.yearShown()), str(self.monthShown()).zfill(2))
                day = str(date.toPython())
                if day.startswith(month):
                    if date != self.selectedDate(): 
                        painter.setPen(QtGui.QPen(QtGui.QColor("white")))
                        painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))
                    if date == self.selectedDate(): 
                        if date != date.currentDate():
                            painter.setPen(QtCore.Qt.NoPen)
                            painter.setBrush(QtGui.QColor(255, 255, 255, 13))
                            r = QtCore.QRect(QtCore.QPoint(), min(rect.width(), rect.height())*QtCore.QSize(1, 1))
                            r.moveCenter(rect.center())
                            painter.drawEllipse(r)
                            painter.setPen(QtGui.QPen(QtGui.QColor(hexa)))
                            painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))
                else:
                    painter.setPen(QtGui.QPen(QtGui.QColor(150, 150, 150)))
                    painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))
    else:
        def paintCell(self, painter, rect, date):
            if date == date.currentDate():
                painter.save()
                painter.fillRect(rect, QtGui.QColor("transparent"))
                painter.setPen(QtCore.Qt.NoPen)
                painter.setBrush(QtGui.QColor(hexa))
                r = QtCore.QRect(QtCore.QPoint(), min(rect.width(), rect.height())*QtCore.QSize(1, 1))
                r.moveCenter(rect.center())
                painter.drawEllipse(r)
                painter.setPen(QtGui.QPen(QtGui.QColor("white")))
                painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))
                painter.restore()
            else:
                month = "{0}-{1}".format(str(self.yearShown()), str(self.monthShown()).zfill(2))
                day = str(date.toPython())
                if day.startswith(month):
                    if date != self.selectedDate(): 
                        painter.setPen(QtGui.QPen(QtGui.QColor("black")))
                        painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))
                    if date == self.selectedDate(): 
                        if date != date.currentDate():
                            painter.setPen(QtCore.Qt.NoPen)
                            painter.setBrush(QtGui.QColor(0, 0, 0, 13))
                            r = QtCore.QRect(QtCore.QPoint(), min(rect.width(), rect.height())*QtCore.QSize(1, 1))
                            r.moveCenter(rect.center())
                            painter.drawEllipse(r)
                            painter.setPen(QtGui.QPen(QtGui.QColor(hexa)))
                            painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))
                else:
                    painter.setPen(QtGui.QPen(QtGui.QColor(100, 100, 100)))
                    painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))

