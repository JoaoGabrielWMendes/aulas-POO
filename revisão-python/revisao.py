#Cadastro de contas bancarias
#Criar um menu de opções
#1 - Criar uma conta
#2 - Listar contas
#3 - Depositar
#4 - Sacar
#5 - Sair
import os
lista_contas = {}
def checar_conta(conta):
    return conta in lista_contas

def criar_conta():
    numero_conta = int(input("Digite o numero da conta: "))
    valor_conta=0
    lista_contas[numero_conta] = valor_conta
    print("Conta criada com sucesso")


def listar_contas():
    print("Listar contas")
    for conta in lista_contas:
        print(conta)


def depositar():
    print("Depositar")
    numero_conta = int(input("Digite o numero da conta: "))
    if checar_conta(numero_conta):
        valor_deposito = float(input("Digite o valor do depósito: "))
        lista_contas[numero_conta] += valor_deposito
        print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso na conta {numero_conta}.")
        print(f"A conta {numero_conta} agora tem um saldo de R${lista_contas[numero_conta]:.2f}.")
    else:
        print("Conta não encontrada.")


def sacar():
    print("Sacar")
    numero_conta = int(input("Digite o número da conta: "))
    if checar_conta(numero_conta):
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque <= lista_contas[numero_conta]:
            lista_contas[numero_conta] -= valor_saque
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso na conta {numero_conta}.")
            print(f"A conta {numero_conta} agora tem um saldo de R${lista_contas[numero_conta]:.2f}.")
        else:
            print("Saldo insuficiente.")
    else:
        print("Conta não encontrada.")


def menu():
    opcoes={
        1: criar_conta,
        2: listar_contas,
        3: depositar,
        4: sacar,
    }


    while True:
        os.system('cls')
        print("1 - Criar uma conta\n2 - Listar contas\n3 - Depositar\n4 - Sacar\n5 - Sair")
       
        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao in opcoes:
                os.system('cls')
                opcoes[opcao]()
            elif opcao == 5:
                os.system('cls')
                print("Sair")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Opção inválida. Tente novamente.")
        input("Pressione Enter para continuar...")


menu()

