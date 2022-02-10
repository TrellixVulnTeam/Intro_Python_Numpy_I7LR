'''
       if <condição>:
           <instrução caso a consição seja verdadeira>
       else:
           <instrução caso a condição seja falsa>
    '''

'''
Operadores Lógicos: and, or, not
Operadores de Comparação: ==, !=, >, <, >=, <=
'''
# 1º item da lista - Nome do veículo
# 2º item da lista - Ano de fabricação
# 3º item da lista - Veículo é zero km?

dados = [
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2019, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2012, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Jorney', 2019, False],
    ['Carens', 2011, False]
]
# Caso seja Zero KM
zero_km_V = []
for lista in dados:
    if (lista[2] is True):
        zero_km_V.append(lista)

print(zero_km_V)

# Caso não seja Zero KM
zero_km_F = []
for lista in dados:
    if (lista[2] is False):
        zero_km_F.append(lista)

print(zero_km_F)
