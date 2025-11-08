import math

def calcularAreaCirculo(raio):
    resultado = math.pi * raio * raio
    return resultado

raio = float(input("Digite o raio do círculo: "))

print(f"A área do círculo de raio {raio} é {round(calcularAreaCirculo(raio), 2)}")