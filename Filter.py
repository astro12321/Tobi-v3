from Packet import *

#ip.dst=209.59.129.18 port.dst=443 port.src=443
class Filter():
    def __init__(self, filters):
        self.filtersStr = filters
        self.filtersDict = {"ip.src": "", "ip.dst": "", "port.src": "", "port.dst": ""}

        self.__numberOfFilters = 0

        for filter in filters.split(' '):
            filter = filter.split('=')

            key = filter[0]
            value = filter[1]

            if key in self.filtersDict:
                self.filtersDict[key] = value
                self.__numberOfFilters += 1 #Keep track of the number of filters we have in this filter

    def check(self, pkt: Packet) -> bool:
        numberOfFilters = 0

        for k, v in self.filtersDict.items():
            #IPs
            if k == "ip.src":
                if pkt.src == v:
                    numberOfFilters += 1
            if k == "ip.dst":
                if pkt.dst == v:
                    numberOfFilters += 1

            #Ports
            if k == "port.src":
                if hasattr(pkt, "sport"):
                    if str(pkt.sport) == v:
                        numberOfFilters += 1
            if k == "port.dst":
                if hasattr(pkt, "dport"):
                    if str(pkt.dport) == v:
                        numberOfFilters += 1

        if numberOfFilters == self.__numberOfFilters: #The packet match on ALL the filters we had in __init__
            return False
        return True

    def toString(self) -> str:
        return self.filtersStr


def isFilterValid(filters: str): #Simple filter validation used when adding the filters
    for filter in filters.split(' '):
        filter = filter.split('=')

        if len(filter) != 2: return False

        return True