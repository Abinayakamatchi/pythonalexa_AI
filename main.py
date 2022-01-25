import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# to recognize the voice
listener = sr.Recognizer()
# create an engine that will speak to you
engine = pyttsx3.init()
# variable voices to get all the voices speech to text can provide
voices = engine.getProperty('voices')
# set a female voice to alexa
engine.setProperty('voice', voices[1].id)

global shutdown
shutdown = False


def talk(text):
    engine.say(text)
    engine.runAndWait()


def takes_command():
    try:
        with sr.Microphone() as Source:
            print('listening...')
            # to listen to the listener
            voice = listener.listen(Source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace("alexa", "")
                print(command)
                return command
            else:
                return ""
    except:
        return ""
        pass


def run_alexa():
    command = takes_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', "")
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'are you human' in command:
        talk('No,i am a bot')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif " shut down" in command:
        global shutdown
        talk("Shutting down...")
        shutdown = True
    else:
        talk('sorry,i am not getting you')

while True:
 run_alexa()
