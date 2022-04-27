numeros = [1, 2, 4, 6, 7, 9]
num = int(input('Digite um valor: '))
if num not in numeros:
    numeros.append(num)
else:
    print('O valor já existe na lista')
print(numeros)
