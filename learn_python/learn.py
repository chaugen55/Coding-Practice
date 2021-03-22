import tkinter as tk
from get_user_input import *
from Student import * 
from LearningModule import *

class Application(tk.Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def say_name_of_module(self):
        print(self.name['text'])

    def createWidgets(self):
        self.QUIT = tk.Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack({"side": "left"})


        for topic in self.topic_buttons_to_create:
            name = str(topic['class_name'])
            side = "top"
            self.name = tk.Button(self)
            self.name['text'] = "{}".format(name)
            self.name['command'] = self.say_name_of_module
            self.name['fg'] = topic['button_color']
            self.name.pack({'side' : side})

    def __init__(self, master=None, topic_buttons_to_create: list = [], modules_student_has_learned: list = []):
        tk.Frame.__init__(self, master)
        self.topic_buttons_to_create = topic_buttons_to_create
        self.modules_student_has_learned = modules_student_has_learned
        self.pack()
        self.createWidgets()


user = get_user_name()
proficiency = get_user_proficiency(user)
student = Student(user, proficiency)

student.has_learned_topic('Numbers')
student.has_learned_topic('Puppies')
student.has_learned_multiple_topics(topics =['Strings', 'Lists', 'Functions'])
student.print_total_progress()
print(student.progress)
student.print_topics_learned_so_far()
print(student.is_beginner)


root = tk.Tk(className="Let's learn Python!")
app = Application(master=root, topic_buttons_to_create=curriculum, modules_student_has_learned= student.learned_topics)
app.mainloop()
