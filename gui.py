import tkinter as tk

WHITE = "#FFFFFF"
BLACK = "#000000"
DARK_GREY = "#1C1C1C"

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.call('wm', 'attributes', '.', '-topmost', True)
        self.root.title("Speech to CAD")
        self.root.geometry("1280x718")
        
        self.root.configure(bg=BLACK)
        
        header_height = 2
        
        self.recording = False
        record = tk.Frame(self.root, bg=DARK_GREY, padx=1, height=30)
        record.grid(row = 3, column = 1, pady = 1)
        title = tk.Label(record, text="Audio Recording", height=header_height, bg="#DC143C", fg=WHITE, width=30, font=("Karla", 18)).grid(row = 1)
        self.record = tk.Button(record, text="Record", highlightbackground = DARK_GREY, command = self.Record, font=("Karla", 18)).grid(row = 3, pady = (5, 5))
        self.exit = tk.Button(record, text="Exit", highlightbackground = DARK_GREY, command = self.Exit, font=("Karla", 18)).grid(row = 2, pady = (5, 5))
        #Indicator GIFs
        #record.place(x = 1, y = 1, width=30, height=30)
        
        stt = tk.Frame(self.root, bg=DARK_GREY, padx=1)
        stt.grid(row = 4, column = 2, pady = 1)
        title = tk.Label(stt, text="Text Parsing", height=header_height, bg="#00B300", width=35, fg=WHITE, font=("Karla", 18)).grid(row = 1)
        self.current_text = CustomText(stt, width = 30, height = 15, bg=BLACK, highlightbackground = DARK_GREY, fg=WHITE, highlightcolor = "#7BAEDC", wrap = tk.WORD, font=("Karla", 18), pady=5)
        self.current_text.grid(row = 2, padx = 15)
        self.current_text.tag_configure("red", foreground="#ff0000")
        self.current_text.highlight_pattern("this should be red", "red")
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
        
    def Exit(self):
        self.root.destroy()
        quit()
        
    def Record(self):
        print("The user clicked the 'Record' button.")
       
    def update(self, b = None):
        print(self.current_text.get("1.0",'end-1c'))
       
       
class CustomText(tk.Text):
    '''A text widget with a new method, highlight_pattern()

    example:

    text = CustomText()
    text.tag_configure("red", foreground="#ff0000")
    text.highlight_pattern("this should be red", "red")

    The highlight_pattern method is a simplified python
    version of the tcl code at http://wiki.tcl.tk/3246
    '''
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

    def highlight_pattern(self, pattern, tag, start="1.0", end="end",
                          regexp=False):
        '''Apply the given tag to all text that matches the given pattern

        If 'regexp' is set to True, pattern will be treated as a regular
        expression according to Tcl's regular expression syntax.
        '''

        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        count = tk.IntVar()
        while True:
            index = self.search(pattern, "matchEnd","searchLimit",
                                count=count, regexp=regexp)
            if index == "": break
            if count.get() == 0: break # degenerate pattern which matches zero-length strings
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")
            
class Processor:
    def __init__(self, text):
        self.text = text
        
    # def update(self, b = None):
    #     print(


if __name__=="__main__":
    Application()