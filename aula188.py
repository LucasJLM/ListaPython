galera = list()
dado = list()
maior = menor = 0
for c in range(0,3) :
    dado.append(str(input("Qual o seu nome: ")))
    dado.append(int(input("Qual a sua idade: ")))
    galera.append(dado[:])
    dado.clear()

for p in galera : 
    if p[1] >= 18 :
        print(f'{p[0]} tem {p[1]} anos, logo é de MAIOR.')
        maior += 1
    else :
        print(f'{p[0]} tem {p[1]} anos, logo é de MENOR.')
        menor += 1

print(f'No total tem {maior} de maior e {menor} menores de idade.')
    