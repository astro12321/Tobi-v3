import sys
import time

from Packet import *
from Kamui import *
from GUI import *

from PySide2 import QtGui
from PySide2.QtCore import *

from scapy.all import raw
from multiprocessing import Process, Queue, Array
from threading import Thread


def RunApp(packetQueueIn, packetQueueOut):
    kamui = Kamui()

    while True:
        buffer = kamui.recv()

        packetQueueIn.put(buffer)

        if packetQueueOut:
            kamui.send(packetQueueOut.get())


def updateUI(packetQueueForUI, view, model):
    count = 0

    while True:
        if packetQueueForUI:
            time.sleep(0.05) #Slows down the UI to not make it crash (0.05s seems like the sweet spot)
            count += 1


            #buffer = packetQueueIn.get()
            #packetQueueIn.put(buffer)


            #model.addPkt(buffer) #This lags out the app (because of the sleep)


            pkt = Packet(count, packetQueueForUI.get())
            #pkt = Packet(count, packetQueueIn.get())
            view.packetsListViewModel.appendRow(QtGui.QStandardItem(f"{pkt.index}. {pkt.resume()}"))



def analyzePkt(packetQueueIn, packetQueueOut, packetQueueForUI):
    while True:
        if packetQueueIn:
            buffer = packetQueueIn.get()

            #Analayze packet
            pkt = Packet(1, buffer)

            packetQueueForUI.put(buffer)
            packetQueueOut.put(buffer)


if __name__ == "__main__":
    packetQueueIn = Queue() #The queue in which the packets are entering in the TUN interface
    packetQueueOut = Queue() #The queue containing only the packets we want to use
    packetQueueForUI = Queue() #The queue containing only the packets we want to show in the UI

    model = Model(packetQueueOut) #Prepare the queue for packets

    controller = Controller(model) #Create Controller

    #Prepare the View
    app = QApplication(sys.argv)
    mainWindow = QWidget()
    view = View(controller)
    view.setupUi(mainWindow)

    controller.setView(view)

    #Run the TUN interface on its own process
    Process(target=RunApp, args=(packetQueueIn, packetQueueOut, )).start()
    Process(target=analyzePkt, args=(packetQueueIn, packetQueueOut, packetQueueForUI, )).start()

    mainWindow.show()

    #Open a thread to put items in the list view (using only a thread for this and not a process)
    Thread(target=updateUI, args=(packetQueueForUI, view, model, )).start()


    

    app.exec_()