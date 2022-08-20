# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowrUrjBj.ui'
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
        Dialog.resize(976, 682)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.removeFilterButton = QPushButton(Dialog)
        self.removeFilterButton.setObjectName(u"removeFilterButton")

        self.gridLayout_4.addWidget(self.removeFilterButton, 0, 1, 1, 1)

        self.addFilterButton = QPushButton(Dialog)
        self.addFilterButton.setObjectName(u"addFilterButton")

        self.gridLayout_4.addWidget(self.addFilterButton, 0, 0, 1, 1)

        self.startCaptureButton = QPushButton(Dialog)
        self.startCaptureButton.setObjectName(u"startCaptureButton")

        self.gridLayout_4.addWidget(self.startCaptureButton, 1, 0, 1, 1)

        self.openPacketButton = QPushButton(Dialog)
        self.openPacketButton.setObjectName(u"openPacketButton")

        self.gridLayout_4.addWidget(self.openPacketButton, 1, 1, 1, 1)

        self.filtersListView = QListView(Dialog)
        self.filtersListView.setObjectName(u"filtersListView")

        self.gridLayout_4.addWidget(self.filtersListView, 0, 2, 2, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.packetsListView = QListView(Dialog)
        self.packetsListView.setObjectName(u"packetsListView")

        self.gridLayout_3.addWidget(self.packetsListView, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hideBlockedPktcheckBox = QCheckBox(Dialog)
        self.hideBlockedPktcheckBox.setObjectName(u"hideBlockedPktcheckBox")

        self.horizontalLayout.addWidget(self.hideBlockedPktcheckBox)

        self.UIprogressBar = QProgressBar(Dialog)
        self.UIprogressBar.setObjectName(u"UIprogressBar")
        self.UIprogressBar.setValue(24)

        self.horizontalLayout.addWidget(self.UIprogressBar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.removeFilterButton.setText(QCoreApplication.translate("Dialog", u"Remove Filter", None))
        self.addFilterButton.setText(QCoreApplication.translate("Dialog", u"Add filter", None))
        self.startCaptureButton.setText(QCoreApplication.translate("Dialog", u"STOP", None))
        self.openPacketButton.setText(QCoreApplication.translate("Dialog", u"Open Packet", None))
        self.hideBlockedPktcheckBox.setText(QCoreApplication.translate("Dialog", u"Hide blocked packets", None))
    # retranslateUi

