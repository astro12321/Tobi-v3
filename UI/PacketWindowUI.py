# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'packetxXudnd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class PacketWindowUI(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 19, 381, 261))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.contentTextEdit = QPlainTextEdit(self.verticalLayoutWidget)
        self.contentTextEdit.setObjectName(u"contentTextEdit")

        self.verticalLayout.addWidget(self.contentTextEdit)

        self.closeButton = QPushButton(self.verticalLayoutWidget)
        self.closeButton.setObjectName(u"closeButton")

        self.verticalLayout.addWidget(self.closeButton)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        self.closeButton.setText(QCoreApplication.translate("Dialog", u"Close", None))
    # retranslateUi


