valor = (int(input("Digite um valor: "))),(int(input("Digite um valor: "))),(int(input("Digite um valor: "))),(int(input("Digite um valor: ")))

print(f"Os valores digitados foram : {valor}")

print(f'O numero 9 apareceu {valor.count(9)} vezes')
if 3 in valor: 
    print(f"O numero 3 apareceu na {valor.index(3)+1} posição")
else :
    print('O valor 3 não foi digit ado')
print('Os numeros pares são esses : ')
for n in valor :
    if n % 2 == 0 :
        print(n)
        