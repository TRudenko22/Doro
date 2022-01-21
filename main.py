from rich import print as rprint
from ascii import * 
from os import system
import time
import simpleaudio as sa
import typer
you_suffer = sa.WaveObject.from_wave_file("Napalm Death - You Suffer.wav")

app = typer.Typer()

@app.command
def doro(minutes, rminutes, rounds):
    system('clear')
    rprint(main_title)

    system('clear')
    for loop in range(rounds):
        
        lMinutes1 = minutes * 60
        lMinutes2 = rminutes * 60

        rprint(f'\n{working}\n')
        while lMinutes1: 
            mins, secs = divmod(lMinutes1, 60)
            timer = f"\t\t[cyan][b]     Working: {'{:02d}:{:02d}'.format(mins, secs)}[/b][/cyan]"
            rprint(timer, end='\r')
            time.sleep(1)
            lMinutes1 -= 1

        you_suffer.play()
        system('clear')
        
        rprint(f'\n{resting}\n')
        while lMinutes2:
            mins, secs = divmod(lMinutes2, 60)
            timer = f"\t\t[cyan][b]     Resting: {'{:02d}:{:02d}'.format(mins, secs)}[/b][/cyan]"
            rprint(timer, end='\r')
            time.sleep(1)
            lMinutes2 -= 1
        
        you_suffer.play()
        system('clear')
