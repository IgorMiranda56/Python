import os
os.system("cls || clear")

# Constante.
QUANTIDADE_ALUNOS = 2

# Vetor.
nomes = []
idades = []

for i in range(QUANTIDADE_ALUNOS):
    nome = input("Digite seu nome")
    idade = int(input("Digite seu nome"))

    nomes.append(nome)
    idades.append(idade)

# Exibindo dados para o usúario.
for i in range(QUANTIDADE_ALUNOS):
    print(f"Nomes: {nomes[i]}")
    print(f"Idades: {idades[i]}")