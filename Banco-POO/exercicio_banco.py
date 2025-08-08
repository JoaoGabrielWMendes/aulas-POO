import os
bancos = {}
class Conta_bancaria:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return

    def sacar(self, valor):
        if valor > self.saldo:
            return ("Saldo insuficiente")
        self.saldo -= valor
        return 

    def consultar_saldo(self):
        print(f"Saldo da conta {self.titular}: R${self.saldo}")
        return

class Banco:
    def __init__(self, nome, lista_contas):
        self.nome = nome
        self.lista_contas = lista_contas

    def adicionar_conta(self, conta_bancaria):
        self.lista_contas.append(conta_bancaria)

    def mostrar_contas(self):
        for conta in self.lista_contas:
            print (f"Titular: {conta.titular}, Número: {conta.numero}, Saldo: {conta.saldo}")
        return 
    
    def quantidade_contas(self):
        return len(self.lista_contas)
    
    def total_valor_em_contas(self):
        total = 0
        for conta in self.lista_contas:
            total += conta.saldo
        return total

def criar_banco():
    while True:
        nome_banco = input("Digite o nome do banco: ")
        if nome_banco == "":
            print("Nome do banco não pode ser vazio.")
            break
        banco = Banco(nome_banco, [])
        if nome_banco in bancos:
            print(f"Banco {nome_banco} já existe.")
        else:
            bancos[nome_banco] = banco
            print(f"Banco {nome_banco} criado com sucesso!")
        break

def escolher_banco():
    nome_banco = input("Digite o nome do banco: ")
    if nome_banco not in bancos:
        return None
    return bancos[nome_banco]

def checar_conta():
    numero = input("Digite o número da conta: ")
    banco=escolher_banco()
    if banco is not None:
        for conta in banco.lista_contas:
            if conta.numero==numero:
                return conta
    print("Banco ou conta não encontrados")
    return None



def criar_conta():
    while True:
        titular = input("Digite o nome do titular: ")
        numero = input("Digite o número da conta: ")
        if titular == "" or numero == "":
            print("Nenhum elemento pode ser vazio. ")
            break
        banco = escolher_banco()
        saldo = float(input("Digite o saldo inicial: "))
        conta_bancaria = Conta_bancaria(titular, numero, saldo)
        banco.adicionar_conta(conta_bancaria)
        print("Conta criada com sucesso!")
        break

def depositar():
    valor = float(input("Digite o valor a ser depositado: "))
    conta = checar_conta()
    if conta is None:
        return
    conta.depositar(valor)

def sacar():
    valor = float(input("Digite o valor a ser sacado: "))
    conta = checar_conta()
    if conta is None:
        return
    resultado = conta.sacar(valor)
    if resultado == "Saldo insuficiente":
        print(resultado)
        return
    print(f"Saque realizado com sucesso! Saldo atual: R${conta.saldo}")

def transferir():
    numero_transferidor = input("Número da conta de quem irá transferir:")
    banco_transferidor = escolher_banco()
    valor = float(input("Valor transferido: "))
    numero_destinatario = input("Número do destinatário: ")
    banco_destinatario = escolher_banco()
    if banco_transferidor is None or banco_destinatario is None:
        print("Banco ou conta não encontrados")
        return
    for conta in banco_transferidor.lista_contas:
        if conta.numero == numero_transferidor:
            conta.sacar(valor)
    for conta in banco_destinatario.lista_contas:
        if conta.numero == numero_destinatario:
            conta.depositar(valor)
    print(f"R${valor} transferido da conta {numero_transferidor} para a conta {numero_destinatario}")

def consultar_saldo():
    conta = checar_conta()
    conta.consultar_saldo()

def mostrar_contas():
    banco = escolher_banco()
    banco.mostrar_contas()

def quantidade_contas():
    banco = escolher_banco()
    quantidade = banco.quantidade_contas()
    print(f"Quantidade de contas no banco {banco.nome}: {quantidade}")

def total_valor_em_contas():
    banco = escolher_banco()
    total = banco.total_valor_em_contas()
    print(f"Total em contas no banco {banco.nome}: R${total}")

def menu_principal():
    while True:
        input("Clique em Enter para continuar...")
        os.system('cls')
        opcoes = {
            1: criar_banco,
            2: criar_conta,
            3: depositar,
            4: sacar,
            5: transferir,
            6: consultar_saldo,
            7: mostrar_contas,
            8: quantidade_contas,
            9: total_valor_em_contas,
        }
        print("Selecione uma opção:\n 1: Criar banco\n 2: Criar conta\n 3: Depositar\n 4: Sacar\n 5: Transferir valor\n 6: Consultar saldo\n 7: Mostrar contas\n 8: Quantidade de contas\n 9: Total em contas\n 10: Sair")

        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao in opcoes:
                opcoes[opcao]()
            elif opcao == 10:
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
menu_principal()
'''conta_bancaria1 = Conta_bancaria("João", "1234", 1000)
conta_bancaria2 = Conta_bancaria("Maria", "5678", 2000)
conta_bancaria3 = Conta_bancaria("Pedro", "9101", 3000)

banco.adicionar_conta(conta_bancaria1)
banco.adicionar_conta(conta_bancaria2)
banco.adicionar_conta(conta_bancaria3)

conta_bancaria1.depositar(500)
conta_bancaria2.sacar(3000)
conta_bancaria3.sacar(1000)

conta_bancaria1.consultar_saldo()
conta_bancaria2.consultar_saldo()
conta_bancaria3.consultar_saldo()

banco.mostrar_contas()
banco.quantidade_contas()
banco.total_valor_em_contas()'''