valor = int(input("Digite o valor da compra: "))

if(valor >= 200 and valor < 500):
    valor *= 0.85
    print("O valor da compra com 15% de desconto é:", valor)
elif(valor >= 500):
    valor *= 0.75
    print("O valor da compra com 25% de desconto é:", valor)
else:
    print("O valor da compra é:", valor)