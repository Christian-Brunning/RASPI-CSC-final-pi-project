#####################################
# Calin Farmer, Christian Brunning, Zach Morgan
#
# Final Pi Project
####################################
from pygame import mixer, time
from time import sleep
from tkinter import *

song1Lyrics = [" ", "Twinkle twinkle little star", "How I wonder what you are", "Up above the world so high", "Like a diamond in the sky", \
    "Twinkle twinkle little star", "How I wonder what you are", " ", " "]

song2Lyrics = [" ", "You know there's a light that glows by the front door", "Don't forget the keys under the mat", "When childhood stars shine Always stay humble and kind", \
        " ", "Go to church 'cause your mama says to", "Visit grandpa every chance that you can", "It won't be wasted time Always stay humble and kind", \
        " ", "Hold the door, say please, say thank you", "Don't steal, don't cheat, and don't lie", "I know you got mountains to climb but Always stay humble and kind", \
        " ", "When the dreams you're dreamin' come to you", "When the work you put in is realized", "Let yourself feel the pride but Always stay humble and kind", \
        " ", "Don't expect a free ride from no one", "Don't hold a grudge or a chip and here's why", "Bitterness keeps you from flyin' Always stay humble and kind", \
        " ", "Know the difference between sleepin' with someone", "And sleepin' with someone you love", "I love you ain't no pickup line so Always stay humble and kind", \
        " ", "Hold the door, say please, say thank you", "Don't steal, don't cheat, and don't lie", "I know you got mountains to climb but Always stay humble and kind", \
        " ", "When those dreams you're dreamin' come to you", "When the work you put in is realized", "Let yourself feel the pride but Always stay humble and kind", \
        " ", " ", " ", " ", " ", " ", " ", " ", \
        "When it's hot eat a root beer popsicle", "Shut off the A/C and roll the windows down", "Let that summer sun shine Always stay humble and kind", \
        " ", "Don't take for granted the love this life gives you", "When you get where you're goin' don't forget turn back around", "And help the next one in line", \
        " ", "Always stay humble and kind"]

song3Lyrics = [" ", "Baby, lay on back and relax", "Kick your pretty feet up on my dash", "No need to go nowhere fast", "let's enjoy right here where we at", \
        "Who knows where this road is supposed to lead?", "We got nothing but time", "As long as you're right here next to me", "everything's gonna be alright", \
        "If it's meant to be, it'll be, it'll be", "Baby, just let it be", "If it's meant to be, it'll be, it'll be", "Baby, just let it be", "So won't you ride with me, ride with me?",\
        "See where this thing goes", "If it's meant to be, it'll be, it'll be", "Baby, if it's meant to be", \
        "I don't mean to be so uptight","But my heart's been hurt a couple times by a couple guys that didn't treat me right", "I ain't gon' lie, ain't gon' lie", "Cause I'm tired of the fake love, show me what you're made of ", "Boy, make me believe", \
        "Oh, hold up girl, don't you know you're beautiful?", "And it's easy to see", "If it's meant to be, it'll be, it'll be" , "Baby, just let it be" , "If it's meant to be, it'll be, it'll be", "Baby just let it be",\
        "So won't you ride with me, ride with me?", "See where this thing goes", "If it's meant to be, it'll be, it'll be", "Baby, if it's meant to be", "So c'mon ride with me, ride with me", "See where this thing goes", "So c'mon ride with me, ride with me", "Baby, if it's meant to be",\
        "Maybe we do", "Maybe we don't", "Maybe we will", "Maybe we won't", \
        "But if it's meant to be, it'll be, it'll be", "Baby, just let it be (sing it baby)", "If it's meant to be, it'll be, it'll be (c'mon)",  "Baby, just let it be (let's go)", "So won't you ride with me, ride with me?",\
        "See where this thing goes", "If it's meant to be, it'll be, it'll be" ,"Baby, if it's meant to be" ,"If it's meant to be, it'll be, it'll be", "Baby, if it's meant to be", "If it's meant to be, it'll be, it'll be", "Baby, if it's meant to be" ]

menu= ["What song would you like to play: Twinkle Twinkle Little Star, Humble and Kind, Meant to Be? "]
#####################################################################################
#Tkinter face code
class Song:
    def __init__(self, Lyrics, image, title):
        self.Lyrics = Lyrics
        self.image = image
        self.title = title
