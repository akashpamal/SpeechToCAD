import tkinter as tk
import pyttsx3
import speech_recognition as sr

from text_parser import TextParser 

WHITE = "#FFFFFF"
BLACK = "#000000"
DARK_GREY = "#1C1C1C"

class Application:
    def __init__(self):
        self.parser = TextParser()
        
        
        
        self.root = tk.Tk()
        self.root.call('wm', 'attributes', '.', '-topmost', True)
        self.root.title("Speech to CAD")
        self.root.geometry("1280x718")
        
        self.root.configure(bg=BLACK)
        
        header_height = 2
        #self.speak("your mom a hoe")
        
        self.recording = False
        record = tk.Frame(self.root, bg=DARK_GREY, padx=1, height=30)
        record.grid(row = 4, column = 1, pady = 1)
        title = tk.Label(record, text="Audio Recording", height=header_height, bg="#DC143C", fg=WHITE, width=30, font=("Karla", 18)).grid(row = 1)
        
        options = sr.Microphone.list_microphone_names()
        self.variable = tk.StringVar(self.root)
        self.variable.set(options[1]) # default value

        w = tk.OptionMenu(record, self.variable, *options).grid(row = 3, pady = (5, 5))
        
        self.mic = self.create_audio_dropdown(record)
        self.record = tk.Button(record, text="Record", highlightbackground = DARK_GREY, command = self.record, font=("Karla", 18)).grid(row = 2, pady = (5, 5))
        self.exit = tk.Button(record, text="Exit", highlightbackground = DARK_GREY, command = self.exit, font=("Karla", 18)).grid(row = 4, pady = (5, 5))
        #Indicator GIFs
        #record.place(x = 1, y = 1, width=30, height=30)
        
        stt = tk.Frame(self.root, bg=DARK_GREY, padx=1)
        stt.grid(row = 4, column = 2, pady = 1)
        title = tk.Label(stt, text="Text Parsing", height=header_height, bg="#00B300", width=35, fg=WHITE, font=("Karla", 18)).grid(row = 1)
        self.current_text = tk.Text(stt, width = 30, height = 15, bg=BLACK, highlightbackground = DARK_GREY, fg=WHITE, highlightcolor = "#7BAEDC", wrap = tk.WORD, font=("Karla", 18), pady=5)
        self.current_text.grid(row = 2, padx = 15)
        self.refresh = tk.Button(stt, text="Update Parsing", highlightbackground = DARK_GREY, command = self.update, font=("Karla", 18)).grid(row = 3, pady = (5, 5))
        self.sysnthezied_info = tk.Label(stt, text="Example translation", font=("Karla", 18)).grid(row = 4, padx = 10)
        #stt.place(x = 33, y = 1, width=30, height=30)
        
        view = tk.Frame(self.root, bg=DARK_GREY, padx=1)
        view.grid(row = 3, column = 3, pady = 1)
        title = tk.Label(view, text="STL Synthesization", height=header_height, bg="#3792CB", width=40, fg=WHITE, font=("Karla", 18)).grid(row = 1)
        # View Module
        
        # The below code is a workaround that allows us to determine the window size in
        # pixels and then position the window wherever we want before drawing it.
        self.root.withdraw()
        self.root.update_idletasks()
        
        self.root.deiconify()
        self.root.mainloop()
        
        
    def create_audio_dropdown(self, master):
        options = sr.Microphone.list_microphone_names()
        variable = tk.StringVar(master)
        variable.set(options[0]) # default value

        w = tk.OptionMenu(master, variable, *options)
        return variable

    def exit(self):
        self.root.destroy()
        quit()
        
    def refresh_info(self):
        new_text = self.record()
        self.set_text(new_text)
        objects = self.parser.text_to_objects(new_text)
        #self.sysnthezied_info
        
    def record(self):
        print("Recording Audio from " + self.variable.get())
        self.recording = True
        r=sr.Recognizer()
        index = sr.Microphone.list_microphone_names().index(self.variable.get())
        mic = sr.Microphone(device_index=index)
        audio_file = sr.AudioFile('./Audio Inputs/cylinder_audio.wav')
        with audio_file as source:
            #r.adjust_for_ambient_noise(source, duration=3)
            # r.energy_threshold()
            print("say anything : ")
            audio = r.listen(source, timeout=10.0)
            try:
                text = r.recognize_google(audio)
                print(text)
                self.recording = False
                # self.set_text(text)
                return text
            except:
                print("sorry, could not recognize")
                
    def set_text(self, text):
        #self.current_text.delete(1.0,"end")
        self.current_text.insert(1.0, text)
    
    def update(self, b = None):
        print(self.current_text.get("1.0",'end-1c'))
        
    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text) 
        engine.runAndWait()

if __name__=="__main__":
    Application()