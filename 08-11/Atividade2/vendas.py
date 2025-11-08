def calcularSalario(valorVendas, anosDeEmpresa):
    if(valorVendas > 50000 and anosDeEmpresa >= 5):
        valorFinal = valorVendas * 1.1
        mensagem = f"Parabéns! Você recebeu um bônus de 10%, resultando em {valorFinal:.2f}"
        return mensagem
    else:
        valorFinal = valorVendas
        mensagem = f"Você recebeu {valorFinal:.2f}"
        return mensagem

valorVendas = float(input("Digite o valor das vendas: "))
anosDeEmpresa = float(input("Digite quantos anos de empresa você possui: "))

print(calcularSalario(valorVendas, anosDeEmpresa))