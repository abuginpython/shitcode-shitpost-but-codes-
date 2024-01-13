import tkinter as tk
import ttkbootstrap as ttk
import random as rnd

#replace if nessececry lol 
placeholder = "Gay"

class Application(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.mainWidgets()
    
    def mainWidgets(self):
        def windowass():
            self.thingS = ttk.dialogs.dialogs.Messagebox.ok(message = f"You are {rnd.randint(0,100)}% {placeholder}!", title=' Oh my god ', alert=False)
        self.titleLabel = ttk.Label(text = f'How {placeholder} are you?', font = "Arial 24")
        self.startButton = ttk.Button(text = "Start", command = windowass)
        # self.quitButton = ttk.Button(text = "Quit", command=self.quit)
        self.titleLabel.grid()
        self.startButton.grid()

app = Application()
app.master.title(f'{placeholder} rating!')
app.mainloop()