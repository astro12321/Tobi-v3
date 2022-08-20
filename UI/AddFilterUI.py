# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addFilterRreGHw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class AddFilterUI(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(512, 88)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addFilterLineEdit = QLineEdit(Dialog)
        self.addFilterLineEdit.setObjectName(u"addFilterLineEdit")

        self.verticalLayout.addWidget(self.addFilterLineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.addFilterButton = QPushButton(Dialog)
        self.addFilterButton.setObjectName(u"addFilterButton")

        self.horizontalLayout.addWidget(self.addFilterButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Add Filter", None))
        self.addFilterButton.setText(QCoreApplication.translate("Dialog", u"Add", None))
    # retranslateUi

