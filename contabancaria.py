class ContaBancaria:
    def __init__(self, numero, titular, saldo=0, limite=1200):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.transacoes = []
    # Comportamentos, Métodos
    # - Sacar, depositar, ver saldo
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Seu saldo foi atualizado")
            self.transacoes.append(f"Depósito realizado de R$ {valor},00")
            return f'Depósito de {valor} realizado'
        else:
            return "Valor de depósito inválido"


    def sacar(self, valor):
        if valor > 0 and valor <= (self.saldo + self.limite):
            self.saldo -= valor
            self.transacoes.append(f"Saque realizado de {valor}")
            return f"Saque de {valor} realizado"
        else:
            return "Nâo é possível sacar esse valor."

    def consultar_saldo(self):
        return f"O seu saldo é R$ {self.saldo:.2f}"


conta_ana = ContaBancaria('001', "Ana", 2000)
conta_carlos = ContaBancaria('002', "Carlos", 1500, 2100)

print(conta_ana.depositar(500))
print(conta_ana.sacar (200))
print(conta_ana.consultar_saldo())
print(conta_ana.numero)
#print