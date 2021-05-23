import pandas as pd

import guiManager
from CompanyList import getCompList


def main():
    df = getCompList()
    coCode = df['종목코드'].to_list()
    coName = df['회사명'].to_list()

    gi = guiManager.MainWindow()
    gi.setConfig(coCode=coCode, coName=coName)

    gi.insert_data()
    gi.show()
    gi.exit()


if __name__ == '__main__':
    main()
