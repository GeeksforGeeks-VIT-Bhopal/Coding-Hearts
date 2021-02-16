import pyttsx3      #pip install pyttsx3
import datetime     
import speech_recognition as sr     #pip install speechRecognition #$pip install speech-recognition
import wikipedia            #pip install wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')          #sapi5 is the speech recognization application developed by Microsoft 
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    """Speak function is defined to let the system to speak """
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """ Call the date and time module and help to recogize the time and date which wll help to say GM/GA/GE"""
    hour = int(datetime.datetime.now().hour)    
    if hour >=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hey Sir I am Siere your Virtual Assistant. How may I help you")

def takeCommand():
    '''
   It takes michrophone input from the user and returns string as output
   In simple words it listen your commands and gives the output that you spoked
   '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening!!!......")
        r.pause_threshold = 0.9
        r.energy_threshold =380
        r.phrase_threshold = 0.4
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in') # Converssion of audio data to English language 
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception:
        print("Please say that again......")
        speak("Please say that again")
        return "None"

    return query


# if __name__ == '__main__':
wishMe()
while True:
    query = takeCommand().lower()

    #Logic for executing tasks bassed on query
    if 'wikipedia' in query:
        # speak("Searching Wikipedia....")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=1)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open amazon' in query:
        webbrowser.open("amazon.in")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'play music'  in query:
        music_dir = 'C:\\Users\\ayush\\OneDrive\\Desktop\\AYUSHMAAN\\musics\\English'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[random.randrange(0,len(songs))]))
        speak("Sure!")

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")     

    elif 'open code' in query:
        codepath = "C:\\Users\\ayush\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        # speak("Opening VS Code")
        print("<Here it is>")
        os.startfile(codepath)

    elif 'next' in query:
        music_dir = 'C:\\Users\\ayush\\OneDrive\\Desktop\\AYUSHMAAN\\musics\\English'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[random.randrange(0,len(songs))]))
        
    elif 'developer' in query:
        speak("I was developed by Ayushmaan on 21 OCtober 2020")

    elif 'who are you' in query:
        speak("I am an Assistant which does not contain any AI or ML techniques but still can help you")

    elif 'help' in query:
        speak("I can help you with the mentioned things")
        print("Wikipedia,Amazon,Google,PlayMusic,Time,Open code, who are you,new,\n At End to close say quit")
        speak("I can search for you in Wikipedia, I can open Amazon ,I can Open Youtube ,I can Play Music ,I can tell you time and many more")
        

    elif 'new' in query:
        webbrowser.open("aajtak.in")
        

    elif 'quit' in query:
        speak("Hold it don't go ")
        speak("Meet you Soon Sir")
        exit(0)
