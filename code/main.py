import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtWidgets
import pandas as pd

import guiManagerE
from companyList import getCompList


def main():
    app = QApplication(sys.argv)
    df = getCompList()
    coCode = df['종목코드'].to_list()
    coName = df['회사명'].to_list()

    MainWindow = QtWidgets.QMainWindow()
    gi = guiManagerE.Ui_MainWindow()
    gi.setupUi(MainWindow)
    gi.setConfig(coCode=coCode, coName=coName)

    gi.insert_data()

    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
