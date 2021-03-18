import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.say_hi = tk.Button(self)
        self.say_hi['text'] = 'Hello, world! \n(click me)'
        self.say_hi['command'] = self.welcome
        self.say_hi = tk.Button(self)

    def welcome(self):
        print('Hey there, everyone!')





root = tk.Tk(screenName="Let's learn Python!", baseName="main_window")


root.mainloop()
