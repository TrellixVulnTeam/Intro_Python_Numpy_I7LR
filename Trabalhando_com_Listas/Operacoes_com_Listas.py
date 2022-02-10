Acessorios = ['Rodas de liga',
              'Travas elétricas',
              'Piloto automático',
              'Bancos de couro',
              'Ar condicionado',
              'Sensor de estacionamento',
              'Sensor crepuscular',
              'Sensor de chuva']

print('Rodas de liga' in Acessorios)     # True
print('Rodas de liga' not in Acessorios)  # False

print('4 x 4' in Acessorios)     # False
print('4 x 4' not in Acessorios)  # True

# ---------------------------------------- #

a = ['Rodas de liga', 'Travas elétricas',
     'Piloto automático', 'Bancos de couro']
b = ['Ar condicionado', 'Sensor de estacionamento',
     'Sensor crepuscular', 'Sensor de chuva']

print(a + b)  # Junta as 2 listas

# ---------------------------------------- #

# Tamanho da Lista
print(len(Acessorios))  # O len conta a quantidade de itens na nossa lista
