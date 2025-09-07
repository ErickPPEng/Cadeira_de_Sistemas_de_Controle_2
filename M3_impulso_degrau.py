""" Plotando o Impulso e o Degrau juntos """

import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

# Definindo denominador e numerador:
num = [1, 3]
den = [1, 2, 3]

# Criando a FT
G = ctrl.TransferFunction(num, den)

# Definindo tempo da simulação
tempo = np.linspace(0, 10, 500)

# Resposta ao Degrau
degrau_t, degrau_r = ctrl.step_response(G, tempo)
# Resposta ao Impulso
impulso_t, impulso_r = ctrl.impulse_response(G, tempo)

# Plotando o gráfico

plt.figure(figsize=(10, 6))
plt.plot(degrau_t, degrau_r, label='Resposta ao Degrau')
plt.plot(impulso_t, impulso_r, label='Resposta ao impulso')
plt.title('Resposta no tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()
