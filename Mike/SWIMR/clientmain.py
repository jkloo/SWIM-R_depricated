

import sys
sys.path.append('../SWIMR/PacketStructure')
sys.path.append('../SWIMR/EthernetCommunication')
sys.path.append('../SWIMR/SerialCommunication')





from swim_client import SwimClient
from swim_packet import SwimPacket
from swim_serial import SwimSerial
import time



###############Command Line helper################
try:
    IP,PORT = str(sys.argv[1]),int(sys.argv[2])
except:
    print "try: python clientmain.py <SERVERIP> <PORT>"
    exit(1)
##################################################




while 1:
    try:
        ########setup()#########
        
        #Setting up Ethernet Communication
        print 'finding server....'
        ethernet = SwimClient(IP,PORT)
        print 'server found......'
        print 'starting receive thread'
        ethernet.start()
        ############
        #########################
        
        
        ############loop()#######
        #main loop of the program
        while ethernet.ISCONNECTED:
            time.sleep(0.2)
            ethernet.setpayload('test')
            ethernet.send()
            if ethernet.ISCONNECTED:
                print "still connected"
            else:
                print 'not connected!'
                
            if ethernet.NEWMESSAGE:
                print "this is a new message: " + ethernet.getreceive()
            else:
                print 'this is not a new message: ' + ethernet.getreceive()
        ######################### 
         
         
         
        ###########cleanup()#####
        #Things in this section are called if something goes wrong in loop()
        print "cleaning up"
        ethernet.cleanup()
        print 'cleaned up!'
        ########################
    except KeyboardInterrupt:
        print "bye bye"
        exit(0)