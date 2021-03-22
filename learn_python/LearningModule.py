class LearningModule:
    def __init__(self, moduleName: str, topicsCovered: list):
        self.moduleName = moduleName
        self.topicsCovered = topicsCovered
        self.numOfModules = len(topicsCovered)
        self.presentModuleInfo()

    def presentModuleInfo(self):
        print()
        print(f'Congrats on starting {self.moduleName}! In this module, there are going over {self.numOfModules} topics covering the following:')
        for topic in self.topicsCovered: # Returns a numbered list containing each topic in self.topicsCovered
            print(f'{self.topicsCovered.index(topic) + 1}. {topic}')
        print()

    def displayModuleWindow(self):
        # Need to find out how to do this with ipywidgets or other gui 
        pass





