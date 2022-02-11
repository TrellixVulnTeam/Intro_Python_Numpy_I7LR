import numpy as np
anos = np.loadtxt(
    fname='/home/marcelo/Downloads/Numpy/data/carros-anos.txt', dtype=int)
km = np.loadtxt(
    fname='/home/marcelo/Downloads/Numpy/data/carros-km.txt')
valor = np.loadtxt(
    fname='/home/marcelo/Downloads/Numpy/data/carros-valor.txt')

# print(anos, km, valor)
print(anos.shape, km.shape, valor.shape)

# -------------------------------------- #
# .column_stack
# Transforma arrays em colunas Bidimensionais
dataset = np.column_stack((anos, km, valor))
# print(dataset)
print(dataset.shape)

# .mean
print(np.mean(dataset, axis=0))  # Pega a media de todas as colunas

# .sum
print(dataset.sum(axis=0))  # Desta forma somo todas as colunas
print(dataset[:, 1].sum())  # Desta forma somo apenas a kilometragem
