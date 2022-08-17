from scapy.all import raw

from Packet import *
from Kamui import *


class Tobi:
    def __init__(self):
        self.totalPackets = 0

    #Construct the packet
    def check(self, pktBytes: bytes) -> Packet:
        self.totalPackets += 1
        return Packet(self.totalPackets, pktBytes)


if __name__ == "__main__":
    tobi = Tobi()
    kamui = Kamui()

    while True:
        buffer = kamui.recv()

        pkt = tobi.check(buffer)

        print("-------------------------------------------")
        pkt.show()
        print("-------------------------------------------")

        kamui.send(raw(pkt))
