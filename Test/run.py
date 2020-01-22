# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import pyqtgraph as pg
from _UI.Main import Ui_MainWindow
import numpy as np


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        
        #pg.setConfigOption('background', '#f0f0f0')  # 设置背景为灰色
        #pg.setConfigOption('foreground', 'w')  # 设置前景（包括坐标轴，线条，文本等等）为黑色。

        #pg.setConfigOptions(antialias=True) # 使曲线看起来更光滑，而不是锯齿状
        # pg.setConfigOption('antialias',True) # 等价于上一句，所不同之处在于setconfigOptions可以传递多个参数进行多个设置，而setConfigOption一次只能接受一个参数进行一个设置。
        self.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
