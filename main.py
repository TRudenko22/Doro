import time
from rich import print as rprint
import simpleaudio as sa

you_suffer = sa.WaveObject.from_wave_file("Napalm Death - You Suffer.wav")

minutes = int(input("\nEnter Working Minutes: "))*60
rminutes = int(input("Enter Resting Minutes: "))*60


print("\n")
while minutes:
    mins, secs = divmod(minutes, 60)
    timer = f"[cyan]Working: {'{:02d}:{:02d}'.format(mins, secs)}[/cyan]"
    rprint(timer, end="\r")
    time.sleep(1)
    minutes -= 1


print("\n")    
you_suffer.play()


while rminutes:
    mins, secs = divmod(rminutes, 60)
    timer = f"[cyan]Resting: {'{:02d}:{:02d}'.format(mins, secs)}[/cyan]"
    rprint(timer, end="\r")
    time.sleep(1)
    rminutes -= 1
 

