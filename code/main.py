import sys
from types import ClassMethodDescriptorType
from typing import Any, ClassVar
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtWidgets
import pandas as pd
import guiManager
from companyList import getCompList

def main():
    global gi
    app = QApplication(sys.argv)
    df = getCompList()
    coCode = df['종목코드'].to_list()
    coName = df['회사명'].to_list()

    MainWindow = QtWidgets.QMainWindow()
    gi = guiManager.Ui_MainWindow()
    gi.setupUi(MainWindow)
    gi.setConfig(coCode=coCode, coName=coName)

    gi.insert_data(guiManager.data_params)

    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
