import tkinter as tk

WHITE = "#FFFFFF"
BLACK = "#000000"
DARK_GREY = "#1C1C1C"

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.call('wm', 'attributes', '.', '-topmost', True)
        self.root.title("Speech to CAD")
        self.root.geometry("1280x720")
        
        self.root.configure(bg=BLACK)
        
        header_height = 2
        
        self.recording = False
        record = tk.Frame(self.root, bg=DARK_GREY)
        record.grid(row = 3, column = 1, pady = 1)
        title = tk.Label(record, text="Record Some Audio", height=header_height, bg="#DC143C", fg=WHITE, width=45, font=("Karla", 20)).grid(row = 1, padx = 2)
        self.exit = tk.Button(record, text="Exit", highlightbackground = DARK_GREY, command = self.Exit, font=("Karla", 20)).grid(row = 2, pady = (5, 5))
        self.record = tk.Button(record, text="Record", highlightbackground = DARK_GREY, command = self.Record, font=("Karla", 20)).grid(row = 3, pady = (5, 5))
        #Indicator GIFs
        #record.place(x = 1, y = 1, width=30, height=30)
        
        stt = tk.Frame(self.root, borderwidth = 3, bg=DARK_GREY)
        stt.grid(row = 3, column = 2, pady = 1)
        title = tk.Label(stt, text="Audio Translation", height=header_height, bg="#00B300", width=45, fg=WHITE, font=("Karla", 20)).grid(row = 1, padx = 5)
        self.current_text = tk.Text(stt, width = 30, height = 30, highlightbackground = DARK_GREY, highlightcolor = "#7BAEDC", wrap = tk.WORD, font=("Karla", 20)).grid(row = 2, padx = 10)
        self.sysnthezied_info = tk.Label(stt, text="Example translation", font=("Karla", 20)).grid(row = 3, padx = 10)
        #stt.place(x = 33, y = 1, width=30, height=30)
        
        view = tk.Frame(self.root, borderwidth = 3, height=30, bg=DARK_GREY)
        view.grid(row = 3, column = 3, pady = 1)
        title = tk.Label(view, text="View CAD Model", height=header_height, bg="#3792CB", width=45, fg=WHITE, font=("Karla", 20)).grid(row = 1, padx = 10)
        #view.place(x = 450, y = 10, width=200, height=100)
        # View Module
        
        # The below code is a workaround that allows us to determine the window size in
        # pixels and then position the window wherever we want before drawing it.
        self.root.withdraw()
        self.root.update_idletasks()
        
        self.root.deiconify()
        self.root.mainloop()
        
    def Exit(self):
        self.root.destroy()
        quit()
        
    def Record(self):
        print("The user clicked the 'Record' button.")
       
       
       
       
class Processor:
    def __init__(self, text):
        self.text = text
        
    def update(new_text):
        pass


if __name__=="__main__":
    Application()