valor = int(input("Digite o valor da compra: "))

if(valor >= 200 and valor < 500):
    valor *= 0.85
    print(f"O valor da compra com 15% de desconto é: R${valor}")
elif(valor >= 500):
    valor *= 0.75
    print(f"O valor da compra com 25% de desconto é: R${valor}")
else:
    print(f"O valor da compra é: R${valor}")