
# desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo

r1 = float(input("Digite a primeira reta: "))
r2= float(input("Digite a segunda reta: "))
r3 = float(input("Digite a terceira reta: "))

if (r1 + r2) > r3 or (r1 + r3) > r2 or (r2 + r3) > r1:
    print("É possivel formar um triangulo")

else:
    print("Não é possivel formar um triangulo")