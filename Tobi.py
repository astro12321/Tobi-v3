from scapy.all import raw
from threading import Thread

from Packet import *
from Kamui import *
from GUI import *


def RunApp(kamui, model, controller):
    while True:
        buffer = kamui.recv()

        model.addPkt(buffer) #Adding the packet to the queue
        controller.notifyItemAdded() #This method act a bit like a user, so we need to interact with the controller (tell him it needs to display a new packet)

        #When the user will be able to drop packets, there will need to be a condition here to verify if the queue is not empty
        kamui.send(model.getPkt().raw)


if __name__ == "__main__":
    model = Model() #Prepare the queue for packets
    kamui = Kamui() #Prepare TUN interface

    #view = View(700, 600)
    controller = Controller(model)
    view = View(controller, 700, 600)
    controller.setView(view)

    #Run the TUN interface
    thr = Thread(target=RunApp, args=(kamui, model, controller, )).start()

    view.window.mainloop()
    thr.join() #If the code gets here, it's because the program needs to be stopped
