import logging as log
from LearningModule import *

curriculum =  ['Numbers', 'Variables', 'Strings', 'Lists', 'Booleans',
              'Dictionaries', 'Conditionals', 'Operators: And, Or, Not',
              'Operators: Comparison', 'For Loops', 'While Loops', 
              'Functions', 'Arguments', 'Scope', 'Libraries']

numbers_module =                LearningModule(moduleName = "Numbers", topicsCovered = ["Integers", "Floats", "Simple math", "+=, -=. *=, /="])
variables_module =              LearningModule(moduleName = "Variables", topicsCovered = ["Variables: The basics", "The DRY Method", "Variables: Conventions"])
strings_module =                LearningModule(moduleName = "Strings", topicsCovered = ["String indexing", "String slicing", "Strings: Properties", "Strings Methods", "Print formatting"])
lists_module =                  LearningModule(moduleName = "Lists", topicsCovered = ["Lists: The basics", "Covered", "List indexing"])
booleans_module =               LearningModule(moduleName = "Booleans", topicsCovered = ["Booleans: The basics"])
dictionaries_module =           LearningModule(moduleName = "Dictionaries", topicsCovered = ["Dictionaries: The basics", "Dictionary referencing"])
conditionals_module =           LearningModule(moduleName = "Conditionals", topicsCovered = ["If, Else, and Elif", "Nesting conditionals (and why you shouldn't)"])
operators_and_or_not_module =   LearningModule(moduleName = "Operators: And, Or, Not", topicsCovered = ["And, Or, and Not", "Chaining operators"])
operators_comparison_module =   LearningModule(moduleName = "Operators: Comparison", topicsCovered = ["Comparison operartors"])
for_loops_module =              LearningModule(moduleName = "For Loops", topicsCovered = ["For Loops: The basics"])
while_loops_module =            LearningModule(moduleName = "While Loops", topicsCovered = ["While Loops: The basics"])
functions_module =              LearningModule(moduleName = "Functions", topicsCovered = ["Why functions are so useful", "Functions: Conventions", "Returning values", "Paramaters: Setting rules for your function", "Type hinting your parameters"])
arguments_module =              LearningModule(moduleName = "Arguments", topicsCovered = ["Arguments? Don't you mean paramaters? (NO!)", "Arguments: Conventions"])
scope_module =                  LearningModule(moduleName = "Scope", topicsCovered = ["Local vs. Global Scope", "Global Variables: Conventions"])
libraries_module =              LearningModule(moduleName = "Libraries", topicsCovered = ["Using your programming to change the world"])
class Student:
    progress = 0
    topics_learned = {
        'Numbers':                  {'has_been_learned': False},
        'Variables':                {'has_been_learned': False},
        'Strings':                  {'has_been_learned': False},
        'Lists':                    {'has_been_learned': False},
        'Booleans':                 {'has_been_learned': False},
        'Dictionaries':             {'has_been_learned': False},
        'Conditionals':             {'has_been_learned': False},
        'Operators: And, Or, Not':  {'has_been_learned': False},
        'Operators: Comparison':    {'has_been_learned': False},
        'For Loops':                {'has_been_learned': False},
        'While Loops':              {'has_been_learned': False},
        'Functions':                {'has_been_learned': False},
        'Arguments':                {'has_been_learned': False},
        'Scope':                    {'has_been_learned': False},
        'Libraries':                {'has_been_learned': False}
    }

    def __init__(self, name: str, is_beginner: bool = True):
        self.name = name
        self.is_beginner = is_beginner

    def has_learned_topic(self, topic: str):
        if topic not in curriculum:
            log.warning(
                f'Looks like "{topic}" isn\'t in this curriculum . . . Email chaugen@apple.com to see if Christian can add it!')
            return
        else:
            print(f'Nice job learning "{topic}"!')
            self.topics_learned[topic]['has_been_learned'] = True

    def has_learned_multiple_topics(self, topics: list):
        for topic in topics:
            self.has_learned_topic(topic)

    def print_topics_learned_so_far(self):
        topics = []
        for topic, value_dict in self.topics_learned.items():
            if value_dict['has_been_learned'] == True:
                topics.append(topic)

        statement = f'So far {self.name} has learned: '
        for topic in topics:
            if topic == topics[-1]:
                statement += ('and ' + topic + '!')
            else:
                statement += (topic + ', ')
        print(statement + ' Awesome work!')

    def print_total_progress(self):
        topics_learned_count = 0
        for topic, value_dict in self.topics_learned.items():
            if value_dict['has_been_learned'] == True:
                topics_learned_count += 1
        self.progress = (topics_learned_count / len(self.topics_learned)) * 100
        print(f'Total progress: {self.progress}%')

    def save_learning_progress(self):
        pass
        #TODO need to figure out how to save data in a program so students don't lose their progress


# christian = Student('Christian', is_beginner=False)

# christian.has_learned_topic('Numbers')
# christian.has_learned_topic('Puppies')
# christian.has_learned_multiple_topics( ['Strings', 'Lists', 'Functions'])
# christian.print_total_progress()
# print(christian.progress)
# christian.print_topics_learned_so_far()
# print(christian.is_beginner)