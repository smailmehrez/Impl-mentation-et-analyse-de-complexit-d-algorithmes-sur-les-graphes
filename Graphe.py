# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Graphe.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random
import networkx as nx
import pydot as pydot
import numpy as np
from PyQt5.QtGui import QPixmap
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 850)
        MainWindow.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-170, 80, 1850, 7))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.line.setFont(font)
        self.line.setStyleSheet("color: rgb(52, 101, 164);\n"
"background-color: rgb(52, 101, 164);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, -10, 1051, 81))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(52, 101, 164);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"    color: rgb(255, 155, 1);\n"
"    font-size: 20px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 160, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background: #E8F9FD;\n"
"    border: 2px solid #2155CD; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:20px;\n"
"    color: #2155CD;\n"
"\n"
"}\n"
"QPushButton:focus{\n"
"     border: 2px solid #2e2c2c; \n"
"     background: #EFFFFD;\n"
"    \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.resu)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 230, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background: #E8F9FD;\n"
"    border: 2px solid #2155CD; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:20px;\n"
"    color: #2155CD;\n"
"\n"
"}\n"
"QPushButton:focus{\n"
"     border: 2px solid #2e2c2c; \n"
"     background: #EFFFFD;\n"
"    \n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.densite)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 240, 100, 41))
        self.textEdit.setStyleSheet("background: #E8F9FD;border: 2px solid #2155CD;align=center; border-radius: 10px;font-family: Arial;font-size:15px;color: #2155CD;")
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 284, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"color: rgb(255, 155, 1);\n"
" font-size: 18px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 370, 351, 45))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"color: rgb(255, 155, 1);\n"
" font-size: 17px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 460, 351, 45))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"color: rgb(255, 155, 1);\n"
" font-size: 17px;")
        self.label_5.setObjectName("label_5")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 510, 321, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    background: #E8F9FD;\n"
"    border: 2px solid #2155CD; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:20px;\n"
"    color: #2155CD;\n"
"\n"
"}\n"
"QPushButton:focus{\n"
"     border: 2px solid #2e2c2c; \n"
"     background: #EFFFFD;\n"
"    \n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.chc)
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"    background: #E8F9FD;\n"
"    border: 2px solid #2155CD; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #2155CD;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #2e2c2c; \n"
"    background: #EFFFFD;\n"
"    \n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
"    background: #E8F9FD;\n"
"    border: 2px solid #2155CD; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #2155CD;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #2e2c2c; \n"
"    background: #EFFFFD;\n"
"    \n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_4.addWidget(self.lineEdit_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 540, 351, 45))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"color: rgb(255, 155, 1);\n"
" font-size: 17px;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 620, 351, 45))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("\n"
"color: rgb(255, 155, 1);\n"
" font-size: 17px;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 710, 351, 45))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("\n"
"color: rgb(255, 155, 1);\n"
" font-size: 17px;")
        self.label_8.setObjectName("label_8")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 590, 321, 30))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    background: #E8F9FD;\n"
