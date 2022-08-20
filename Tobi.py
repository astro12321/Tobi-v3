import sys, time

from Packet import *
from Kamui import *
from GUI import *
from Filter import *

from PySide2.QtCore import *

from multiprocessing import Process, Queue #Gotta use Queue and not SimpleQueue
from threading import Thread


def RunApp(packetQueue, filterQueue):
    kamui = Kamui()
    filters = list()
    count = 0

    while True:
        while not filterQueue.empty(): #Verify if the filters have been updated
            value = filterQueue.get()

            #If the item in the queue is an int, remove the filter at the index in the list, if not, add the filter
            if isinstance(value, int):
                filters.pop(value)
            else:
                filters.append(Filter(value))

        buffer = kamui.recv()

        count += 1

        #Analyze packets
        allow = analyzePacket(filters, Packet(buffer, count))

        packetQueue.put([allow, buffer]) #The UI will refer to this queue to update, it contains the buffer and the packet status (allow or not)

        if allow:
            kamui.send(buffer)


def analyzePacket(filters: list, pkt: Packet) -> bool:
    for filter in filters:
        if not filter.check(pkt): #If the filter check doesn't pass
            return False
    return True


def updateUI(packetQueue, controller):
    while True:
        if not packetQueue.empty():
            time.sleep(0.1) #Slows down the UI to not make it crash
            
            pktSkeleton = packetQueue.get()
            pktAllow = pktSkeleton[0]
            buffer = pktSkeleton[1]
            controller.addPkt(pktAllow, buffer)


if __name__ == "__main__":
    packetQueue = Queue()
    filterQueue = Queue()

    model = Model()
    view = View()
    controller = Controller(model, view, filterQueue)
    view.setController(controller)
    app = QApplication(sys.argv)
    mainWindow = QWidget()
    view.setupUi(mainWindow)

    #Run the TUN interface on its own process
    Process(target=RunApp, args=(packetQueue, filterQueue, )).start()

    mainWindow.show()

    #Open a thread to put items in the list view (using only a thread for this and not a process)
    Thread(target=updateUI, args=(packetQueue, controller, )).start()

    app.exec_()