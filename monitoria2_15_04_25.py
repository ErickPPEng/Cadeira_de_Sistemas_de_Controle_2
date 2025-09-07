"""Exemplo 2
EE para FT"""

import numpy as np
import control as ct

# Matrizes do EE
A = np.array([[7.5, -3.5], 
              [1, 0]])

B = np.array([[1],
              [0]])

C = np.array([1, -10])

D = np.array([0])

# Criando o EE
EE = ct.StateSpace(A, B, C, D)

# Encontrando FT
FT = ct.ss2tf(EE)

display(FT)
display(EE)
print(EE)