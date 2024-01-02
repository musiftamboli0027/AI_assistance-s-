import os
import pyaudio
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
Dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}    

def openappweb(query):
    speak("Launching, sir")
    if ".com " in query or ".co.in" in query or "org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("lanuching","")
        query = query.replace("","")
        webbrowser.open.replace("https://www.{query}")
    else:
        keys = list(Dictapp.keys())
        for app in keys:
            if app in query:
               os.system(f"start {Dictapp[app]}")
               
def closeappweb(query):
    speak("Closing,  sir")
    if "one tab" in query or "1 tab" in query:
        pyaudio.hotkey("ctrl","w") 
        speak("All tabs closed , sir")    
    elif "2 tab" in query:
        pyaudio.hotkey("ctrl","w")
        sleep(0.5)
        pyaudio.hotkey("ctrl","w")
        speak("All tabs closed , sir")
    elif "3 tab" in query:
        pyaudio.hotkey("ctrl","w")
        sleep(0.5)
        pyaudio.hotkey("ctrl","w")
        sleep(0.5)
        pyaudio.hotkey("ctrl","w")
        speak("All tabs closed , sir") 
         
    elif "4 tab" in query:
        pyaudio.hotkey("ctrl","w")
        sleep(0.5)
        pyaudio.hotkey("ctrl","w")
        sleep(0.5)
        pyaudio.hotkey("ctrl","w")
        sleep(0.5)
        pyaudio.hotkey("ctrl","w")
        speak("All tabs closed , sir")           
    elif "5 tab" in query:
        pyaudio.hotkey("ctrl","w")
        sleep(0.5)
        pyaudio.hotkey("ctrl","w")
        sleep(0.5)
        pyaudio.hotkey("ctrl","w")
        sleep(0.5)
        pyaudio.hotkey("ctrl","w")
        sleep(0.5)
        pyaudio.hotkey("ctrl","w")
        speak("All tabs closed , sir")       
                      
    else:
        keys = list(Dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {Dictapp[app]}.exe")        
        