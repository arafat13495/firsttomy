import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
tomy = pyttsx3.init()
voices = tomy.getProperty('voices')
tomy.setProperty('voice', voices[1].id)


def talk(text):
    tomy.say(text)
    tomy.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'tomy' in command:
                command = command.replace('tomy', '')
    except:
        pass
    return command


def run_tomy():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'date' in command:
        talk('Sorry vaiya, I am in another relation')
    elif 'my name' in command:
        talk('your name is arafat')
    elif 'tomy' in command:
        talk('how can i help you?')
    elif 'what do you do' in command:
        talk('i am talk with you')
    elif 'my father name' in command:
        talk('your father name is toufiqul alam')
    elif 'my mother name' in command:
        talk('your moher name is laila akter')
    elif 'my sister name' in command:
        talk('your sister name is tuba and aroshi')
    elif 'my grandmother name' in command:
        talk('your grandmother name is helena akter')
    elif 'my grandfather name' in command:
        talk('your grandfather name is abdul wadud')
    elif 'how are you' in command:
        talk('i am fine')
    elif 'is your boss' in command:
        talk('my boss is MD Yasir Arafat')
    elif 'what is your name' in command:
        talk('my name is tomy')
    elif 'how old are you' in command:
        talk('i am a robbot so i have no years or no birtday ,i am upgrade everyday by my boss Arafat')
    else:
        talk('I did not get it but I am going to search it for you')
        pywhatkit.search(command)


while True:
    run_tomy()