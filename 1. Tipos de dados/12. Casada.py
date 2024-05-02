import os

os.system("cls || clear")

nome = str(input("Digite seu nome: "))
sexo = str(input("Digite seu sexo F ou M: "))
estadoCivil = str(input("Digite seu estado civil: "))

sexo = sexo.lower()
estadoCivil = estadoCivil.lower()

if sexo == 'f' and estadoCivil == "casada":
    tempoCasada = int(input("Quantos anos de casamento? "))
    
print(f"Nome: {nome}")
if sexo == "f":
    print(f"Sexo: feminino")
else: 
    print("Sexo: Masculino")
print(f"Estado civil: {estadoCivil}")
if sexo == 'f' and estadoCivil == "casada":
    print(f"Casada a {tempoCasada} anos")
