# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
import os
import glob
import json
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(628, 473)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_info = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_info.setFont(font)
        self.groupBox_info.setObjectName("groupBox_info")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_info)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.checkBox_pbtxt = QtWidgets.QCheckBox(self.groupBox_info)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_pbtxt.setFont(font)
        self.checkBox_pbtxt.setObjectName("checkBox_pbtxt")
        self.gridLayout.addWidget(self.checkBox_pbtxt, 1, 1, 1, 1)
        self.formLayout_info = QtWidgets.QFormLayout()
        self.formLayout_info.setObjectName("formLayout_info")
        self.label_ImgDir = QtWidgets.QLabel(self.groupBox_info)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_ImgDir.setFont(font)
        self.label_ImgDir.setObjectName("label_ImgDir")
        self.formLayout_info.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_ImgDir)
        self.pushButton_ImgDir = QtWidgets.QPushButton(self.groupBox_info)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.pushButton_ImgDir.setFont(font)
        self.pushButton_ImgDir.setText("")
        self.pushButton_ImgDir.setObjectName("pushButton_ImgDir")
        self.formLayout_info.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton_ImgDir)
        self.label_Outpath = QtWidgets.QLabel(self.groupBox_info)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_Outpath.setFont(font)
        self.label_Outpath.setObjectName("label_Outpath")
        self.formLayout_info.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_Outpath)
        self.pushButton_Outpath = QtWidgets.QPushButton(self.groupBox_info)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.pushButton_Outpath.setFont(font)
        self.pushButton_Outpath.setText("")
        self.pushButton_Outpath.setObjectName("pushButton_Outpath")
        self.formLayout_info.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_Outpath)
        self.label_pbtxt = QtWidgets.QLabel(self.groupBox_info)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_pbtxt.setFont(font)
        self.label_pbtxt.setObjectName("label_pbtxt")
        self.formLayout_info.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_pbtxt)
        self.pushButton_pbtxt = QtWidgets.QPushButton(self.groupBox_info)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.pushButton_pbtxt.setFont(font)
        self.pushButton_pbtxt.setText("")
        self.pushButton_pbtxt.setObjectName("pushButton_pbtxt")
        self.formLayout_info.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton_pbtxt)
        self.gridLayout.addLayout(self.formLayout_info, 0, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_info)
        self.groupBox_Ratio = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Ratio.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        
        
        self.groupBox_Ratio.setFont(font)
        self.groupBox_Ratio.setObjectName("groupBox_Ratio")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_Ratio)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_Ratio = QtWidgets.QFormLayout()
        self.formLayout_Ratio.setObjectName("formLayout_Ratio")
        self.label_TrainRatio = QtWidgets.QLabel(self.groupBox_Ratio)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_TrainRatio.setFont(font)
        self.label_TrainRatio.setObjectName("label_TrainRatio")
        self.formLayout_Ratio.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_TrainRatio)
        self.spinBox_TrainRatio = QtWidgets.QSpinBox(self.groupBox_Ratio)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_TrainRatio.setFont(font)
        self.spinBox_TrainRatio.setObjectName("spinBox_TrainRatio")
        self.formLayout_Ratio.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_TrainRatio)
        self.label_ValidateRatio = QtWidgets.QLabel(self.groupBox_Ratio)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_ValidateRatio.setFont(font)
        self.label_ValidateRatio.setObjectName("label_ValidateRatio")
        self.formLayout_Ratio.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_ValidateRatio)
        self.spinBox_ValidateRatio = QtWidgets.QSpinBox(self.groupBox_Ratio)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_ValidateRatio.setFont(font)
        self.spinBox_ValidateRatio.setObjectName("spinBox_ValidateRatio")
        self.formLayout_Ratio.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_ValidateRatio)
        self.label_TestRatio = QtWidgets.QLabel(self.groupBox_Ratio)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_TestRatio.setFont(font)
        self.label_TestRatio.setObjectName("label_TestRatio")
        self.formLayout_Ratio.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_TestRatio)
        self.spinBox_TestRatio = QtWidgets.QSpinBox(self.groupBox_Ratio)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox_TestRatio.setFont(font)
        self.spinBox_TestRatio.setObjectName("spinBox_TestRatio")
        self.formLayout_Ratio.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox_TestRatio)
        self.gridLayout_2.addLayout(self.formLayout_Ratio, 0, 0, 1, 1)
        self.tableWidget_Object = QtWidgets.QTableWidget(self.groupBox_Ratio)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget_Object.setFont(font)
        self.tableWidget_Object.setObjectName("tableWidget_Object")
        self.tableWidget_Object.setColumnCount(0)
        self.tableWidget_Object.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget_Object, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_Ratio)
        
        self.pushButton_run = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_run.setFont(font)
        self.pushButton_run.setObjectName("pushButton_run")
        self.verticalLayout.addWidget(self.pushButton_run)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 628, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #set infomation
        self.pushButton_pbtxt.pressed.connect(lambda: self.Input_Images(self.pushButton_pbtxt))
        self.pushButton_Outpath.pressed.connect(lambda: self.Input_ImageFiles(self.pushButton_Outpath))
        self.pushButton_ImgDir.pressed.connect(lambda: self.Input_ImageFiles(self.pushButton_ImgDir))
        
        #set ratio
        self.spinBox_TrainRatio.setValue(50)
        self.spinBox_TrainRatio.setSingleStep(1)
        self.spinBox_TrainRatio.setRange(0,100)
        self.spinBox_TrainRatio.valueChanged.connect(self.ratioCheck)
        
        self.spinBox_ValidateRatio.setValue(30)
        self.spinBox_ValidateRatio.setSingleStep(1)
        self.spinBox_ValidateRatio.setRange(0,100)
        self.spinBox_ValidateRatio.valueChanged.connect(self.ratioCheck)
        
        self.spinBox_TestRatio.setValue(20)
        self.spinBox_TestRatio.setSingleStep(1)
        self.spinBox_TestRatio.setRange(0,100)
        self.spinBox_TestRatio.valueChanged.connect(self.ratioCheck)
        
        self.pushButton_run.pressed.connect(self.Run)
        
    def ratioCheck(self):
        t1 = int(self.spinBox_TrainRatio.value())
        t2 = int(self.spinBox_ValidateRatio.value())
        t3 = int(self.spinBox_TestRatio.value())
        if t1+t2+t3!=100:
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        else:
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
            
        self.spinBox_TrainRatio.setPalette(palette)        
        self.spinBox_ValidateRatio.setPalette(palette)        
        self.spinBox_TestRatio.setPalette(palette)        
            
    
    def Run(self):
        if self.pushButton_pbtxt.text()==""  and self.checkBox_pbtxt.isChecked()==False: return
        if self.pushButton_Outpath.text()=="" : return
        if self.pushButton_ImgDir.text()=="" : return
        t1 = round(float(self.spinBox_TrainRatio.value())/100,2)
        t2 = round(float(self.spinBox_ValidateRatio.value())/100,2)
        t3 = round(float(self.spinBox_TestRatio.value())/100,2)
        print("t1,t2,t3=",(t1,t2,t3))
        if t1+t2+t3!=1: return
        
        ImgDir = os.path.relpath(self.pushButton_ImgDir.text())
        Outpath= os.path.relpath(self.pushButton_Outpath.text())
        if self.checkBox_pbtxt.isChecked():
            pbtxt  = self.Create_pbtxt(ImgDir, Outpath)
        else:
            pbtxt  = os.path.relpath(self.pushButton_pbtxt.text())
        batcmd='python _Function\create_tf_record.py {0} {1} {2} --images_dir="{3}" --annotations_json_dir="{3}" --label_map_path="{4}" --output_path="{5}"'.format(t1, t2, t3, ImgDir, pbtxt, Outpath)
        print(batcmd)
        A = subprocess.check_output(batcmd, shell=True,stderr=subprocess.STDOUT)
        T = A.decode(encoding='utf-8').split("\r\n")[-2]
        exec(T)
        self.setTableInfo(eval(T.split("=")[0]))
        #DirNum = eval(A[7:-2])

        #os.system('python _Function\create_tf_record.py {0} {1} {2} --images_dir="{3}" --annotations_json_dir="{3}" --label_map_path="{4}" --output_path="{5}"'.
        #          format(t1, t2, t3, ImgDir, pbtxt, Outpath))
        #DirNum[0]["TT"]=20
    def setTableInfo(self, DirNum):
        self.tableWidget_Object.clear()
        TypeNum = 0
        TypeList = []
        for Dir in DirNum:
            if len(Dir.keys())> TypeNum:
                TypeNum = len(Dir.keys())
                TypeList = []
                for key in Dir.keys():
                    TypeList.append(str(key))

        self.tableWidget_Object.setColumnCount(TypeNum)
        self.tableWidget_Object.setRowCount(3)
        self.tableWidget_Object.setVerticalHeaderLabels(["Train","Validate","Test"])
        self.tableWidget_Object.setHorizontalHeaderLabels(TypeList)
        for colume in range(TypeNum):
            for row in range(3):
                name = TypeList[colume]
                print((row,colume),"  ",name)
                w = str(DirNum[row].get(name,"0"))
                item = QTableWidgetItem(w)
                item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                self.tableWidget_Object.setItem(row,colume, item)

    def Create_pbtxt(self, Imgpath, Outpath):
        annotations_json_path = []
        for root, dirs, files in os.walk(Imgpath):
          for f in files:
            fullpath = os.path.join(root, f)
            if ".json" in fullpath: 
                annotations_json_path.append(fullpath)        
        
        Name = []
        for json_path in annotations_json_path:
            with open(json_path, 'r') as f:
                json_text = json.load(f)
                shapes = json_text.get('shapes', None)
                for shape in shapes:
                    if shape["label"] not in Name: Name.append(shape["label"])
                    
        fo = open(Outpath+os.sep+"path_to_label_map.pbtxt", "w")
        for i, name in enumerate(Name):
            fo.write("item { \n")
            fo.write("        id: {0}\n".format(i+1))
            fo.write("        name: '{0}'\n".format(name))
            fo.write("}\n")
            fo.write("\n")
        fo.close()
        return Outpath+os.sep+"path_to_label_map.pbtxt"
    
    def Input_Images(self, btn):
        fileName_choose, filetype = QFileDialog.getOpenFileNames(self,  
                                    "Input pbtxt",  
                                    ".", # 起始路径 
                                    "pbtxt Files (*.pbtxt);;All Files (*)")   # 设置文件扩展名过滤,用双分号间隔

        if not fileName_choose: return
        btn.setText(fileName_choose[0])
        
    def Input_ImageFiles(self, btn):
        dir_choose = QFileDialog.getExistingDirectory(self,  
                                    "Choose Dir ",  
                                    ".") # 起始路径
        if not dir_choose: return
        btn.setText(dir_choose)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Label2tf"))
        self.groupBox_info.setTitle(_translate("MainWindow", "Infomatio"))
        self.checkBox_pbtxt.setText(_translate("MainWindow", "pbtxt autoProduct"))
        self.label_ImgDir.setText(_translate("MainWindow", "Image Dir: "))
        self.label_Outpath.setText(_translate("MainWindow", "Output Path: "))
        self.label_pbtxt.setText(_translate("MainWindow", "Input pbtxt"))
        self.groupBox_Ratio.setTitle(_translate("MainWindow", "Data Ratio"))
        self.label_TrainRatio.setText(_translate("MainWindow", "Train(%):"))
        self.label_ValidateRatio.setText(_translate("MainWindow", "Validate(%):"))
        self.label_TestRatio.setText(_translate("MainWindow", "Test(%):"))
        self.pushButton_run.setText(_translate("MainWindow", "Run"))

