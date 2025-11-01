def verificaSomatoria(num1, num2, num3):
    somatoria = num1 + num2 + num3

    if(somatoria > 20):
        return somatoria
    else:
        return "Valor mínimo não atingido"

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

print(verificaSomatoria(num1, num2, num3))