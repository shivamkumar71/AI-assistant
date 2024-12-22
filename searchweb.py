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

# Initialize the recognizer and TTS engine
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech



def talk(text):
    global engine
    engine.say(text)
    engine.runAndWait()
    
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

def searchGoogle(command):
    if "google" in command:
        import wikipedia as googleScrap
        command = command.replace("jarvis","")
        command = command.replace("google search","")
        command = command.replace("google","")
        talk("This is what I found on google")

        try:
            pywhatkit.search(command)
            result = googleScrap.summary(command,1)
            talk(result)

        except:
            talk("No speakable output available")

def searchYoutube(command):
    if "youtube" in command:
        talk("This is what I found for your search!") 
        command = command.replace("youtube search","")
        command = command.replace("youtube","")
        command = command.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + command
        webbrowser.open(web)
        pywhatkit.playonyt(command)
        talk("Done, Sir")

def searchWikipedia(command):
    if "wikipedia" in command:
        talk("Searching from wikipedia....")
        command = command.replace("wikipedia","")
        command = command.replace("search wikipedia","")
        command = command.replace("jarvis","")
        results = wikipedia.summary(command,sentences = 2)
        talk("According to wikipedia..")
        print(results)
        talk(results)