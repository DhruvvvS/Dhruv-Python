# creating a countdown timer which shows digital clock

import time
#time module gives us different functions to use for our program
# time.sleep(any number) : this function helps to sleep our program for that number seconds time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time,0,-1): # this allows decreasing time by step -1 
    seconds = x % 60 # seconds need remainder
    minutes = int(x / 60) % 60 
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
# 02 will give zero padding
# countdown timer will sleep for 1 sec

print("YOUR TIME IS UP!!!")