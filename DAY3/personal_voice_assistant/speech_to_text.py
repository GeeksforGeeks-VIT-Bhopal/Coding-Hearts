# SPEECH TO TEXT RECOGNITION

# pip install speech_recognition
import speech_recognition

# IN CASE OF "PYAUDIO" ERROR, USE BELOW COMMANDS
# pip install pipwin 
# pipwin install pyaudio

# speech_recognition setup
jarvis = speech_recognition.Recognizer()

# main function
with speech_recognition.Microphone() as source:
    print("Listening...\n")
    audioCapture = jarvis.listen(source)

    try:
        print("Recognizing...")
        recognizedText = jarvis.recognize_google(audioCapture)
        print(recognizedText)

    except:
        print("Say that again!")
