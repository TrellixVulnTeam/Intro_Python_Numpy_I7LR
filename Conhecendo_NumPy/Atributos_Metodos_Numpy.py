import numpy as np
km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])
dados = np.array([km, anos])

# --------------------------------------- #
# # ### ATRIBUTOS #####
# .shape
print(dados.shape)  # Retorna as dimensões do array.(2,5)

# .ndim
print(dados.ndim)  # Retorna o numero de dimensões do array. 2 dimensões

# .size
print(dados.size)  # Retorna todos os elementos do array. 10 elementos

# .dtype
print(dados.dtype)  # Retorna o tipo de dados do array. 'float 64'

# .t
print(dados.T)  # Transforma linha em coluna ou coluna em linha.
print(dados.transpose())  # Mesma coisa que .T

# --------------------------------------- #
# --------------------------------------- #

# ### MÉTODOS #####

# .tolist()
print(dados.tolist())  # Transforma o array em lista

# .reshape()
# Retorna um array com os mesmos dados na ordem estipulada
print(dados.reshape(5, 2))
print(dados.reshape(1, 10))

# .resize
dados_new = dados.copy()
dados_new.resize((3, 5))  # Desta forma criamos uma nova linha na nossa tabela
print(dados_new)
# Aqui colocamos a media na 3 linha
dados_new[2] = dados_new[0] / (2019 - dados_new[1])
print(dados_new)
