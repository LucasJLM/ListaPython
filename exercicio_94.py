dic =  {}
lista = list ()
soma = media =  0
while True : 
    dic.clear()
    dic['nome'] = str(input("Qual é o seu nome: "))
    
    while True : 
        dic['sexo'] = str(input('Qual o seu sexo [M/F]: ')).strip().upper()
        if dic['sexo'] in 'MF' :
            break
    
        else :
            print('Opção inválida.')

    dic['idade'] = int(input("Qual a sua idade: "))
    soma += dic['idade']
    lista.append(dic.copy())
    while True : 
        pergunta = str(input("Quer continuar [S/N]:  ")).strip().upper()
        if pergunta in 'SN' :
            break
        else :
            print("Opção indisponível.")
    if pergunta == 'N' :
            
        break


print('*'*30)

print(f'Ao todo foram cadastradas {len(lista)} pessoas')
media =  soma / len(lista)
print(f'A media de idade dos cadastrados é de: {media} anos')
print(f'As mulheres cadastradas foram' , end='')
for p in lista :
    if p['sexo'] == 'F' :
        print(f'{p["nome"]}', end='')
