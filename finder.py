import os
from colorama import init, Fore, Back, Style
from time import sleep

init()

class Objeto:
    #-----------------------------------------------------------------------------
    # This variables are passed by a instance locate on the end of this code
    currentExtension = ''
    currentPath = os.getcwd()
    filesPath = []
    #-----------------------------------------------------------------------------
    
    def insertExtension(self, extension):
        ...

class Main:
    print("Github > @pedro.makaveli\n")
    print("A finalidade do Finder e buscar por arquivos especificos e oferecendo uma busca filtrada por nomes de arquivos\n\n")
    print("SELECIONE O TIPO DOS ARQUIVOS QUE VOCE DESEJA VERIFICAR")

    extension_choice = int(input("\n[1] .pdf [2] .docx"))

    # -----------------------------------------
    #[!] Very important: this variables was be alter after the menu verification

    obj = Objeto()

    # [!] Very important: this variables was be alter after the menu verification
    #------------------------------------------

    def menuVerify(self, numberChoice):
        if numberChoice == 1:
            self.obj.insertExtension('.pdf') # This line alter selectedExtension variable on Objeto scope  

        elif numberChoice == 2:
            self.obj.insertExtension('.docx')
            
        else:
            print("Opção inválida, tente novamente")
            
main = Main()
main.menuVerify(main.extension_choice)