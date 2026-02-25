# Variational Quantum Eigensolver (VQE) for Ground State Energy

## Overview
This project implements the Variational Quantum Eigensolver (VQE) using Qiskit to estimate the ground state energy of a simple quantum system. VQE is a hybrid quantum-classical algorithm widely used in quantum chemistry and near-term quantum computing research.

## Objectives
- Implement a hybrid quantum-classical workflow
- Design parameterized quantum circuits (ansatz)
- Use classical optimization to minimize energy
- Simulate quantum execution using Qiskit Aer

## Methodology
1. Define a Hamiltonian operator
2. Construct a parameterized ansatz circuit
3. Use SLSQP optimizer
4. Evaluate expectation values using a statevector simulator
5. Iteratively minimize energy

## Tools & Technologies
- Python
- Qiskit
- Qiskit Aer
- NumPy

## Project Structure
