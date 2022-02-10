'''
    for <variavel> in <coleção>:
        <instruções>
'''
# ------------------------------ #

Acessorios = ['Rodas de liga',
              'Travas elétricas',
              'Piloto automático',
              'Bancos de couro',
              'Ar condicionado',
              'Sensor de estacionamento',
              'Sensor crepuscular',
              'Sensor de chuva']

# ------------------------------ #
# Neste cado listamos cada item da lista
for item in Acessorios:
    print(item)

# ------------------------------ #
'''range() me da um tamanho para minha lista,
     neste cado preenchemos com i ao quadrado'''
for i in range(10):
    print(i**2)

''' neste caso criamos a lista quadrado
    e com o FOR, varremos a lista, o.append preenche essa lista'''
quadrado = []
for i in range(10):
    quadrado.append(i ** 2)

print(quadrado)
# ------------------------------ #
# ------------------------------ #

# Podemos fazer desta forma tambem,muito mais simplificado
print([i ** 2 for i in range(10)])
