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

    def getPkt(self) -> Packet: #The item in the queue cannot be pop(), because this function is called by 2 classes
        return self.queue[-1]


#Receive data and modify the View
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def notifyItemAdded(self):
        pkt = self.model.getPkt()
        itemToAdd = f"{pkt.index}. {pkt.resume()}"

        self.view.packetsListBox.insert(pkt.index, itemToAdd)
        self.view.packetsListBox.yview(END)


#GUI
class View(Frame):
    def __init__(self, width, height):
        self.window = Tk()
        self.window.title("Tobi")

        self.window.geometry(f"{str(width)}x{str(height)}")

        Label(self.window, text="Capture").pack()

        frame = Frame(self.window)
        frame.pack()

        self.packetsListBox = Listbox(frame, width=width, height=height, font=("Helvetica", 12))
        self.packetsListBox.pack(side="left", fill="y")

        scrollbar = Scrollbar(frame, orient="vertical")
        scrollbar.config(command=self.packetsListBox.yview)
        scrollbar.pack(side="right", fill="y")

        self.packetsListBox.config(yscrollcommand=scrollbar.set)

        self.window.protocol("WM_DELETE_WINDOW", sys.exit)

    def setController(self, controller):
        self.controller = controller
