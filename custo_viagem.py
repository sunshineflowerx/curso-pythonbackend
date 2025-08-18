print("=== Planejador de Custo de Viagem ===")

try:
    distancia = float(input("Distância da viagem (Km): "))
    consumo = float(input("Consumo do carro (Km/l): "))
    preco = float(input("Preço do combustível (R$/l): "))

    custo = (distancia / consumo) * preco
    print(f"\nCusto total estimado: R$ {custo:.2f}")
except ValueError:
    print("Erro: insira apenas números válidos.")