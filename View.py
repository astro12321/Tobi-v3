from GUI import *
from UI.MainWindowUI import *
from UI.PacketWindowUI import *
from UI.AddFilterUI import *

from PySide2 import QtGui

#This add and modifies functions to the UI class generated by QTDesigner
class View(MainWindowUI):
    def __init__(self):
        super().__init__()

        self.controller = None

    def setupUi(self, Dialog):
        super().setupUi(Dialog)

        #Set model on packet list view
        self.packetsListViewModel = QtGui.QStandardItemModel()
        self.packetsListView.setModel(self.packetsListViewModel)
        self.packetsListView.setEditTriggers(QAbstractItemView.NoEditTriggers) #Cannot edit list view

        #Set model on filters list view
        self.filtersListViewModel = QtGui.QStandardItemModel()
        self.filtersListView.setModel(self.filtersListViewModel)
        self.filtersListView.setEditTriggers(QAbstractItemView.NoEditTriggers) #Cannot edit list view

        self.openPacketButton.clicked.connect(self.popUpPacket) #Sets function on button to open packet        
        self.startCaptureButton.clicked.connect(self.toggleUpdateView) #Sets function on button to toggle capture
        self.addFilterButton.clicked.connect(self.popUpAddFilter) #Sets function on button to add filter
        self.removeFilterButton.clicked.connect(self.removeFilter)
        self.hideBlockedPktcheckBox.stateChanged.connect(self.hideBlockedPkt)

        self.UIprogressBar.setValue(0)

    def retranslateUi(self, Dialog):
        super().retranslateUi(Dialog)
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Tobi", None)) #Set windows title

    def hideBlockedPkt(self) -> bool:
        if self.hideBlockedPktcheckBox.isChecked():
            self.controller.setHideBlockedPkt(True)
        else:
            self.controller.setHideBlockedPkt(False)

    def popUpMsgBox(self, msg: str):
        msgBox = QMessageBox()
        msgBox.setText(msg)
        msgBox.exec()

    def setProgressBar(self, ind: int):
        self.UIprogressBar.setValue(ind)

    def setProgressBarText(self, desc: str):
        self.UIprogressBar.setFormat(desc)

    #Create the function to popup a window with the packet info
    def popUpPacket(self):
        if not self.controller.isPktQueueEmpty():
            pktIndex = int(self.packetsListView.currentIndex().data().split('.')[0]) - 1 #Only takes the first character of the line, which is the index of the packet in the queue
            pkt = self.controller.getPkt(pktIndex) #Not sure if this call respect MVC...
            if pkt: #If there's a packet and the controller didn't return None
                self.popUpwindow = QWidget()
                packetWindowObj = PacketWindow(self.popUpwindow, pkt) 
                packetWindowObj.setupUi(self.popUpwindow)
                self.popUpwindow.show()

    #Toggle the packet capture (only in the UI)
    def toggleUpdateView(self):
        toggleState = self.controller.toggleUpdateView()

        if toggleState:
            self.startCaptureButton.setText("STOP")
        elif not toggleState:
            self.startCaptureButton.setText("START")

    def addItemToPacketsListView(self, pktAllow: bool, desc: str):
        #if self.packetsListViewModel.rowCount() > 10: #Clear the listview if there's too much items, tend to make the app crash
        #    self.packetsListViewModel.clear()
        item = QtGui.QStandardItem(desc)

        if not pktAllow: #Set the color of the item if the packet is refused
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0)) #Red
            item.setBackground(brush)

        self.packetsListViewModel.appendRow(item)
        self.packetsListView.scrollToBottom()

    def addItemToFiltersListView(self, filter: str):
        item = QtGui.QStandardItem(filter)
        self.filtersListViewModel.appendRow(item)
        self.filtersListView.scrollToBottom()

    def popUpAddFilter(self):
        self.addFilterWindow = QWidget()
        self.addFilterObj = AddFilter(self.addFilterWindow, self.controller) 
        self.addFilterObj.setupUi(self.addFilterWindow)
        self.addFilterWindow.show()

    def removeFilter(self):
        filterIndex = self.filtersListView.currentIndex().row()
        if filterIndex >= 0:
            self.controller.removeFilter(filterIndex)
            self.filtersListViewModel.removeRow(filterIndex)

    def setController(self, controller):
        self.controller = controller


class PacketWindow(PacketWindowUI):
    def __init__(self, window, pkt):
        super().__init__()

        self.window = window
        self.pkt = pkt

    def setupUi(self, Dialog):
        super().setupUi(Dialog)

        #Modify packet text
        self.contentTextEdit.textCursor().insertText(self.pkt.show(dump=True))

        #The close button closes the window
        self.closeButton.clicked.connect(self.window.close)

    def retranslateUi(self, Dialog):
        super().retranslateUi(Dialog)

        #Set the window title
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", f"Packet {self.pkt.index}", None))


class AddFilter(AddFilterUI):
    def __init__(self, window, controller):
        super().__init__()

        self.controller = controller
        self.window = window

    def setupUi(self, Dialog):
        super().setupUi(Dialog)

        #Set focus on the lineEdit and add the filter if ENTER is pressed
        self.addFilterLineEdit.setFocus()
        self.addFilterLineEdit.returnPressed.connect(self.addFilterButton.click)

        self.addFilterButton.clicked.connect(self.addFilter)

    def addFilter(self):
        filter = self.addFilterLineEdit.text()
        self.controller.addFilter(filter)
        self.window.close()