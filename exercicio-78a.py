valores = [5,1,5,1,5]
'''c = 0
for v in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
print(f'Você digitou os valores {valores}')'''
print(f'O maior valor é {(max(valores))} nas posições',end=' ')
for c, v in enumerate(valores):
    if v == (max(valores)):
        print(f'{c}',end='...')
