import os

class Finder:
    filesName = []
    personalExtensions = []
    currentExtension = ''
    currentPath = None

    def __init__(self, filesList=None, extensionsList=None, putExtension=None, path=None):

        if filesList is not None:
            self.filesName = filesList

        if extensionsList is not None:
            self.personalExtensions = extensionsList

        if putExtension is not None:
            self.currentExtension = putExtension

        if path is not None:
            self.path = path

    def findExtensions_onPath(self):

        try:
            if len(self.filesName) < 1:
                raise ValueError('The files passed is empty')

            if len(self.personalExtensions) < 1:
                raise ValueError('The extensions passed is empty')

            if len(self.currentExtension) < 1:
                raise ValueError('The extension passed is empty')

            if len(self.currentPath) < 1:
                raise ValueError('The path passed is empty')

        except ValueError as err:
            print(err)

        for file in os.listdir(self.currentPath):
            for selectedExtension in self.personalExtensions:
                if file.endswith(selectedExtension):
                    print(f'{file}')

    def findExtensions_withWordlist(self):
        '''
        Finder start a verification and run the search

        self.filesName: Passed by the user. This is about the files names what you want find on your current path
        self.personalCurrentExtensions: Passed by the user. This is about what file extensions do you want find on your current path
        self.currentExtension: Passed by the user. This is about what file extension do you want find on your current path
        self.currentPath: Your current directory

        This variables is passed on the constructor function
        
        '''

        try:
            if len(self.filesName) < 1:
                raise ValueError('The files passed is empty')

            if len(self.personalExtensions) < 1:
                raise ValueError('The extensions passed is empty')

            if len(self.currentExtension) < 1:
                raise ValueError('The extension passed is empty')

            if len(self.currentPath) < 1:
                raise ValueError('The path passed is empty')

        except ValueError as err:
            print(err)

        for file in os.listdir(self.currentPath):
            for selectedExtension in self.personalExtensions:
                for fileName in self.filesName:
                    fileName_withExtension = str(fileName) + str(selectedExtension)
                    if fileName_withExtension == file:
                        print(f'File with extension {selectedExtension} found: {fileName_withExtension}')

if __name__ == '__main__':
    directory = os.getcwd()
    fd = Finder(extensionsList=['.pdf', '.docx'], path=directory, filesList=['pedro', 'joao'])
    fd.findExtensions_withWordlist()
    fd.findExtensions_onPath()