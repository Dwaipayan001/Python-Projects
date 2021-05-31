import pyttsx3
import json
from difflib import get_close_matches
import speech_recognition as sr

# speech recognition
r = sr.Recognizer()
mic = sr.Microphone()

# talking portion
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)

volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')

engine.say("""WELCOME TO THE TALKING DICTIONARY.
listen to the instructions carefully :
Do you want Male assistant or female assistant ?
Say Male for Male voice 
Say Female for Female voice""")
engine.runAndWait()

with mic as source:
    r.adjust_for_ambient_noise(source, duration=0.2)
    audio = r.listen(source)

audio = r.recognize_google(audio)
# voice_choice = int(input("Do you want Male or Female voice ?"))


# voice_choice == 0 or
if audio == "Female".lower():
    engine.setProperty('voice', voices[1].id)
else:
    engine.setProperty('voice', voices[0].id)

data = json.load(open("E:\pythonProjects2\dictionary_compact.json"))


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





