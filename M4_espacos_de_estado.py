""" Representação de Espaços de Estado"""

import control as ctrl
import numpy as np

# Criando Função para arredondar os valores


def arredondar(ft):
    ft.num = [[ft.num[0][0].round(4)]]
    return ft


# Definindo as matrizes de Espaço de Estado
A = np.array([[0, 1, 0],
              [0, 0, 1],
              [-3, -2, -5]])
B = np.array([[0],
              [0],
              [1]])
C = np.array([[1, 0, 0]])
D = np.array([[0]])

# Definindo o espaço de estado
sist_ss = ctrl.StateSpace(A, B, C, D)

# Definindo a FT
G = ctrl.ss2tf(sist_ss)

# Corrigindo erros computacionais
G = arredondar(G)

print(G)

# outro exemplo para encontrar o Espaço de Estado (SS)
num = [10, 10]
den = [1, 8, 15]

# Definindo segundo espaço de estado
sist_2 = ctrl.tf2ss(num, den)
print(f'Matrizes de Espaço de Estado do segundo exemplo: \n{sist_2}')
