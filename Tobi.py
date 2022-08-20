import sys, time

from Packet import *
from Kamui import *
from GUI import *

from PySide2.QtCore import *

from multiprocessing import Process, Queue
from threading import Thread


def RunApp(packetQueue, filterQueue):
    kamui = Kamui()
    filters = list()
    count = 0

    while True:
        buffer = kamui.recv()

        count += 1

        packetQueue.put(buffer) #The UI will refer to this queue to update

        #Analyze packets
        pkt = Packet(buffer, count)

        while not filterQueue.empty():
            filter = Filter(filterQueue.get())
            filters.append(filter)

        allow = analyzePacket(filters, pkt)

        if allow: #ip.src=8.8.8.8
            kamui.send(buffer)


class Filter():
    def __init__(self, filters):
        self.filtersDict = {"ip.src": "", "ip.dst": "", "port.src": "", "port.dst": ""}

        for filter in filters.split(' '):
            filter = filter.split('=')
            key = filter[0]
            value = filter[1]

            if key in self.filtersDict:
                self.filtersDict[key] = value

    def check(self, pkt: Packet) -> bool:
        for k, v in self.filtersDict.items():
            if k == "ip.src": #There should be a check making sure the ip.src exists in the packet
                if pkt.src == v:
                    return False
            if k == "ip.dst":
                if pkt.dst == v:
                    return False
        return True


def analyzePacket(filters: list, pkt: Packet) -> bool:
    for filter in filters:
        if not filter.check(pkt): #If the check doesn't pass
            return False
    return True


def updateUI(packetQueue, controller):
    while True:
        if packetQueue:
            time.sleep(0.1) #Slows down the UI to not make it crash
            
            buffer = packetQueue.get()
            controller.addPkt(buffer)


if __name__ == "__main__":
    packetQueue = Queue()
    filterQueue = Queue()

    model = Model() #Prepare the queue for packets
    controller = Controller(model, filterQueue) #Create Controller

    #Prepare the View
    app = QApplication(sys.argv)
    mainWindow = QWidget()
    view = View(controller)
    view.setupUi(mainWindow)

    controller.setView(view)

    #Run the TUN interface on its own process
    Process(target=RunApp, args=(packetQueue, filterQueue, )).start()

    mainWindow.show()

    #Open a thread to put items in the list view (using only a thread for this and not a process)
    Thread(target=updateUI, args=(packetQueue, controller, )).start()

    app.exec_()