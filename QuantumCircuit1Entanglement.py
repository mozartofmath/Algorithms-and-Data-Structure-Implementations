from QuantumComputer import QuantumComputer
from QuantumGate import QuantumGate
from Complex import Complex
from State import State
computer = QuantumComputer(2)
computer.gatearray = [[computer.universal_gate_set["I"],computer.universal_gate_set["X"]],
                      [computer.universal_gate_set["H"],computer.universal_gate_set["P"]]]
computer.compute()
computer.display_current_state()
