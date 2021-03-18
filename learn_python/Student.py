import logging as log

curriculum = ['Numbers', 'Strings', 'Lists', 'Booleans',
              'Dictionaries', 'Conditionals', 'Operators: And, Or, Not',
              'Operators: Comparison', 'For Loops', 'While Loops', 'Variables',
              'Functions', 'Arguments', 'Scope', 'Libraries']


class Student:
    progress = 0
    concepts_learned = {
        'Numbers':                  {'has_been_learned': False},
        'Strings':                  {'has_been_learned': False},
        'Lists':                    {'has_been_learned': False},
        'Booleans':                 {'has_been_learned': False},
        'Dictionaries':             {'has_been_learned': False},
        'Conditionals':             {'has_been_learned': False},
        'Operators: And, Or, Not':  {'has_been_learned': False},
        'Operators: Comparison':    {'has_been_learned': False},
        'For Loops':                {'has_been_learned': False},
        'While Loops':              {'has_been_learned': False},
        'Variables':                {'has_been_learned': False},
        'Functions':                {'has_been_learned': False},
        'Arguments':                {'has_been_learned': False},
        'Scope':                    {'has_been_learned': False},
        'Libraries':                {'has_been_learned': False}
    }

    def __init__(self, name: str, is_beginner: bool = True):
        self.name = name
        self.is_beginner = is_beginner

    def has_learned_concept(self, concept: str):
        if concept not in curriculum:
            log.warning(
                f'Looks like "{concept}" isn\'t in this curriculum . . . Email chaugen@apple.com to see if Christian can add it!')
            return
        else:
            print(f'Nice job learning "{concept}"!')
            self.concepts_learned[concept]['has_been_learned'] = True

    def has_learned_multiple_concepts(self, concepts: list):
        for concept in concepts:
            self.has_learned_concept(concept)

    def print_concepts_learned_so_far(self):
        concepts = []
        for concept, value_dict in self.concepts_learned.items():
            if value_dict['has_been_learned'] == True:
                concepts.append(concept)

        statement = f'So far {self.name} has learned: '
        for concept in concepts:
            if concept == concepts[-1]:
                statement += ('and ' + concept + '!')
            else:
                statement += (concept + ', ')
        print(statement + ' Awesome work!')

    def print_total_progress(self):
        concepts_learned_count = 0
        for concept, value_dict in self.concepts_learned.items():
            if value_dict['has_been_learned'] == True:
                concepts_learned_count += 1
        self.progress = (concepts_learned_count / len(self.concepts_learned)) * 100
        print(f'Total progress: {self.progress}%')

    def save_learning_progress(self):
        pass
        #TODO need to figure out how to save data in a program so students don't lose their progress


# christian = Student('Christian', is_beginner=False)

# christian.has_learned_concept('Numbers')
# christian.has_learned_concept('Puppies')
# christian.has_learned_multiple_concepts(['Strings', 'Lists', 'Functions'])
# christian.print_total_progress()
# print(christian.progress)
# christian.print_concepts_learned_so_far()
# print(christian.is_beginner)
