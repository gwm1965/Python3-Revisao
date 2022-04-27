
numeros = []
num = (int(input('Digite um valor: ')))
numeros.append(num)
resposta = input('Quer continuar?[S/N]: ').upper()
print('Valor adcionado com sucesso!')




while resposta != 'N':
    num = (int(input('Digite um valor:')))
    if num not in numeros:
        numeros.append(num)
        resposta = input('Quer continuar?[S/N]: ').upper()
        print('Valor adcionado com sucesso!')
    else:
        print('Valor ja existe na lista')
print(numeros)