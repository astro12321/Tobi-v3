from Packet import *
from Filter import *
from View import *


#Receive packets and analyze them
class Model:
    def __init__(self):
        self.packetQueue = list()

    def addPkt(self, pkt: Packet):
        self.packetQueue.append(pkt)

    def getPkt(self, ind=-1) -> Packet:
        if ind < 0 or ind > len(self.packetQueue) - 1:
            return None
        return self.packetQueue[ind]


#Receive data and modify the View
class Controller:
    def __init__(self, model: Model, view, filterQueue):
        self.model = model
        self.filterQueue = filterQueue
        self.view = view
        self.updateView = True
        self.hideBlockedPkt = False

    def addPkt(self, pktAllow: bool, buffer: bytes, packetQueueSize: int):
        pkt = Packet(buffer, len(self.model.packetQueue) + 1)

        #Modify model
        self.model.addPkt(pkt)

        #Set the progress bar
        curProgress = 100 - (packetQueueSize + len(self.model.packetQueue)) / len(self.model.packetQueue) + 1
        self.view.setProgressBar(curProgress)
        self.view.setProgressBarText(f"{len(self.model.packetQueue)} / {packetQueueSize + len(self.model.packetQueue)}    {int(curProgress)}%")

        #Modify view 
        if self.updateView:
            if self.hideBlockedPkt:
                if pktAllow:
                    self.view.addItemToPacketsListView(pktAllow, f"{pkt.index}. {pkt.resume()}")
            else:
                self.view.addItemToPacketsListView(pktAllow, f"{pkt.index}. {pkt.resume()}")

    def isPktQueueEmpty(self) -> bool:
        if self.model.packetQueue:
            return False
        return True

    def getPkt(self, ind=-1) -> Packet:
        return self.model.getPkt(ind)

    def toggleUpdateView(self) -> bool:
        self.updateView = not self.updateView
        return self.updateView

    def addFilter(self, filter: str):
        if not isFilterValid(filter):
            self.view.popUpMsgBox("Filter is invalid")
        else:
            self.filterQueue.put(filter)
            self.view.addItemToFiltersListView(filter)

    def removeFilter(self, ind: int):
        self.filterQueue.put(ind)

    def setHideBlockedPkt(self, state: bool):
        self.hideBlockedPkt = state