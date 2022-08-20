from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


#This UI is generated by QTDesigner, and modified by the child class View
class MainWindowUI():
    def setupUi(self, Dialog, width, height):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(width, height)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 10, width, height))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.packetsListView = QListView(self.verticalLayoutWidget)
        self.packetsListView.setObjectName(u"packetsListView")

        self.gridLayout.addWidget(self.packetsListView, 4, 0, 1, 4)

        self.filtersListView = QListView(self.verticalLayoutWidget)
        self.filtersListView.setObjectName(u"filtersListView")

        self.gridLayout.addWidget(self.filtersListView, 1, 3, 2, 1)

        self.startCaptureButton = QPushButton(self.verticalLayoutWidget)
        self.startCaptureButton.setObjectName(u"startCaptureButton")

        self.gridLayout.addWidget(self.startCaptureButton, 2, 1, 1, 1)

        self.openPacketButton = QPushButton(self.verticalLayoutWidget)
        self.openPacketButton.setObjectName(u"stopCaptureButton")
        

        self.gridLayout.addWidget(self.openPacketButton, 2, 2, 1, 1)

        self.removeFilterButton = QPushButton(self.verticalLayoutWidget)
        self.removeFilterButton.setObjectName(u"removeFilterButton")

        self.gridLayout.addWidget(self.removeFilterButton, 1, 2, 1, 1)

        self.addFilterButton = QPushButton(self.verticalLayoutWidget)
        self.addFilterButton.setObjectName(u"addFilterButton")

        self.gridLayout.addWidget(self.addFilterButton, 1, 1, 1, 1)

        self.titleLabel = QLabel(self.verticalLayoutWidget)
        self.titleLabel.setObjectName(u"titleLabel")

        self.gridLayout.addWidget(self.titleLabel, 3, 1, 1, 3, Qt.AlignHCenter)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Tobi", None))
        self.startCaptureButton.setText(QCoreApplication.translate("Dialog", u"STOP", None))
        self.openPacketButton.setText(QCoreApplication.translate("Dialog", u"Open Packet", None))
        self.removeFilterButton.setText(QCoreApplication.translate("Dialog", u"Remove Filter", None))
        self.addFilterButton.setText(QCoreApplication.translate("Dialog", u"Add filter", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"Packet Capture", None))