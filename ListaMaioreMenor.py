valores = []
maior = 0
menor = 0
for c in range(0,5) : 
    valores.append(int(input(f"Digite um valor na posição {c}: ")))
    if c == 0 :
        maior = menor = valores[c] 
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor :
            menor = valores[c]

print(*'-')
print(f'Os valores adcionados a lista foram: {valores}')
print(f'O maior valor digitado foi : {maior},nas posições ', end='')
for i,v in enumerate(valores) :
    if v == maior:
        print(f'{i}...')
print(f'O menor valor digitado foi: {menor}')
for i,v in enumerate(valores):
    if v == menor :
        print(f'{i}...')




