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
        ...
    
main = Main()