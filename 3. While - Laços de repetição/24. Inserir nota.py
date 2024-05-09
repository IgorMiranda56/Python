import os

os.system("cls || clear")

soma = 0
contador = 0

while True: 
    nota = float(input("Digite sua nota: "))
    pergunta = input("Deseja insera mais uma nota, se não digite 'N': ")

    pergunta = pergunta.upper()
    soma += nota
    contador += 1
    
    if pergunta == "N":
        break 
        
media = soma / contador

print(f"Média: {media}")
