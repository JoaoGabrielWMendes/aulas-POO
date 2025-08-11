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

def escolher_banco():
    nome_banco = input("Digite o nome do banco: ")
    if nome_banco not in bancos:
        return None
    return bancos[nome_banco]

def checar_banco():
    nome_banco=escolher_banco()
    if nome_banco is None:
        print("Banco não encontrado")
        return None
    return nome_banco

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

def checar_conta():
    numero = int(input("Digite o número da conta: "))
    banco=escolher_banco()
    if banco is None:
        print("Banco ou conta não encontrados")
        return
    for conta in banco.lista_contas:
        if conta.numero==numero:
            return conta

def criar_conta():
    while True:
        saldo = float(input("Digite o saldo inicial: "))
        titular = input("Digite o nome do titular: ")
        numero = int(input("Digite o número da conta: "))
        if titular == "" or numero == "":
            print("Nenhum elemento pode ser vazio. ")
            break
        banco = checar_banco()
        for conta in banco.lista_contas:
            if conta.numero == numero:
                print("Erro ao criar a conta")
                return
        if banco is not None:
            conta_bancaria = Conta_bancaria(titular, numero, saldo)
            banco.adicionar_conta(conta_bancaria)
            print("Conta criada com sucesso!")
        break

def depositar():
    valor = float(input("Digite o valor a ser depositado: "))
    conta = checar_conta()
    if conta is not None:
        conta.depositar(valor)
        print(f"Depósito de R${valor} realizado com sucesso! Saldo atual: R${conta.saldo}")
    return

def sacar():
    valor = float(input("Digite o valor a ser sacado: "))
    conta = checar_conta()
    if conta is not None:
        resultado = conta.sacar(valor)
        if resultado == "Saldo insuficiente":
            print(resultado)
            return
        print(f"Saque realizado com sucesso! Saldo atual: R${conta.saldo}")
    return

def transferir():
        valor = float(input("Valor transferido: "))
        numero_transferidor = int(input("Número da conta de quem irá transferir: "))
        banco_transferidor = checar_banco()
        if banco_transferidor is None:
            print("Banco não encontrado. Tente novamente.")
            return

        conta_que_ira_transferir = None    
        for conta_trasferidor in banco_transferidor.lista_contas:
            if numero_transferidor == conta_trasferidor.numero:
                conta_que_ira_transferir = conta_trasferidor
                
        if conta_que_ira_transferir is None:
            print("Conta não encontrada.")
            return     

        numero_destinatario = int(input("Número do destinatário: "))
        banco_destinatario = checar_banco()
        if banco_destinatario is None:
            print("Banco não encontrado. Tente novamente.")
            return 
        
        conta_que_ira_receber = None
        for conta_destinatario in banco_destinatario.lista_contas:
                if numero_destinatario == conta_destinatario.numero:
                    conta_que_ira_receber = conta_destinatario
        
        if conta_que_ira_receber is None:
            print("Conta não encontrada.")
            return
        
        conta_que_ira_transferir.sacar(valor)
        conta_que_ira_receber.depositar(valor)
        print(f"R${valor} transferido da conta {numero_transferidor} para a conta {numero_destinatario}")

def consultar_saldo():
    conta = checar_conta()
    print(conta)
    if conta is not None:
        conta.consultar_saldo()
    return

def mostrar_contas():
    banco = checar_banco()
    banco.mostrar_contas()

def quantidade_contas():
    banco = checar_banco()
    quantidade = banco.quantidade_contas()
    print(f"Quantidade de contas no banco {banco.nome}: {quantidade}")

def total_valor_em_contas():
    banco = checar_banco()
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
            print("Entrada inválida. Por favor, digite um valor válido.")
            
menu_principal()