import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("Listeing....")
            r.pause_threshold = 1
            
            r.energy_threshold = 300
            audio = r.listen(source,0,4)
        
        try:
            print("understand...")
            query = r.recognize_google(audio,language='en,in')
            print(f"you siad: {query}\n")  
        except Exception as e:
            print("say that agian") 
            return "None"
        return query
    
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()    
        if "wake up" in query:   
            from Greetme import greetMe
            greetMe()
            
            while True:
                query = takeCommand().lower()  
                if "go to sleep" in query:
                    speak("ok sir, you can me call anytime")
                    break  

                elif "hello" in query:
                    speak("hello sir , how are you ? ")
                elif " i am fine "in query:
                    speak("that's great sir")
                elif "how are you" in query:
                    speak("perfect sir")        
                elif "thank you" in query:
                    speak("you are welcome , sir")    
                    
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)    
                    
                elif " google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)
                elif "Youtube" in query:
                    from searchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipidia" in query:
                    from searchNow import searchWikipidia
                    searchWikipidia(query)       
                    
                elif "temperature" in query or "weather" in query:
                    location = "solapur"
                    search = f"{query} in {location}"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"Current {search} is {temp}")

                elif "Weather" in query:
                    search = "weather in solapur"   
                    url = f"https://www.google.com/search?q={search}" 
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}") 
                    
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"sir, the time is {strTime}")  
                     
                elif "finally sleep" in query:
                    speak(f"ok sir, I am going to sleep now,.. if you need any kind of help please call me sir, ..I am always there for you sir...ok sir,... bye ")    
                    exit()
                     