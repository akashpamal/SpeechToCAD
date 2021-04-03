import tkinter as Tkinter

class Application:
    def __init__(self):
        self.root = Tkinter.Tk()
        self.root.call('wm', 'attributes', '.', '-topmost', True)
        self.root.title("Speech to CAD")
        
        bgColor = "#000000"
        self.root.configure(bg=bgColor)
        
        self.root.wm_grid(row = 1, column = 3, padx = 10)
        maintop = Tkinter.Frame(self.root, borderwidth = 1, relief = 'sunken')
        maintop.pack()
        
        frontColor = "#1C1C1C"
        
        record = Tkinter.Frame(self.root, borderwidth = 1, relief = 'sunken')
        record.grid(row = 3, column = 1, pady = 20)
        title = tk.Label(record, text="Record Some Audio").grid(row = 1, padx = 10)
        self.exit = tk.Button(record, text="Exit", highlightbackground = bgColor, command = self.Exit).grid(row = 2, pady = (5, 5))
        self.record = tk.Button(record, text="Record", highlightbackground = bgColor, command = self.Record).grid(row = 3, pady = (5, 5))
        record.configure(bg=frontColor)
        record.pack()
        
        stt = Tkinter.Frame(self.root, borderwidth = 1, relief = 'sunken')
        stt.grid(row = 3, column = 1, pady = 20)
        title = tk.Label(record, text="Audio Translation").grid(row = 1, padx = 10)
        record.configure(bg=frontColor)
        self.current_text = Tkinter.Text(record, width = 60, height = 60, highlightbackground = frontColor, highlightcolor = "#7BAEDC", wrap = Tkinter.WORD, font=("Helvetica Neue", 12)).grid(row = 2, padx = 10)
        self.sysnthezied_info = tk.Label(record, text="Example translation").grid(row = 3, padx = 10)
        stt.pack()
        
        view = Tkinter.Frame(self.root, borderwidth = 1, relief = 'sunken')
        view.grid(row = 3, column = 1, pady = 20)
        title = tk.Label(view, text="View CAD Model").grid(row = 1, padx = 10)
        record.configure(bg=frontColor)
        view.pack()
        
        
        # The below code is a workaround that allows us to determine the window size in
        # pixels and then position the window wherever we want before drawing it.
        self.root.withdraw()
        self.root.update_idletasks()
        
        # These lines will position this window in the middle of the screen horizontally
        # and two thirds of the way up vertically (a position I prefer as it is a little
        # more catching to the eye and exact centering)
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 3
        self.root.geometry("+{0}+{1}".format(x, y))
        
        self.root.deiconify()
        self.root.mainloop()
        
    def Exit(self):
        self.root.destroy()
        quit()
        
    def Record(self):
        print("The user clicked the 'Record' button.")
       
class SubModule:
    def __init__(self):
        self.frame = Tkinter.Frame(self.root, borderwidth = 1, relief = 'sunken')
        



# Calling the class will execute our GUI.
Application()