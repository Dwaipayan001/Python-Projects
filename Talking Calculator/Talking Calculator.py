import pyttsx3
import speech_recognition as sr
import math


r = sr.Recognizer()
mic = sr.Microphone()

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)

volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')


print("============================================================= \n")
print("\t \t WELCOME TO TALKING CALCULATOR \n")
print("============================================================== \n")
print("SAY MALE FOR MALE VOICE \nSAY FEMALE FOR FEMALE VOICE")


engine.say("""WELCOME TO TALKING CALCULATOR 
SAY MALE FOR MALE VOICE
SAY FEMALE FOR FEMALE VOICE""")
engine.runAndWait()


with mic as source:
    r.adjust_for_ambient_noise(source, duration=0.2)
    audio = r.listen(source)

audio = r.recognize_google(audio)

if audio == "Female".lower():
    engine.setProperty('voice', voices[1].id)
else:
    engine.setProperty('voice', voices[0].id)


engine.say("DO YOU WANT TO LISTEN TO THE TYPES OF OPERATION WE HAVE ?")
engine.runAndWait()

with mic as source:
    r.adjust_for_ambient_noise(source, duration=.5)
    query = r.listen(source)

query = r.recognize_google(query)

if query.lower() == "yes":
    engine.say("""PLEASE TELL ME THE OPERATION YOU WANT TO DO ? 
SAY ADDITION TO DO ADDITION 
SAY SUBTRACTION TO DO SUBTRACTION
SAY MULTIPLICATION TO DO MULTIPLICATION
SAY INTEGER DIVISION TO DO INTEGER DIVISION
SAY DIVISION TO DO REGULAR DIVISION (RESULT IN FLOAT)
SAY REMAINDER TO FIND THE REMAINDER OF TWO NUMBERS
SAY FACTORIAL TO DO THE FACTORIAL OF A NUMBER
SAY SQUARE ROOT TO FIND THE SQUARE ROOT OF A NUMBER
SAY POWER TO FIND THE VALUE RAISED TO THE POWER N 
SAY PERCENTAGE TO FIND THE PERCENTAGE OF SOME AMOUNT 
""")
    engine.runAndWait()
else:
    pass


