import numpy as np

km = np.array([1000, 2300, 4987, 1500])

print(km)
print(km.dtype)


km = np.loadtxt(
    fname='/home/marcelo/Downloads/Numpy/data/carros-km.txt', dtype=int)

print(km)
print(km.dtype)

# ----------------------------------------------- #
# ----------------------------------------------- #

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

acessorios = np.array(dados)
print(acessorios)
print(acessorios.shape)

np_array = np.arange(1000000)
py_list = list(range(1000000))
