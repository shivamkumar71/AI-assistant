import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import webbrowser
import musiclibrary

# Initialize the recognizer and TTS engine
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech



def talk(text):
    global engine
    engine.say(text)
    engine.runAndWait()
    
def greet_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
       greeting = "Good morning"
    elif 12 <= hour < 15:
        greeting = "Good afternoon"
    elif 15 <= hour < 18:
        greeting = "Good evening"
    else:
        greeting = "Good night"
    talk(f"{greeting} My dad. how can i assit you")

def listen_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            
            if 'hello' in command:
                command = command.replace('hello', ' ')
                print("Command:", command)
    
    except sr.UnknownValueError:
        command = "not listen"
    return command
def wake_word():
    
    while True:
        try:
            with sr.Microphone() as source:
                print("listening....")
                voice = listener.listen(source)
                trigger_word = listener.recognize_google(voice).lower()
                if 'hello jarvis' in trigger_word:
                    talk("yes sir, i am yere")
                    break
        except sr.UnknownValueError:
            pass
        
def run_jarvis():
    command = listen_command()
    
    if 'play song' in command:
        song = command.replace('open play', '')
        talk(f'i am playing song')
        webbrowser.open("https://youtu.be/5C8ZXQ1SmbQ?si=4dW6Lp11uQJVIeSM")
        
    if command.startswith("play"):
        # Extract the song name by removing the "play" keyword
        song = command.replace("play", "").strip()
        
        # Check if the song exists in the music library
        if song in musiclibrary.music:
            link = musiclibrary.music[song]
            talk(f'I am playing {song}')
            webbrowser.open(link)
        else:
            talk(f"Sorry, I couldn't find the song '{song}' in the music library.")
        
        
    elif 'open youtube' in command:
        talk("i am opening youtube.")
        webbrowser.open("https://www.youtube.com")
        
    elif 'open facebook' in command:
        talk("i am opening facebook.")
        webbrowser.open("https://www.facebook.com")
        
    elif 'open instagram' in command:
        talk("i am opening instagram.")
        webbrowser.open("https://www.instagram.com")
        
    elif 'open gmail' in command:
        talk("i am opening gmail.")
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    
    elif 'open linkdin' in command:
        talk("i am opening linkdin.")
        webbrowser.open("https://www.linkedin.com/feed/")
    
    elif 'open github' in command:
        talk("i am opening github.")
        webbrowser.open("https://github.com/BlackHat2024-25")
        
    elif 'tell me current time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        
    elif 'you know' in command:
        person = command.replace('you know about', '')
        info = wikipedia.summary(person, sentences=3)
        talk(info)
        
    elif 'what is date today' in command:
        date = datetime.datetime.now().strftime('%A, %B %d, %Y')
        talk(f'Today is {date}')
    else:
        talk("say again")
            
    
        

# greet_user()
# Main loop to keep Jarvis running
wake_word()
greet_user()


while True:
    run_jarvis()


