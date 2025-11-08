def parImpar(numero):
    if(numero % 2 == 0):
        print(f"O número {numero} é par")
    else:
        print(f"o número {numero} é ímpar")

numero = int(input("Digite um número: "))
parImpar(numero)