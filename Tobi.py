import sys, time

from Packet import *
from Kamui import *
from GUI import *

from PySide2.QtCore import *

from multiprocessing import Process, Queue
from threading import Thread


def RunApp(packetQueue):
    kamui = Kamui()
    count = 0

    while True:
        buffer = kamui.recv()

        count += 1

        packetQueue.put(buffer) #The UI will refer to this queue to update

        #Analyze packets HERE
        pkt = Packet(buffer, count)
        filter = Filter("ip.src=8.8.8.8")
        filters = [filter]

        allow = analyzePacket(filters, pkt)

        if allow:
            kamui.send(buffer)


class Filter():
    def __init__(self, filters):
        self.filtersDict = {"ip.src": list(), "port": list()}

        for filter in filters.split(' '):
            filter = filter.split('=')
            key = filter[0]
            value = filter[1]

            if key in self.filtersDict:
                self.filtersDict[key].append(value)

    def check(self, pkt: Packet) -> bool:
        for k in self.filtersDict.keys():
            if k == "ip.src": #There should be a check making sure the ip.src exists in the packet
                for condition in self.filtersDict[k]:
                    if pkt.src == condition:
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

    model = Model() #Prepare the queue for packets
    controller = Controller(model) #Create Controller

    #Prepare the View
    app = QApplication(sys.argv)
    mainWindow = QWidget()
    view = View(controller)
    view.setupUi(mainWindow)

    controller.setView(view)

    #Run the TUN interface on its own process
    Process(target=RunApp, args=(packetQueue, )).start()

    mainWindow.show()

    #Open a thread to put items in the list view (using only a thread for this and not a process)
    Thread(target=updateUI, args=(packetQueue, controller, )).start()

    app.exec_()