class LearningModule:
    def __init__(self, moduleName: str, topicsCovered: list):
        self.moduleName = moduleName
        self.topicsCovered = topicsCovered
        self.numOfModules = len(topicsCovered)
        self.present_module_info()

    def present_module_info(self):
        print()
        print(f'Congrats on starting {self.moduleName}! In this module, there are going over {self.numOfModules} topics covering the following:')
        for topic in self.topicsCovered: # Returns a numbered list containing each topic in self.topicsCovered
            print(f'{self.topicsCovered.index(topic) + 1}. {topic}')
        print()

    def start_module(self):
        # TODO need to figure out how to change windows to start each module on its own
        pass

    def display_module_window(self):
        # Need to find out how to do this with ipywidgets or other gui 
        pass





