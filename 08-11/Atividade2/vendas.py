def calcularSalario(valorVendas, anosDeEmpresa):
    if(valorVendas > 50000 and anosDeEmpresa >= 5):
        mensagem = f"Parabéns! Você vendeu {valorVendas} e ganhou uma comissão de {(valorVendas * 0.1):.2f}"
        return mensagem
    else:
        mensagem = f"Você não atingiu os requisitos para o bônus"
        return mensagem

valorVendas = float(input("Digite o valor das vendas: "))
anosDeEmpresa = float(input("Digite quantos anos de empresa você possui: "))

print(calcularSalario(valorVendas, anosDeEmpresa))