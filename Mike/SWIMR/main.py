'''
Created on Oct 17, 2012

@author: Mike
'''

from swim_serial import SwimSerial
from swim_client import SwimClient
client = SwimClient()
s = SwimSerial(baudrate = 9600)

while True:
    client.setpayload('bbbb')
    client.send()
    
    client.receive()
    b = client.getreceived()

    
    print b