#Libraries
#biblioteka ev3dev2 
#https://pypi.org/project/smbus2/

from smbus2 import SMBus
import time
import spidev

#Adresses
adressDistance1=0x01D
adressDistance2=0x02D

busI2C= smbus.SMBus(1) #connect to I2C-bus (port I2C1), 

#SPI
busSPI= 0
#Device is the chip select pin. Set to 0 or 1, depending on the connections
device=1
spi = spidev.SpiDev()
spi.open(busSPI, device)
# Settings (for example)
spi.max_speed_hz = 500000
spi.mode = 0

#Program
while True:

	# read form sensors
	# Read a block of 16 bytes from address 0, offset 0
	distance1_value=busI2C.read_i2c_block_data(adressDistance1,0,16)
	# Read from address, offset 0
	distance2_value=busI2C.read_byte_data(adressDistance2,0)
	print(distance1_value)
	print(distance2_value)


#sending due to SPI to STM32
	to_send= ["ramka","ramka"] #lista
	spi.xfer(to_send)



