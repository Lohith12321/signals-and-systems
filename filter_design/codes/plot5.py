import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, exp, I

# Define symbolic variables
s, s_L, z, omega = symbols('s s_L z omega')

# Given transfer function
H_s_L = 0.3125 / (s_L**4 + 1.1068*s_L**3 + 1.61245*s_L**2 + 0.91397*s_L + 0.33656)

Omega_0_val = 0.4916700645054545
B_val = 0.09772701432990072


s_L_expr = (s**2 + Omega_0_val**2) / (B_val * s)
H_s = H_s_L.subs(s_L, s_L_expr)

# Substitute s expression
s_expr = (1 - z**(-1)) / (1 + z**(-1))
H_s = H_s.subs(s, s_expr)

# Define the expression for z
z_expr = exp(1j * omega)

# Substitute z expression
H_z = H_s.subs(z, z_expr)


omega_values = np.linspace(-np.pi/2, np.pi/2, 1000)  
H_values = [np.abs(H_z.evalf(subs={omega: om_val})) for om_val in omega_values]

# Plot
plt.plot(omega_values/np.pi, H_values)
plt.xlabel(r'$\omega/\pi$')
plt.ylabel(r'$|H_{d,BP}(\omega)|$')
plt.title("Digital Band Pass Filter")
plt.grid(True)
plt.savefig("plot5.png")