"    border: 2px solid #2155CD; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:20px;\n"
"    color: #2155CD;\n"
"\n"
"}\n"
"QPushButton:focus{\n"
"     border: 2px solid #2e2c2c; \n"
"     background: #EFFFFD;\n"
"    \n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.Ajouter_un_noeud)
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_6.setStyleSheet("QLineEdit{\n"
"    background: #E8F9FD;\n"
"    border: 2px solid #2155CD; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #2155CD;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #2e2c2c; \n"
"    background: #EFFFFD;\n"
"    \n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_5.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_7.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.lineEdit_7.setStyleSheet("QLineEdit{\n"
"    background: #E8F9FD;\n"
"    border: 2px solid #2155CD; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #2155CD;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #2e2c2c; \n"
"    background: #EFFFFD;\n"
"    \n"
"}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_5.addWidget(self.lineEdit_7)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 670, 191, 30))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    background: #E8F9FD;\n"
"    border: 2px solid #2155CD; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:20px;\n"
"    color: #2155CD;\n"
"\n"
"}\n"
"QPushButton:focus{\n"
"     border: 2px solid #2e2c2c; \n"
"     background: #EFFFFD;\n"
"    \n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.supN)
        self.horizontalLayout_6.addWidget(self.pushButton_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_8.setStyleSheet("QLineEdit{\n"
"    background: #E8F9FD;\n"
"    border: 2px solid #2155CD; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #2155CD;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #2e2c2c; \n"
"    background: #EFFFFD;\n"
"    \n"
"}")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_6.addWidget(self.lineEdit_8)
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 770, 321, 30))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    background: #E8F9FD;\n"
"    border: 2px solid #2155CD; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:20px;\n"
"    color: #2155CD;\n"
"\n"
"}\n"
"QPushButton:focus{\n"
"     border: 2px solid #2e2c2c; \n"
"     background: #EFFFFD;\n"
"    \n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.Ajouter_un_lien)
        self.horizontalLayout_7.addWidget(self.pushButton_9)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_9.setStyleSheet("QLineEdit{\n"
"    background: #E8F9FD;\n"
"    border: 2px solid #2155CD; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #2155CD;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #2e2c2c; \n"
"    background: #EFFFFD;\n"
"    \n"
"}")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_7.addWidget(self.lineEdit_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_10.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.lineEdit_10.setStyleSheet("QLineEdit{\n"
"    background: #E8F9FD;\n"
"    border: 2px solid #2155CD; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #2155CD;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #2e2c2c; \n"
"    background: #EFFFFD;\n"
"    \n"
"}")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_7.addWidget(self.lineEdit_10)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(400, 100, 7, 691))
        self.line_4.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(450, 130, 561, 641))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 541, 621))
        self.label_9.setObjectName("label_9")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(1030, 130, 561, 641))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 541, 621))
        self.label_10.setObjectName("label_10")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 140, 102, 76))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.T10 = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.T10.setFont(font)
        self.T10.setStyleSheet("color: rgb(1, 92, 255);")
        self.T10.setCheckable(True)
        self.T10.setChecked(False)
        self.T10.setAutoRepeat(False)
        self.T10.setObjectName("T10")
        self.verticalLayout.addWidget(self.T10)
        self.T20 = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.T20.setFont(font)
        self.T20.setStyleSheet("color: rgb(1, 92, 255);")
        self.T20.setCheckable(True)
        self.T20.setChecked(False)
        self.T20.setAutoRepeat(False)
        self.T20.setObjectName("T20")
        self.verticalLayout.addWidget(self.T20)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.T30 = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.T30.setFont(font)
        self.T30.setStyleSheet("color: rgb(1, 92, 255);")
        self.T30.setCheckable(True)
        self.T30.setChecked(False)
        self.T30.setAutoRepeat(False)
        self.T30.setObjectName("T30")
        self.verticalLayout_2.addWidget(self.T30)
        self.T50 = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.T50.setFont(font)
        self.T50.setStyleSheet("color: rgb(1, 92, 255);")
        self.T50.setCheckable(True)
        self.T50.setChecked(False)
        self.T50.setAutoRepeat(False)
        self.T50.setObjectName("T50")
        self.verticalLayout_2.addWidget(self.T50)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 340, 191, 30))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background: #E8F9FD;\n"
