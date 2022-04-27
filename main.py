# Listas

'''frutas = ["Uva", "Abacaxi", "Maça"]
Lista_misturada = ['Uva', 45, True]


print(frutas)
print(frutas[0])
print(frutas[0:2])
print(frutas[-1:])
print(frutas[-2])
frutas[1] = 'Laranja'
print(frutas)'''

frutas_1 = ['Uva', 'Abacaxi', 'Maça', 'Abacaxi', 'Laranja', 'Banana']
numeros_da_sorte = [30, 4, 8, 15, 16, 23]
frutas_2 = frutas_1.copy()

#frutas_1.extend(numeros_da_sorte )
frutas_1.append('Limão')
frutas_1.insert(1,'Batata')
frutas_1.remove('Maça')
frutas_1.pop()
print(frutas_1.index('Uva'))
print(frutas_1.count('Abacaxi'))
frutas_1.sort()
frutas_1.reverse()

print(frutas_1)
print(frutas_2)