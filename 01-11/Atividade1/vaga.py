nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
formacao = input("Você possui formação acadêmica? (sim/nao): ")
experiencia = int(input("Digite quantos anos de experiência você possui: "))

if (idade >= 18 and experiencia >= 2 and formacao == "sim"):
    mensagem = f"Candidato {nome}, você foi aprovado, prossiga para o RH para mais instruções"
else:
    mensagem = f"Candidato {nome}, você não possui as exigências necessárias, tenha um bom dia"

print(mensagem)