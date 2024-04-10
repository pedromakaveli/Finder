import os
import argparse

class Finder:

    def __init__(self, fileNames=None, personalExtensions=None, currentPath=None):

        self.fileNames = fileNames
        self.personalExtensions = personalExtensions
        self.currentPath = currentPath

    def findExtensions_onPath(self):

        if len(self.personalExtensions) < 1:
            raise ValueError('The extensions passed is empty')

        if len(self.currentPath) < 1:
            raise ValueError('The path passed is empty')

        filesFound = []

        for file in os.listdir(self.currentPath):
            for selectedExtension in self.personalExtensions:
                if file.endswith(selectedExtension):
                    filesFound.append(os.path.abspath(file))

        return filesFound


    def findExtensions_withWordlist(self):
        if len(self.fileNames) == 0 and len(self.personalExtensions) == 0:
            raise ValueError('Please inform a list of files or extensions!')

        if len(self.personalExtensions) == 0:
            raise ValueError('The extensions passed is empty')

        if len(self.currentPath) == 0:
            raise ValueError('The path passed is empty')

        filesFound = []

        for file in os.listdir(self.currentPath):
            for selectedExtension in self.personalExtensions:
                for fileName in self.fileNames:
                    fileName_withExtension = f'{fileName}.{selectedExtension}'

                    if fileName_withExtension == file:
                        filesFound.append(os.path.abspath(fileName_withExtension))

        return filesFound

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Finder', description='Finder is a script for search of files')

    parser.add_argument('-e', '--extensions', nargs='+')
    parser.add_argument('-f', '--filenames', nargs='+')

    args = parser.parse_args()

    directory = os.getcwd()

    fd = Finder(personalExtensions=args.extensions, currentPath=directory, fileNames=args.filenames)

    if args.extensions is not None:
        filesFound = fd.findExtensions_onPath()

        for file in filesFound:
            print(file)

    if args.filenames is not None:
        filesFound = fd.findExtensions_withWordlist()

        for file in filesFound:
            print(file)
