import os
os.system("cls || clear")

class Pet:
    def __init__(self, nomePet, idadePet, racaPet, portePet, alimentacaoPet):
        self.nome = nomePet
        self.idade = idadePet
        self.raca = racaPet
        self.porte = portePet
        self.alimentacao = alimentacaoPet

QUANTIDADE = 2
pets = []

os.system("cls || clear")
for i in range(QUANTIDADE):
    nomePet = input("Digite o nome do cão: ")
    idadePet = input("Digite a idade do cão: ")
    racaPet = input("Digite a raça do cão: ")
    portePet = input("Digite o porte do cão: ")
    alimentacaoPet = input("Digite a alimentação do cão: ")
    pets.append(Pet(nomePet, idadePet, racaPet, portePet, alimentacaoPet))

os.system("cls || clear")
for i in pets:
    print(f"Nome do pet: {i.nome}")
    print(f"Idade do pet: {i.idade}")
    print(f"Raça do pet: {i.raca}")
    print(f"Porte do pet: {i.porte}")
    print(f"Alimentação do pet: {i.alimentacao}")