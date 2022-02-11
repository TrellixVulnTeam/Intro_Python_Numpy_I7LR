import numpy as np
km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])
dados = np.array([km, anos])

print(dados)  # Matriz de 5 linhas e 2 colunas

# ------------------------------------------ #
# OBSERVAÇÃO - Indexação tem origem em zero

contador = np.arange(10)
print(contador)

item = 6
index = item - 1
print(contador[index])
# ------------------------------------------ #
# ------------------------------------------ #

'''             0      1      2      3      4

array dados = 44410,  5712,  37123,  0,   25757  <-- 0
                2003,  1991,  1990,  2019,  2006   <-- 1
'''

print(dados[1][2])  # Desta forma conseguimos atingir a tupla 1990
print(dados[1, 2])  # Funciona da mesma forma

# ------------------------------------------ #
# ------------------------------------------ #

contador = np.arange(10)
print(contador[1:4])    # desta forma pegamos apenas os numeros [1, 2, 3]

print(contador[1:8:2])  # Desta forma varremos do 1 ao 7, de 2 em 2 [1 3 5 7]
print(contador[::2])   # Desta forma varremos todo o codigo de 2 em 2
print(contador > 5)    # Me mostra um array de verdadeiro e falso
print(contador[contador > 5])  # [6 7 8 9]

print(dados[0][0:3])    # Desta forma pegamos apenas [44410.  5712. 37123.]
print(dados[1] > 2000)  # Array com verdadeiro ou falso
print(dados[:, dados[1] > 2000])
