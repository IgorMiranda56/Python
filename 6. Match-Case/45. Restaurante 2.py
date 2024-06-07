import os
import time

prato = ""
preco = 0
somarPreco = 0
lista_prato = []
resultado = 0

while True:
    print("=== MENU ===")
    print("1 - Picanha.")
    print("2 - Lasanha.")
    print("3 - Strogonoff.")
    print("4 - Batata.")
    print("5 - Pão com ovo.")
    print("6 - Salada.")
    print("7 - Bolo.")
    print("0 - Para finalizar. ")
    opcao = int(input("Adicione uma opção do menu ou finalize: "))
    os.system("cls || clear")
    if opcao > 7 or opcao < 0:
        os.system("cls || clear")
        print("Opção inválida. ")
    match(opcao):
        case 1:
            prato = "1 - Picanha"
            preco = 25.00
            somarPreco += preco
            lista_prato.append(prato)
        case 2:
            prato = "2 - Lasanha"
            preco = 20.00
            somarPreco += preco
            lista_prato.append(prato)
        case 3:
            prato = "3 - Strogonoff"
            preco = 30.00
            somarPreco += preco
            lista_prato.append(prato)
        case 4:
            prato = "4 - Batata"
            preco = 10.00
            somarPreco += preco
            lista_prato.append(prato)
        case 5:
            prato = "5 - Pão com ovo"
            preco = 5.00
            somarPreco += preco
            lista_prato.append(prato)
        case 6:
            prato = "6 - Salada"
            preco = 4.00
            somarPreco += preco
            lista_prato.append(prato)
        case 7:
            prato = "7 - Bolo"
            preco = 6.00
            somarPreco += preco
            lista_prato.append(prato)
        case 0:
            if prato == "":
                print("Nenhum prato adicionado.")
                break
            else:
                formaPagamento = int(input("Forma de pagamento: 1 - à vista ou 2 - cartão de crédito: "))
                if formaPagamento == 1:
                    formaPagamento = "À vista"
                    desconto = somarPreco * 0.1
                    resultado = somarPreco - desconto
                    tipoPagamento = "Desconto"
                elif formaPagamento == 2:
                    formaPagamento = "Cartão de crédito"
                    desconto = somarPreco * 0.1
                    resultado = somarPreco + desconto
                    tipoPagamento = "Acréscimo"
                os.system("cls || clear")
                for i, prato in enumerate(lista_prato):
                    print(f"Opção escolhida: {prato}")
                print(f"Forma de pagamento: {formaPagamento}")
                print(f"Valor do {tipoPagamento}: {desconto:.2f}")
                print(f"Subtotal: {somarPreco:.2f}")
                print(f"Total a pagar: {resultado:.2f}")
                break
        case _:
            time.sleep(2)
    tenteNovamente = str(input("Deseja adicionar outra opção? (S/N):"))
    tenteNovamente = tenteNovamente.upper()
    if tenteNovamente != "S":
        time.sleep(2)
        continue
