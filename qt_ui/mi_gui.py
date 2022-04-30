# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mi_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pickMi(object):
    def setupUi(self, pickMi):
        pickMi.setObjectName("pickMi")
        pickMi.resize(493, 766)
        self.centralwidget = QtWidgets.QWidget(pickMi)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rockLabel = QtWidgets.QLabel(self.centralwidget)
        self.rockLabel.setObjectName("rockLabel")
        self.verticalLayout.addWidget(self.rockLabel)
        self.rockCombo = QtWidgets.QComboBox(self.centralwidget)
        self.rockCombo.setObjectName("rockCombo")
        self.verticalLayout.addWidget(self.rockCombo)
        self.textureLabel = QtWidgets.QLabel(self.centralwidget)
        self.textureLabel.setObjectName("textureLabel")
        self.verticalLayout.addWidget(self.textureLabel)
        self.textureCombo = QtWidgets.QComboBox(self.centralwidget)
        self.textureCombo.setObjectName("textureCombo")
        self.verticalLayout.addWidget(self.textureCombo)
        self.miLabel = QtWidgets.QLabel(self.centralwidget)
        self.miLabel.setObjectName("miLabel")
        self.verticalLayout.addWidget(self.miLabel)
        self.miList = QtWidgets.QListWidget(self.centralwidget)
        self.miList.setObjectName("miList")
        self.verticalLayout.addWidget(self.miList)
        self.formWidget = QtWidgets.QWidget(self.centralwidget)
        self.formWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formWidget.sizePolicy().hasHeightForWidth())
        self.formWidget.setSizePolicy(sizePolicy)
        self.formWidget.setObjectName("formWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.formWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.miBox = QtWidgets.QTextEdit(self.formWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.miBox.sizePolicy().hasHeightForWidth())
        self.miBox.setSizePolicy(sizePolicy)
        self.miBox.setMaximumSize(QtCore.QSize(50, 30))
        self.miBox.setBaseSize(QtCore.QSize(0, 0))
        self.miBox.setFrameShape(QtWidgets.QFrame.Box)
        self.miBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.miBox.setReadOnly(False)
        self.miBox.setObjectName("miBox")
        self.gridLayout.addWidget(self.miBox, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.formWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 0, 3, 1, 1)
        self.miValue = QtWidgets.QLabel(self.formWidget)
        self.miValue.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.miValue.setObjectName("miValue")
        self.gridLayout.addWidget(self.miValue, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.formWidget)
        pickMi.setCentralWidget(self.centralwidget)

        self.retranslateUi(pickMi)
        QtCore.QMetaObject.connectSlotsByName(pickMi)

    def retranslateUi(self, pickMi):
        _translate = QtCore.QCoreApplication.translate
        pickMi.setWindowTitle(_translate("pickMi", "Pick mi value"))
        self.rockLabel.setText(_translate("pickMi", "Rock type"))
        self.textureLabel.setText(_translate("pickMi", "Texture"))
        self.miLabel.setText(_translate("pickMi", "List of Mi values"))
        self.miValue.setText(_translate("pickMi", "Selected mi value"))
