class Conta_bancária:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        if valor > self.saldo:
            return "Saldo insuficiente"
        self.saldo -= valor
        return self.saldo
        
    def consultar_saldo(self):
        return self.saldo
        
class Banco:
    def __init__(self, nome, lista_contas):
        self.nome = nome
        self.lista_contas = lista_contas

    def adicionar_conta(self, conta_bancaria):
        self.lista_contas.append(conta_bancaria)

    def mostrar_contas(self):
        for conta in self.lista_contas:
            return (f'Titular: {conta.titular}, Número: {conta.numero}, Saldo: {conta.saldo}')

    def quantidade_contas(self):
        return len(self.lista_contas)
    
    def total_valor_em_contas(self):
        total = 0
        for conta in self.lista_contas:
            total += conta.saldo
        return total
def opcoes_conta_bancária():
    print("Opçoes de conta: ")

def opcoes_banco():
    print("Opções do banco:")

opcoes = {
    1: opcoes_conta_bancária(),
    2: opcoes_banco(), 
}
print("Opções disponíveis:\n1: Contas bancárias\n2: Banco")
opcao=int(input("O que você deseja fazer? "))
if opcao in opcoes.items():
    opcoes(opcao)
else: 
    print("Opção inválida, tente novamente.")


'''banco = Banco("Banco do Brasil", [])
conta_bancaria1 = Conta_bancária("João", "1234", 1000)
conta_bancaria2 = Conta_bancária("Maria", "5678", 2000)
conta_bancaria3 = Conta_bancária("Pedro", "9101", 3000)
banco.adicionar_conta(conta_bancaria1)
banco.adicionar_conta(conta_bancaria2)
banco.adicionar_conta(conta_bancaria3)
conta_bancaria1.depositar(500)
print(conta_bancaria1.consultar_saldo())
print(conta_bancaria2.sacar(3000))
print(banco.mostrar_contas())
print(banco.quantidade_contas())
print(banco.total_valor_em_contas())'''