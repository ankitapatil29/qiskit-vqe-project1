import numpy as np
import matplotlib.pyplot as plt
import os
from itertools import product

# ------------------------
# Pauli matrices
# ------------------------

I = np.array([[1, 0], [0, 1]])
X = np.array([[0, 1], [1, 0]])
Z = np.array([[1, 0], [0, -1]])

# ------------------------
# Helper: Kronecker product for operator on site
# ------------------------

def operator_on_site(op, site, N):
    ops = []
    for i in range(N):
        ops.append(op if i == site else I)
    result = ops[0]
    for o in ops[1:]:
        result = np.kron(result, o)
    return result

# ------------------------
# Build Hamiltonian
# ------------------------

def transverse_ising_hamiltonian(N, J, h):
    H = np.zeros((2**N, 2**N))

    # ZZ interaction
    for i in range(N - 1):
        H -= J * operator_on_site(Z, i, N) @ operator_on_site(Z, i + 1, N)

    # Transverse field
    for i in range(N):
        H -= h * operator_on_site(X, i, N)

    return H

# ------------------------
# Parameters
# ------------------------

N = 3          # number of spins
J = 1.0
h_values = np.linspace(0, 2, 20)

ground_energies = []

# ------------------------
# Parameter sweep
# ------------------------

for h in h_values:
    H = transverse_ising_hamiltonian(N, J, h)
    eigenvalues = np.linalg.eigvalsh(H)
    ground_energies.append(eigenvalues[0])

# ------------------------
# Save plot
# ------------------------

project_root = os.path.dirname(__file__)
plots_dir = os.path.join(project_root, "plots")
os.makedirs(plots_dir, exist_ok=True)

plt.plot(h_values, ground_energies)
plt.xlabel("Transverse field h")
plt.ylabel("Ground state energy")
plt.title(f"{N}-spin Transverse Ising Model")
plt.savefig(os.path.join(plots_dir, "energy_vs_field.png"))
plt.show()

print("Plot saved in ising_model/plots/")