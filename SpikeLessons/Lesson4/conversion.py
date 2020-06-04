from spike import PrimeHub
from spike import Motor
from spike import ColorSensor 
from spike import ForceSensor              
import utime
from spike import MotorPair

hub = PrimeHub()
pointer = Motor('A')
touch = ForceSensor('E') 
pointer.run_to_position(0) #Note: not tested yet
 
blue_temp = 0
red_temp = 40
angle_bw_blueandred = 180
 

"""WE CAN"T DO THIS, SO WE WRITE ANOTHER PYTHON FILE TO DO IT FOR US ################
  # Get the API key from openweathermap.org and replace the text YOUR_API_KEY with the key
  # don't remove the  quotes
  key = "YOUR_API_KEY "
   
  # Replace the city id with your city's id
  #Find the entire list of id here http://bulk.openweathermap.org/sample/
   
  city_id = "CITY_ID"
   
  # base url of the API
  baseurl = "https://api.openweathermap.org/"
   
  # format the baseurl, city and API key into a url
  url = baseurl + "data/2.5/weather?id=" + city_id + "&appid=" + key
   
""" #################################################################################

def turn_pointer():

    temp_in_kelvin = 300 # TODO: GET THIS VALUE FROM OTHER PYTHON FILE
    city_name = "tester" # TODO: GET THIS VALUE FROM OTHER PYTHON FILE  
    temp_in_celsius = round(temp_in_kelvin -273.15)

    print(temp_in_celsius)

    unit_degree =  angle_bw_blueandred / (red_temp-blue_temp)

    turn_angle = unit_degree * temp_in_celsius

    pointer.run_for_degrees(20, turn_angle)
    return temp_in_celsius, city_name
 
counter=180000 #start with 1800 so that the pointer function  (called below)  turns the first time
#runs forever
while True:

    #Since the temperature don't change significantly over short period of time
    # we can update the pointer every half an hour

    if counter==180000:
        # call the function that moves the motor and save temperature and city name
        temp_in_celsius, city_name = turn_pointer()

        # reset counter
        counter = 0               

        # increase counter by one     
        counter += 1                         

    # The EV3 will say out the temperature from the speaker when the touch sensor is pressed
    if touch.is_pressed():
        hub._light_matrix.write("It's "+ str(temp_in_celsius)+ "degree celsius in" + city_name)
    utime.sleep(.01) # wait for 10 milliseconds