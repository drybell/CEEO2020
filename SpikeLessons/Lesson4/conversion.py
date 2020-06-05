from spike import PrimeHub, Motor, ForceSensor             
import utime
hub = PrimeHub()
pointer = Motor('A')
touch = ForceSensor('E') 
pointer.run_to_position(0) #Note: not tested yet
blue_temp = 0
red_temp = 40
angle_bw_blueandred = 180
def turn_pointer():
    temp_in_kelvin = 300 
    city_name = "tester"
    temp_in_celsius = round(temp_in_kelvin - 273.15)
    print(temp_in_celsius)
    unit_degree =  angle_bw_blueandred / (red_temp-blue_temp)
    turn_angle = unit_degree * temp_in_celsius
    pointer.run_for_degrees(20, turn_angle)
    return temp_in_celsius, city_name 
while True:
    temp_in_celsius, city_name = turn_pointer()                    
    if touch.is_pressed():
        hub._light_matrix.write("It's "+ str(temp_in_celsius)+ "degree celsius in" + city_name)
    utime.sleep(1)


