
# desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens até 200km
# e R$ 0,45 para viagens mais longas 

distancia = int(input("Qual a distância da sua viagem? "))

if distancia <= 200:
    preco = distancia * 0.5
    print(f"O preço de sua passagem custa: R$ {preco:.2f}")

else:
    preco = distancia * 0.45
    print(f"O preço de sua passagem custa: R$ {preco:.2f}")