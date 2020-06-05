import serial 
import time
import requests 

# This code sends an API request to weathermap, then 
# outputs the weather from city_id in celsius to the Spike Prime 
# by serial connection 

key = "INSERT KEY HERE"

# Replace the city id with your city's id
#Find the entire list of id here http://bulk.openweathermap.org/sample/

city_id = "7872695" # Olbendorf 

# base url of the API
baseurl = "https://api.openweathermap.org/"

# format the baseurl, city and API key into a url
url = baseurl + "data/2.5/weather?id=" + city_id + "&appid=" + key

ret = requests.get(url).json()

# pull out the data from json 
temp_in_kelvin = ret['main']['temp'] # the temperature in kelvin
temp_in_celsius = temp_in_kelvin - 273
city_name = ret['name']

print(temp_in_kelvin)
print(city_name)

# print(ret)

# MIGHT BE A DIFFERENT CONNECTION HERE, 
ser = serial.Serial("/dev/tty.usbmodem14131", baudrate=115200)

ser.write(b'\x03') # Ctrl-C 
ser.write(b'\x04') # Ctrl-D
time.sleep(5)
ser.write(b'\x03')
ser.reset_input_buffer()

inc = 2
time.sleep(2)
ser.write(b"from spike import PrimeHub\r")
ser.reset_input_buffer()
time.sleep(1)
ser.write(b"hub = PrimeHub()\r")
ser.reset_input_buffer()
time.sleep(1)
ser.write(b"hub.sound.beep(1000,1000,1)\r")
time.sleep(2)
ser.reset_input_buffer()
lightup = "hub._light_matrix.write(\'It is "+ str(int(temp_in_celsius)) + " degrees celsius in " + city_name + "\')\r"
ser.write(bytes(lightup, 'utf-8'))
time.sleep(10)
ser.reset_input_buffer()

ser.close()

# TODO THOUGHTS: Maybe create a wrapper that automatically parses the 



