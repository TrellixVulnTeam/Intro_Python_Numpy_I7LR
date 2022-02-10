Acessorios = ['Rodas de liga',
              'Travas elétricas',
              'Piloto automático',
              'Bancos de couro',
              'Ar condicionado',
              'Sensor de estacionamento',
              'Sensor crepuscular',
              'Sensor de chuva']

Carro_1 = ['Jetta Variant', 'Motor 4.0 Turbo', 2003, 44410.0, False, [
    'Rodas de liga', 'Travas elétricas', 'Piloto automático'], 88078.64]
Carro_2 = ['Passat', 'Motor Diesel', 1991, 5712.0, False, [
    'Central multimídia', 'Teto panorâmico', 'Freios ABS'], 106161.94]

carros = [Carro_1 + Carro_2]

print(Acessorios[0])  # Desta maneira acessamos 'Rodas de liga'
print(Acessorios[1])  # Desta maneira acessamos 'Travas elétricas'
# Desta maneira acessamos de tras para frente 'Sensor de chuva'
print(Acessorios[-1])

# ---------------------------------------- #

print(carros[0][0])


# Inclui na lista os elementos definidos. Do 2 ao 4, o 5 nao entra.
print(Acessorios[2:5])
print(Acessorios[2:])
