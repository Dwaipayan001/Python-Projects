"""Python Program to build a voice controlled Talking Dictionary using pyttsx3 (python text to speech) module , json (to parse the dictionary json file and use it in the program)
speech_recognition module to continue the conversation with the program and difflib (get close matches) if someone enters a mispelled word then it will search for the closest correct
one in the dictionary json file and say it out loud"""

#importing the modules
import pyttsx3
import json
from difflib import get_close_matches
import speech_recognition as sr

# speech recognition
r = sr.Recognizer()
mic = sr.Microphone()

# setting the rate of speech of the AI
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)

volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')

#Greetings from the AI and the part to select our assistant (Male or Female)
engine.say("""WELCOME TO THE TALKING DICTIONARY.
listen to the instructions carefully :
Do you want Male assistant or female assistant ?
Say Male for Male voice 
Say Female for Female voice""")
engine.runAndWait()

#Getting the first voice input from the user and using adjust_ambient method to remove the noise in the background.
with mic as source:
    r.adjust_for_ambient_noise(source, duration=0.2)
    audio = r.listen(source)

#Recognizing the voice input by user.    
audio = r.recognize_google(audio)



# condition to check if the input is mail or female
if audio == "Female".lower():
    engine.setProperty('voice', voices[1].id)
else:
    engine.setProperty('voice', voices[0].id)

#importing the dictionary json file
data = json.load(open("E:\pythonProjects2\dictionary_compact.json"))


#dictionary function where the main magic happens
def dictionary(word):
    if word in data:
        print(data[word])
        engine.say("The meaning of %s is:" % (word))
        engine.say(data.get(word))
        engine.runAndWait()
    elif len(get_close_matches(word, data.keys())) > 0:
        engine.say("Did you mean %s instead? : " % get_close_matches(word, data.keys())[0])
        engine.runAndWait()
        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
        pass
        if (action == "yes"):
            print(data[get_close_matches(word, data.keys())[0]])
            engine.say("The correct meaning is %s:" % (data[get_close_matches(word, data.keys())[0]]))
            engine.runAndWait()
        elif (action == "no"):
            print("The word doesn't exist in the dictionary")
        else:
            print("We can't understand your input, Sorry.")
    else:
        pass

#some documentation 
print("====================================================== \n")
print("\t WELCOME TO THE TALKING DICTIONARY \n")
print("====================================================== \n")

engine.say("Tell us your word : ")
engine.runAndWait()

with mic as source:
    r.adjust_for_ambient_noise(source, duration=0.2)
    audio = r.listen(source)

word = r.recognize_google(audio)

dictionary(word)

engine.say("Do you want to continue : Y/N ")
engine.runAndWait()

with mic as source:
    r.adjust_for_ambient_noise(source, duration=0.2)
    audio = r.listen(source)

choice = r.recognize_google(audio)

while choice.lower() == "yes":
    engine.say("Tell us your word : ")
    engine.runAndWait()
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)

        word_1 = r.recognize_google(audio)
        dictionary(word_1)
        engine.say("Do you want to continue : Y/N ")
        engine.runAndWait()

    with mic as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)

    choice = r.recognize_google(audio)
else:
    pass





