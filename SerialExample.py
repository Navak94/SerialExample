import serial
import sys
import serial
import os
import subprocess
from time import sleep

def serial_ports():

    ports = ['COM%s' % (i + 1) for i in range(256)] 

    result = []

    for port in ports: 
        try:
            s = serial.Serial(port) 
            s.close()  
            result.append(port) 
        except (OSError, serial.SerialException): 
            pass 
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
        
        sleep(0.1) 
        serialData=str(ser.readline()) 
        serialData = serialData.replace("b'","").replace("'","").replace("\\r","").replace("\\n","") 

        if(serialData!=""): 
            print(serialData) 
            
    ser.close()


if __name__ == '__main__':
    comavailable = str(serial_ports()).replace("[","").replace("]","").replace("'","") 
    loopSerial(comavailable) 
    
