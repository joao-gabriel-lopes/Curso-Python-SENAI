def CalcularTabuada():
    valor = int(input("Digite um número para o cálculo da tabuada: "))

    for i in range(0, 11):
        print(f"{valor} X {i} = {valor * i}")

CalcularTabuada()