from QuantumComputer import QuantumComputer
from QuantumGate import QuantumGate
from Complex import *
from State import State

rX = QuantumGate("rx",[[Complex(0.5,0.5), Complex(0.5,-0.5)],
                        [Complex(0.5,-0.5), Complex(0.5,0.5)]])

computer = QuantumComputer(3) 
computer.gatearray = [
                      [computer.universal_gate_set["I"],computer.universal_gate_set["I"],computer.universal_gate_set["P"],computer.universal_gate_set["I"],computer.universal_gate_set["P"],computer.universal_gate_set["P"] ],
                      [computer.universal_gate_set["X"],computer.universal_gate_set["P"],computer.universal_gate_set["X"],computer.universal_gate_set["P"],computer.universal_gate_set["X"],computer.universal_gate_set["I"] ],
                      [computer.universal_gate_set["X"],rX                              ,computer.universal_gate_set["I"],rX.hermitian_conjugate()        ,computer.universal_gate_set["I"],rX                               ]
                     ]
computer.compute()
computer.display_current_state()
