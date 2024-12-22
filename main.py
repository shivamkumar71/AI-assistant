import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import webbrowser
import musiclibrary
import os
import requests
import bs4
import searchweb
from searchweb import searchGoogle
from searchweb import searchYoutube
from searchweb import searchWikipedia
import time

# Initialize the recognizer and TTS engine
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 140)  # Speed of speech



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
    talk(f"{greeting} My dad. how can i help you")

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
                if 'hello bro' in trigger_word:
                    talk("yes sir, i am yere")
                    break
        except sr.UnknownValueError:
            pass

def get_credentials():
    my_username = "shivam"
    password = 717334
    talk("Welcome to Shivam creative World. Please login to continue")
    time.sleep(1)
    
    while True:
        talk("Please enter your username")
        username = input("Enter your username: ")
        if not username.isalpha():
            talk("Username must be alphabetic. Try again.")
            continue
        
        talk("Please enter your password")
        try:
            login_code_input = int(input("Enter your password: "))
        except ValueError:
            talk("Password must be numeric. Try again.")
            continue
        
        if username == my_username and login_code_input == password:
            talk("Login successful")
            time.sleep(1)
            talk("Welcome to Shivam creative world. wakeup me by saying. hello bro")
            print()
            break
        elif username != my_username and login_code_input != password:
            talk("Invalid username and password, Try again")
        elif username != my_username:
            talk("Invalid username, Try again")
        elif login_code_input != password:
            talk("Invalid Password, Try again")
        
def run_jarvis():
    command = listen_command()
    executed = False
    
    if 'play song' in command:
        song = command.replace('open play', '')
        talk(f'i am playing song')
        webbrowser.open("https://youtu.be/5C8ZXQ1SmbQ?si=4dW6Lp11uQJVIeSM")
        executed = True
        
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
        executed = True
        
    elif 'open youtube' in command:
        talk("i am opening youtube.")
        webbrowser.open("https://www.youtube.com")
        executed = True
        
    elif 'open tmu portal' in command:
        talk("i am opening tmu portal.")
        webbrowser.open("https://portal.tmu.ac.in")
        executed = True
    
    elif "hi jarvis" in command:
        talk("Hello sir, how are you ?")
        executed = True
        
    elif "i am fine" in command:
        talk("that's great, sir")
        executed = True
        
    elif "how are you" in command:
        talk("Perfect, sir")
        executed = True
        
    elif "what can you do for me" in command:
        talk("i can everything which you want because. maine tumhara. namak khaayaa. hai")
        executed = True
        
    elif "thanks" in command:
        talk("you are welcome, sir")
        executed = True
        
    elif 'open facebook' in command:
        talk("i am opening facebook.")
        webbrowser.open("https://www.facebook.com")
        executed = True
        
    elif 'open instagram' in command:
        talk("i am opening instagram.")
        webbrowser.open("https://www.instagram.com")
        executed = True
        
    elif 'open gmail' in command:
        talk("i am opening gmail.")
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        executed = True
    
    elif 'open linkdin' in command:
        talk("i am opening linkdin.")
        webbrowser.open("https://www.linkedin.com/feed/")
        executed = True
    
    elif 'open github' in command:
        talk("i am opening github.")
        webbrowser.open("https://github.com/BlackHat2024-25")
        executed = True
        
    elif 'tell me current time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        executed = True
        
    elif 'you know' in command:
        person = command.replace('you know about', '')
        info = wikipedia.summary(person, sentences=3)
        talk(info)
        executed = True
        
    elif 'what is date today' in command:
        date = datetime.datetime.now().strftime('%A, %B %d, %Y')
        talk(f'Today is {date}')
        executed = True
        
    elif "google" in command:
        talk("Searching...")
        searchGoogle(command)
        executed = True
        
    elif "youtube" in command:
        talk("Searching...")
        searchYoutube(command)
        executed = True
        
    elif "wikipedia" in command:
        talk("Searching...")
        searchWikipedia(command)
        executed = True
        
    elif "shutdown computer" in command:
        talk("Shutting down the system.")
        talk("Goodbye")
        os.system("shutdown /s /t 1")
        executed = True
        
    elif "now you can sleep" in command:
        talk("Going to sleep dad. wake up me when you need. good bye")
        exit()
        
    if not executed:
        talk("say again")
            
    
        

# greet_user()
# Main loop to keep Jarvis running
get_credentials()
wake_word()
greet_user()


while True:
    run_jarvis()


