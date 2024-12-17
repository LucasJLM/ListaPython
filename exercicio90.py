boletim = {}

boletim['nome'] = str(input("Qual o seu nome: "))
boletim['media'] = float(input(f"Média de {boletim['nome']}: "))
if boletim['media'] >= 7 :
    boletim['situação'] = 'Aprovado'
elif 5 <= boletim['media'] < 7 :
    boletim['situação'] = 'Recuperação'
else :
    boletim['situação'] = 'Reprovado'

for k,v in boletim.items():
    print(f'{k} é igual a {v}')