class Karaoke(Frame):
    def __init__(self, parent):
		# call the constructor in the superclass
        Frame.__init__(self, parent)
        self.song1 = Song(song1Lyrics, "twinkle.gif", "Twinkle Twinkle Little Star")
        self.song2 = Song(song2Lyrics, "DCM.gif", "Humble and Kind")
        self.song3 = Song(song3Lyrics, "MTB.gif", "Meant to Be")
        self.menu = Song(menu, "Menu.gif", "Menu")
        Karaoke.currentSong = self.menu 
        
    def show_lyric1(self, index = None):  #for song 1
        if index is not None:
            if index < len(Karaoke.currentSong.Lyrics):
                txt = Karaoke.currentSong.Lyrics[index]
                self.setStatus(txt)
                index += 1
                window.after(5500, lambda: self.show_lyric1(index))
        else:
            self.setStatus(" ")
 
    def show_lyric2(self, index=None):    #for song 2
        if index is not None:
            if index < len(Karaoke.currentSong.Lyrics):
                txt = Karaoke.currentSong.Lyrics[index]
                # textw.delete('1.0', 'end')
                self.setStatus(txt)
                index += 1
                window.after(4750, lambda: self.show_lyric2(index))
        else:
            self.setStatus(" ")

    def show_lyric3(self, index=None):    #for song 2
        if index is not None:
            if index < len(Karaoke.currentSong.Lyrics):
                txt = Karaoke.currentSong.Lyrics[index]
                # textw.delete('1.0', 'end')
                self.setStatus(txt)
                index += 1
                window.after(3250, lambda: self.show_lyric3(index))
        else:
            self.setStatus(" ")

    def process(self, event):
        choice = Karaoke.user_input.get()
        choice = choice.lower()
        if (choice == "twinkle twinkle little star"):
            Karaoke.currentSong = self.song1 
            self.setSongImage()
            Karaoke.user_input.delete(0, END)
            mixer.init()
            mixer.music.load("Twinkle Twinkle Little Star.mp3")
            mixer.music.play()
            window.after(12000), self.show_lyric1(0)
            window.after(8000), self.show_lyric1(0)

        elif (choice == "humble and kind"):
            Karaoke.currentSong = self.song2 
            self.setSongImage()
            Karaoke.user_input.delete(0, END)
            mixer.init()
            mixer.music.load("Humble and kind.mp3")
            mixer.music.play()
            window.after(18000, self.show_lyric2(0))

        elif(choice == "meant to be"):
            Karaoke.currentSong = self.song3
            self.setSongImage()
            Karaoke.user_input.delete(0, END)
            mixer.init()
            mixer.music.load("Meant to be.mp3")
            mixer.music.play()
            window.after(6000, self.show_lyric3(0))
        else:
            print(self.menu.Lyrics)
        

    def setupGUI(self):
		#organize the GUI
        self.pack(fill = BOTH, expand = 1)
		#setup the player input at the bottom of the GUI, The widget is a Tkinter Entry, set its background to white and bind the return key to the, function process in the class, push it to the bottom of the GUI and let it fill, horizontally, give it focus so the player doesn't have to click on it
        Karaoke.user_input = Entry(self, bg = "white")
        Karaoke.user_input.bind("<Return>", self.process)
        Karaoke.user_input.pack(side=BOTTOM, fill = X)
        Karaoke.user_input.focus()
		# setup the image to the left of the GUI, the widget is a Tkinter Label, don't let the image control the widget's size
        img = None
        Karaoke.image = Label(self, width=WIDTH // 2, image = img)
        Karaoke.image.image = img
        Karaoke.image.pack(side = LEFT, fill=Y)
        Karaoke.image.pack_propagate(False)
		# setup the text to the right of the GUI
		# first, the frame in which the text will be placed
        text_frame = Frame(self, width = WIDTH // 2)
		# the widget is a Tkinter Text, disable it by default, don't let the widget control the frame's size
        Karaoke.text = Text(text_frame, bg="lightgrey", state = DISABLED)
        Karaoke.text.pack(fill = Y, expand = 1)
        text_frame.pack(side = RIGHT, fill = Y)
        text_frame.pack_propagate(False)

    def run(self):
		# configure the GUI
        self.setupGUI()
        # configure main menu text
        self.setStatus("What song would you like to play: Twinkle Twinkle Little Star, Humble and Kind, Meant to Be? ")
        # display menu image
        self.setSongImage()
        
    def setStatus(self, Lyric):
		# sets the status displayed on the right of the GUI
        Karaoke.text.config(state=NORMAL)
        Karaoke.text.delete("1.0", END)
        if(Karaoke.currentSong == None):
            Karaoke.text.insert(END, "What song would you like to play: Twinkle Twinkle Little Star, Humble and Kind, Meant to Be? \n " )
        else:
            #otherwise display appropriate status
            Karaoke.text.insert(END, str(Lyric)) 

    def setSongImage(self): 
        Karaoke.img = PhotoImage(file = Karaoke.currentSong.image)
        Karaoke.image.config(image = Karaoke.img)
        Karaoke.image.image = Karaoke.currentSong.image
        

##################################################################
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Karaoke Machine")

# create the GUI as a Tkinter canvas inside the window
g = Karaoke(window)
# play the game
g.run()

# wait for the window to close
window.mainloop()
