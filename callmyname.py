from gtts import gTTS
#import vlc
import os

name = input('Enter Your Name Here: ')
#language = input('Enter Language: English|Hindi|French ')
language = 'en'

mySpeech = gTTS(text=name,lang=language,slow=False)
mySpeech.save('name.mp3')

#p = vlc.MediaPlayer("name.mp3")
#p.play()


