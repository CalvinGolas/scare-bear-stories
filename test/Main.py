import pygame 
import time
import BearControl as bc
#The pygame mixer module automatically runs the audio in the background!

# initalizes the various moving parts
pygame.mixer.init()
pygame.mixer.music.load("test.ogg")

motors = bc.BearControl(mouthServoPin=26, neckServoPin=5)
motors.straighten_head()
motors.raise_fangs()

# start up the various functions
pygame.mixer.music.play()
print("done running all that boring setup stuff")
# This is where the actions will take place

#on wakeup
time.sleep(5)
motors.turn_head_backwards()
time.sleep(5)
motors.vibrate_head()
time.sleep(5)
motors.lower_fangs()
time.sleep(5)
motors.straighten_head()
time.sleep(5)
motors.raise_fangs()
time.sleep(2)
#cleanup
motors.halt()