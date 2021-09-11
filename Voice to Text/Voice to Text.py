"""A simple Voice to text program where using the speech_recognition module we will open Notepad using our voice and a text file in writing mode , then using the SR module we will say 
something, the voice input automatically gets converted into string so we will just use that to write what has been said into the opened text file"""



import pyttsx3
import speech_recognition as sr
import os



file = open("test.txt","w")

r = sr.Recognizer()
mic = sr.Microphone()


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)

volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')

engine.say("""WELCOME SIR !
I AM HERE TO HELP YOU.
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

while True:
    engine.say("PLEASE TELL ME THE NAME OF THE SOFTWARE YOU WANT TO OPEN OR SAY EXIT TO STOP ME !")
    engine.runAndWait()

    with mic as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)

    audio = r.recognize_google(audio)

    if audio.lower() == "notepad":
        engine.say("Starting Notepad")
        engine.runAndWait()
        os.system("start notepad")
        engine.say("PLEASE TELL ME WHAT YOU WANT TO WRITE IN NOTEPAD")
        engine.runAndWait()
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)
        f = file.write(audio)
        continue

    elif audio.lower()=="exit":
        engine.say("EXITING ! THANK YOU FOR CHOOSING ME, HAVE A NICE DAY !")
        engine.runAndWait()
        exit()
    else:
        engine.say("I CAN'T RECOGNIZE YOU SIR ! PLEASE TRY AGAIN.")
        engine.runAndWait()

file.close()



