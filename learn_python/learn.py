import tkinter as tk
from get_user_input import *
from Student import * 
from LearningModule import *

class Application(tk.Frame):
    def say_hi(self):
        print("Hi!")

    def createWidgets(self):
        self.PYTHON_IMAGE = tk.PhotoImage(name='python.png')

        self.QUIT = tk.Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.grid(row=7 , column=4)    

        # Easy stuff label
        self.easy_stuff = tk.Label(self)
        self.easy_stuff['text'] = 'Easy concepts'
        self.easy_stuff.grid(row=1, column=1)

        # Numbers
        self.numbers = tk.Button(self)
        self.numbers['text'] = 'Numbers'
        self.numbers['command'] = self.say_hi
        self.numbers.grid(row=2, column=1)

        # Variables
        self.variables = tk.Button(self)
        self.variables['text'] = 'Variables'
        self.variables['command'] = self.say_hi
        self.variables.grid(row=2, column=2)

        # Strings
        self.strings = tk.Button(self)
        self.strings['text'] = 'Strings'
        self.strings['command'] = self.say_hi
        self.strings.grid(row=2, column=3)

        # Lists
        self.lists = tk.Button(self)
        self.lists['text'] = 'Lists'
        self.lists['command'] = self.say_hi
        self.lists.grid(row=2, column=4)

        # Booleans
        self.booleans = tk.Button(self)
        self.booleans['text'] = 'Booleans'
        self.booleans['command'] = self.say_hi
        self.booleans.grid(row=2, column=5)

        # Dictionaries
        self.dictionaries = tk.Button(self)
        self.dictionaries['text'] = 'Dictionaries'
        self.dictionaries['command'] = self.say_hi
        self.dictionaries.grid(row=2, column=6)

        # This content isn't difficult either label
        self.not_difficult_label = tk.Label(self)
        self.not_difficult_label['text'] = 'This content isn\'t difficult either'
        self.not_difficult_label.grid(row=3, column=1)

        # Conditionals
        self.conditionals = tk.Button(self)
        self.conditionals['text'] = 'Conditionals'
        self.conditionals['command'] = self.say_hi
        self.conditionals.grid(row=4, column=2)

        # Operators: And, Or, Not
        self.operators_and_or_not = tk.Button(self)
        self.operators_and_or_not['text'] = 'Operators: And, Or, Not'
        self.operators_and_or_not['command'] = self.say_hi
        self.operators_and_or_not.grid(row=4, column=3)

        # Operators: Comparison
        self.operators_comparison = tk.Button(self)
        self.operators_comparison['text'] = 'Operators: Comparison'
        self.operators_comparison['command'] = self.say_hi
        self.operators_comparison.grid(row=4, column=4)

        # You're almost done, then your programming career begins
        self.youre_almost_done_label = tk.Label(self)
        self.youre_almost_done_label['text'] = 'You\'re almost done, then your programming career begins'
        self.youre_almost_done_label.grid(row=5, column=1)

        # For Loops
        self.for_loops = tk.Button(self)
        self.for_loops['text'] = 'For Loops'
        self.for_loops['command'] = self.say_hi
        self.for_loops.grid(row=6, column=1)

        # While Loops
        self.while_loops = tk.Button(self)
        self.while_loops['text'] = 'While Loops'
        self.while_loops['command'] = self.say_hi
        self.while_loops.grid(row=6, column=2)

        # Functions
        self.functions = tk.Button(self)
        self.functions['text'] = 'Functions'
        self.functions['command'] = self.say_hi
        self.functions.grid(row=6, column=3)

        # Arguments
        self.arguments = tk.Button(self)
        self.arguments['text'] = 'Arguments'
        self.arguments['command'] = self.say_hi
        self.arguments.grid(row=6, column=4)

        # Scope
        self.scope = tk.Button(self)
        self.scope['text'] = 'Scope'
        self.scope['command'] = self.say_hi
        self.scope.grid(row=6, column=5)

        # Libraries
        self.libraries = tk.Button(self)
        self.libraries['text'] = 'Libraries'
        self.libraries['command'] = self.say_hi
        self.libraries.grid(row=6, column=6)

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
