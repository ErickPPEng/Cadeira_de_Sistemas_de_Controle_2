""" Tendo Zeros, Polos e Ganho plote o degrau """

import control as ctrl
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

# Dados os ZPK:
zeros = [-1]
polos = [-5, -3]
ganho = [10]

num, den = signal.zpk2tf(zeros, polos, ganho)

# Definindo a FT
G = ctrl.TransferFunction(num, den)
print(f"Função de transferencia: {G}")

# Vetor tempo de 0 a 10 segundos (por 500 pontos)
tempo = np.linspace(0, 10, 500)
tempo_d, resposta_d = ctrl.step_response(G, tempo)

# Plot do gráfico da resposta no degrau
plt.figure(figsize=(8, 4))
plt.plot(tempo_d, resposta_d, label='Resposta ao Degrau')
plt.title('Resposta no tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()
