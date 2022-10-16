from gtts import gTTS
from playsound import playsound

# This module is imported so that we can
# play the converted audio
import os
file_path = os.getcwd()

# The text that you want to convert to audio
mytext = 'Speech synthesis is the computer-generated simulation of human speech. It converts human language text into human-like speech audio.'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("tmp.mp3")
playsound(file_path+"\\"+"tmp.mp3")

# Playing the converted file

