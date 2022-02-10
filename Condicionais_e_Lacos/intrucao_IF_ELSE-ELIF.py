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

'''Neste caso, separamos entre os carros novos,
carros usados e carros antigos'''
A, B, C = [], [], []

for lista in dados:
    if lista[1] <= 2000:
        A.append(lista)
    elif lista[1] >= 2000 and lista[1] <= 2010:
        B.append(lista)
    else:
        C.append(lista)

print(f'''Carros Antigos: {A}
Carros Usados: {B}
Carros Novos: {C}
''')
