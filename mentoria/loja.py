from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, nome: str, preco_base: float):
        self.nome = nome
        self.preco_base = preco_base
        
    @abstractmethod
    def calcular_preco_final(self) -> float:
        pass
    
class ProdutoFisico(Produto):
    def __init__(self, nome: str, preco_base: float, custo_frete: float):
        super().__init__(nome, preco_base)
        self.custo_frete = custo_frete
    
    def calcular_preco_final(self) -> float:
        return self.preco_base + self.custo_frete
    
class ProdutoDigital(Produto):
    def __init__(self, nome: str, preco_base: float, taxa_download: float):
        super().__init__(nome, preco_base)
        self.taxa_servico = taxa_download
    
    def calcular_preco_final(self) -> float:
        return self.preco_base + self.taxa_servico
    
    
#teste:
if __name__ == "__main__":
    produto_fisico = ProdutoFisico("Livro", 50.0, 10.0)
    produto_digital = ProdutoDigital("E-book", 30.0, 5.0)
    
    print(f"Preço final do produto físico ({produto_fisico.nome}): R$ {produto_fisico.calcular_preco_final()}")
    print(f"Preço final do produto digital ({produto_digital.nome}): R$ {produto_digital.calcular_preco_final()}")

