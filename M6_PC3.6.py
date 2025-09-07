""" Resolução da questão PC3.6 do Dorf"""

import control as ctrl
import matplotlib.pyplot as plt

# Definindo a FT do controlador:
numc = [3]
denc = [1, 3]

Gc = ctrl.TransferFunction(numc, denc)

# Transformando em variaveis de estado
sist_ssc = ctrl.tf2ss(Gc)

# Resposta (a)
print('(a) Representação do controlador em espaços de estado:')
print(sist_ssc)

# Definindo a FT para o processo:
nump = [1]
denp = [1, 2, 5]

Gp = ctrl.TransferFunction(nump, denp)

# transformando em variaveis de estado
sist_ssp = ctrl.tf2ss(Gp)

# Resposta (b)
print('(b) Representação do processo em espaços de estado:')
print(f'A = \n{sist_ssp.A}')
print(f'B = \n{sist_ssp.B}')
print(f'C = \n{sist_ssp.C}')
print(f'D = \n{sist_ssp.D}')

# Multiplicando o controlador pelo processo
sist_serie = ctrl.series(Gp, Gc)

# Fazendo a relaimentação negativa
sist_realiment = ctrl.feedback(sist_serie)

# transformando em variaveis de estado
sist_sst = ctrl.tf2ss(sist_realiment)

# calculando o impulso
t, impulso = ctrl.impulse_response(sist_sst)

# Resposta (c)
plt.figure()
plt.plot(t, impulso)
plt.xlabel('$Tempo (s)$')
plt.ylabel('$Amplitude$')
plt.title('(c) Resposta do sistema em malha fechada ao impulso')
plt.grid()
plt.show()