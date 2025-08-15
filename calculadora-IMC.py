peso = float(input("Qual seu peso(kg)?"))
altura = float(input("Qual sua altura(m)?"))

imc = peso / (altura ** 2)

print(f"Seu IMC é {imc:.2f}")