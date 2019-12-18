from QuantumGate import QuantumGate
from Complex import Complex
from State import State
class QuantumComputer:
    def __init__(self,num_of_qubits):
        self.num_of_qubits = num_of_qubits
        self.current_state = State(self.initialize())
        self.gatearray = []
        self.universal_gate_set = {"I":QuantumGate("I",[[Complex(1,0),Complex(0,0)],[Complex(0,0),Complex(1,0)]]),
                                   "X":QuantumGate("X",[[Complex(0,0),Complex(1,0)],[Complex(1,0),Complex(0,0)]]),
                                   "Y":QuantumGate("Y",[[Complex(0,0),Complex(0,-1)],[Complex(0,1),Complex(0,0)]]),
                                   "Z":QuantumGate("Z",[[Complex(1,0),Complex(0,0)],[Complex(0,0),Complex(-1,0)]]),
                                   "H":QuantumGate("H",[[Complex(1/((2)**(0.5)),0),Complex(1/((2)**(0.5)),0)],[Complex(1/((2)**(0.5)),0),Complex(-1/((2)**(0.5)),0)]]),
                                   "P":QuantumGate("P",[[Complex(0,0),Complex(0,0)],[Complex(0,0),Complex(1,0)]]),

                                   }
    def compute(self):
        control_qubit_index = 0
        for i in range(len(self.gatearray[0])):
            controlled_operation = False
            operator = self.gatearray[0][i]
            
            #=======================================
            if self.gatearray[0][i].name == "P":
                    controlled_operation = True
                    control_qubit_index = 0
            #=======================================
            for j in range(1,len(self.gatearray)):
                #=======================================
                if self.gatearray[j][i].name == "P":
                    controlled_operation = True
                    control_qubit_index = j
                #=======================================
                operator = operator.tensor(self.gatearray[j][i])
            if controlled_operation:
                self.controlled_R(operator, control_qubit_index)
            #mutiplication of operator and amplitude vector
            self.current_state = operator.dot(self.current_state)

    def controlled_R(self, operator, control_qubit_index):
        index_to_be_modified = 0
        for i in range(2**control_qubit_index):
            for j in range(2**(self.num_of_qubits - control_qubit_index - 1)):
                
                operator.matrix[index_to_be_modified][index_to_be_modified] = Complex(1,0)
                index_to_be_modified+=1
            index_to_be_modified = (i+1) * 2**(self.num_of_qubits - control_qubit_index)

    def initialize(self):
        initial_state = [Complex(1,0)]
        for i in range(2**(self.num_of_qubits) - 1):
            initial_state.append(Complex(0,0))
        return initial_state
            
    def measure(self):
        pass
    def measure(self,position):
        pass

    def display_current_state(self):
        res = Complex(0,0)
        for i in range(len(self.current_state.state_vector)):
            res = res.add(self.current_state.state_vector[i].multiply(self.current_state.state_vector[i].conjugate()))
            print("({amplitude}) |{standard_basis_state}>".format_map({'amplitude': self.current_state.state_vector[i].print(), 'standard_basis_state' : i}))
        print(res.real)
'''def main():
    computer = QuantumComputer(3)
    computer.gatearray = [[computer.universal_gate_set["I"]],[computer.universal_gate_set["P"]],[computer.universal_gate_set["X"]]]
    computer.compute()
    computer.display_current_state()
    computer.current_state.state_vector[0].print()
    computer.current_state.state_vector[1].print()
    computer.current_state.state_vector[2].print()
    computer.current_state.state_vector[3].print()
    computer.current_state.state_vector[4].print()
    computer.current_state.state_vector[5].print()
    computer.current_state.state_vector[6].print()
    computer.current_state.state_vector[7].print()
main()'''
    

















