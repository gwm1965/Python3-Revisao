nome = 'Mario'
idade = 56
n_filhos = 3

print(nome + ' tem ' + str(idade) + ' anos e ' + str(n_filhos) + ' filhos')
print('{} tem {} anos e {} filhos'.format(nome,idade,n_filhos))
print(f'{nome} tem {idade} anos e {n_filhos} filhos. ')

preco_gasolina = 3.476
print('O preço da gasolina hoje subiu e está em R$ {:.2f}'.format(preco_gasolina))