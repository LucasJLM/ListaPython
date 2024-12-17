pessoa = {}

pessoa['nome'] = str(input("Digite o seu nome: "))
nascimento = int(input("Digite a data de nascimento: "))
pessoa['idade'] = 2024 - 2003
pessoa['ctps'] = int(input("Carteira de trabalho (0 não tem): "))

if pessoa['ctps'] == 0 :
    for k,v in pessoa.items() :
        print(f'{k} é {v}')

else :
    pessoa['ano_contratação'] = int(input("Ano da contratação: "))
    pessoa['salario'] = float(input("Digite o seu salário: "))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['ano_contratação']+35)-2024)
    for k, v in pessoa.items() :
        print(f'{k} é {v}')


