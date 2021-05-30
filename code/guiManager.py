#from PyQt5 import QtWidgets, uic
#from pyqtgraph import PlotWidget, plot

from typing import List
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

import sys
import os

from requests.api import head

#Load the UI Page
form_class = uic.loadUiType('./gui/guiView.ui')[0]

class MainWindow(QMainWindow, form_class):
    app: QApplication
    __data_params = {
        'len': int,
        'coName': List,
        'coCode': List,
    }

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print(self.btnSearch.text())

        self.initProgressBar()

    def initProgressBar(self):
        return 0
        
    def setConfig(self, **kwargs):
        self.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])

        self.confCorpList(kwargs.items())

    def confCorpList(self, items: list):
        for key, value in items:
            self.__data_params[key] = value
            if key == 'coName':
                self.__data_params['len'] = len(value)
        
        self.listCorp.setRowCount(self.__data_params['len'])
        self.listCorp.setColumnCount(2)
        cHeader = self.listCorp.verticalHeader()
        cHeader.setDefaultSectionSize(3)
        cHeader.sectionResizeMode(QHeaderView.Fixed)
        rHeader = self.listCorp.horizontalHeader()
        rHeader.resizeSection(0, 120)
        rHeader.resizeSection(1, 204)

        self.pgBarSearch.setValue(0)
        


    def plot(self, hour ,temperature):
        self.graphWidget.plot(hour, temperature)

    def insert_data(self):

        for i in range(0, self.__data_params['len']):
            self.listCorp.setItem(i, 0, QtWidgets.QTableWidgetItem(self.__data_params['coCode'][i]))
            self.listCorp.setItem(i, 1, QtWidgets.QTableWidgetItem(self.__data_params['coName'][i]))

    def exit(self):
        sys.exit(self.app.exec_())


#if __name__ == '__main__':
#    main()