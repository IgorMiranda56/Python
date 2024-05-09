import os
import time
os.system("cls || clear")

soma = 0 
contador = 0

while True:
    nota = float(input("Digite sua nota: "))
    
    if nota > 0:
        contador+= 1
        soma += nota
    else:
        if contador == 0:
            print("Digite novamente. ")
            time.sleep(1)
            os.system("clear")
        else:        
            break    

media = soma / contador 

print(f"Média: {media}")