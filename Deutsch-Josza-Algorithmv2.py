from QuantumComputer import QuantumComputer
from QuantumGate import QuantumGate
from Complex import *
from State import State
from time import time

t1 = time()
rX = QuantumGate("rx",[[Complex(0.5,0.5), Complex(0.5,-0.5)],
                        [Complex(0.5,-0.5), Complex(0.5,0.5)]])

computer = QuantumComputer(6) 

I = computer.universal_gate_set["I"]
X = computer.universal_gate_set["X"]
Y = computer.universal_gate_set["Y"]
Z = computer.universal_gate_set["Z"]
H = computer.universal_gate_set["H"]
P = computer.universal_gate_set["P"]

computer.gatearray = [
                      [I,I,P,I],
                      [I,H,I,H],
                      [I,H,I,H],
                      [I,H,I,H],
                      [I,H,I,H],
                      [X,H,X,H],
                     ]
computer.compute()
print(time() - t1)
computer.display_current_state()
