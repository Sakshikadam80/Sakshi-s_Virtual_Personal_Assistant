import speech_recognition as sr #speech to text
import pyttsx3  #text to speech
import pywhatkit  #to search youtube
import datetime  #python buildin package
import wikipedia  #import externally
import pyjokes

listener = sr.Recognizer()  #to recognize our voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')  #to convert male voice into female
engine.setProperty('voice', voices[1].id) #2nd position id is female voice
def talk(text):
    engine.say(text)
    engine.runAndWait()
#talk('Hello!, I am personal assistant of saakshi, What can I do for you')
#talk('What can I do for you')
talk('Hello!, I am personal assistant of saakshi, What can I do for you')
def take_command():
    #command = None
    try:  #sometimes our microphone could not work or another error can be occurred
        command = ''
        with sr.Microphone() as source:  #source of our audio/command
            print('Please talk, I am Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)  #voice to text-google will give us text
            #print(command)
            command = command.lower()
            if 'sakshi' in command:
                command = command.replace('sakshi', '')
                #talk(command)
                print(command)
    except:
        pass
    return command
def run_sakshi() :
    command = take_command()
    print(command)
    if 'play' in command:
        video = command.replace('play', '')
        talk('Playing' + video)
        pywhatkit.playonyt(video) #to seach on yt
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p') #current time in string format
        print(time)
        talk('Current time is' + time)
    elif 'information about' in command:
        person = command.replace('information about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'coffee' in command:
        talk('sorry, I have an headache')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say the command again.')


run_sakshi()
