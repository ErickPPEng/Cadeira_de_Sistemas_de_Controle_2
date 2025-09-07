""" Resolução da questão PC3.8 do Dorf"""

import numpy as np
import matplotlib.pyplot as plt

# Definindo os autovalores da matriz A dada
def calc_autovalores(K):
    A = np.array([[0, 1, 0],
                  [0, 0, 1],
                  [-2, -K, -2]])
    autovalores, _ = np.linalg.eig(A)
    return autovalores

# Range do valores de K
valores_K = np.linspace(0, 100, 500)

# Plotando o gráfico
plt.figure(figsize=(10,6))

# Lista de valores de K onde todos os valores característicos estão no semiplano esquerdo
valores_K_semiplano_esquerdo = []

# Computar e plotar os valores caracteristicos no gráfico
for K in valores_K:
    autovalores = calc_autovalores(K)
    if np.all(np.real(autovalores) < 0):
        valores_K_semiplano_esquerdo.append(K)
    plt.plot(np.real(autovalores), np.imag(autovalores), 'bx')

# Arredondando os Valores de K para 1 casa decimal
valores_K_semiplano_esquerdo = np.round(valores_K_semiplano_esquerdo, 1)
print('valores de K onde todos os valores característicos estão no semiplano esquerdo\n', valores_K_semiplano_esquerdo)

plt.axvline(0, color='r', linestyle='--') # indicando o eixo imaginário
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Representação graficamente os valores característicos do sistema em função de K na faixa de valores 0 ≤ K ≤ 100')
plt.grid()
plt.show()