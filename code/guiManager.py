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

class MainWindow(QtWidgets.QMainWindow):
    app: QApplication
    __data_params = {
        'len': int,
        'coName': List,
        'coCode': List,
    }

    def __init__(self, *args, **kwargs):
        self.app = QtWidgets.QApplication(sys.argv)
        super(MainWindow, self).__init__(*args, **kwargs)
        
    def setConfig(self, **kwargs):
        for key, value in kwargs.items():
            self.__data_params[key] = value
            if key == 'coName':
                self.__data_params['len'] = len(value)

        #Load the UI Page
        uic.loadUi('./gui/midtest.ui', self)

        self.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])
        
        self.set_table_header()
        self.tableWidget.setRowCount(self.__data_params['len'])
        self.tableWidget.setColumnCount(2)
        header = self.tableWidget.verticalHeader()
        header.setDefaultSectionSize(3)
        header.sectionResizeMode(QHeaderView.Fixed)


    def plot(self, hour ,temperature):
        self.graphWidget.plot(hour, temperature)

    def insert_data(self):

        for i in range(0, self.__data_params['len']):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(self.__data_params['coCode'][i]))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(self.__data_params['coName'][i]))

    def set_table_header(self):
        self.tableWidget.setHorizontalHeaderLabels(["종목코드", "종목명"])

    def exit(self):
        sys.exit(self.app.exec_())


#if __name__ == '__main__':
#    main()