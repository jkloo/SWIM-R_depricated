'''
Created on Oct 17, 2012

@author: Mike
'''

from swim_serial import SwimSerial

message = 'bbbb'
s = SwimSerial(baudrate = 9600)

while True:
    if(s.IS_CONNECTED):
        s.setpayload(message)
        s.write()
        s.read()
        b = s.getreceive()
        print b
    else:
        s.initialize()
        print 'not connected'