''' Encontrar Zeros, Polos e Ganho dado Função de Transferencia '''

import control as ctrl
import scipy.signal as signal

# Definindo denominador e numerador:
num = [10, 10]
den = [1, 8, 15]

# Definindo FT
G = ctrl.TransferFunction(num, den)
print(G)

# Encontrando Zeros, Polos e Ganho
zeros, polos, ganho = signal.tf2zpk(num, den)

print("Os zeros são:", zeros)
print("Os polos são:", polos)
print("O ganho é:", ganho)
