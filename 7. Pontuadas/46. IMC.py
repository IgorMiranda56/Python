import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")
def calculo(valor1, valor2):
    resultado = valor1 / (valor2 * valor2) 
    return resultado
def resposta(imc):
    if imc < 18.5:
        situacao = "Abaixo do peso"
    elif imc >= 18 and imc < 25:
        situacao = "Peso normal"
    elif imc >= 25 and imc < 30:
        situacao = "Sobrepeso"
    elif imc >= 30 and imc < 35:
        situacao = "Obesidade grau I"
    elif imc >= 35 and imc < 40:
        situacao = "Obesidade grau II"
    else:
        situacao = "Obesidade grau III (mórbida)"
    return situacao
# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []
sobrenomes = []
imcs = []
resultados = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    sobrenome = input("Digite o sobrenome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    
#Calculando IMC
    imc = calculo(peso, altura)
    resultado = resposta(imc)
    imcs.append(imc)
    resultados.append(resultado)
    
# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("Nome:", nomes[i], sobrenomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print(f"IMC: {imcs[i]:.2f}")
    print(f"Interpretação do resultado: {resultados[i]}")
