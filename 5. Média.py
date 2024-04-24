# Média
import os

os.system("cls || clear")

print(" === Solicitando dados === \n")
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
primeiraNota = float(input("Digite sua primeira nota: "))
segundaNota = float(input("Digite sua segunda nota: "))

soma = primeiraNota + segundaNota
media = soma / 2

print(" === Exibindo dados === \n")
print(f"Nome do aluno: {nome}")
print(f"Idade do aluno: {idade}")
print(f"Pirmeira nota: {primeiraNota}")
print(f"Segunda nota: {segundaNota}")
print(f"Média do aluno: {media}")