from urllib.request import proxy_bypass
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

listener = sr.Recognizer()
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening... ")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        print("Playing"+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print("Current Time is :- "+time)
        talk("Current Time is"+time)
    elif 'tell me about' in command:
        info = command.replace('tell me about','')
        info1 = wikipedia.summary(info,2)
        print(info1)
        talk(info1)
    elif 'joke' in command:
        humor = pyjokes.get_joke()
        print(humor)
        talk(humor)
    elif 'google' in command:
        word = command.replace('google','')
        pywhatkit.search(word)
    else:
        print("Sorry I could not understand")
        talk("Sorry I could not understand")

while True:
    run_alexa()
    a = input("Want to continue [Y/N]: ")
    if a.lower()=='n':
        break

