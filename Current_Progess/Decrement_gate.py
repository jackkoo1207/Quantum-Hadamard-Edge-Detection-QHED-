from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import XGate, CXGate
import numpy as np
def white_dot_toffoli(qc,n,arr):
    """
    Alternative implementation using controlled gates with ctrl_state parameter
    (Available in newer versions of Qiskit)
    """

    # Create custom controlled gates with specific control states
    # ctrl_state='00' means gate activates when both controls are |0]
    white_dot_gate = XGate().control(n, ctrl_state='0'*n)
    qc.append(white_dot_gate,list(arr))
def decrement_gate(qc, N):
    qc.barrier()
    for i in range(N-1):
        white_dot_toffoli(qc,N-1-i,np.arange(N-i))
    qc.append(XGate(),[0])
    qc.barrier()