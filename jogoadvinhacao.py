import random

num_secreto = random.randint(1, 100)
palpite = 0

print("=== Jogo da Adivinhação ===")
print("Tente advinhar o número secreto entre 1 a 100")

while palpite != num_secreto: 
    
    palpite_str = input("Qual é o seu palpite? ")
    
    if palpite_str.isdigit():
        
        palpite = int(palpite_str)
        
        if palpite > num_secreto:
            print("Nº muito alto, tente novamente. ")
        elif palpite < num_secreto:
            print("Muito baixo, tente novamente. ")
            
    else:
        print("Valor inválido, digite outro número. ")
        
print(f"Parabéns, você acertou o número  {num_secreto}")