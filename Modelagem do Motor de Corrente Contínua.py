import numpy as np
import matplotlib.pyplot as plt

# ------------------ Parâmetros do motor (exemplo) ------------------
p = {
    "Ra": 1,        # resistência de armadura [ohm]
    "La": 1,       # indutância de armadura [H]
    "J":  1,       # inércia [kg.m^2]
    "B":  1,       # atrito viscoso [N.m.s]
    "kt": 0.8,        # constante de torque [N.m/A]  (phi * k)
    "ke": 0.8,        # constante de FEM [V.s/rad]   (phi * k)
}

# --------------- Definição das entradas (exemplos) -----------------
# Você pode alterar livremente estas funções para criar cenários.
def Va(t):
    # Cenário demonstrativo:
    if t < 10:   return 0      # 0–0.5s: parado (0 V)
    if t < 20:   return 500.0  # 0.5–2.5s: partida/ aceleração (300 V)
    if t < 30:   return 200.0  # 2.5–3.5s: afundamento de tensão (200 V)
    if t < 40:   return 300.0  # 3.5–4.5s: volta nominal (300 V)
    if t < 50:   return -80.0  # 4.5–5.5s: frenagem por "plugging" (tensão invertida -80 V)
    if t < 60:   return 0.0    # 5.5–6.0s: parada (0 V)
    if t < 70:   return -300.0 # 6.0–7.5s: inversão de rotação (−300 V)
    return 0.0                 # 7.5–8.0s: zero (parada)

def TL(t):
    # torque de carga (constante aqui, mas pode ser função do tempo/ω)
    return 2.0  # [N.m]

def Ra_eff(t):
    # resistência efetiva de armadura (permite simular frenagem dinâmica adicionando resistor)
    # Aqui mantemos constante, mas você pode, p.ex., aumentar Ra em um intervalo.
    return p["Ra"]

# --------------------- Simulador (Euler explícito) -----------------
def sim_dc_se(Va_fun, TL_fun, Ra_fun, params, t_end=100.0, dt=1e-4, ia0=0.0, w0=0.0):
    Ra, La, J, B, kt, ke = params["Ra"], params["La"], params["J"], params["B"], params["kt"], params["ke"]
    n = int(t_end/dt)+1
    t  = np.linspace(0, t_end, n)
    ia = np.zeros(n); ia[0] = ia0
    w  = np.zeros(n);  w[0]  = w0
    Tm = np.zeros(n); Va_v  = np.zeros(n); TL_v = np.zeros(n)

    for k in range(n-1):
        tk = t[k]
        Ra_k = Ra_fun(tk)
        Va_k = Va_fun(tk)
        TL_k = TL_fun(tk)

        # Equações do motor CC (excitação independente, fluxo constante)
        # La*dia/dt = Va - Ra*ia - ke*w
        dia = (Va_k - Ra_k*ia[k] - ke*w[k]) / La
        # J*dω/dt  = kt*ia - B*w - TL
        dw  = (kt*ia[k] - B*w[k] - TL_k) / J

        # Integração (Euler)
        ia[k+1] = ia[k] + dt*dia
        w[k+1]  = w[k]  + dt*dw

        # Guardar sinais auxiliares
        Va_v[k] = Va_k
        TL_v[k] = TL_k
        Tm[k]   = kt*ia[k]

    Va_v[-1] = Va_fun(t[-1])
    TL_v[-1] = TL_fun(t[-1])
    Tm[-1]   = kt*ia[-1]
    return t, ia, w, Tm, Va_v, TL_v

# ------------------------- Rodar e plotar --------------------------
t, ia, w, Tm, Va_v, TL_v = sim_dc_se(Va, TL, Ra_eff, p, t_end=100.0, dt=2e-4)

# Plots rápidos (remova se quiser ainda mais minimalista)
# Plots mais largos e com grades
plt.figure(figsize=(12,4));
plt.plot(t, Va_v);
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.xlabel('t [s]');
plt.ylabel('Va [V]');
plt.title('Tensão de armadura')

plt.figure(figsize=(12,4));
plt.plot(t, ia);
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.xlabel('t [s]');
plt.ylabel('ia [A]');
plt.title('Corrente de armadura')

plt.figure(figsize=(12,4));
plt.plot(t, w);
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.xlabel('t [s]');
plt.ylabel('ω [rad/s]');
plt.title('Velocidade')

plt.figure(figsize=(12,4));
plt.plot(t, Tm);
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.xlabel('t [s]');
plt.ylabel('T_m [N.m]');
plt.title('Torque eletromagnético')

plt.tight_layout(); plt.show()