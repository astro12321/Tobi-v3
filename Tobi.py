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

        kamui.send(buffer)


def updateUI(packetQueue, controller):
    while True:
        if packetQueue:
            time.sleep(0.05) #Slows down the UI to not make it crash (0.05s seems like the sweet spot)
            
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