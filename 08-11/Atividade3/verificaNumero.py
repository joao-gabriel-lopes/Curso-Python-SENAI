def verificarNumero(numero):
    if(numero % 2 == 0):
        if(numero % 3 == 0):
            return (f"O número {numero} é par e múltiplo de 3")
        else:
            return (f"o número {numero} é par")
    else:
        if(numero % 3 == 0):
            return (f"O número {numero} é ímpar e múltiplo de 3")
        else:
            return (f"o número {numero} é ímpar")

numero = int(input("Digite um número: "))

resultado = verificarNumero(numero)

print(resultado)