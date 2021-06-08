# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from inspect import getsourcefile
from PyQt5 import QtCore, QtGui, QtWidgets
# from pyqtgraph import PlotWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
# import graphManager
import jjson
import numpy as np
import webbrowser
import financeData3
import sys

data_params = {
    'len': int,
    'coName': list,
    'coCode': list,
}

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(911, 979)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.code_lineEdit = QtWidgets.QLineEdit(self.main_tab)
        self.code_lineEdit.setGeometry(QtCore.QRect(160, 30, 191, 31))
        self.code_lineEdit.setObjectName("code_lineEdit")
        self.codelabel = QtWidgets.QLabel(self.main_tab)
        self.codelabel.setGeometry(QtCore.QRect(80, 30, 71, 31))
        self.codelabel.setTextFormat(QtCore.Qt.AutoText)
        self.codelabel.setObjectName("codelabel")
        self.name_lineEdit = QtWidgets.QLineEdit(self.main_tab)
        self.name_lineEdit.setGeometry(QtCore.QRect(160, 80, 191, 31))
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.namelabel = QtWidgets.QLabel(self.main_tab)
        self.namelabel.setGeometry(QtCore.QRect(80, 80, 71, 31))
        self.namelabel.setObjectName("namelabel")
        self.startdate = QtWidgets.QLabel(self.main_tab)
        self.startdate.setGeometry(QtCore.QRect(460, 30, 71, 31))
        self.startdate.setObjectName("startdate")
        self.enddate = QtWidgets.QLabel(self.main_tab)
        self.enddate.setGeometry(QtCore.QRect(460, 80, 71, 31))
        self.enddate.setObjectName("enddate")
        self.start_dateEdit = QtWidgets.QDateEdit(self.main_tab)
        self.start_dateEdit.setGeometry(QtCore.QRect(540, 31, 191, 31))
        self.start_dateEdit.setObjectName("start_dateEdit")
        self.start_dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.start_dateEdit.setCalendarPopup(True)
        self.end_dateEdit = QtWidgets.QDateEdit(self.main_tab)
        self.end_dateEdit.setGeometry(QtCore.QRect(540, 80, 191, 31))
        self.end_dateEdit.setObjectName("end_dateEdit")
        self.end_dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.end_dateEdit.setCalendarPopup(True)
        self.mon_up_label = QtWidgets.QLabel(self.main_tab)
        self.mon_up_label.setGeometry(QtCore.QRect(50, 570, 56, 30))
        self.mon_up_label.setObjectName("mon_up_label")
        self.mon_down_label = QtWidgets.QLabel(self.main_tab)
        self.mon_down_label.setGeometry(QtCore.QRect(50, 600, 56, 30))
        self.mon_down_label.setObjectName("mon_down_label")
        self.mon_eq_label = QtWidgets.QLabel(self.main_tab)
        self.mon_eq_label.setGeometry(QtCore.QRect(50, 630, 56, 30))
        self.mon_eq_label.setObjectName("mon_eq_label")
        self.tue_eq_label = QtWidgets.QLabel(self.main_tab)
        self.tue_eq_label.setGeometry(QtCore.QRect(200, 630, 56, 30))
        self.tue_eq_label.setObjectName("tue_eq_label")
        self.tue_down_label = QtWidgets.QLabel(self.main_tab)
        self.tue_down_label.setGeometry(QtCore.QRect(200, 600, 56, 30))
        self.tue_down_label.setObjectName("tue_down_label")
        self.tue_up_label = QtWidgets.QLabel(self.main_tab)
        self.tue_up_label.setGeometry(QtCore.QRect(200, 570, 56, 30))
        self.tue_up_label.setObjectName("tue_up_label")
        self.wed_up_label = QtWidgets.QLabel(self.main_tab)
        self.wed_up_label.setGeometry(QtCore.QRect(370, 570, 56, 30))
        self.wed_up_label.setObjectName("wed_up_label")
        self.wed_eq_label = QtWidgets.QLabel(self.main_tab)
        self.wed_eq_label.setGeometry(QtCore.QRect(370, 630, 56, 30))
        self.wed_eq_label.setObjectName("wed_eq_label")
        self.wed_down_label = QtWidgets.QLabel(self.main_tab)
        self.wed_down_label.setGeometry(QtCore.QRect(370, 600, 56, 30))
        self.wed_down_label.setObjectName("wed_down_label")
        self.thu_down_label = QtWidgets.QLabel(self.main_tab)
        self.thu_down_label.setGeometry(QtCore.QRect(530, 600, 56, 30))
        self.thu_down_label.setObjectName("thu_down_label")
        self.thu_up_label = QtWidgets.QLabel(self.main_tab)
        self.thu_up_label.setGeometry(QtCore.QRect(530, 570, 56, 30))
        self.thu_up_label.setObjectName("thu_up_label")
        self.thu_eq_label = QtWidgets.QLabel(self.main_tab)
        self.thu_eq_label.setGeometry(QtCore.QRect(530, 630, 56, 30))
        self.thu_eq_label.setObjectName("thu_eq_label")
        self.fri_eq_label = QtWidgets.QLabel(self.main_tab)
        self.fri_eq_label.setGeometry(QtCore.QRect(690, 630, 56, 30))
        self.fri_eq_label.setObjectName("fri_eq_label")
        self.fri_up_label = QtWidgets.QLabel(self.main_tab)
        self.fri_up_label.setGeometry(QtCore.QRect(690, 570, 56, 30))
        self.fri_up_label.setObjectName("fri_up_label")
        self.fri_down_label = QtWidgets.QLabel(self.main_tab)
        self.fri_down_label.setGeometry(QtCore.QRect(690, 600, 56, 30))
        self.fri_down_label.setObjectName("fri_down_label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.main_tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 199, 861, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        # add graph Box by inyong shim
        self.graphBox = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.graphBox.addWidget(self.canvas)
        self.canvas.draw()

        self.searchbtn = QtWidgets.QPushButton(self.main_tab)
        self.searchbtn.setGeometry(QtCore.QRect(180, 150, 501, 41))
        self.searchbtn.setObjectName("searchbtn")
        self.searchbtn.clicked.connect(self.mainSearchBtnClickedEvent)
        self.anal_start_val_edit = QtWidgets.QLineEdit(self.main_tab)
        self.anal_start_val_edit.setGeometry(QtCore.QRect(190, 690, 191, 31))
        self.anal_start_val_edit.setObjectName("anal_start_val_edit")
        self.anal_start_val_edit.setReadOnly(True)
        self.anal_start_value = QtWidgets.QLabel(self.main_tab)
        self.anal_start_value.setGeometry(QtCore.QRect(60, 690, 121, 31))
        self.anal_start_value.setTextFormat(QtCore.Qt.AutoText)
        self.anal_start_value.setObjectName("anal_start_value")
        self.anal_end_val_edit = QtWidgets.QLineEdit(self.main_tab)
        self.anal_end_val_edit.setGeometry(QtCore.QRect(550, 690, 191, 31))
        self.anal_end_val_edit.setObjectName("anal_end_val_edit")
        self.anal_end_val_edit.setReadOnly(True)
        self.anal_end_value = QtWidgets.QLabel(self.main_tab)
        self.anal_end_value.setGeometry(QtCore.QRect(420, 690, 121, 31))
        self.anal_end_value.setTextFormat(QtCore.Qt.AutoText)
        self.anal_end_value.setObjectName("anal_end_value")
        self.diff_data_edit = QtWidgets.QLineEdit(self.main_tab)
        self.diff_data_edit.setGeometry(QtCore.QRect(190, 740, 551, 31))
        self.diff_data_edit.setObjectName("diff_data_edit")
        self.diff_data_edit.setReadOnly(True)
        self.diff_data_label = QtWidgets.QLabel(self.main_tab)
        self.diff_data_label.setGeometry(QtCore.QRect(60, 740, 121, 31))
        self.diff_data_label.setTextFormat(QtCore.Qt.AutoText)
        self.diff_data_label.setObjectName("diff_data_label")
        self.rcmd_buy_date_edit = QtWidgets.QLineEdit(self.main_tab)
        self.rcmd_buy_date_edit.setGeometry(QtCore.QRect(190, 810, 191, 31))
        self.rcmd_buy_date_edit.setObjectName("rcmd_buy_date_edit")
        self.rcmd_buy_date_edit.setReadOnly(True)
        self.rcmd_buy_date_label = QtWidgets.QLabel(self.main_tab)
        self.rcmd_buy_date_label.setGeometry(QtCore.QRect(60, 810, 121, 31))
        self.rcmd_buy_date_label.setTextFormat(QtCore.Qt.AutoText)
        self.rcmd_buy_date_label.setObjectName("rcmd_buy_date_label")
        self.rcmd_sell_date_label = QtWidgets.QLabel(self.main_tab)
        self.rcmd_sell_date_label.setGeometry(QtCore.QRect(420, 810, 121, 31))
        self.rcmd_sell_date_label.setTextFormat(QtCore.Qt.AutoText)
        self.rcmd_sell_date_label.setObjectName("rcmd_sell_date_label")
        self.rcmd_sell_date_edit = QtWidgets.QLineEdit(self.main_tab)
        self.rcmd_sell_date_edit.setGeometry(QtCore.QRect(550, 810, 191, 31))
        self.rcmd_sell_date_edit.setObjectName("rcmd_sell_date_edit")
        self.rcmd_sell_date_edit.setReadOnly(True)
        self.tabWidget.addTab(self.main_tab, "")
        self.list_tab = QtWidgets.QWidget()
        self.list_tab.setObjectName("list_tab")
        self.listCorp = QtWidgets.QTableWidget(self.list_tab)
        self.listCorp.setGeometry(QtCore.QRect(10, 50, 351, 801))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listCorp.sizePolicy().hasHeightForWidth())
        self.listCorp.setSizePolicy(sizePolicy)
        # self.listCorp.cellClicked.connect(self.listIdxChangedEvent)
        self.listCorp.currentCellChanged.connect(self.listIdxChangedEvent)
        self.listCorp.doubleClicked.connect(self.corpDoubleClickedEvent)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(251, 251, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 251, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.listCorp.setPalette(palette)
        self.listCorp.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listCorp.setAutoScroll(True)
        self.listCorp.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listCorp.setDragDropOverwriteMode(False)
        self.listCorp.setAlternatingRowColors(True)
        self.listCorp.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listCorp.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listCorp.setShowGrid(True)
        self.listCorp.setWordWrap(False)
        self.listCorp.setRowCount(31)
        self.listCorp.setColumnCount(4)
        self.listCorp.setObjectName("listCorp")
        item = QtWidgets.QTableWidgetItem()
        self.listCorp.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listCorp.setHorizontalHeaderItem(1, item)
        self.listCorp.verticalHeader().setVisible(False)
        self.btnSearch = QtWidgets.QPushButton(self.list_tab)
        self.btnSearch.setGeometry(QtCore.QRect(290, 10, 71, 31))
        self.btnSearch.setObjectName("btnSearch")
        self.btnSearch.clicked.connect(self.btnClickedEvent)
        self.txtBoxName = QtWidgets.QLineEdit(self.list_tab)
        self.txtBoxName.setGeometry(QtCore.QRect(136, 10, 151, 31))
        self.txtBoxName.setObjectName("txtBoxName")
        self.txtBoxName.returnPressed.connect(self.btnClickedEvent)
        self.comBoxProp = QtWidgets.QComboBox(self.list_tab)
        self.comBoxProp.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.comBoxProp.setObjectName("comBoxProp")
        self.comBoxProp.addItem("")
        self.comBoxProp.addItem("")
        self.groupInfoCorp = QtWidgets.QGroupBox(self.list_tab)
        self.groupInfoCorp.setGeometry(QtCore.QRect(380, 10, 441, 841))
        self.groupInfoCorp.setObjectName("groupInfoCorp")
        self.detailCorp = QtWidgets.QTableWidget(self.groupInfoCorp)
        self.detailCorp.setEnabled(True)
        self.detailCorp.setGeometry(QtCore.QRect(10, 220, 421, 601))
        self.detailCorp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.detailCorp.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.detailCorp.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.detailCorp.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.detailCorp.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
        self.detailCorp.setObjectName("detailCorp")
        self.detailCorp.setColumnCount(0)
        self.detailCorp.setRowCount(0)
        self.detailCorp.setShowGrid(True)
        self.detailCorp.setWordWrap(True)
        self.detailCorp.setAlternatingRowColors(True)
        self.detailCorp.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.detailCorp.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.detailCorp.setAutoScroll(True)
        self.detailCorp.horizontalHeader().setVisible(False)
        self.detailCorp.cellClicked.connect(self.detailCellClicked)
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupInfoCorp)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 421, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.lblCorp = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        self.lblCorp.setFont(font)
        self.lblCorp.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCorp.setObjectName("lblCorp")
        self.gridLayout.addWidget(self.lblCorp, 0, 0, 1, 1)
        self.pgBarSearch = QtWidgets.QProgressBar(self.groupInfoCorp)
        self.pgBarSearch.setGeometry(QtCore.QRect(10, 820, 421, 10))
        self.pgBarSearch.setProperty("value", 24)
        self.pgBarSearch.setAlignment(QtCore.Qt.AlignCenter)
        self.pgBarSearch.setTextVisible(False)
        self.pgBarSearch.setOrientation(QtCore.Qt.Horizontal)
        self.pgBarSearch.setInvertedAppearance(False)
        self.pgBarSearch.setObjectName("pgBarSearch")
        self.tabWidget.addTab(self.list_tab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "주가 분석 프로그램 (Prod. 인생력전)"))
        self.codelabel.setText(_translate("MainWindow", "종목코드  : "))
        self.namelabel.setText(_translate("MainWindow", "종목명     : "))
        self.startdate.setText(_translate("MainWindow", "분석일자  : "))
        self.enddate.setText(_translate("MainWindow", "~            :"))
        self.mon_up_label.setText(_translate("MainWindow", "% 상승"))
        self.mon_up_label.setGeometry(QtCore.QRect(170, 570, 56, 30))
        self.mon_down_label.setText(_translate("MainWindow", "% 하락"))
        self.mon_down_label.setGeometry(QtCore.QRect(170, 600, 56, 30))
        self.mon_eq_label.setText(_translate("MainWindow", "% 동일"))
        self.mon_eq_label.setGeometry(QtCore.QRect(170, 630, 56, 30))
        self.tue_up_label.setText(_translate("MainWindow", "% 상승"))
        self.tue_up_label.setGeometry(QtCore.QRect(300, 570, 56, 30))
        self.tue_down_label.setText(_translate("MainWindow", "% 하락"))
        self.tue_down_label.setGeometry(QtCore.QRect(300, 600, 56, 30))
        self.tue_eq_label.setText(_translate("MainWindow", "% 동일"))
        self.tue_eq_label.setGeometry(QtCore.QRect(300, 630, 56, 30))
        self.wed_up_label.setText(_translate("MainWindow", "% 상승"))
        self.wed_up_label.setGeometry(QtCore.QRect(430, 570, 56, 30))
        self.wed_down_label.setText(_translate("MainWindow", "% 하락"))
        self.wed_down_label.setGeometry(QtCore.QRect(430, 600, 56, 30))
        self.wed_eq_label.setText(_translate("MainWindow", "% 동일"))
        self.wed_eq_label.setGeometry(QtCore.QRect(430, 630, 56, 30))
        self.thu_up_label.setText(_translate("MainWindow", "% 상승"))
        self.thu_up_label.setGeometry(QtCore.QRect(560, 570, 56, 30))
        self.thu_down_label.setText(_translate("MainWindow", "% 하락"))
        self.thu_down_label.setGeometry(QtCore.QRect(560, 600, 56, 30))
        self.thu_eq_label.setText(_translate("MainWindow", "% 동일"))
        self.thu_eq_label.setGeometry(QtCore.QRect(560, 630, 56, 30))
        self.fri_up_label.setText(_translate("MainWindow", "% 상승"))
        self.fri_up_label.setGeometry(QtCore.QRect(690, 570, 56, 30))
        self.fri_down_label.setText(_translate("MainWindow", "% 하락"))
        self.fri_down_label.setGeometry(QtCore.QRect(690, 600, 56, 30))
        self.fri_eq_label.setText(_translate("MainWindow", "% 동일"))
        self.fri_eq_label.setGeometry(QtCore.QRect(690, 630, 56, 30))
        self.searchbtn.setText(_translate("MainWindow", "분석"))
        self.anal_start_value.setText(_translate("MainWindow", "분석 시작일 종가    :"))
        self.anal_end_value.setText(_translate("MainWindow", "분석 시작일 종가    :"))
        self.diff_data_label.setText(_translate("MainWindow", "시작일 대비           :"))
        self.rcmd_buy_date_label.setText(_translate("MainWindow", "매수 추천 요일       :"))
        self.rcmd_sell_date_label.setText(_translate("MainWindow", "매도 추천 요일       :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_tab), _translate("MainWindow", "데이터 분석"))
        item = self.listCorp.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "종목코드"))
        item = self.listCorp.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "기업명"))
        self.btnSearch.setText(_translate("MainWindow", "검색"))
        self.comBoxProp.setItemText(0, _translate("MainWindow", "기업명"))
        self.comBoxProp.setItemText(1, _translate("MainWindow", "종목코드"))
        self.groupInfoCorp.setTitle(_translate("MainWindow", "기업 정보"))
        self.lblCorp.setText(_translate("MainWindow", "Corperation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.list_tab), _translate("MainWindow", "종목 LIST"))


    def btnClickedEvent(self):
        print("A")
        param = {
            "len": int,
            "coIdx": int,
        }
        print(self.txtBoxName.text())
        if self.txtBoxName.text() == "":
            self.insert_data(data_params)
        else:
            #print(data_params)
            param["len"] = 1
            if self.comBoxProp.currentText() == "기업명":
                print(self.txtBoxName.text())
                if self.txtBoxName.text() in data_params["coName"]:
                    param["coIdx"] = data_params["coName"].index(self.txtBoxName.text())
                else:
                    param["len"] = 0
            else:
                if self.txtBoxName.text() in data_params["coCode"]:
                    param["coIdx"] = data_params["coCode"].index(self.txtBoxName.text())
                else:
                    param["len"] = 0

            self.insert_data(param)
            if(param["len"] > 0):
                self.listCorp.setCurrentCell(0, not self.listCorp.currentColumn())

    def mainSearchBtnClickedEvent(self):

        plt.cla()
        self.graphBox.removeWidget(self.canvas)
            
        self.plot(1, 1)
        
    
    def corpDoubleClickedEvent(self):
        r = self.listCorp.currentRow()

        if self.listCorp.item(r, 1).text() != "":
            self.code_lineEdit.setText(self.listCorp.item(r, 0).text())
            self.name_lineEdit.setText(self.listCorp.item(r, 1).text())

            self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex()-1)
        return 0


    def detailCellClicked(self):
        r = self.detailCorp.currentRow()
        rHeadrer = self.detailCorp.verticalHeaderItem(r)

        if rHeadrer.text() == "홈페이지" and self.detailCorp.item(r, 0).text() != '-':
            webbrowser.open(self.detailCorp.currentItem().text())


    
    def listIdxChangedEvent(self):
        param = {}
        dictName = { 
            "corp_name": "기업명", 
            "ceo_nm"   : "대표", 
            "adres"    : "주소",
            "hm_url"   : "홈페이지", 
            "phn_no"   : "전화번호"
        }

        r = self.listCorp.currentRow()
        # c = self.listCorp.currentColumn()
        if self.listCorp.item(r, 1).text() != "":
            print(self.listCorp.item(r, 1).text())
            self.lblCorp.setText(self.listCorp.item(r, 1).text())
            corpNum = jjson.getCompNum(self.listCorp.item(r, 0).text())
            res = jjson.getCompany(corpNum)
            i = 0
            for key in dictName.keys():
                param[dictName[key]] = res[key]

            print("param")
            print(param)
            self.showCorpDetail(param)


    def showCorpDetail(self, param: dict):
        if self.detailCorp.rowCount != len(param):
            self.detailCorp.setRowCount(len(param))
            self.detailCorp.setColumnCount(1)
            rHeader = self.detailCorp.horizontalHeader()
            rHeader.resizeSection(0, 300)
            lparam = list(param.keys())
            for i in range(0, len(param)):
                item = QtWidgets.QTableWidgetItem()
                item.setText(lparam[i])
                self.detailCorp.setVerticalHeaderItem(i, item)
                self.detailCorp.setItem(i, 0, QtWidgets.QTableWidgetItem(param[lparam[i]]))
                self.detailCorp.setCurrentCell(i, 0)
                if lparam[i] == "홈페이지":
                    cell = self.detailCorp.currentItem()
                    cell.setForeground(QtGui.QBrush(QtCore.Qt.blue))
                    font = QtGui.QFont()
                    font.setUnderline(True)
                    cell.setFont(font)

        return 0


    def setConfig(self, **kwargs):
        self.confCorpList(kwargs.items())


    def confCorpList(self, items: list):
        global data_params

        for key, value in items:
            data_params[key] = value
            if key == 'coName':
                data_params['len'] = len(value)
        
        self.listCorp.setRowCount(data_params['len'])
        self.listCorp.setColumnCount(2)
        cHeader = self.listCorp.verticalHeader()
        cHeader.setDefaultSectionSize(35)
        rHeader = self.listCorp.horizontalHeader()
        rHeader.resizeSection(0, 120)
        rHeader.resizeSection(1, 204)

        self.pgBarSearch.setValue(0)

    def plot(self, hour ,temperature):
        #data, blShow = graphManager.getData()
        #self.ax = self.fig.add_subplot(111)
        #self.ax.plot(data.iloc[:, blShow])

        #x_label_list = ['월', '화', '수', '목', '금']
        x_label_list = ['MON', 'TUE', 'WED', 'THU', 'FRI']
        bar_width = 0.2
        bar_height = 1
        index = np.arange(len(x_label_list))

        if hour == 0 and temperature == 0:
            up_data = [0, 0, 0, 0, 0]
            down_data = [0, 0, 0, 0, 0]
            eq_data = [0, 0, 0, 0, 0]

        elif self.code_lineEdit.text() == "삼성":
            up_data = [120, 140, 130, 150, 115]
            down_data = [130, 150, 120, 110, 120]
            eq_data = [110, 130, 145, 115, 125]

        elif self.code_lineEdit.text() == "현대":
            up_data = [220, 240, 230, 250, 215]
            down_data = [230, 250, 220, 210, 220]
            eq_data = [210, 230, 245, 215, 225]

        elif self.code_lineEdit.text() == "LG":
            up_data = [320, 340, 330, 350, 315]
            down_data = [330, 350, 320, 310, 320]
            eq_data = [310, 330, 345, 315, 325]

        else:
            up_data = [20, 40, 30, 50, 15]
            down_data = [30, 50, 20, 10, 120]
            eq_data = [10, 30, 45, 15, 25]
        
        self.ax.bar(index, up_data, color='r', align='edge', edgecolor='lightgray', width=bar_width, label='UP')
        self.ax.bar(index+bar_width, down_data, color='b', align='edge', edgecolor='lightgray', width=bar_width, label='DOWN')
        self.ax.bar(index+bar_width+bar_width, eq_data, color='y', align='edge', edgecolor='lightgray', width=bar_width, label='EQUAL')

        self.ax.legend(loc='upper right', fontsize=7.5)
        
        plt.xticks(index + bar_width + 0.1, x_label_list)

        y_max = plt.ylim()[1] + 100
        plt.ylim([0, y_max])

        self.setLabel(up_data, down_data, eq_data)

        self.canvas = FigureCanvasQTAgg(self.fig)
        self.canvas.draw()

        self.graphBox.addWidget(self.canvas)


    def setLabel(self, up, down, eq):
        _translate = QtCore.QCoreApplication.translate
        
        self.mon_up_label.setText(_translate("MainWindow", str(up[0]) + "% 상승"))
        self.mon_down_label.setText(_translate("MainWindow", str(down[0]) + "% 하락"))
        self.mon_eq_label.setText(_translate("MainWindow", str(eq[0]) + "% 동일"))

        self.tue_up_label.setText(_translate("MainWindow", str(up[1]) + "% 상승"))
        self.tue_down_label.setText(_translate("MainWindow", str(down[1]) + "% 하락"))
        self.tue_eq_label.setText(_translate("MainWindow", str(eq[1]) + "% 동일"))

        self.wed_up_label.setText(_translate("MainWindow", str(up[2]) + "% 상승"))
        self.wed_down_label.setText(_translate("MainWindow", str(down[2]) + "% 하락"))
        self.wed_eq_label.setText(_translate("MainWindow", str(eq[2]) + "% 동일"))

        self.thu_up_label.setText(_translate("MainWindow", str(up[3]) + "% 상승"))
        self.thu_down_label.setText(_translate("MainWindow", str(down[3]) + "% 하락"))
        self.thu_eq_label.setText(_translate("MainWindow", str(eq[3]) + "% 동일"))

        self.fri_up_label.setText(_translate("MainWindow", str(up[4]) + "% 상승"))
        self.fri_down_label.setText(_translate("MainWindow", str(down[4]) + "% 하락"))
        self.fri_eq_label.setText(_translate("MainWindow", str(eq[4]) + "% 동일"))
        

    def insert_data(self, param):
        global data_params
        # print(param)
        for i in range(0, data_params['len']):
            if param["len"] <= 1:
                if i < param["len"]:
                    self.listCorp.setItem(i, 0, QtWidgets.QTableWidgetItem(data_params['coCode'][param["coIdx"]]))
                    self.listCorp.setItem(i, 1, QtWidgets.QTableWidgetItem(data_params['coName'][param["coIdx"]]))
                else:
                    self.listCorp.setItem(i, 0, QtWidgets.QTableWidgetItem(""))
                    self.listCorp.setItem(i, 1, QtWidgets.QTableWidgetItem(""))
            else:
                self.listCorp.setItem(i, 0, QtWidgets.QTableWidgetItem(data_params['coCode'][i]))
                self.listCorp.setItem(i, 1, QtWidgets.QTableWidgetItem(data_params['coName'][i]))
                
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''
