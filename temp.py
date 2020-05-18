import winsound

name = input("Play battle theme")

winsound.PlaySound("battle", winsound.SND_FILENAME | winsound.SND_ASYNC)

name = input("Change to victory theme ");

winsound.PlaySound("victory", winsound.SND_FILENAME | winsound.SND_ASYNC)

name = input("Purge all sound")

winsound.PlaySound(None, winsound.SND_PURGE)

name = input("Exit program");

import os

os.system("aplay battle.wav&") #Linux
os.system("afplay battle.wav&") #Mac