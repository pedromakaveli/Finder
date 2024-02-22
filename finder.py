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
        os.system("cls")
        self.currentExtension = extension.lower()
        
        print(f"\n[!] EXTENSAO SELECIONADA:" + Fore.GREEN + f"{self.currentExtension}\n")
        sleep(1)
    
        print(Fore.WHITE + f"\n[!] PASTA ATUAL: {self.currentPath}")
        sleep(1)
        
        print("-" * 40)
        self.startSearch()
        print("-" * 40)
        
        filesQtd = len(self.filesPath)
        findSucess = Fore.GREEN + str(filesQtd)
        findEmpty = Fore.RED + str(filesQtd)
        
        if filesQtd > 0:
            print(f"\n{findSucess}" + Fore.WHITE + " Arquivos no formato" + Fore.GREEN + f" {self.currentExtension} " +  Fore.WHITE + "foram encontrados!\n")  
        else:
            print(f"\n{findEmpty}" + Fore.WHITE + " Arquivos no formato" + Fore.GREEN + f" {self.currentExtension} " +  Fore.WHITE + "foram encontrados!\n")  
        
        
    def startSearch(self):
        for file in os.listdir(self.currentPath):
            if file.endswith(self.currentExtension):
                print(f'\nArquivo {self.currentExtension} encontrado: {file}\n')
                self.filesPath.append(file)


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