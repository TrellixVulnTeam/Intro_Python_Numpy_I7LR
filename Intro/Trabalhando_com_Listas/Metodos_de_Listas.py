Acessorios = ['Rodas de liga',
              'Travas elétricas',
              'Piloto automático',
              'Bancos de couro',
              'Ar condicionado',
              'Sensor de estacionamento',
              'Sensor crepuscular',
              'Sensor de chuva']

# -------------------------------------------- #
# .sort() ele altera a lista e a deixa em ordem alfabética
Acessorios.sort()
print(Acessorios)

# -------------------------------------------- #
# .append() adiciona ao final da minha lista um elemento
Acessorios.append('4 X 4')
print(Acessorios)

# -------------------------------------------- #
'''pop() remove um item da lista,
    caso eu nao passe quem eu quero, ele remove o utlimo'''
Acessorios.pop()
print(Acessorios)

# -------------------------------------------- #
''' .copy(), cria uma copia de uma lista,
     desta forma oq for feito na copia nao altera a original'''
Acessorios_2 = Acessorios.copy()
Acessorios_2.append('4 X 4')
print(Acessorios)
print(Acessorios_2)
