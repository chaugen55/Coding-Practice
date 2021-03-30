import learn_arguments, learn_booleans, learn_conditionals, learn_dictionaries
import learn_functions, learn_libraries, learn_lists, learn_loops_for
import learn_loops_while, learn_numbers, learn_operators_and_or_not
import learn_operators_comparison, learn_scope, learn_strings, learn_variables

import tkinter as tk

from get_user_input import *
from Student import * 
from LearningModule import *

class Application(tk.Frame):
    def say_hi(self):
        print("Hi!")

    def createWidgets(self):
        self.PYTHON_IMAGE = tk.PhotoImage(name='python.png')

        self.QUIT = tk.Button(self, text='QUIT', fg='red', command=self.quit).grid(row=7 , column=4)    

        # 1st section
        self.easy_stuff =               tk.Label(self, text='Easy concepts').grid(row=1, column=1)

        self.numbers =                  tk.Button(self, text='Numbers', command=self.say_hi).grid(row=2, column=1)
        self.variables =                tk.Button(self, text='Variables', command=self.say_hi).grid(row=2, column=2)
        self.strings =                  tk.Button(self, text='Strings', command=self.say_hi).grid(row=2, column=3)
        self.lists =                    tk.Button(self, text='Lists', command=self.say_hi).grid(row=2, column=4)
        self.booleans =                 tk.Button(self, text='Booleans', command=self.say_hi).grid(row=2, column=5)
        self.dictionaries =             tk.Button(self, text='Dictionaries', command=self.say_hi).grid(row=2, column=6)



        # 2nd section
        self.not_difficult_label =      tk.Label(self, text="This content isn't difficult either").grid(row=3, column=1)

        self.conditionals =             tk.Button(self, text='Conditionals', command=self.say_hi).grid(row=4, column=2)
        self.operators_and_or_not =     tk.Button(self, text='Operators: And, Or, Not', command=self.say_hi).grid(row=4, column=3)
        self.operators_comparison =     tk.Button(self, text='Operators: Comparison', command=self.say_hi).grid(row=4, column=4)



        # 3rd section
        self.youre_almost_done_label =  tk.Label(self, text="You're almost done, then your programming career begins").grid(row=5, column=1)

        self.for_loops =                tk.Button(self, text='For Loops', command=self.say_hi).grid(row=6, column=1)
        self.while_loops =              tk.Button(self, text='While Loops', command=self.say_hi).grid(row=6, column=2)
        self.functions =                tk.Button(self, text='Functions', command=self.say_hi).grid(row=6, column=3)
        self.arguments =                tk.Button(self, text='Arguments', command=self.say_hi).grid(row=6, column=4)
        self.scope =                    tk.Button(self, text='Scope', command=self.say_hi).grid(row=6, column=5)
        self.libraries =                tk.Button(self, text='Libraries', command=self.say_hi).grid(row=6, column=6)

    def __init__(self, master=None, topic_buttons_to_create: list = [], modules_student_has_learned: list = []):
        tk.Frame.__init__(self, master)
        self.topic_buttons_to_create = topic_buttons_to_create
        self.modules_student_has_learned = modules_student_has_learned
        self.grid()
        self.createWidgets()


user = get_user_name()
proficiency = get_user_proficiency(user)
student = Student(user, proficiency)

student.has_learned_topic('Numbers')
student.has_learned_topic('Puppies')
student.has_learned_multiple_topics(topics =['Strings', 'Lists', 'Functions', 'Kitties'])
student.print_total_progress()
print(student.progress)
student.print_topics_learned_so_far()
print(student.is_beginner)


root = tk.Tk(className="Let's learn Python!")
app = Application(master=root, topic_buttons_to_create=curriculum, modules_student_has_learned= student.learned_topics)
app.mainloop()
