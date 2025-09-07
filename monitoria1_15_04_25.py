""" Monitoria
Encontrando FT, ZPK E EE do sistema"""

import control as ct
import scipy.signal as signal

# Criando a FT
num = [2, -20]
den = [2, -15, 7]

FT = ct.TransferFunction(num, den)
display(FT)

# Encontrando zeros, polos e ganhos
z, p, k = signal.tf2zpk(num, den)
print('zero = ', z)
print('polo = ', p)
print(f'ganho = {k}')

# Encontrando o espaço de estados
EE = ct.tf2ss(FT)
display(EE)
print(EE)