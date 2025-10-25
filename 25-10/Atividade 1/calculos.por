programa {
  funcao inicio() {
    inteiro num1, num2, num3, num4, num5, num6, soma, subtracao, divisao, resto_divisao

    escreva("Digite o primeiro número: ")
    leia(num1)

    escreva("Digite o segundo número: ")
    leia(num2)

    escreva("Digite o terceiro número: ")
    leia(num3)

    escreva("Digite o quarto número: ")
    leia(num4)

    escreva("Digite o quinto número: ")
    leia(num5)

    escreva("Digite o sexto número: ")
    leia(num6)

    soma = num1 + num2
    subtracao =  num2 - num3
    divisao =  num3 / num4
    resto_divisao = num5 % num6

    escreva("\n")

    escreva("O resultado da soma é: ", soma, "\n")
    escreva("O resultado da subtração é: ", subtracao, "\n")
    escreva("O resultado da divisão é: ", divisao, "\n")
    escreva("O resto da divisão é: ", resto_divisao, "\n")
  }
}
