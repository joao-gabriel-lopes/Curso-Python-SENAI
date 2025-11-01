def verificaIdade(idade):
    if(idade >= 18):
        return "Olá, você é maior de idade"
    else:
        return "Olá, você é menor de idade"
    
idade = int(input("Digite a sua idade: "))

print(verificaIdade(idade))