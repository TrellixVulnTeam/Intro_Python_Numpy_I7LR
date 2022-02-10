dados = [
    ['Rodas de liga', 'Travas elétricas',
     'Piloto automático', 'Bancos de couro',
     'Ar condicionado', 'Sensor de estacionamento',
     'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico',
     'Freios ABS', '4 X 4', 'Painel digital',
     'Piloto automático', 'Bancos de couro',
     'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade',
     'Sensor crepuscular', 'Freios ABS',
     'Câmbio automático', 'Bancos de couro',
     'Central multimídia', 'Vidros elétricos']
]
# Desta maneira mostramos todos os itens contidos em dados.
for lista in dados:
    for item in lista:
        print(item)

''' Desta forma nos conseguimos preencher uma nova lista
    com os itens de outras listas'''
Acessorios = []
for lista in dados:
    for item in lista:
        Acessorios.append(item)
print(Acessorios)

# ------------------------------------------- #

# .set() ultilizamos para remover duplicatas
print(list(set(Acessorios)))

# ------------------------------------------- #
# ------------------------------------------- #


# Podemos fazer de uma melhor forma
print(list(set([item for lista in dados for item in lista])))
