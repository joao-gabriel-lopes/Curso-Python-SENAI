def MaioresIdade():
    QuantidadeMaioresIdade = 0
    contador = 1

    while(contador <= 5):
        idade = int(input(f"Digite a idade da pessoa {contador}: "))
        
        if(idade >= 18):
            QuantidadeMaioresIdade += 1
        
        contador += 1
        
    if(QuantidadeMaioresIdade == 0):
        print("Nenhuma pessoa é maior de idade")
    elif (QuantidadeMaioresIdade == 1):
        print(f"{QuantidadeMaioresIdade} pessoa é maior de idade")
    else:
        print(f"{QuantidadeMaioresIdade} pessoas são maiores de idade")

MaioresIdade()