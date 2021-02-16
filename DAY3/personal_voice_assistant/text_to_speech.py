# TEXT TO SPEECH RECOGNITION

# pip install pyttsx3
import pyttsx3

# Call this funstion to let the system speak
def speak(text):
    # pyttsx3 supports sapi5 TTS(text-to-speech) engine
    # sapi5 is a free text-to-speech engine provided by Microsoft that provides voice to your system
    engine = pyttsx3.init('sapi5')
    # UN-COMMENT LINE 10 & 12 TO CHANGE THE VOICE
    # voices = engine.getProperty('voices')
    # # 0 -> MALE , 1 -> FEMALE
    # engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()

# main() function
speak("Hello Hardik how are you")
