from pygame import mixer, time
from time import sleep

song1 = [" ", "Twinkle twinkle little star", "How I wonder what you are", "Up above the world so high", "Like a diamond in the sky", \
    "Twinle twinkle little star", "How I wonder what you are", " ", " "]

song2 = [" ", "You know there's a light that glows by the front door", "Don't forget the keys under the mat", "When childhood stars shine always stay humble and kind", \
        "Go to church 'cause your mama says to", "Visit grandpa every chance that you can", "It won't be wasted time always stay humble and kind", \
        "Hold the door, say please, say thank you", "Don't steal, don't cheat, and don't lie", "I know you got mountains to climb but always stay humble and kind", \
        "When the dreams you're dreamin' come to you", "When the work you put in is realized", "Let yourself feel the pride but always stay humble and kind", \
        "Don't expect a free ride from no one", "Don't hold a grudge or a chip and here's why", "Bitterness keeps you from flyin' always stay humble and kind", \
        "Know the difference between sleepin' with someone", "And sleepin' with someone you love", "I love you ain't no pickup line so always stay humble and kind", \
        "Hold the door, say please, say thank you", "Don't steal, don't cheat, and don't lie", "I know you got mountains to climb but always stay humble and kind", \
        "When those dreams you're dreamin' come to you", "When the work you put in is realized", "Let yourself feel the pride but always stay humble and kind", \
        " ", " ", " ", " ", " ", "When it's hot eat a root beer popsicle", "Shut off the A/C and roll the windows down", "Let that summer sun shine always stay humble and kind", \
        "Don't take for granted the love this life gives you", "When you get where you're goin' don't forget turn back around", "And help the next one in line", \
        "Always stay humble and kind"]

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
elif (choice == "Humble and kind"):
    mixer.init
    mixer.music.load("Humble and kind.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        time.Clock().tick(10)
        sleep(12.5)
        for i in range(len(song2)): 
            print(song2[i])
            sleep(5.5)
        break
        
        
