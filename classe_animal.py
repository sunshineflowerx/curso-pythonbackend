class Animal:
    def __init__(self, especie: str, nome: str, idade: int):
        self.especie = especie
        self.nome = nome
        self.idade = idade
        self.vivo = True
        self.fome = 50

    def comer(self):
        if self.vivo:
            self.fome += 10
            return f"{self.nome} comeu."
        else:
            return f"O animal não pode comer"

    def dormir(self):
        if self.vivo:
            return f"{self.nome} está dormindo."
        else:
            f"{self.nome} não pode dormir"

    def emitir_som(self):
        if self.vivo:
            return f"{self.nome} está emitindo um som."
        else:
            return f"{self.nome} não pode emitir som"

    def mover(self):
        if self.vivo:
            return f"{self.nome} está se movendo."
        else:
            return f"{self.nome} não pode se mover."

cachorro = Animal("Mamifero", "Rex", 2)
c = cachorro.emitir_som()
print (c)