while True or audio.lower() == "yes":
    engine.say("PLEASE TELL ME WHAT OPERATION YOU WANT TO DO OR SAY EXIT IF YOU WANT ME TO STOP ")
    engine.runAndWait()

    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    audio = r.recognize_google(audio)

    # Addition Operation
    if audio.lower() == "addition":
        engine.say("SAY THE NUMBERS YOU WANT TO ADD")
        engine.runAndWait()
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)

        audio = audio.split("and")

        add = 0
        no_list = []
        for j in audio:
            no_list.append(j)

        for i in no_list:
            i = float(i)
            add += i

        add = '{:.2f}'.format(add)

        print("The numbers you wanted to add are : ", *no_list)

        engine.say("The result is : ")
        engine.say(add)
        engine.runAndWait()

        print("The result of the addition is ", add)

        engine.say("Do you want to continue ? ")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)

        if audio.lower() == "no":
            engine.say("THANK YOU ! GOOD BYE")
            engine.runAndWait()
            exit()
        else:
            pass


    #Subtraction Operation
    elif audio.lower() == "subtraction":
        engine.say("SAY THE NUMBERS YOU WANT TO SUBTRACT")
        engine.runAndWait()
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)
        no_list = []
        audio = audio.split("and")
        for i in audio:
            no_list.append(float(i))

        print("The numbers are : ",*no_list)

        sub_res = float(no_list[0])-float(sum(no_list[1:]))
        sub_res_1 = "{:.3f}".format(sub_res)
        engine.say("The result of the subtraction is :")
        engine.say(sub_res_1)
        engine.runAndWait()

        print("The result of the subtraction is ",sub_res_1)

        engine.say("Do you want to continue ? ")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)

        if audio.lower() == "no":
            engine.say("THANK YOU ! GOOD BYE")
            engine.runAndWait()
            exit()

     #Multiplication
    elif audio.lower()=="multiplication":
        engine.say("SAY THE NUMBERS YOU WANT TO MULTIPLY")
        engine.runAndWait()
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)
        no_list_multi = []
        audio = audio.split("and")
        for i in audio:
            no_list_multi.append(i)

        multi = 1
        for l in no_list_multi:
            multi *= float(l)

        multi_1 = "{:.3f}".format(multi)

        print("The numbers you have provided are : ",*no_list_multi)

        engine.say("The result of the multiplication is :")
        engine.say(multi_1)
        engine.runAndWait()

        print("The multiplication is : ",multi_1)
        engine.say("Do you want to continue ? ")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)

        if audio.lower() == "no":
            engine.say("THANK YOU ! GOOD BYE ")
            engine.runAndWait()
            exit()


    #Integer Divison Part
    elif audio.lower()=="integer division":
        engine.say("SAY THE DIVIDEND (THE NUMBER YOU WANT TO DIVIDE) ")
        engine.runAndWait()
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio_1 = r.listen(source)

        audio_1 = r.recognize_google(audio_1)

        engine.say("SAY THE DIVISOR (THE NUMBER WITH WHICH YOU WANT TO DIVIDE) ")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio_2 = r.listen(source)

        audio_2 = r.recognize_google(audio_2)

        res = int(audio_1)//int(audio_2)

        engine.say("The result of the Integer Division is ")
        engine.say(res)
        engine.runAndWait()

        print("The result of the Integer Division is ", res)

        engine.say("Do you want to continue ? ")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)
        if audio.lower() == "no":
            engine.say("THANK YOU ! GOOD BYE ")
            engine.runAndWait()
            exit()

    #Divison Part
    elif audio.lower() == "division":
        engine.say("SAY THE DIVIDEND (THE NUMBER YOU WANT TO DIVIDE) ")
        engine.runAndWait()
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio_3 = r.listen(source)

        audio_3 = r.recognize_google(audio_3)
        audio_3 = float(audio_3)

        engine.say("SAY THE DIVISOR (THE NUMBER WITH WHICH YOU WANT TO DIVIDE) ")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio_4 = r.listen(source)

        audio_4 = r.recognize_google(audio_4)
        audio_4 = float(audio_4)

        div_res = audio_3/audio_4
        div_res_1 = "{:.3f}".format(div_res)

        engine.say("The Dividend you provided is :")
        engine.say(audio_3)
        engine.say("The Divisor you provided is : ")
        engine.say(audio_4)
        engine.runAndWait()


        engine.say("The result of the division is :")
        engine.say(div_res_1)
        engine.runAndWait()


        print("The result of the divison is :",div_res_1)

        engine.say("Do you want to continue ? ")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)

        if audio.lower() == "no":
            engine.say("THANK YOU ! GOOD BYE ")
            engine.runAndWait()
            exit()

    #Remainder Part
    elif audio.lower() == "remainder":
        engine.say("SAY THE DIVIDEND (THE NUMBER YOU WANT TO DIVIDE) ")
        engine.runAndWait()
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio_5 = r.listen(source)

        audio_5 = r.recognize_google(audio_5)

        engine.say("SAY THE DIVISOR (THE NUMBER YOU WITH WHICH YOU WANT TO DIVIDE) ")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio_6 = r.listen(source)

        audio_6 = r.recognize_google(audio_6)

        remain = int(audio_5)%int(audio_6)

        print("The numbers you provided are : ",audio_5,audio_6)

        engine.say("The remainder is :")
        engine.say(remain)
        engine.runAndWait()

        print("The remainder is :",remain)

        engine.say("Do you want to continue ? ")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)

        if audio.lower() == "no":
            engine.say("THANK YOU ! GOOD BYE ")
            engine.runAndWait()
            exit()

    #Factorial Part
    elif audio.lower() == "factorial":
        engine.say("SAY THE NUMBER WHOSE FACTORIAL YOU WANT ")
        engine.runAndWait()
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)

        fact = 1
        aud_conv = int(audio)
        if (aud_conv == 0 or aud_conv == 1):
            print(1)

        else:
            for k in range(1,aud_conv+1):
                fact *= k
            
        print("The number you provided is ",aud_conv)

        engine.say("The result of the factorial is : ")
        engine.say(fact)
        engine.runAndWait()

        print("THe result of the factorial is :",fact)


        engine.say("Do you want to continue ? ")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)

        if audio.lower() == "no":
            engine.say("THANK YOU ! GOOD BYE ")
            engine.runAndWait()
            exit()

    #SQUARE ROOT
    elif audio.lower() == "square root":
        engine.say("SAY THE NUMBER WHOSE SQUARE ROOT YOU WANT")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            sqrt_audio = r.listen(source)

        sqrt_audio = r.recognize_google(sqrt_audio)

        sqrt_audio = int(sqrt_audio)

        engine.say("THE NUMBER YOU PROVIDED IS ")
        engine.say(sqrt_audio)
        engine.runAndWait()

        sqrt = math.sqrt(sqrt_audio)

        print("The square root of %d is %d" %(sqrt_audio,sqrt))

        engine.say("THE SQUARE ROOT IS ")
        engine.say(sqrt)
        engine.runAndWait()

        engine.say("Do you want to continue ? ")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)

        if audio.lower() == "no":
            engine.say("THANK YOU ! GOOD BYE ")
            engine.runAndWait()
            exit()

     #Exponential
    elif audio.lower()=="power":
        engine.say("SAY THE NUMBER WHOSE POWER YOU WANT ")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            pow_audio = r.listen(source)

        pow_audio_1 = r.recognize_google(pow_audio)

        pow_audio_1 = int(pow_audio_1)

        engine.say("THE NUMBER YOU PROVIDED IS ")
        engine.say(pow_audio_1)
        engine.runAndWait()

        engine.say("SAY THE NUMBER TO RAISE TO THE POWER ")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            pow_audio_2 = r.listen(source)

        pow_audio_2 = r.recognize_google(pow_audio_2)

        pow_audio_2 = int(pow_audio_2)

        engine.say("THE NUMBER YOU PROVIDED IS ")
        engine.say(pow_audio_2)
        engine.runAndWait()


        pow = math.pow(pow_audio_1,pow_audio_2)

        print("The value of %d raise to the power %d is %d" % (pow_audio_1,pow_audio_2, pow))

        engine.say("THE FINAL ANSWER IS ")
        engine.say(pow)
        engine.runAndWait()

        engine.say("Do you want to continue ? ")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)

        if audio.lower() == "no":
            engine.say("THANK YOU ! GOOD BYE ")
            engine.runAndWait()
            exit()


    #percentage
    elif audio.lower() == "percentage":
        engine.say("SAY THE NUMBER WHOSE PERCENTAGE YOU WANT ")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            per_audio_1 = r.listen(source)

        per_audio_1 = r.recognize_google(per_audio_1)

        per_audio_1 = int(per_audio_1)

        engine.say("THE NUMBER YOU PROVIDED IS ")
        engine.say(per_audio_1)
        engine.runAndWait()

        engine.say("SAY THE AMOUNT OF PERCENTAGE ")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            per_audio_2 = r.listen(source)

        per_audio_2 = r.recognize_google(per_audio_2)

        per_audio_2 = int(per_audio_2)

        engine.say("THE NUMBER YOU PROVIDED IS ")
        engine.say(per_audio_2)
        engine.runAndWait()

        per = (per_audio_1*per_audio_2)/100

        print("The value of %d percent of %d is %.2f" %(per_audio_2, per_audio_1, per))

        engine.say("THE FINAL ANSWER IS ")
        engine.say(per)
        engine.runAndWait()

        engine.say("Do you want to continue ? ")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)

        if audio.lower() == "no":
            engine.say("THANK YOU ! GOOD BYE ")
            engine.runAndWait()
            exit()





    else:
        engine.say("I CAN'T RECOGNIZE YOU ! PLEASE SAY YES IF YOU WANT TO CONTINUE OR ELSE SAY EXIT TO EXIT")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)

    if audio.lower() == "exit":
        exit()









