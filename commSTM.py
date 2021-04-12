#comunication RPI->STM
#send information via I2C
#RPI Master STM Slave
'''
from smbus2 import SMBus
import time

# I2C address of Slaves
i2c_address = 0x07 #zmienic

bus=smbus.SMBus(1)

data_received = ""
data_send = "test" #functionwrite_i2c_block_data() send max 32byte

def writeData(value):
    byteValue = StringToBytes(value)
    bus.write_i2c_block_data(i2c_address, 0x00, byteValue) #first byte is 0=command byte.. just is xD
    return -1

def StringToBytes(val):
        retVal = []
        for c in val:
                retVal.append(ord(c))
        return retVal
    
while(True):
    print('sending')
    writeData(data_send)
    time.sleep(5)

    print("sending")
    writeData("test")
    time.sleep(5)

    print("sending")
    writeData("test_dluzszy1234")
    time.sleep(5)
'''

#comunication RPI->STM#send information via UART

    
import serial
import time

ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate
while True:
    #sending frame
    ser.write("#9_mGo_"+pwm+"_" + time1 + "\r\n")
