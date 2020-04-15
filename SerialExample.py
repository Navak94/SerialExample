import serial
import sys
import serial
import os
import subprocess
from time import sleep

def serial_ports():

    ports = ['COM%s' % (i + 1) for i in range(256)] # %s is a conversion specifier for string.  so in com%s the %s IS (i+1)

    result = []

    for port in ports: # loop through coms until something responds
        try:
            s = serial.Serial(port) #peek to see if something is on the com
            s.close()  
            result.append(port) #eyyy lookit that something's there! append it to the list
        except (OSError, serial.SerialException): #ruh roh nothing's there bro
            pass # in python you can't have blank spaces under tabbed things, so often pass is used to leave the exception
    return result


def loopSerial(Text):
    ser = serial.Serial(
        port=Text,\
        baudrate=9600,\
        parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS,\
            timeout=0)

    print("connected to: " + ser.portstr) 
    
    while True:
        
        sleep(0.1) #serial goes in 0.1 second intervals after synchronizing
        serialData=str(ser.readline()) #read from the serial and make it a string
        serialData = serialData.replace("b'","").replace("'","").replace("\\r","").replace("\\n","") #get rid of carriage return and shit, nobody wants that...eww

        if(serialData!=""): #if the string isn't blank, print
            print(serialData) #formatted serial data
            
    ser.close()


if __name__ == '__main__':
    comavailable = str(serial_ports()).replace("[","").replace("]","").replace("'","") #get rid of those stupid fucking brackets >:( tired of dat shit
    loopSerial(comavailable) # throw comavailable into loopSerial
    
