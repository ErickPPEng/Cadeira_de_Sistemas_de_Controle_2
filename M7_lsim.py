""" Demonstração de como utilizar o lsim """

import control.matlab as ctrl #lsim só funciona no control.matlab!!
import numpy as np

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

# Definindo entrada U, tempo e X0
u = 0
t = np.linspace(0, 10, 500)
x0 = np.array([[1],[0],[0]])

y_out, T_out, x_out = ctrl.lsim(sist_ss, u, t, x0)
