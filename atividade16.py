# Crie um programa que receba o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal (IMC). O programa deve classificar o IMC da pessoa de acordo com a tabela a seguir:
# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 ≤ IMC < 25
# Sobrepeso: 25 ≤ IMC < 30
# Obesidade: IMC ≥ 30
p = float(input("digite o seu peso:"))
a = float(input("digite sua altura:"))

imc = p/(a*a)

if imc <18.5:
    print("abaixo do peso")
elif imc >18.5<25:
    print("peso normal")
elif imc >25<30:
    print("sobrepeso")
elif imc >30:
    print("obesidade")
    