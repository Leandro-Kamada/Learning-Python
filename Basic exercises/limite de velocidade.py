velocidade = float(input("Digite a velocidade do carro: "))
if velocidade > 80: 
    multa = (velocidade-80)*5 
    print(f"Você foi multado com o valor de {multa}")
else:
    print("Você não foi multado")