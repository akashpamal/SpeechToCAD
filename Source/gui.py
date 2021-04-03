import tkinter as tk

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.call('wm', 'attributes', '.', '-topmost', True)
        self.root.title("Speech to CAD")
        
        backColor = "#000000"
        frontColor = "#1C1C1C"
        self.root.configure(bg=backColor)
        
        self.recording = False
        record = tk.Frame(self.root, borderwidth = 1)
        record.grid(row = 3, column = 1, pady = 20)
        title = tk.Label(record, text="Record Some Audio").grid(row = 1, padx = 10)
        self.exit = tk.Button(record, text="Exit", highlightbackground = backColor, command = self.Exit).grid(row = 2, pady = (5, 5))
        self.record = tk.Button(record, text="Record", highlightbackground = backColor, command = self.Record).grid(row = 3, pady = (5, 5))
        #Indicator GIFs
        record.configure(bg=frontColor)
        
        
        stt = tk.Frame(self.root, borderwidth = 1)
        stt.grid(row = 3, column = 2, pady = 20)
        title = tk.Label(stt, text="Audio Translation").grid(row = 1, padx = 10)
        stt.configure(bg=frontColor)
        self.current_text = tk.Text(stt, width = 30, height = 30, highlightbackground = frontColor, highlightcolor = "#7BAEDC", wrap = tk.WORD, font=("Helvetica Neue", 12)).grid(row = 2, padx = 10)
        self.sysnthezied_info = tk.Label(stt, text="Example translation").grid(row = 3, padx = 10)
    
        
        view = tk.Frame(self.root, borderwidth = 1)
        view.grid(row = 3, column = 3, pady = 20)
        title = tk.Label(view, text="View CAD Model").grid(row = 1, padx = 10)
        # View Module
        view.configure(bg=frontColor)
        
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
       
if __name__=="__main__":
    Application()