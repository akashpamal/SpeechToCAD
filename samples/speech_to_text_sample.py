import speech_recognition as sr
import pyaudio

init_rec = sr.Recognizer()
print("Let's speak!!")
with sr.Microphone() as source: # TODO check this offline
    audio_data = init_rec.record(source, duration=5)
    print("Recognizing your text.............")
    text = init_rec.recognize_google(audio_data)
    print(text)

"""
If the above script throws a "speech_recognition.UnknownValueError", run the script from the "Terminal" application on Mac, rather than the integrated terminal in VSCode. If you still get this error, make sure that your audio input device is able to capture audio.
"""