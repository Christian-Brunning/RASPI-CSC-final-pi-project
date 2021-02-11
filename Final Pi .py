####################################################################
#Names: Calin Farmer
#Date: 2/4/21
#Assignment: Final Pi Project, Karaoke Machine
####################################################################
#must download pygame for this to work
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

song3 = [" ","Baby, lay on back and relax", "Kick your pretty feet up on my dash", "No need to go nowhere fast", "let's enjoy right here where we at", \
        "Who knows where this road is supposed to lead?", "We got nothing but time", "As long as you're right here next to me, everything's gonna be alright",\
        "If it's meant to be, it'll be, it'll be", "Baby, just let it be", "If it's meant to be, it'll be, it'll be", "Baby, just let it be" "So won't you ride with me, ride with me?",\
        "See where this thing goes", "If it's meant to be, it'll be, it'll be", "Baby, if it's meant to be", \
        "I don't mean to be so uptight","But my heart's been hurt a couple times by a couple guys that didn't treat me right", "I ain't gon' lie, ain't gon' lie", "Cause I'm tired of the fake love, show me what you're made of ", "Boy, make me believe" \
        "Oh, hold up girl, don't you know you're beautiful?", "And it's easy to see", "If it's meant to be, it'll be, it'll be" , "Baby, just let it be" , "If it's meant to be, it'll be, it'll be", "Baby just let it be",\ 
        "So won't you ride with me, ride with me?", "See where this thing goes", "If it's meant to be, it'll be, it'll be", "Baby, if it's meant to be", "So c'mon ride with me, ride with me", "See where this thing goes", "So c'mon ride with me, ride with me", "Baby, if it's meant to be",\
        "Maybe we do", "Maybe we don't", "Maybe we will", "Maybe we won't", \
        "But if it's meant to be, it'll be, it'll be", "Baby, just let it be (sing it baby)", "If it's meant to be, it'll be, it'll be (c'mon)",  "Baby, just let it be (let's go)", "So won't you ride with me, ride with me?",\
        "See where this thing goes", "If it's meant to be, it'll be, it'll be" ,"Baby, if it's meant to be" ,"If it's meant to be, it'll be, it'll be", "Baby, if it's meant to be", "If it's meant to be, it'll be, it'll be", "Baby, if it's meant to be" ]
        

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
    mixer.init()
    mixer.music.load("Humble and kind.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        time.Clock().tick(10)
        sleep(12.5)
        for i in range(len(song2)): 
            print(song2[i])
            sleep(5.5)
        break
        
        
elif (choice == "Meant To Be" )