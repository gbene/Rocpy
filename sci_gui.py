# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sci_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sciWindow(QtWidgets.QMainWindow):
    def setupUi(self, sciWindow):
        sciWindow.setObjectName("sciWindow")
        sciWindow.resize(1000, 703)
        sciWindow.setMinimumSize(QtCore.QSize(1000, 703))
        sciWindow.setMaximumSize(QtCore.QSize(1000, 703))
        self.centralwidget = QtWidgets.QWidget(sciWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridWidget = QtWidgets.QWidget(self.horizontalWidget)
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.gridWidget)
        self.label_5.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridWidget)
        self.label_10.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.gridWidget)
        self.label_6.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridWidget)
        self.label_8.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridWidget)
        self.label_4.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridWidget)
        self.label_7.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 5, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridWidget)
        self.label_9.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 7, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.gridWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.gridWidget)
        self.line = QtWidgets.QFrame(self.horizontalWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.gridWidget_2 = QtWidgets.QWidget(self.horizontalWidget)
        self.gridWidget_2.setObjectName("gridWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_16 = QtWidgets.QLabel(self.gridWidget_2)
        self.label_16.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 7, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridWidget_2)
        self.label_11.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.line_4 = QtWidgets.QFrame(self.gridWidget_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridWidget_2)
        self.label_15.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 6, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridWidget_2)
        self.label_13.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 4, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridWidget_2)
        self.label_14.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridWidget_2)
        self.label_17.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 8, 0, 1, 1)
        self.horizontalLayout.addWidget(self.gridWidget_2)
        self.line_2 = QtWidgets.QFrame(self.horizontalWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.gridWidget_3 = QtWidgets.QWidget(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget_3.sizePolicy().hasHeightForWidth())
        self.gridWidget_3.setSizePolicy(sizePolicy)
        self.gridWidget_3.setObjectName("gridWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridWidget_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Button025 = QtWidgets.QPushButton(self.gridWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button025.sizePolicy().hasHeightForWidth())
        self.Button025.setSizePolicy(sizePolicy)
        self.Button025.setObjectName("Button025")
        self.gridLayout_4.addWidget(self.Button025, 15, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Button25 = QtWidgets.QPushButton(self.gridWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button25.sizePolicy().hasHeightForWidth())
        self.Button25.setSizePolicy(sizePolicy)
        self.Button25.setObjectName("Button25")
        self.gridLayout_4.addWidget(self.Button25, 9, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 10, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem2, 16, 0, 1, 1)
        self.Button100 = QtWidgets.QPushButton(self.gridWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button100.sizePolicy().hasHeightForWidth())
        self.Button100.setSizePolicy(sizePolicy)
        self.Button100.setObjectName("Button100")
        self.gridLayout_4.addWidget(self.Button100, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 4, 0, 1, 1)
        self.Button250 = QtWidgets.QPushButton(self.gridWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button250.sizePolicy().hasHeightForWidth())
        self.Button250.setSizePolicy(sizePolicy)
        self.Button250.setObjectName("Button250")
        self.gridLayout_4.addWidget(self.Button250, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 6, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem5, 14, 0, 1, 1)
        self.Button1 = QtWidgets.QPushButton(self.gridWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button1.sizePolicy().hasHeightForWidth())
        self.Button1.setSizePolicy(sizePolicy)
        self.Button1.setObjectName("Button1")
        self.gridLayout_4.addWidget(self.Button1, 13, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Button50 = QtWidgets.QPushButton(self.gridWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button50.sizePolicy().hasHeightForWidth())
        self.Button50.setSizePolicy(sizePolicy)
        self.Button50.setObjectName("Button50")
        self.gridLayout_4.addWidget(self.Button50, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem6, 8, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 12, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Button5 = QtWidgets.QPushButton(self.gridWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button5.sizePolicy().hasHeightForWidth())
        self.Button5.setSizePolicy(sizePolicy)
        self.Button5.setObjectName("Button5")
        self.gridLayout_4.addWidget(self.Button5, 11, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.line_5 = QtWidgets.QFrame(self.gridWidget_3)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_4.addWidget(self.line_5, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.gridWidget_3)
        self.verticalLayout.addWidget(self.horizontalWidget)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.sciButtonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.sciButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.sciButtonBox.setObjectName("sciButtonBox")
        self.gridLayout_6.addWidget(self.sciButtonBox, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_20 = QtWidgets.QLabel(self.widget)
        self.label_20.setObjectName("label_20")
        self.gridLayout_6.addWidget(self.label_20, 0, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.widget)
        self.label_21.setObjectName("label_21")
        self.gridLayout_6.addWidget(self.label_21, 0, 0, 1, 1)
        self.sciBox = QtWidgets.QDoubleSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sciBox.sizePolicy().hasHeightForWidth())
        self.sciBox.setSizePolicy(sizePolicy)
        self.sciBox.setMinimumSize(QtCore.QSize(0, 0))
        self.sciBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.sciBox.setMaximum(10000000.0)
        self.sciBox.setObjectName("sciBox")
        self.gridLayout_6.addWidget(self.sciBox, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignRight)
        sciWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(sciWindow)
        QtCore.QMetaObject.connectSlotsByName(sciWindow)

    def retranslateUi(self, sciWindow):
        _translate = QtCore.QCoreApplication.translate
        sciWindow.setWindowTitle(_translate("sciWindow", "MainWindow"))
        self.label_5.setText(_translate("sciWindow", "Specimen requires many blows of a geological hammer to fracture it"))
        self.label_10.setText(_translate("sciWindow", "Indented by thumbnail"))
        self.label_2.setText(_translate("sciWindow", "Field Estimate of Strength"))
        self.label_6.setText(_translate("sciWindow", "Specimen requires more than one blow of a geological hammer to fracture it"))
        self.label_8.setText(_translate("sciWindow", "Can be peeled with a pocket knofe with difficulty, shallow indentation made by firm blow with point of a geological hammer"))
        self.label_4.setText(_translate("sciWindow", "Specimen can only be chipped with a geological hammer"))
        self.label_7.setText(_translate("sciWindow", "Cannot be scraped or peeled with a pocket knife, speciman can be fracuterd with a single blow from a geological hammer"))
        self.label_9.setText(_translate("sciWindow", "Crumbles under firm blows with point of a geological hammer, can be peeled by a pocket knife"))
        self.label_16.setText(_translate("sciWindow", "Highly weathered or altered rock."))
        self.label_11.setText(_translate("sciWindow", "Fresh basalt, chert, diabase, gneiss, granite, quarzite"))
        self.label.setText(_translate("sciWindow", "Examples"))
        self.label_15.setText(_translate("sciWindow", "Chalck, rocksalt, potash"))
        self.label_13.setText(_translate("sciWindow", "Limestone, marble, phyllite, sandstone, schist, shale."))
        self.label_14.setText(_translate("sciWindow", "Claystone, coal, concrete, schist, shale, silstone."))
        self.label_12.setText(_translate("sciWindow", "Amphibolite, sandstone, basalt, gabbro, gneiss, granodiorite, limestone, marble,rhyolite, tuff."))
        self.label_17.setText(_translate("sciWindow", "Stiff fault gouge"))
        self.Button025.setText(_translate("sciWindow", "0.25-1"))
        self.Button25.setText(_translate("sciWindow", "25-50"))
        self.Button100.setText(_translate("sciWindow", "100-250"))
        self.Button250.setText(_translate("sciWindow", ">250"))
        self.Button1.setText(_translate("sciWindow", "1-5"))
        self.Button50.setText(_translate("sciWindow", "50-100"))
        self.label_3.setText(_translate("sciWindow", "Strength (Mpa)"))
        self.Button5.setText(_translate("sciWindow", "5-25"))
        self.label_20.setText(_translate("sciWindow", "MPa"))
        self.label_21.setText(_translate("sciWindow", "Uniaxial compressive Strength (sigci)"))
