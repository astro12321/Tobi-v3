import sys

from scapy.all import raw
from threading import Thread

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Packet import *
from Kamui import *
from GUI import *


def RunApp(kamui: Kamui, model: Model, controller: Controller):
    while True:
        buffer = kamui.recv()

        model.addPkt(buffer) #Adding the packet to the queue
        controller.notifyItemAdded() #This method act a bit like a user, so we need to interact with the controller (tell him it needs to display a new packet)

        #When the user will be able to drop packets, there will need to be a condition here to verify if the queue is not empty
        kamui.send(model.getPkt().raw)


if __name__ == "__main__":
    model = Model() #Prepare the queue for packets
    kamui = Kamui() #Prepare TUN interface

    controller = Controller(model) #Create Controller

    #Prepare the View
    app = QApplication(sys.argv)
    mainWindow = QWidget()
    view = View(controller)
    view.setupUi(mainWindow)

    controller.setView(view)

    #Run the TUN interface
    thr = Thread(target=RunApp, args=(kamui, model, controller, )).start()

    mainWindow.show()
    app.exec_()