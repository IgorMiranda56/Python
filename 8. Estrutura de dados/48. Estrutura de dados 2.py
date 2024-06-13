import os
from dataclasses import dataclass
os.system("cls || clear")

# Constante.
QUANTIDADE_ALUNOS = 1

# Classe.
@dataclass
class Aluno:
    nome: str
    idade: int
    altura: float
    peso: float

alunos = []

for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome= input("Digite seu nome: "),
        idade = int(input("Digite sua idade: ")),
        altura = float(input("Digite sua altura: ")),
        peso = float(input("Digite seu peso: "))
    )

    alunos.append(aluno)

os.system("cls || clear")

# Exibindo dados para o usúario.
for i in alunos:
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
    print(f"Altura: {i.altura}")
    print(f"Peso: {i.peso}")