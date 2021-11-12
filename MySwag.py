import pyttsx3 as pts
import speech_recognition as sr
import pyaudio
import pyjokes as pj
import os
import webbrowser as wb

def speak(voice):
    engine=pts.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-40)
    engine.say(voice)
    engine.runAndWait()
    
def command():
    r=sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Swag is Listenening ...")
            audio=r.listen(source)
            try:
                query=r.recognize_google(audio)
                query=query.lower()
                return query
                break
            except:
                print("Try Again")
                
while True:
    query=command().split(" ")
    print(query)
    if 'name' in query:
        name=query.index('name')
        name+=2
        line="Hi"+query[name]+"this is Swag Your Voice Assistant"
        speak(line)
    elif 'open' in query:
        name=query.index('open')
        name+=1
        line="Swag Opening"+query[name]
        speak(line)
        os.system(query[name])
    elif 'search' in query:
        s_query="https://www.google.com/search?client=firefox-b-d&q="+str(query)
        wb.open(s_query)
    elif 'joke' in query:
        joke=pj.get_joke()
        speak(joke)
    elif  'play' in query:
        name=query.index('play')
        name+=1
        speak("Opening YouTube to play Video")
        s_query="https://www.youtube.com/results?search_query="+query[name]
        wb.open(s_query)
    elif "who is " in query:
        
    else:
        speak("Swag is closing")
        break
