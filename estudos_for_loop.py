nomes_cidades = ['São Paulo', 'Londres', 'Tóquio' ,'Paris']
for nome in nomes_cidades:
    print(nome)

contador = 0
nomes_cidades = ['São Paulo', 'Londres', 'Tóquio', 'Paris']
while contador < len(nomes_cidades):
    print(nomes_cidades[contador])
    contador += 1

nomes_cidades = 'São Paulo', 'Londres', 'Tóquio' ,'Paris'
for nome in nomes_cidades:
    print(nome)

cidade = {
    'nome' : 'São Paulo',
    'estado' : 'São Paulo',
    'populacao_milhoes' : 12.2
}

for chave in cidade:
    print(f'{chave} : {cidade[chave]}')



print(list(range(10)))
print(list(range(2, 10)))
print(list(range(2, 10, 2)))