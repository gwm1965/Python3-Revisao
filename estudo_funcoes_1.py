

'''def calcula_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media'''

def calcula_media(*args, margem):
    soma = sum(args)
    media = soma / len(args)
    return media + margem

print(calcula_media(10, 8, 9, margem = 0.3))

def print_info(**kwargs):
    print(kwargs, type(kwargs))

print_info(nome = 'Mario', seg_nome = 'Wilson', sobrenome = 'Garcia')