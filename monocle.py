#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:00:47 2020

@author: Oliver C. Sandli

A waveform analysis program.
"""

import sys

from PyQt5.QtWidgets import (
    QApplication, QLabel, QMainWindow, QStatusBar, QToolBar,
    QWidget, QGridLayout, QBoxLayout, QFormLayout, QPushButton,
    QSlider, QFileDialog, QLineEdit
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

import numpy as np
import scipy.io.wavfile
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar
)
from matplotlib.figure import Figure

import srcery_colors


class SuperSlider(QWidget):
    """slider with label and entry box"""

    def __init__(self, label,
                 direction=QBoxLayout.LeftToRight,
                 slider_orientation=Qt.Horizontal,
                 parent=None
                 ):
        """init"""
        QWidget.__init__(self, parent=parent)

        self.label = QLabel(label)
        self.slider = QSlider(slider_orientation)

        self.entry = QLineEdit()
        self.entry.returnPressed.connect(self._link_entry_slider)

        self.slider.valueChanged.connect(self._link_slider_entry)

        layout = QBoxLayout(direction, self)
        layout.addWidget(self.label)
        layout.addWidget(self.entry)
        layout.addWidget(self.slider)

    def slider_connect(self, function):
        """connect a function to the slider"""
        self.slider.valueChanged.connect(function)

    def set_minimum(self, value):
        """set the slider's minimum value"""
        self.slider.setMinimum(value)

    def set_maximum(self, value):
        """set the slider's maximum value"""
        self.slider.setMaximum(value)

    def set_value(self, value):
        """set the slider's and entry box's value"""
        self.slider.setValue(value)
        self.entry.setText(str(value))

    def get_value(self):
        """get the slider's and entry box's value"""
        return self.slider.value()

    def _link_entry_slider(self):
        """send the values of self.entry to self.slider"""
        self.slider.setValue(self._ignore_nonint(self.entry.text()))

    def _link_slider_entry(self):
        """send the values of self.slider to self.entry"""
        self.entry.setText(str(self.slider.value()))

    def _ignore_nonint(self, value):
        """return 0 if value is not convertable to an int; otherwise convert"""
        try:
            return int(value)
        except ValueError:
            return 0


class MainWindow(QMainWindow):
    """the main window"""

    def __init__(self, parent=None):
        """init"""
        super().__init__(parent)

        self.custom_palette_enable = False  # set to True to enable the
                                            # unfinished color palette
        self.file_name = ""

        # set the window title
        self.setWindowTitle("Monocle")

        if self.custom_palette_enable:
            # create a SrceryColors object
            self.srccol = srcery_colors.SrceryColors()

            # set the window colors
            p = self.palette()
            p.setColor(QPalette.Active, QPalette.Window, self.srccol.qt.black)
            p.setColor(QPalette.Active, QPalette.WindowText, self.srccol.qt.white)
            p.setColor(QPalette.Active, QPalette.Base, self.srccol.qt.xgray6)
            p.setColor(QPalette.Active, QPalette.AlternateBase, self.srccol.qt.xgray1)
            p.setColor(QPalette.Active, QPalette.PlaceholderText, self.srccol.qt.white)
            p.setColor(QPalette.Active, QPalette.Text, self.srccol.qt.white)
            p.setColor(QPalette.Active, QPalette.Button, self.srccol.qt.brightblack)
            p.setColor(QPalette.Active, QPalette.ButtonText, self.srccol.qt.white)
            p.setColor(QPalette.Active, QPalette.BrightText, self.srccol.qt.yellow)
            p.setColor(QPalette.Active, QPalette.Highlight, self.srccol.qt.blue)
            self.setPalette(p)

        # plot modifier sliders
        self.x_start_sldr = SuperSlider("X Start")
        self.x_start_sldr.slider_connect(self._plot)

        self.x_end_sldr = SuperSlider("X End")
        self.x_end_sldr.slider_connect(self._plot)

        self.x_pos_sldr = SuperSlider("X Pos")
        self.x_pos_sldr.slider_connect(self._plot)

        # plot size labels
        self.x_range = QLabel("")
        self.y_range = QLabel("")

        # set up the plot
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.fig_toolbar = NavigationToolbar(self.canvas, self)

        # lay out the widgets
        main_layout = QGridLayout()

        main_layout.addWidget(self.fig_toolbar, 0, 0)
        main_layout.addWidget(self.canvas, 1, 0)

        main_layout.addWidget(self.x_range, 2, 0)
        main_layout.addWidget(self.y_range, 3, 0)

        main_layout.addWidget(self.x_start_sldr, 4, 0)
        main_layout.addWidget(self.x_end_sldr, 5, 0)
        main_layout.addWidget(self.x_pos_sldr, 6, 0)

        window = QWidget()
        window.setLayout(main_layout)
        self.setCentralWidget(window)

        self._create_menu()
        # self._create_toolbar()
        self._create_status_bar()

    def _create_menu(self):
        """create the menu bar"""
        self.file_menu = self.menuBar().addMenu("&File")
        self.file_menu.addAction("&Open", self._open_file)
        self.file_menu.addAction("&Exit", self.close)

    def _create_toolbar(self):
        """create the toolbar"""
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction("Exit", self.close)

    def _create_status_bar(self):
        """create the status bar"""
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.statusbar.showMessage("Program Startup")

    def _open_file(self):
        """an open file dialog"""
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.file_name = dialog.selectedFiles()[0]
            self._init_plot()

    def _init_plot(self):
        """read data into the plot"""
        rate, self.data = scipy.io.wavfile.read(self.file_name)
        if len(self.data.shape) != 1:
            self.data = self.data[:,0]

        self.x_start_sldr.set_minimum(0)
        self.x_start_sldr.set_maximum(self.data.size)
        self.x_start_sldr.set_value(0)

        self.x_end_sldr.set_minimum(0)
        self.x_end_sldr.set_maximum(self.data.size)
        self.x_end_sldr.set_value(self.data.size)

        self.x_pos_sldr.set_minimum(0)
        self.x_pos_sldr.set_maximum(self.data.size - self.x_end_sldr.get_value())
        self.x_pos_sldr.set_value(0)



        self._plot()
        self.statusbar.showMessage(f"Loaded {self.file_name} @ {rate} Hz")

    def _plot(self):
        """plot random data"""
        if self.file_name != "":
            self.ax.clear()
            if self.custom_palette_enable:
                self.ax.plot(self.data, color=self.srccol.mpl.magenta)
            else:
                self.ax.plot(self.data)

            x_min = self.x_start_sldr.get_value() + self.x_pos_sldr.get_value()
            x_max = self.x_end_sldr.get_value() + self.x_pos_sldr.get_value()
            y_min = self.data.min() + self.data.min() * 0.1
            y_max = self.data.max() + self.data.max() * 0.1

            self.ax.axis([x_min, x_max, y_min, y_max])
            self.canvas.draw()

            self.x_pos_sldr.set_maximum(self.data.size - self.x_end_sldr.get_value())

            self.x_range.setText(f"x=({x_min}, {x_max})")
            self.y_range.setText(f"y=({y_min}, {y_max})")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Windows")
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
