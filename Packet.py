from scapy.all import *

class Packet(IP):
    def __init__(self, index: int, pktBytes: bytes):
        super().__init__(pktBytes)
