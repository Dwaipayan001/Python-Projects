"""Python program to create a voice assistant by which one can open certain applications like MS Word, Excel, Powerpoint, Notepad etc"""

import pyttsx3
import os
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)

volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')

engine.say("""WELCOME SIR !
YOUR VIRTUAL ASSISTANT IS READY TO HELP YOU.
PLEASE SAY MALE FOR MALE ASSISTANT
PLEASE SAY FEMALE FOR FEMALE ASSISTANT""")
engine.runAndWait()

with mic as source:
    r.adjust_for_ambient_noise(source, duration=0.2)
    audio = r.listen(source)

audio = r.recognize_google(audio)


if audio == "Female".lower():
    engine.setProperty('voice', voices[1].id)
else:
    engine.setProperty('voice', voices[0].id)

engine.say("PLEASE TELL ME THE NAME OF THE SOFTWARE YOU WANT TO OPEN")
engine.runAndWait()
engine.say("""WE HAVE THE FOLLOWING LIST OF SOFTWARE :
    SAY MS WORD FOR > MICROSOFT WORD
    SAY MS POWERPOINT FOR > MICROSOFT POWERPOINT
    SAY MS EXCEL For > MICROSOFT EXCEL
    SAY GOOGLE CHROME FOR > GOOGLE CHROME
    SAY VLC PLAYER FOR > VLC PLAYER
    SAY NOTEPAD FOR > NOTEPAD
    SAY EXIT TO STOP ME """)

engine.runAndWait()


while True:
    engine.say("PLEASE TELL ME THE NAME OF THE SOFTWARE YOU WANT TO OPEN")
    engine.runAndWait()

    with mic as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)

    audio = r.recognize_google(audio)

    if audio.lower() == "ms word":
        engine.say("Starting Microsoft Word")
        engine.runAndWait()
        os.system("start winword")
        continue

    elif audio.lower() == "ms powerpoint":
        engine.say("Starting Microsoft Powerpoint")
        engine.runAndWait()
        os.system("start powerpnt")
        pass

    elif audio.lower() == "ms excel":
        engine.say("Starting Microsoft Excel")
        engine.runAndWait()
        os.system("start excel")
        pass

    elif audio.lower() == "google chrome":
        engine.say("Starting Google Chrome")
        engine.runAndWait()
        os.system("start chrome")
        pass

    elif audio.lower() == "vlc player":
        engine.say("Starting VLC Player")
        engine.runAndWait()
        os.system("start vlc")
        pass

    elif audio.lower() == "notepad":
        engine.say("Starting Notepad")
        engine.runAndWait()
        os.system("start notepad")
        pass

    elif audio.lower() == "exit":
        engine.say("EXITING ! THANK YOU FOR CHOOSING ME, HAVE A NICE DAY !")
        engine.runAndWait()
        exit()

    else:
        engine.say("I CAN'T RECOGNIZE YOU SIR ! PLEASE TRY AGAIN.")









