""" PC3.4 Dorf
a) Usando a função tf, determine a função de transferência Y(s)/U(s).
b) Represente graficamente a resposta do sistema para a condição inicial x(0) = [0 –1 1]^T para 0 ≤ t ≤ 10.
c) Calcule a matriz de transição de estado usando a função expm e determine x(t) em t = 10 para a condição inicial 
dada na parte (b). Compare o resultado com a resposta do sistema obtida na parte (b).
"""
import control as ctrl
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

# Resolução letra (a)

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

print(f'(a)\n{G}')

# Resolução letra (b)

# Definindo x(0)
x0 = np.array([0, -1, 1])

# Dado que 0 ≤ t ≤ 10
t = np.linspace(0, 10, 500)

# Calculando a resposta inicial (initial response)
resposta_t, resposta_y, resposta_x = ctrl.initial_response(sist_ss, t, x0, return_x=True)

# Plotando gráfico da resposta inicial
plt.figure()
plt.plot(resposta_t, resposta_x[0], label='$x_1(t)$')
plt.plot(resposta_t, resposta_x[1], label='$x_2(t)$')
plt.plot(resposta_t, resposta_x[2], label='$x_3(t)$')
plt.xlabel('Tempo (s)')
plt.ylabel('$x(t)$')
plt.title('(b) Resposta do Sistema para a condição inicial $x(0) = [0 –1 1]^T$')
plt.legend()
plt.grid()
plt.show()

# Calculando a matriz de transição de estados (phi) para t = 10
phi_t10 = expm(A*t[-1])

# Calculando x(t) para t = 10
x_t10 = np.dot(phi_t10,x0)

# conclusão (c)
print(f'(c) \nMatriz de transição de estados: \n{phi_t10}')
print(f'Condição inicial para t = 0 \n{x0}')
print(f'Condição inicial para t = 10 \n{x_t10}')