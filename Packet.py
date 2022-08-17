from scapy.all import *

class Packet(IP):
    def __init__(self, index: int, pktBytes: bytes):
        super().__init__(pktBytes)

        self.index = index

    def __getProtos(self):
        counter = 0
        while True:
            layer = self.getlayer(counter)

            if layer is None:
                break

            counter += 1
            yield layer.name

    def resume(self):
        IPs = f"src: {self.src} dst: {self.dst} | "
        ports = ""
        protocols = "Protos: " + " ".join(x for x in self.__getProtos()) + " | "

        if (TCP or UDP) in self:
            ports = f"srcPort: {self.sport} dstPost: {self.dport} | "

        return IPs + ports + protocols
