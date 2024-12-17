from time import sleep
valores = []

while True:
    valor = int(input("Digite um valor: "))
    if valor not in valores :
        valores.append(valor)
        print("Valor adicionado com sucesso...")
    else :
        print("Valor duplicado !! Não adicionado")

    resposta = str(input("Quer continuar ? [ S ] ou [ N ]: "))
    
    if resposta in 'Nn':
        break

print('A sua lista ficou assim: ')
print(valores)    
print('Organizando sua lista...')
sleep(2)
valores.sort()
print(valores)
