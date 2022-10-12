from LIBRARIES.functlb import *
from LIBRARIES.importlb import *
from os import system

def qrgen():
    item = input('Input Item for QR generation: ')

    cl()

    qr = qrcode.make(item)

    qr.save(item + '.png')