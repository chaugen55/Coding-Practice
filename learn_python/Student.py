import logging as log
from LearningModule import *

curriculum = [
    {'class_name': 'Numbers'},
    {'class_name': 'Variables'},
    {'class_name': 'Strings'},
    {'class_name': 'Lists'},
    {'class_name': 'Booleans'},
    {'class_name': 'Dictionaries'},
    {'class_name': 'Conditionals'},
    {'class_name': 'Operators: And, Or, Not'},
    {'class_name': 'Operators: Comparison'},
    {'class_name': 'For Loops'},
    {'class_name': 'While Loops'},
    {'class_name': 'Functions'},
    {'class_name': 'Arguments'},
    {'class_name': 'Scope'},
    {'class_name': 'Libraries'}
]

numbers_module = LearningModule(moduleName="Numbers", topicsCovered=["Integers", "Floats", "Simple math", "+=, -=. *=, /="])
variables_module = LearningModule(moduleName="Variables", topicsCovered=["Variables: The basics", "The DRY Method", "Variables: Conventions"])
strings_module = LearningModule(moduleName="Strings", topicsCovered=["String indexing", "String slicing", "Strings: Properties", "Strings Methods", "Print formatting"])
lists_module = LearningModule(moduleName="Lists", topicsCovered=["Lists: The basics", "Covered", "List indexing"])
booleans_module = LearningModule(moduleName="Booleans", topicsCovered=["Booleans: The basics"])
dictionaries_module = LearningModule(moduleName="Dictionaries", topicsCovered=["Dictionaries: The basics", "Dictionary referencing"])
conditionals_module = LearningModule(moduleName="Conditionals", topicsCovered=["If, Else, and Elif", "Nesting conditionals (and why you shouldn't)"])
operators_and_or_not_module = LearningModule(moduleName="Operators: And, Or, Not", topicsCovered=["And, Or, and Not", "Chaining operators"])
operators_comparison_module = LearningModule(moduleName="Operators: Comparison", topicsCovered=["Comparison operartors"])
for_loops_module = LearningModule(moduleName="For Loops", topicsCovered=["For Loops: The basics"])
while_loops_module = LearningModule(moduleName="While Loops", topicsCovered=["While Loops: The basics"])
functions_module = LearningModule(moduleName="Functions", topicsCovered=["Why functions are so useful", "Functions: Conventions", "Returning values", "Paramaters: Setting rules for your function", "Type hinting your parameters"])
arguments_module = LearningModule(moduleName="Arguments", topicsCovered=["Arguments? Don't you mean paramaters? (NO!)", "Arguments: Conventions"])
scope_module = LearningModule(moduleName="Scope", topicsCovered=["Local vs. Global Scope", "Global Variables: Conventions"])
libraries_module = LearningModule(moduleName="Libraries", topicsCovered=["Using your programming to change the world"])


class Student:
    progress = 0
    topics_to_learn = {
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

    def update_button_colors_for_learned_topics(self):
        for c in curriculum:
            if self.topics_to_learn[c['class_name']]['has_been_learned'] == True:
                c['button_color'] = 'green'
            else:
                c['button_color'] = 'red'


    def has_learned_topic(self, topic: str):
        if topic not in self.topics_to_learn.keys():
            log.warning(
                f'Looks like "{topic}" isn\'t in this curriculum . . . Email chaugen@apple.com to see if Christian can add it!')
            return
        else:
            print(f'Nice job learning "{topic}"!')
            self.topics_to_learn[topic]['has_been_learned'] = True
            self.update_button_colors_for_learned_topics()

    def has_learned_multiple_topics(self, topics: list):
        for topic in topics:
            self.has_learned_topic(topic)

    def learned_topics(self):
        results = []
        for topic in self.topics_to_learn.items():
            if topic['has_been_learned'] == True:
                results.append(topic.key())
        return results

    def print_topics_learned_so_far(self):
        topics = []
        for topic, value_dict in self.topics_to_learn.items():
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
        topics_to_learn_count = 0
        for topic, value_dict in self.topics_to_learn.items():
            if value_dict['has_been_learned'] == True:
                topics_to_learn_count += 1
        self.progress = (topics_to_learn_count / len(self.topics_to_learn)) * 100
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
# christian.print_topics_to_learn_so_far()
# print(christian.is_beginner)