import os
from unidecode import unidecode

path = os.getcwd()

listNames = [
    'Put your file names here'
]

pdfs = []
notFind = []

filenames_lower = [unidecode(file.lower()) for file in os.listdir(path) if file.endswith('.pdf')]

for name in listNames:
    name_lower = name.lower()
    
    
    if name_lower in filenames_lower:
        print(f"=> O nome {name} está na pasta")
    else:
        notFind.append(name)

if notFind:
    with open("teste.txt", "w", encoding="utf-8") as wr:
        for name in notFind:
            wr.write(name.capitalize() + '\n')

print("")
print('=' * 30)
print('Nomes não encontrados: ')
print('=' * 30)
print("")

for name in notFind:
    print(name.replace('.pdf', ''))

print("")
