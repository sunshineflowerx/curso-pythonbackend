import random

num_secreto = random.randint(1, 101)
print(f"n: {num_secreto}")
palpite = 0

print("=== JOGO DE ADVINHAÇÃO ===")
print("Tente advinhar o número secreto entre 1 a 100.")

while palpite != num_secreto:

    palpite_str = input("Qual é o seu palpite? ")

    if palpite_str.isdigit():

        palpite = int(palpite_str)

        if palpite > num_secreto:
            print("-> N° muito alto, tente novamente. ")
        elif palpite < num_secreto:
            print("-> Muito baixo, tente novamente. ")

    else:

        print("Valor inválido, digite outro número. ")

print(f"Parabéns, Você acertou o número {num_secreto}")