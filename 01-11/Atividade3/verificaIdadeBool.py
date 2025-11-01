def verificaIdadeBool(idade):
    if(idade >= 18):
        return True
    else:
        return False
    
idade = int(input("Digite a sua idade: "))

print(verificaIdadeBool(idade))