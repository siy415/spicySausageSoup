#from PyQt5 import QtWidgets, uic
#from pyqtgraph import PlotWidget, plot

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

import sys
import os

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('midtest.ui', self)

        self.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])
        self.set_table_header()
        self.insert_data()
        

    def plot(self, hour ,temperature):
        self.graphWidget.plot(hour, temperature)

    def insert_data(self):
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("005930"))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("삼성전자"))

        self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem("000660"))
        self.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem("SK하이닉스"))

        self.tableWidget.setItem(2, 0, QtWidgets.QTableWidgetItem("005380"))
        self.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem("현대차"))

        self.tableWidget.setItem(3, 0, QtWidgets.QTableWidgetItem("035420"))
        self.tableWidget.setItem(3, 1, QtWidgets.QTableWidgetItem("NAVER"))

        self.tableWidget.setItem(4, 0, QtWidgets.QTableWidgetItem("005490"))
        self.tableWidget.setItem(4, 1, QtWidgets.QTableWidgetItem("POSCO"))

        self.tableWidget.setItem(5, 0, QtWidgets.QTableWidgetItem("015760"))
        self.tableWidget.setItem(5, 1, QtWidgets.QTableWidgetItem("한국전력"))

        self.tableWidget.setItem(6, 0, QtWidgets.QTableWidgetItem("028260"))
        self.tableWidget.setItem(6, 1, QtWidgets.QTableWidgetItem("삼성물산"))

        self.tableWidget.setItem(7, 0, QtWidgets.QTableWidgetItem("012330"))
        self.tableWidget.setItem(7, 1, QtWidgets.QTableWidgetItem("현대모비스"))

        self.tableWidget.setItem(8, 0, QtWidgets.QTableWidgetItem("032830"))
        self.tableWidget.setItem(8, 1, QtWidgets.QTableWidgetItem("삼성생명"))

    def set_table_header(self):
        self.tableWidget.setHorizontalHeaderLabels(["종목코드", "종목명", "종목코드", "종목명", "종목코드", "종목명"])


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
    #os.system('pause')

if __name__ == '__main__':
    main()