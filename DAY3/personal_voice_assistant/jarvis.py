# pip install speech-recognition
import speech_recognition 

# pip install pyttsx3
import pyttsx3   

# speech_recognition setup
jarvis = speech_recognition.Recognizer()

# TO GET INPUT AUDIO
# pip install pipwin
# pipwin install pyaudio

# Call this funstion to let the system speck
def speak(audio):
    # sapi5 is the speech application developed by Microsoft 
    # sapi5 is a free module provided by Microsoft that provides voice to ypur system
    engine = pyttsx3.init('sapi5')  
    # voices = engine.getProperty('voices')
    # 0 -> MALE , 1 -> FEMALE
    # engine.setProperty('voice',voices[0].id)
    engine.say(audio)
    engine.runAndWait()

# main()
condition = True
while condition:
    with speech_recognition.Microphone() as source:
        print('Listening...')
        audio = jarvis.listen(source)

    try:
        print("Recognizing...")
        text = jarvis.recognize_google(audio)

        if 'exit' in text:
            print("YOU: " + text)
            print("Alex: Good Bye")
            speak("Good Bye")
            condition = False

        else:
            print("YOU: " + text)
            print("Alex: Hii there!")
            speak("Hii there")
    except:
        print('Please say that again...')
        speak("Please say that again")
