import hub 
import random 
import utime 

num_notes = 15 # change for longer notes 
duration = .5 # utime sleep, make a list if you want to change note speeds along the way
hub.sound.volume(10)

for i in range(num_notes):
	hub.sound.beep(random.randint(800,2000), 1000, 0)
	utime.sleep(duration)


