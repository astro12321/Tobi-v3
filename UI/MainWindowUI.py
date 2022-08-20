# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowpJopxP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class MainWindowUI(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(960, 693)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.titleLabel = QLabel(Dialog)
        self.titleLabel.setObjectName(u"titleLabel")

        self.gridLayout.addWidget(self.titleLabel, 3, 1, 1, 3, Qt.AlignHCenter)

        self.startCaptureButton = QPushButton(Dialog)
        self.startCaptureButton.setObjectName(u"startCaptureButton")

        self.gridLayout.addWidget(self.startCaptureButton, 2, 1, 1, 1)

        self.addFilterButton = QPushButton(Dialog)
        self.addFilterButton.setObjectName(u"addFilterButton")

        self.gridLayout.addWidget(self.addFilterButton, 1, 1, 1, 1)

        self.packetsListView = QListView(Dialog)
        self.packetsListView.setObjectName(u"packetsListView")

        self.gridLayout.addWidget(self.packetsListView, 4, 0, 1, 4)

        self.filtersListView = QListView(Dialog)
        self.filtersListView.setObjectName(u"filtersListView")

        self.gridLayout.addWidget(self.filtersListView, 1, 3, 2, 1)

        self.removeFilterButton = QPushButton(Dialog)
        self.removeFilterButton.setObjectName(u"removeFilterButton")

        self.gridLayout.addWidget(self.removeFilterButton, 1, 2, 1, 1)

        self.openPacketButton = QPushButton(Dialog)
        self.openPacketButton.setObjectName(u"openPacketButton")

        self.gridLayout.addWidget(self.openPacketButton, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"Packet Capture", None))
        self.startCaptureButton.setText(QCoreApplication.translate("Dialog", u"STOP", None))
        self.addFilterButton.setText(QCoreApplication.translate("Dialog", u"Add filter", None))
        self.removeFilterButton.setText(QCoreApplication.translate("Dialog", u"Remove Filter", None))
        self.openPacketButton.setText(QCoreApplication.translate("Dialog", u"Open Packet", None))
    # retranslateUi

