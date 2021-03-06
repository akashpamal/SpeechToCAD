import pyttsx3
import speech_recognition as sr

from text_parser import TextParser 
from fusion_script_generator import FusionScriptGenerator
import tkinter as tk
import tkinter.filedialog
from PIL import ImageTk, Image

WIDTH = 1640
HEIGHT = 800

WHITE = "#FFFFFF"
DARKER_WHITE = "#DDDDDD"
BLACK = "#000000"
DARK_GREY = "#1C1C1C"
DARK_GREY_2 = "#101010"

RED = "#DC143C"
GREEN = "#00B300"
BLUE = "#3792CB"

class Application:
    def __init__(self):
        self.display = tk.Tk() 
        self.display.title("Speech to CAD Generator")
        self.display.geometry(str(WIDTH) + "x" + str(HEIGHT) + "+0+0")
        self.display.configure(bg=BLACK)
        
        self.parser = TextParser()
        header_height = 2
        self.recording = False
        
        
        record = tk.Frame(self.display, bg=DARK_GREY, highlightbackground=RED, highlightcolor=RED, highlightthickness=2)
        record.grid(row = 0, column = 0, sticky="n")
        tk.Label(record, text="Audio Recording", height=header_height, bg=RED, fg=WHITE, font=("Karla", 25, 'bold'), width = 33).grid(row = 1, column = 0)
        tk.Label(record, text="Welcome to our fully automatic speach to STL file generator. To begin, please click on the record button and describe a simple shape for the system to generate!", bg=DARK_GREY, fg=WHITE, font=("Karla", 17), wraplength=400, pady = 15).grid(row = 2, column = 0)
        
        tk.Label(record, text="Open a .WAV filetype", height=header_height, bg=DARK_GREY_2, fg=WHITE, font=("Karla", 18, 'bold'), width = 25, pady=10).grid(row = 3, column = 0)
        tk.Button(record, text="Open File", highlightbackground = DARK_GREY, bg=DARK_GREY_2,command = self.open_file, font=("Karla", 18), pady=10).grid(row = 4, column = 0, pady = 5)
        
        tk.Label(record, text="Read Audio from Microphone", height=header_height, bg=DARK_GREY_2, fg=WHITE, font=("Karla", 18, 'bold'), width = 25, pady=10).grid(row = 5, column = 0)
        options = sr.Microphone.list_microphone_names()
        self.variable = tk.StringVar(self.display)
        self.variable.set(options[1]) # default value
        tk.OptionMenu(record, self.variable, *options).grid(row = 6, column = 0, pady = 10)
        self.mic = self.create_audio_dropdown(record)
        tk.Button(record, text="Record", highlightbackground = DARK_GREY, fg=DARK_GREY_2, command = self.refresh_info, font=("Karla", 18), pady=5).grid(row = 7, column = 0, pady = 5)
        tk.Button(record, text="Exit", highlightbackground = DARK_GREY, fg=RED, command = self.exit, font=("Karla", 18), pady=5).grid(row = 8, column = 0, pady = 10)
        tk.Label(record, text="", bg=DARK_GREY, fg=WHITE, font=("Karla", 17), wraplength=400, height = 60).grid(row = 9, column = 0)
        
        
        stt = tk.Frame(self.display, bg=DARK_GREY_2, highlightbackground=GREEN, highlightcolor=GREEN, highlightthickness=2)
        stt.grid(row = 0, column = 1, sticky="n")
        tk.Label(stt, text="Text Parsing", height=header_height, bg=GREEN, fg=WHITE, font=("Karla", 25, 'bold'), width = 33).grid(row = 1, column = 1)
        tk.Label(stt, text="Below is the raw text heard by the Speach-to-text software. An intelligent parsing algorithm will then search this text for useful terms.", bg=DARK_GREY_2, fg=WHITE, font=("Karla", 17), wraplength=400, pady = 15).grid(row = 2, column = 1)
        self.current_text = tk.Text(stt, width = 32, height = 15, bg=DARK_GREY_2, highlightbackground = DARK_GREY, fg=DARKER_WHITE, highlightcolor = "#7BAEDC", wrap = tk.WORD, font=("Karla", 16), pady=5)
        self.current_text.grid(row = 3, column = 1, padx = 1)
        tk.Button(stt, text="Update Parsing", highlightbackground = DARK_GREY, bg=DARK_GREY_2, command = self.refresh, font=("Karla", 18)).grid(row = 4, column = 1, pady = 10)
        self.final_info = tk.Text(stt, width = 32, height = 10, bg=DARK_GREY_2, highlightbackground = DARK_GREY, fg=DARKER_WHITE, highlightcolor = "#7BAEDC", wrap = tk.WORD, font=("Karla", 16), pady=10)
        self.final_info.grid(row = 5, column = 1, padx = 1)
        tk.Label(stt, text="", bg=DARK_GREY, fg=WHITE, font=("Karla", 17), wraplength=400, height = 70).grid(row = 9, column = 1)
        
        view = tk.Frame(self.display, bg=DARK_GREY, highlightbackground=BLUE, highlightcolor=BLUE, highlightthickness=2)
        view.grid(row = 0, column = 2, sticky="n")
        tk.Label(view, text="STL Synthesization", height=header_height, bg=BLUE, fg=WHITE, font=("Karla", 25, 'bold'), width = 33).grid(row = 1, column = 2)
        tk.Label(view, text="Once the terms are found and organized, an STL file is generated by calling Fusion360 API methods.", bg=DARK_GREY, fg=WHITE, font=("Karla", 17), wraplength=400, pady = 15).grid(row = 2, column = 2)
        
        img = ImageTk.PhotoImage(Image.open("./res/Fusion.jpeg"))
        tk.Label(view, image=img).grid(row = 3, column = 2)
        tk.Label(view, text="Now head over to Fusion 360 to see your script in action!", bg=DARK_GREY, fg=WHITE, font=("Karla", 17), wraplength=400, pady=10).grid(row = 4, column = 2)
        tk.Label(view, text="", bg=DARK_GREY, fg=WHITE, font=("Karla", 17), height = 75).grid(row = 100, column = 2)
        # The below code is a workaround that allows us to determine the window size in
        # pixels and then position the window wherever we want before drawing it.
        self.display.withdraw()
        self.display.update_idletasks()
        
        self.display.deiconify()
        self.display.mainloop()
        
    def create_audio_dropdown(self, master):
        options = sr.Microphone.list_microphone_names()
        variable = tk.StringVar(master)
        variable.set(options[0]) # default value

        w = tk.OptionMenu(master, variable, *options)
        return variable

    def exit(self):
        self.root.destroy()
        quit()
        
    def open_file(self):
        filename = tk.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("WAV files","*.wav")])
        print (filename)
        self.refresh_info(filename)
        
    def refresh_info(self, file = None):
        new_text = self.record(file)
        self.set_text(new_text)
        created_object_list = self.parser.text_to_objects(new_text)
        self.final_info.delete(1.0,"end")
        self.final_info.insert(1.0, '\n'.join(str(elem) for elem in created_object_list))
        
        f = FusionScriptGenerator('./Fusion Scripts/FusionScript1/FusionScript1.py')
        for elem in created_object_list:
            f.add_object(elem)
        f.close_generator()
    
    def refresh(self):
        text = self.current_text.get("1.0",'end-1c')
        created_object_list = self.parser.text_to_objects(text)
        self.final_info.delete(1.0,"end")
        self.final_info.insert(1.0, '\n'.join(str(elem) for elem in created_object_list))
        fusion_script_generator = FusionScriptGenerator('./Fusion Scripts/FusionScript1/FusionScript1.py')
    
        for elem in created_object_list:
            fusion_script_generator.add_object(elem)
        
        fusion_script_generator.close_generator()
        
    def record(self, file = None):
        print("Recording Audio from " + self.variable.get())
        self.recording = True
        r=sr.Recognizer()
        index = sr.Microphone.list_microphone_names().index(self.variable.get())
        inputing = sr.Microphone(device_index=index)
        if file != None:
            inputing = sr.AudioFile(file)
        with inputing as source:
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