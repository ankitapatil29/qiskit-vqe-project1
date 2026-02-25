from qiskit import Aer
from qiskit.algorithms import VQE
from qiskit.algorithms.optimizers import SLSQP
from qiskit.circuit.library import TwoLocal
from qiskit.opflow import Z, I
from qiskit.utils import QuantumInstance

# Simple Hamiltonian for demonstration
hamiltonian = (Z ^ I) + (I ^ Z)

# Ansatz
ansatz = TwoLocal(2, ['ry', 'rz'], 'cz', reps=2)

# Optimizer
optimizer = SLSQP(maxiter=100)

# Backend
backend = Aer.get_backend('statevector_simulator')
qi = QuantumInstance(backend)

# VQE
vqe = VQE(ansatz, optimizer=optimizer, quantum_instance=qi)
result = vqe.compute_minimum_eigenvalue(hamiltonian)

print("Ground state energy:", result.eigenvalue.real)