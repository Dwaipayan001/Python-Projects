import pyttsx3
import speech_recognition as sr
import pandas as pd
import matplotlib.pyplot as plt

r = sr.Recognizer()
mic = sr.Microphone()

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)

volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')

print("====================================\n")
print("WELCOME TO TALKING PANDA'S ASSISTANT\n")
print("====================================\n")


engine.say("WELCOME TO TALKING PANDA ASSISTANT IF YOU WANT TO START ME PLEASE SAY YES.")
engine.runAndWait()

#importing csv file
df = pd.read_csv('data.csv')

#importing json file
js = pd.read_json("data.js")

with mic as source:
    r.adjust_for_ambient_noise(source,duration=0.2)
    audio = r.listen(source)

choice = r.recognize_google(audio)




def head_value(audio ,df):

    engine.say("HOW MANY ROWS FROM THE BEGINNING YOU WANT TO SEE")
    engine.runAndWait()

    with mic as source:
        r.adjust_for_ambient_noise(source,duration=0.2)
        audio = r.listen(source)

    audio = r.recognize_google(audio)

    return df.head(int(audio))

#Defining tail values
def tail_value(audio,df):
    engine.say("HOW MANY ROWS FROM THE LAST YOU WANT TO SEE")
    engine.runAndWait()

    with mic as source:
        r.adjust_for_ambient_noise(source,duration=0.2)
        audio = r.listen(source)

    audio = r.recognize_google(audio)

    print(df.tail(int(audio)))

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

"""========================================
Data Cleaning Functions Starting From here
==========================================="""


#Clearing Empty Cells
def empty_cell(audio,df):

        engine.say("DO YOU WANT IT TO BE INPLACE ")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source,duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)

        if audio.lower()=="yes":
            count_row = df.shape[0]  # Gives number of rows
            count_col = df.shape[1] # GIves number of columns
            engine.say("BEFORE DELETING THE NULL VALUES THERE WERE %d ROWS" % count_row)
            engine.runAndWait()
            df.dropna(inplace=True)
            new_count_row = df.shape[0]
            engine.say("AFTER DELETING THE NULL VALUES THERE WERE %d ROWS" % new_count_row)
            engine.runAndWait()
            print(df.to_string(),"After Deleting the Null values the number of rows are "+str(new_count_row),sep="\n")
        else:
            count_row = df.shape[0]  # Gives number of rows
            engine.say("BEFORE DELETING THE NULL VALUES THERE WERE %d ROWS" % count_row)
            engine.runAndWait()
            new_df = df.dropna()
            new_count_row = new_df.shape[0]
            engine.say("AFTER DELETING THE NULL VALUES THERE WERE %d ROWS" % new_count_row)
            engine.runAndWait()
            print(new_df.to_string(),"After Deleting the Null Values the number of rows are "+str(new_count_row),sep="\n")

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

#Fill Empty Cells

def fill_empty(audio,df):
        engine.say("DO YOU WANT TO REPLACE FOR ALL OR CERTAIN COLUMNS")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source,duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)

        if audio.lower()=='all':

            engine.say("DO YOU WANT IT TO BE INPLACED")
            engine.runAndWait()

            with mic as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)

            audio = r.recognize_google(audio)

            if audio.lower()=="yes":
                engine.say("TELL THE VALUE")
                engine.runAndWait()

                with mic as source:
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    audio = r.listen(source)

                audio = r.recognize_google(audio)

                is_nan = df.isnull().any(axis=1)


                print(df[is_nan])

                df.fillna(audio, inplace=True)

                print("=========================\n")

                return df.to_string()

            else:
                engine.say("TELL THE VALUE")
                engine.runAndWait()

                with mic as source:
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    audio = r.listen(source)

                audio = r.recognize_google(audio)
                new_df = df.fillna(audio)

                return new_df.to_string()
        else:
            engine.say("TELL THE COLUMN NAME")
            engine.runAndWait()

            with mic as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)

            audio = r.recognize_google(audio)

            del_df = df[audio]

            engine.say("THE COLUMN YOU CHOSE  %s" % audio)
            engine.runAndWait()

            is_nan = df.isnull().any(axis=1)

            print(df[is_nan])

            print("===========================\n")

            engine.say("TELL THE VALUE")
            engine.runAndWait()

            with mic as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)

            audio = r.recognize_google(audio)

            del_df.fillna(audio, inplace=True)


            print(del_df.to_string())

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

#Plotting Functions
def plot(audio,df):

        engine.say("WHAT KIND OF PLOT YOU WANT")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source,duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)

        if audio.lower()=="normal":
            df = df.plot()
            return plt.show()

        elif audio.lower()=="scatter":

            engine.say("WHAT WILL BE THE X AXIS")
            engine.runAndWait()

            with mic as source:
                r.adjust_for_ambient_noise(source,duration=0.2)
                audio = r.listen(source)

            audio_x = r.recognize_google(audio)

            engine.say("WHAT WILL BE THE Y AXIS")
            engine.runAndWait()

            with mic as source:
                r.adjust_for_ambient_noise(source,duration=0.2)
                audio = r.listen(source)

            audio_y = r.recognize_google(audio)

            df.plot(kind='scatter',x=audio_x,y=audio_y)

            return plt.show()

        elif audio.lower()=="histogram":
            engine.say("WHICH COLUMNS HISTOGRAM YOU WANT")
            engine.runAndWait()

            with mic as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)

            audio = r.recognize_google(audio)

            df[audio].plot(kind='hist')

            return plt.show()

        else:
            pass

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

#asking for audio
def wanna_continue(audio):
    engine.say("DO YOU WANT TO CONTINUE")
    engine.runAndWait()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    audio = r.recognize_google(audio)

    return audio




#Calling the functions
if __name__=='__main__':
    while choice.lower()=="yes":

        engine.say("PLEASE SAY THE COMMAND OTHERWISE SAY EXIT TO QUIT")
        engine.runAndWait()

        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

        audio = r.recognize_google(audio)


        if audio.lower()=="string":
            print(df.to_string())


        elif audio.lower()=="js":
            print(js.to_string())


        elif audio.lower()=='head':
            print(head_value(audio,df))


        elif audio.lower()=='bottom':
            print(tail_value(audio,df))


        elif audio.lower()=='info':
            print(df.info())


        elif audio.lower()=='clean':
            empty_cell(audio,df)


        elif audio.lower()=='crowd':
            print(fill_empty(audio,df))


        elif audio.lower()=='plot':
            plot(audio,df)

        elif audio.lower()=='exit':
            engine.say("QUITTING ! THANK YOU")
            engine.runAndWait()
            break


        else:
            engine.say("SORRY I CAN'T RECOGNIZE YOU . PLEASE SAY YES TO RETRY OR SAY EXIT TO QUIT")
            engine.runAndWait()

            with mic as source:
                r.adjust_for_ambient_noise(source,duration=0.2)
                audio = r.listen(source)
            choice = r.recognize_google(audio)










