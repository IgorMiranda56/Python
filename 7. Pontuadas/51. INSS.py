import os

def cabecalho():
    os.system("cls || clear")
    print("==== Calculo ====")
    
def calculoInss(salarioBase):
    if salarioBase <= 1100:
        descontoInss = salarioBase * 0.075
    elif salarioBase <= 2203.48:
        descontoInss = salarioBase * 0.09
    elif salarioBase <= 3305.22:
        descontoInss = salarioBase * 0.12
    elif salarioBase <= 6433.57:
        descontoInss = salarioBase * 0.14
    else:
        descontoInss = 854.36
    return descontoInss
    
def calculoImpostoRenda(salarioBase, quantidadeDependentes):
    if salarioBase > 2259.20 and salarioBase <= 2826.65:
        descontoImpostoRenda = salarioBase * 0.075
        deducaoImposto = quantidadeDependentes * 189.59
        descontoImpostoRendaTotal = descontoImpostoRenda + deducaoImposto
    elif salarioBase <= 3751.05:
        descontoImpostoRenda = salarioBase * 0.15
        deducaoImposto = quantidadeDependentes * 189.59
        descontoImpostoRendaTotal = descontoImpostoRenda + deducaoImposto
    elif salarioBase <= 4664.68:
        descontoImpostoRenda = salarioBase * 0.225
        deducaoImposto = quantidadeDependentes * 189.59
        descontoImpostoRendaTotal = descontoImpostoRenda + deducaoImposto 
    else: 
        descontoImpostoRenda = salarioBase * 0.275
        deducaoImposto = quantidadeDependentes * 189.59
        descontoImpostoRendaTotal = descontoImpostoRenda + deducaoImposto
    return descontoImpostoRendaTotal
    
def calculoValeTransporte(salarioBase):
    if pergunteValeTransporte == 's':
        descontoValeTransporte = salarioBase * 0.06
    else:
        descontoValeTransporte = 0
    return descontoValeTransporte
    
def calculoValeRefeicao(valeRefeicao):
    descontoValeRefeicao = valeRefeicao * 0.2
    return descontoValeRefeicao
    
def calculoPlanoSaude(quantidadeDependentes):
    if perguntaPlanoSaude == 's':
        descontoPlanoSaude = 150
        descontoDependente = descontoPlanoSaude * quantidadeDependentes
        descontoPlanoSaudeTotal = descontoDependente + descontoPlanoSaude
    else: 
        descontoPlanoSaudeTotal = 150
    return descontoPlanoSaudeTotal

while True:   
    cabecalho()
    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")
    if matricula == "789" and senha == "123":
        salarioBase = float(input("Digite seu salário: "))
        pergunteValeTransporte = str(input("Deseja receber vale transporte (s/n)? "))
        pergunteValeTransporte = pergunteValeTransporte.lower()
        valeRefeicao = float(input("Qual o valor do vale refeição? "))
        break
    else:
        cabecalho()
        print("Matrícula ou senha inválida.")
        
while True:
    perguntaPlanoSaude = str(input("Você possui dependente (s/n)? ")).lower()
    if perguntaPlanoSaude == 's':
        quantidadeDependentes = int(input("Quantos dependentes? "))
        break
    elif perguntaPlanoSaude == 'n':
        quantidadeDependentes = 0
        break
    else:
        print("Digite s ou n.")

if pergunteValeTransporte == 's':
    descontoTotal = calculoInss(salarioBase) + calculoImpostoRenda(salarioBase, quantidadeDependentes) + calculoValeTransporte(salarioBase) + calculoValeRefeicao(valeRefeicao) + calculoPlanoSaude(quantidadeDependentes)
else:
    descontoTotal = calculoInss(salarioBase) + calculoImpostoRenda(salarioBase, quantidadeDependentes) + calculoValeRefeicao(valeRefeicao) + calculoPlanoSaude(quantidadeDependentes)
    
salarioLiquido = salarioBase - descontoTotal
cabecalho()
print(f"salário Base: {salarioBase}")
print(f"INSS: {calculoInss(salarioBase)}")
print(f"Imposto de renda: {calculoImpostoRenda(salarioBase, quantidadeDependentes)}")
if pergunteValeTransporte == 'S':
    print(f"Vale refeição: {calculoValeTransporte(salarioBase)}")
print(f"Vale transporte: {calculoValeRefeicao(valeRefeicao)}")
print(f"Plano saúde: {calculoPlanoSaude(quantidadeDependentes)}")
print(f"Salário líquido: {salarioLiquido:.2f}")