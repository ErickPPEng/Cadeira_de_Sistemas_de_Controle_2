"""Resolução da Questão PC2.4 do Dorf"""

import control as ct
import numpy as np
import matplotlib.pyplot as plt

m = 10
k = 1
b = 0.5

# Função de Transferencia do Sistama Massa-mola-amortecedor

num = [1]
den = [m, b, k]
G = ct.TransferFunction(num, den)

# Definindo Tempo

tempo = np.linspace (0, 200, 500)

# Resposta ao Degrau Unitário

tempo_degrau, resposta_degrau = ct.step_response(G, tempo)

# Plotando a resposta ao degrau

plt.figure()
plt.plot(tempo_degrau, resposta_degrau, label='Resposta ao Degrau Unitário')
plt.title('Resposta ao Degrau Unitário do Sistema Massa-Mola-Amortecedor')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()
plt.show()