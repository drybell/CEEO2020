import serial 


ser = serial.Serial("/dev/tty.usbmodem15131", baudrate=115200)
ser.readlines()