"    border: 2px solid #2155CD; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:20px;\n"
"    color: #2155CD;\n"
"\n"
"}\n"
"QPushButton:focus{\n"
"     border: 2px solid #2e2c2c; \n"
"     background: #EFFFFD;\n"
"    \n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.RN)
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background: #E8F9FD;\n"
"    border: 2px solid #2155CD; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #2155CD;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #2e2c2c; \n"
"    background: #EFFFFD;\n"
"    \n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 420, 321, 30))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    background: #E8F9FD;\n"
"    border: 2px solid #2155CD; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:20px;\n"
"    color: #2155CD;\n"
"\n"
"}\n"
"QPushButton:focus{\n"
"     border: 2px solid #2e2c2c; \n"
"     background: #EFFFFD;\n"
"    \n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.ch)
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    background: #E8F9FD;\n"
"    border: 2px solid #2155CD; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #2155CD;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #2e2c2c; \n"
"    background: #EFFFFD;\n"
"    \n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    background: #E8F9FD;\n"
"    border: 2px solid #2155CD; \n"
"    border-radius: 10px;  \n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"   color: #2155CD;\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"     border: 2px solid #2e2c2c; \n"
"    background: #EFFFFD;\n"
"    \n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(190, 100, 131, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel{\n"
                                    "    color: rgb(255, 155, 1);\n"
                                    "    font-size: 20px;\n"
                                    "}")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.textEdit_22 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_22.setStyleSheet("    background: #E8F9FD;\n"
                                    "    border: 2px solid #2155CD; \n"
                                    "    border-radius: 10px;  \n"
                                    "    font-family: Arial;\n"
                                    "    font-size:15px;\n"
                                    "   color: #2155CD;")
        self.textEdit_22.setObjectName("textEdit")
        self.horizontalLayout_8.addWidget(self.textEdit_22)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Implémentation et analyse de complexité d’algorithmes sur les graphes"))
        self.label_2.setText(_translate("MainWindow", "La  taille de graphe :"))
        self.pushButton_2.setText(_translate("MainWindow", "afficher graphe"))
        self.pushButton_3.setText(_translate("MainWindow", "la densité :"))
        self.label_3.setText(_translate("MainWindow", "Recherche un nœud dans le graphe :"))
        self.label_4.setText(_translate("MainWindow", "Recherche d’un chemin entre deux nœud :"))
        self.label_5.setText(_translate("MainWindow", "Recherche du chemin le plus court :"))
        self.pushButton_6.setText(_translate("MainWindow", "Recherche"))
        self.lineEdit_4.setText(_translate("MainWindow", "noeud A"))
        self.lineEdit_5.setText(_translate("MainWindow", "noeud B"))
        self.label_6.setText(_translate("MainWindow", "Ajouter un nœud A avec ses liens :"))
        self.label_7.setText(_translate("MainWindow", "Supprimer un nœud A avec ses liens :"))
        self.label_8.setText(_translate("MainWindow", "Ajouter un lien entre deux nœuds existants:"))
        self.pushButton_7.setText(_translate("MainWindow", "Ajouter"))
        self.lineEdit_6.setText(_translate("MainWindow", "noeud A"))
        self.lineEdit_7.setText(_translate("MainWindow", "liens"))
        self.pushButton_8.setText(_translate("MainWindow", "Supprimer"))
        self.lineEdit_8.setText(_translate("MainWindow", "noeudA"))
        self.pushButton_9.setText(_translate("MainWindow", "Ajouter"))
        self.lineEdit_9.setText(_translate("MainWindow", "noeud A"))
        self.lineEdit_10.setText(_translate("MainWindow", "noeud B"))
        self.label_9.setText(_translate("MainWindow", ""))
        self.label_10.setText(_translate("MainWindow", ""))
        self.T10.setText(_translate("MainWindow", "10"))
        self.T20.setText(_translate("MainWindow", "20"))
        self.T30.setText(_translate("MainWindow", "30"))
        self.T50.setText(_translate("MainWindow", "50"))
        self.pushButton_4.setText(_translate("MainWindow", "Recherche"))
        self.lineEdit.setText(_translate("MainWindow", "noeud"))
        self.pushButton_5.setText(_translate("MainWindow", "Recherche"))
        self.lineEdit_2.setText(_translate("MainWindow", "noeud A"))
        self.lineEdit_3.setText(_translate("MainWindow", "noeud B"))
        self.label_11.setText(_translate("MainWindow", "temp : "))

    def crerr_un_graphe(self):
            start = time.time()
            global graph
            global M
            if (self.T10.isChecked() == True):
                    N = 10
                    M= np.full(shape=(N, N), fill_value=0, dtype=int)
                    for i in range(N):
                            for j in range(i + 1, N):
                                    M[i][j] = int(random.randint(0, 1))
                                    M[j][i] = M[i][j]
                    print(M)
                    # ------graphe

                    graph = pydot.Dot("mehrez", graph_type='graph')
                    for i in range(N):
                            graph.add_node(pydot.Node(str(i + 1)))
                            for j in range(i + 1, N):
                                    if M[i][j] == 1:
                                            d = j + 1
                                            s = i + 1
                                            graph.add_edge(pydot.Edge(str(s), str(d), color="blue"))
            if (self.T20.isChecked() == True):
                    N = 20
                    M = np.full(shape=(N, N), fill_value=0, dtype=int)
                    for i in range(N):
                            for j in range(i + 1, N):
                                    M[i][j] = int(random.randint(0, 1))
                                    M[j][i] = M[i][j]
                    print(M)
                    # ------graphe

                    graph = pydot.Dot("mehrez", graph_type='graph')
                    for i in range(N):
                            graph.add_node(pydot.Node(str(i + 1)))
                            for j in range(i + 1, N):
                                    if M[i][j] == 1:
                                            d = j + 1
                                            s = i + 1
                                            graph.add_edge(pydot.Edge(str(s), str(d), color="blue"))
            if (self.T30.isChecked() == True):
                    N = 30
                    M = np.full(shape=(N, N), fill_value=0, dtype=int)
                    for i in range(N):
                            for j in range(i + 1, N):
                                    M[i][j] = int(random.randint(0, 1))
                                    M[j][i] = M[i][j]
                    print(M)
                    # ------graphe

                    graph = pydot.Dot("mehrez", graph_type='graph')
                    for i in range(N):
                            graph.add_node(pydot.Node(str(i + 1)))
                            for j in range(i + 1, N):
                                    if M[i][j] == 1:
                                            d = j + 1
                                            s = i + 1
                                            graph.add_edge(pydot.Edge(str(s), str(d), color="blue"))
            if (self.T50.isChecked() == True):
                    N = 50
                    M = np.full(shape=(N, N), fill_value=0, dtype=int)
                    for i in range(N):
                            for j in range(i + 1, N):
                                    M[i][j] = int(random.randint(0, 1))
                                    M[j][i] = M[i][j]
                    print(M)
                    # ------graphe

                    graph = pydot.Dot("mehrez", graph_type='graph')
                    for i in range(N):
                            graph.add_node(pydot.Node(str(i + 1)))
                            for j in range(i + 1, N):
                                    if M[i][j] == 1:
                                            d = j + 1
                                            s = i + 1
                                            graph.add_edge(pydot.Edge(str(s), str(d), color="blue"))
            end = time.time()
            temp = end - start
            temp = "{0:.5f}".format(temp)
            self.textEdit_22.setText(str(temp))

            return (graph,M)
    def resu(self):
            g=self.crerr_un_graphe()
            g[0].write_png("GraG.png")
            GG = QPixmap("GraG.png")
            self.label_10.setPixmap(GG)
    def densite(self ):
            start = time.time()
            s = 0
            x = len(M)
            for i in range(x):
                    for j in range(x):
                            s = s + M[i][j]
            d = s / (x * (x - 1))
            d="{0:.5f}".format(d)
            self.textEdit.setText(str(d))
            end = time.time()
            temp = end - start
            temp = "{0:.5f}".format(temp)
            self.textEdit_22.setText(str(temp))
    def ini(self):
            n=len(M)
            for i in range(n):
                    graph.get_node((str(i + 1)))[0].set_color("black")
                    for j in range(i + 1, n):
                            if M[i][j] == 1:
                                    d = j + 1
                                    s = i + 1
                                    graph.get_edge(str(s), str(d))[0].set_color("blue")
            return graph
    def RN(self):
            start = time.time()
            Z=self.lineEdit.text()
            graph.get_node(Z)[0].set_color("red")
            n=len(M)
            for j in range(n):
                    l = int(Z) - 1
                    if M[l][j] == 1:
                            d = j + 1
                            graph.get_node(str(d))[0].set_color("yellow")
            graph.write_png("recher.png")
            GG = QPixmap("recher.png")
            self.label_9.setPixmap(GG)
            end = time.time()
            temp = end - start
            temp = "{0:.5f}".format(temp)
            self.textEdit_22.setText(str(temp))
            self.ini()
    def ch(self):
            start = time.time()
            X = nx.drawing.nx_pydot.from_pydot(graph)
            a=self.lineEdit_2.text()
            b=self.lineEdit_3.text()
            r = nx.shortest_path(X, a, b, weight="weight")
            for i in r:
                    graph.get_node(i)[0].set_color("red")
            for i in range(len(r) - 1):
                    graph.get_edge(r[i], r[i + 1])[0].set_color("red")
            graph.write_png("ch.png")
            GG = QPixmap("ch.png")
            self.label_9.setPixmap(GG)
            end = time.time()
            temp = end - start
            temp = "{0:.5f}".format(temp)
            self.textEdit_22.setText(str(temp))
            self.ini()
    def chc(self):
            start = time.time()
            X = nx.drawing.nx_pydot.from_pydot(graph)
            a=self.lineEdit_4.text()
            b=self.lineEdit_5.text()
            r = nx.shortest_path(X, a, b, weight="weight")
            for i in r:
                    graph.get_node(i)[0].set_color("red")
            for i in range(len(r) - 1):
                    graph.get_edge(r[i], r[i + 1])[0].set_color("red")
            graph.write_png("chc.png")
            GG = QPixmap("chc.png")
            self.label_9.setPixmap(GG)
            end = time.time()
            temp = end - start
            temp = "{0:.5f}".format(temp)
            self.textEdit_22.setText(str(temp))
            self.ini()
    def supN(self):
            start = time.time()
            N=len(M)
            a=self.lineEdit_8.text()
            print(a)
            for i in range(N):
                    M[int(a) - 1][i] = 0
                    M[i][int(a) - 1] = 0
            supn = pydot.Dot("supn", graph_type='graph')
            for i in range(N):
                    if i != int(a) - 1:
                            supn.add_node(pydot.Node(str(i + 1)))
                    for j in range(i + 1, N):
                            if M[i][j] == 1:
                                    d = j + 1
                                    s = i + 1
                                    supn.add_edge(pydot.Edge(str(s), str(d), color="blue"))
            supn.write_png("supn.png")
            GG = QPixmap("supn.png")
            self.label_9.setPixmap(GG)
            end = time.time()
            temp = end - start
            temp = "{0:.5f}".format(temp)
            self.textEdit_22.setText(str(temp))
            return M
    def Ajouter_un_lien(self):
            start = time.time()
            a=self.lineEdit_9.text()
            b=self.lineEdit_10.text()
            M[int(a) - 1][int(b) - 1] = 1
            M[int(b) - 1][int(a) - 1] = 1
            graph.add_edge(pydot.Edge(str(a), str(b), color="yellow"))
            graph.write_png("Ajouter_un_lien.png")
            GG = QPixmap("Ajouter_un_lien.png")
            self.label_9.setPixmap(GG)
            end = time.time()
            temp = end - start
            temp = "{0:.5f}".format(temp)
            self.textEdit_22.setText(str(temp))
    def Ajouter_un_noeud(self):
            start = time.time()
            s = self.lineEdit_6.text()
            graph.add_node(pydot.Node(s))
            a = self.lineEdit_7.text()
            for i in range(len(a)):
                    b = a[i]
                    graph.add_edge(pydot.Edge(s, b, color="yellow"))
            graph.write_png("Ajouter_un_nœud.png")
            GG = QPixmap("Ajouter_un_nœud.png")
            self.label_9.setPixmap(GG)
            end = time.time()
            temp = end - start
            temp = "{0:.5f}".format(temp)
            self.textEdit_22.setText(str(temp))




app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())