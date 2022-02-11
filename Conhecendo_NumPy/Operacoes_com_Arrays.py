import numpy as np

km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])

idade = 2022 - anos
print(idade)

km_media = km / idade
print(km_media)

# --------------------------- #

dados = np.array([km, anos])
print(dados)

km_media = dados[0] / (2022 - dados[1])
print(km_media)
