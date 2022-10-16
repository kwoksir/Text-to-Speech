# Python program to convert
# text to speech

# import the required module from text to speech conversion
import win32com.client

# Calling the Dispatch method of the module which
# interact with Microsoft Speech SDK to speak
# the given input from the keyboard

speaker = win32com.client.Dispatch("SAPI.SpVoice")
text = "Speech synthesis is the computer-generated simulation of human speech. It converts human language text into human-like speech audio."

speaker.Speak(text)

