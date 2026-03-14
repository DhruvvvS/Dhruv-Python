# Python Alarm Clock

# importing time module to increase time by one second
import time

# importing datetime module to get current time and string representation of time
import datetime

# importing pygame module to play alarm sound 
import pygame

def set_alarm(alarm_time):
    print(f"Alarm is set for {alarm_time}")
    sound_file = "music.mp3"  # Path to your alarm sound file
    is_running = True

    while is_running:
        # getting current time in HH:MM:SS format
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        # checking if current time matches the alarm time
        if current_time == alarm_time:

            # mixer is a module for loading and playing sounds in pygame
            # initializing the mixer module and loading the alarm sound file
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)

            # playing the alarm sound
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                print("WAKE UP!")
                time.sleep(1)  # Wait until the music finishes playing

            is_running = False  # Stop the loop after playing the alarm sound
        
        # wait for 1 second before checking the time again
        time.sleep(1)

if __name__ == "__main__":
    # taking input from user for alarm time in HH:MM:SS format
    alarm_time = input("Enter the alarm time in (HH:MM:SS) format: ")
    set_alarm(alarm_time)