class Conta_bancária:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Adicionado R${valor} na conta {self.titular}")
        return

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
            return
        self.saldo -= valor
        print(f"Sacado R${valor} na conta {self.titular}")

    def consultar_saldo(self):
        print(f"Saldo da conta {self.titular}: R${self.saldo}")

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
        print(f"Quantidade de contas: {len(self.lista_contas)}")
    
    def total_valor_em_contas(self):
        total = 0
        for conta in self.lista_contas:
            total += conta.saldo
        print(f"Valor total em contas: R${total}")

banco = Banco("Banco do Brasil", [])
print(banco.nome)

conta_bancaria1 = Conta_bancária("João", "1234", 1000)
conta_bancaria2 = Conta_bancária("Maria", "5678", 2000)
conta_bancaria3 = Conta_bancária("Pedro", "9101", 3000)

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
banco.total_valor_em_contas()