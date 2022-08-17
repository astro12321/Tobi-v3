import fcntl
import os
import struct
import subprocess
import time


class Kamui:
    def __init__(self):
       self.TUNSETIFF = 0x400454ca
       self.TUNSETOWNER = self.TUNSETIFF + 2
       self.IFF_TUN = 0x0001
       self.IFF_NO_PI = 0x1000
       self.BUFFERSIZE = 4096

       self.tun = open('/dev/net/tun', 'r+b', buffering=0)
       ifr = struct.pack('16sH', b'tun0', self.IFF_TUN | self.IFF_NO_PI)
       fcntl.ioctl(self.tun, self.TUNSETIFF, ifr)

    def recv(self) -> bytes:
        return os.read(self.tun.fileno(), self.BUFFERSIZE)

    def send(self, rawPkt: bytes):
        os.write(self.tun.fileno(), bytes(rawPkt))
