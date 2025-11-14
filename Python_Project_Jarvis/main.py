# AI Assistant who's name is JARVIS who perform all tasks for you 

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI

# Initialize pyttsx3 voice engine
engine = pyttsx3.init('sapi5')  # works best on Windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # male voice
engine.setProperty('rate', 175)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()  # ensures the voice actually plays

def processCommand(c):
    c = c.lower()

    if "who made you" in c or "who created you" in c:
        speak("I was created by Adesh.")

    elif "open google" in c:
        speak("Opening Google.")
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        speak("Opening YouTube.")
        webbrowser.open("https://youtube.com")

    elif c.startswith("play"):
        song = c.replace("play", "").strip()
        if song in musicLibrary.music:
            speak(f"Playing {song} on YouTube.")
            webbrowser.open(musicLibrary.music[song])
        else:
            speak(f"Sorry, I couldn't find {song} in your music library.")

    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word 'Jarvis'...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
            word = recognizer.recognize_google(audio).lower()

            if "jarvis" in word:
                speak("Yes sir, how may I help you?")
                with sr.Microphone() as source:
                    print("Listening for your command...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    print("Command:", command)
                    processCommand(command)

        except Exception as e:
            print("Error:", e)
