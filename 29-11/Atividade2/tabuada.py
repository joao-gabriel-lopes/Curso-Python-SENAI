def CalcularTabuada(valor):
    contador = 1

    while(contador <= 10):
        print(f"{valor} X {contador} = {valor * contador}")
        contador += 1

valor = int(input("Digite o valor para o cálculo da tabuada: "))

CalcularTabuada(valor)