from Packet import *


class Filter(): #ip.src = 8.8.8.8
    def __init__(self, filters):
        self.filtersStr = filters

        self.filtersDict = {"ip.src": "", "ip.dst": "", "port.src": "", "port.dst": ""}

        for filter in filters.split(' '):
            filter = "".join(filters.split()) #Remove spaces
            filter = filter.split('=')
            key = filter[0]
            value = filter[1]

            if key in self.filtersDict:
                self.filtersDict[key] = value

    def check(self, pkt: Packet) -> bool:
        for k, v in self.filtersDict.items():
            if k == "ip.src": #There should be a check making sure the ip.src exists in the packet
                if pkt.src == v:
                    return False
            if k == "ip.dst":
                if pkt.dst == v:
                    return False
        return True

    def toString(self) -> str:
        return self.filtersStr