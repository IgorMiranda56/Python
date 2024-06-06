import os
import time

preco = 0

while True: 

    print("1 - Pagamento á vista.")
    print("2 - Pagamento á prazo.")
    opcao = int(input("Digite uma opção: "))
    if opcao > 2 or opcao < 1:
        os.system("cls || clear")
        print("Opção inválida.")
    match(opcao):
        case 1:
            valorProduto = "R$100,00"
            formaPagamento = "Á vista"
            desconto = "R$10,00"
            TotalPagar = "R$90,00"
            break
        case 2: 
            valorProduto = "R$100,00"
            formaPagamento = "Á prazo"
            quantidadeParcela = 6
            valorParcela = "R$16,66"
            TotalPagar = "R$100,00"
            break
        case _:
            time.sleep(2)

print(f"Valor do produto: {valorProduto}")
print(f"Forma de pagamento: {formaPagamento}")
if opcao == 1:
    print(f"Desconto: {desconto}")
else:
    print(f"Quantidade de parcelas: {quantidadeParcela}")
    print(f"Valor da parcela: {valorParcela}")
print(f"Total á pagar: {TotalPagar}")





