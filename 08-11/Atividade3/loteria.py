def calcularReparticao(valorPremio, valorApostado1, valorApostado2, valorApostado3):
    somaApostas = valorApostado1 + valorApostado2 + valorApostado3

    if(somaApostas < valorPremio):
        
        if(valorApostado1 > 0 and valorApostado2 > 0 and valorApostado3 > 0):
            premioApostador1 = (valorApostado1 / somaApostas) * valorPremio
            premioApostador2 = (valorApostado2 / somaApostas) * valorPremio
            premioApostador3 = (valorApostado3 / somaApostas) * valorPremio
            
            print(f"Jogador 1 ganhou: {premioApostador1:.2f}", f"Jogador 2 ganhou: {premioApostador2:.2f}", f"Jogador 3 ganhou: {premioApostador3:.2f}")
            
        else:
            print("Valores negativos não são válidos!")
    
    else:
        print("Os valores apostados são maiores que o valor do prêmio!")

valorPremio = float(input("Digite o valor do prêmio: "))
valorApostado1 = float(input("Digite o valor apostado pelo primeiro jogador: "))
valorApostado2 = float(input("Digite o valor apostado pelo segundo jogador: "))
valorApostado3 = float(input("Digite o valor apostado pelo terceiro jogador: "))

calcularReparticao(valorPremio, valorApostado1, valorApostado2, valorApostado3)