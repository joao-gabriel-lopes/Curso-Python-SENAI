def analisaTriangulo(lado1, lado2, lado3):
    if(lado1 >= 1 and lado2 >=1 and lado3 >=1):
        if(lado1 == lado2 and lado1 == lado3 and lado2 == lado3):
            tipoTriangulo = "equilátero"
        elif((lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3)):
            tipoTriangulo = "isósceles"
        else:
            tipoTriangulo = "escaleno"

        return tipoTriangulo
    else:
        print("Valores negativos ou iguais a zero não são permitidos!")

lado1 = float(input("Digite o tamanho do primeiro lado do triângulo: "))
lado2 = float(input("Digite o tamanho do segundo lado do triângulo: "))
lado3 = float(input("Digite o tamanho do terceiro lado do triângulo: "))

tipoTriangulo = analisaTriangulo(lado1, lado2, lado3)

print(f"O triângulo é {tipoTriangulo}")