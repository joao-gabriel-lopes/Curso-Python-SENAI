def media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3

    if(media >= 7):
        estado = "aprovado"
    else:
        estado = "reprovado"

    return estado

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

print(f"O aluno está {media(nota1, nota2, nota3)}")
