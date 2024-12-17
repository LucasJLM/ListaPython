valores = []

while True: 
    valor = int(input('Digite um valor: '))
    
    valores.append(valor)

    resposta = str(input("Você deseja continuar ? [ S ] ou [ N ]: "))
    if resposta in 'Nn' :
        break
    
print('-*'*20)
print(f'A lista ficou assim: {valores}')

print(f'A lista possui {len(valores)} valores')  

valores.sort(reverse=True)
print(f'A lista em forma decrescente: {valores}')


if 5 in valores :
    print('O número 5 está presente na lista !!!')
else :
    print('O número 5 não está na lista...')
print('-*'*20)
