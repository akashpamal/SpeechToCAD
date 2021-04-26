import speech_recognition as sr
recognizer = sr.Recognizer()
mic = sr.Microphone()
sr.Microphone.list_microphone_names()

with mic as source:
    print('Adjusting for ambient noise...')
    recognizer.adjust_for_ambient_noise(source)
    print('Say something!')
    audio = recognizer.listen(source)

try:
    print('Recognizing text...')
    recognized_text = recognizer.recognize_google(audio)
    print(recognized_text)
except sr.RequestError:
    # API was unreachable or unresponsive
    recognized_text = False
    # response["error"] = "API unavailable"
    print('API Unavailable')
except sr.UnknownValueError:
    # speech was unintelligible
    # response["error"] = "Unable to recognize speech"
    print('Unable to recognize speech')