galera = []
dado = []
menor = maior = 0
for c in range(0,3):
    dado.append(str(input("Qual é o seu nome: ")))
    dado.append(int(input("Qual é a sua idade: ")))
    galera.append(dado[:])
    dado.clear()

for p in galera :
    if p[1] >= 18 :
        print(f'{p[0]} é maior de idade. ')
        maior += 1
    else :
        print(f'{p[0]} é menor de idade.')
        menor += 1

print(f'Temos {maior} maior de idade e {menor} menores de idade.')