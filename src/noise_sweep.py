import numpy as np
import matplotlib.pyplot as plt
import os

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, state_fidelity
from qiskit_aer.noise import NoiseModel, depolarizing_error
from qiskit_aer import AerSimulator

# ------------------------
# Create Bell State Circuit
# ------------------------

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Ideal state
ideal_state = Statevector.from_instruction(qc)

# ------------------------
# Noise sweep
# ------------------------

noise_levels = np.linspace(0, 0.2, 10)
fidelities = []

for p in noise_levels:
    # Create noise model
    noise_model = NoiseModel()
    error1 = depolarizing_error(p, 1)
    error2 = depolarizing_error(p, 2)

    noise_model.add_all_qubit_quantum_error(error1, ['h'])
    noise_model.add_all_qubit_quantum_error(error2, ['cx'])

    # Simulator
    simulator = AerSimulator(noise_model=noise_model)

    # Run circuit
    qc_save = qc.copy()
    qc_save.save_statevector()

    result = simulator.run(qc_save).result()
    noisy_state = result.get_statevector()

    # Fidelity
    fidelity = state_fidelity(ideal_state, noisy_state)
    fidelities.append(fidelity)

# ------------------------
# Save Plot
# ------------------------

project_root = os.path.join(os.path.dirname(__file__), "..")
results_dir = os.path.join(project_root, "results")
os.makedirs(results_dir, exist_ok=True)

output_path = os.path.join(results_dir, "fidelity_vs_noise.png")

plt.plot(noise_levels, fidelities)
plt.xlabel("Depolarizing noise probability")
plt.ylabel("State Fidelity")
plt.title("Bell State Fidelity vs Noise")
plt.savefig(output_path)
plt.show()

print("Plot saved at:", output_path)