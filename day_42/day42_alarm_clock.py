# Extra Challenge: Create an Alarm clock
# Create a function called alarm that sets an alarm clock for the
#     user. The function should ask the user to enter time they want
# the alarm to go off. The user should enter the hour and
# minute. The function should then print out the time when the
# alarm will go off. When its alarm time, the code should let off a
# sound. Use the winsound module for sound.

#import winsound  This is not working as I am using MAC
import pygame
from datetime import datetime
import re

def set_alarm():
    time_exp= '^(0?[1-9]|1[0-2]):[0-5][0-9]$'

    hour_min_for_alarm = input("WHat time would you like the alarm to go off: Type HH:MM  ")
    match = re.search(time_exp, hour_min_for_alarm)
    if match:
        print("Your alarm is set..wait until then :)")
        while True:
            hora_min_now = datetime.now().strftime('%H:%M')
            #print(hora_min_now)
            if(hour_min_for_alarm==hora_min_now):
                pygame.init()
                pygame.mixer.init()
                sounda= pygame.mixer.Sound("bicycle-bell-155622.mp3")
                sounda.play()
                print("Time to wake up")
                break
    else:
        print("Give an alarm to go off: Type HH:MM")




