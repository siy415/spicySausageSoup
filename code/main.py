import sys
from PyQt5.QtWidgets import QApplication
import pandas as pd

import guiManager
from companyList import getCompList


def main():
    app = QApplication(sys.argv)
    df = getCompList()
    coCode = df['종목코드'].to_list()
    coName = df['회사명'].to_list()

    gi = guiManager.MainWindow()
    gi.setConfig(coCode=coCode, coName=coName)

    gi.insert_data()

    gi.show()
    app.exec_()


if __name__ == '__main__':
    main()
