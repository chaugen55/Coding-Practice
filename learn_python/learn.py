import tkinter as tk
from get_user_input import *
from Student import *

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


user = get_user_name()
proficiency = get_user_proficiency(user)
student = Student(user, proficiency)

student.has_learned_concept('Numbers')
student.has_learned_concept('Puppies')
student.has_learned_multiple_concepts(['Strings', 'Lists', 'Functions'])
student.print_total_progress()
print(student.progress)
student.print_concepts_learned_so_far()
print(student.is_beginner)


root = tk.Tk(className="Let's learn Python!")


root.mainloop()