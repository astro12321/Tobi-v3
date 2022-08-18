import sys

from tkinter import *
from Packet import *


#Receive packets and analyze them
class Model:
    def __init__(self):
        self.queue = deque()

    def addPkt(self, buffer):
        pkt = Packet(len(self.queue) + 1, buffer)
        self.queue.append(pkt)

    def getPkt(self, ind=-1) -> Packet: #The item in the queue cannot be pop(), because this function is called by 2 classes
        return self.queue[ind]


#Receive data and modify the View
class Controller:
    def __init__(self, model):
        self.model = model
        self.view = None

    def notifyItemAdded(self):
        pkt = self.model.getPkt()
        itemToAdd = f"{pkt.index}. {pkt.resume()}"

        self.view.packetsListBox.insert(pkt.index, itemToAdd)
        self.view.packetsListBox.yview(END)

    def getPktFullDesc(self, index):
        return self.model.getPkt(index).show(dump=True)

    def setView(self, view):
        self.view = view


#GUI
class View(Frame):
    def __init__(self, controller, width, height):
        self.controller = controller

        self.window = Tk()
        self.window.title("Tobi")

        self.window.geometry(f"{str(width)}x{str(height)}")

        Label(self.window, text="Capture").pack()

        frame = Frame(self.window)
        frame.pack()

        self.packetsListBox = Listbox(frame, width=width, height=height, font=("Helvetica", 12))
        self.packetsListBox.bind('<Double-Button>', self.openPacketPopUp) #Double clicking on item in listbox call func
        self.packetsListBox.pack(side="left", fill="y")

        scrollbar = Scrollbar(frame, orient="vertical")
        scrollbar.config(command=self.packetsListBox.yview)
        scrollbar.pack(side="right", fill="y")

        self.packetsListBox.config(yscrollcommand=scrollbar.set)

        self.window.protocol("WM_DELETE_WINDOW", sys.exit)

    def openPacketPopUp(self, event):
        pktNumber = event.widget.curselection()[0]

        win = Tk()
        win.title(f"Packet {pktNumber + 1}")

        l = Label(win, text=self.controller.getPktFullDesc(pktNumber))
        l.grid(row=0, column=0)
