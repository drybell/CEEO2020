# Workaround for VISA 
# python3 -m serial.tools.list_ports
import serial 

with serial.Serial("/dev/cu.LEGOHub40BD3230E56D-Ser-1", 9600, timeout=1) as ser: 

	print(ser.readlines())