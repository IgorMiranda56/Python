# Média com aprovação
import os

os.system("cls || clear")

print(" === Solicitando dados === \n")
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
primeiraNota = float(input("Digite sua primeira nota: "))
segundaNota = float(input("Digite sua segunda nota: "))
terceiraNota = float(input("Digite sua terceira nota: "))


soma = primeiraNota + segundaNota + terceiraNota
media = soma / 3

print(" === Exibindo dados === \n")
print(f"Nome do aluno: {nome}")
print(f"Idade do aluno: {idade}")
print(f"Pirmeira nota: {primeiraNota}")
print(f"Segunda nota: {segundaNota}")
print(f"Terceira nota: {terceiraNota}")
print(f"Média do aluno: {media}")

if media >= 7:
    print("Aprovado.")
elif media >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")