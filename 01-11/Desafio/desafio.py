import math

def soma(num1, num2):
    soma = num1 + num2

    return soma

def subtracao(num1, num2):
    subtracao = num1 - num2

    return subtracao

def calculo(num1, num2, num3, num4):
    n1 = soma(num1, num2)
    n2 = subtracao(num3, num4)

    resultado = math.pow(n1, n2) * math.pi

    return resultado

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))

print(calculo(num1, num2, num3, num4))