# program do odczytu z servera UDP informacji (z telefonu)
# tcpCliSock

#Server
from socket import *
import time
#import RPi.GPIO as GPIO


ctrCmd = ['asd', 'asdg'] #komendy do sterowania 

hostName = '127.0.0.1' 
localIP     = '127.0.0.1'
localPort   = 8080
bufferSize  = 1024

tcpSerSock = socket(AF_INET,SOCK_STREAM)
# close port when process exits:
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcpSerSock.bind((hostName,bufferSize))

tcpSerSock.listen(5)
print ("Waiting for a connecting client...")
isConnected = False

while True:
        print ('Waiting for connection')
        tcpCliSock,addr = tcpSerSock.accept()
        print ('...connected from :', addr)
        while True:
                data = ''
                data = tcpCliSock.recv(BUFSIZE) #odbieranie informacji
                if not data:
                        break
                if data == ctrCmd[0]:
                        print ('komenda1 ')
                if data == ctrCmd[1]:
                        print ('komenda2 ')
	
tcpSerSock.close();
