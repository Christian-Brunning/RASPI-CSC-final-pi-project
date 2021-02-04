from pygame import mixer, time
from time import sleep

song1 = [" ", "Twinkle twinkle little star", "How I wonder what you are", "Up above the world so high", "Like a diamond in the sky", \
    "Twinle twinkle little star", "How I wonder what you are", " ", " "]
song2 = [" ", ]
song3 = [" ", ]

choice = input("What song would you like to play: Twinkle twinkle little star, ")
if (choice == "Twinkle twinkle little star"):
    mixer.init()
    mixer.music.load("Twinkle Twinkle Little Star.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        time.Clock().tick(10)
        sleep(14)
        for i in range(len(song1)):
            print (song1[i])    
            sleep(5.5)
        sleep (16)
        for i in range(len(song1)):
            print(song1[i])
            sleep(5.5)
        sleep(16)
        break
elif (choice == " "):
    mixer.init
    mixer.music.load(".mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        time.Clock().tick(10)
elif (choice == " "):
    mixer.init
    mixer.music.load(" .mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        time.Clock().tick(10)
        
        
        
