import pyttsx3

engine = pyttsx3.init()
text = "Speech synthesis is the computer-generated simulation of human speech. It converts human language text into human-like speech audio."
voices = engine.getProperty("voices")

engine.setProperty("rate", 150)
engine.setProperty("voice",voices[1].id)
engine.say(text)
# play the speech
engine.runAndWait()
