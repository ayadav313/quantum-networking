# %%
from qiskit import *

# %%
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(3, 'q')
creg_xc = ClassicalRegister(1, 'xc')
creg_zc = ClassicalRegister(1, 'zc')
creg_c0 = ClassicalRegister(1, 'c0')
circuit = QuantumCircuit(qreg_q, creg_xc, creg_zc, creg_c0)

circuit.h(qreg_q[1])
circuit.cx(qreg_q[1], qreg_q[2])
circuit.cx(qreg_q[0], qreg_q[2])
circuit.h(qreg_q[0])
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2])
circuit.measure(qreg_q[0], creg_zc[0])
circuit.measure(qreg_q[1], creg_xc[0])
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2])
circuit.x(qreg_q[2]).c_if(creg_xc, 1)  # Corrected line
circuit.z(qreg_q[2])
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2])
circuit.measure(qreg_q[2], creg_c0[0]) 
circuit.draw('mpl')


# %%
qreg_q = QuantumRegister (3,'g')
creg_xc = ClassicalRegister (1, 'XC')
creg_zc = ClassicalRegister(1, 'z')
creg_co = ClassicalRegister(1, 'cO')
circuit = QuantumCircuit (qreg_q, creg_xc, creg_zc, creg_c0)
circuit.h(qreg_q[1])
circuit.cx(qreg_q[1], qreg_q [2])
circuit.cx(qreg_q[0], qreg_q[1]) 
circuit.h(qreg_q[0])
circuit.barrier (qreg_q[0], qreg_q[1], qreg_q[2]) 
circuit.measure(qreg_q[0], creg_zc [0]) 
circuit.measure (qreg_q [1], creg_xc[0]) 
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2]) 
circuit.x(qreg_q[2]).c_if(creg_xc, 1)
circuit.z(qreg_q[2])
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2]) 
circuit.measure(qreg_q[2], creg_c0[0]) 
circuit.draw('mpl')

# %%
from qiskit.tools.visualization import plot_histogram
simulator = Aer.get_backend("qasm_simulator")
result = execute(circuit, backend=simulator, shots=1000).result()
counts = result.get_counts()
plot_histogram(counts)


