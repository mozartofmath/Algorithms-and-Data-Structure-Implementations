from Complex import Complex
from State import State
class QuantumGate:
    def __init__(self,name,matrix):
        self.name = name
        self.matrix = matrix
    def tensor(self, othergate):
        resulting_matrix = []
        for i in range(len(self.matrix) * len(othergate.matrix)):
            resulting_matrix.append([])
            for j in range(len(self.matrix) * len(othergate.matrix)):
                resulting_matrix[i].append(Complex(0,0))

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                for k in range(len(othergate.matrix)):
                    for l in range(len(othergate.matrix)):
                        resulting_matrix[i*len(othergate.matrix) + k][j*len(othergate.matrix) + l] = self.matrix[i][j].multiply(othergate.matrix[k][l])
                        
        return QuantumGate("",resulting_matrix)
    def dot(self, state):
        result = []
        for i in range(len(self.matrix)):
            temp = Complex(0,0)
            for j in range(len(self.matrix)):
                temp = temp.add(self.matrix[i][j].multiply(state.state_vector[j]))
                #temp.print()
            result.append(temp)
        return State(result)
    def hermitian_conjugate(self):
        return QuantumGate("",[[self.matrix[0][0].conjugate(), self.matrix[1][0].conjugate()],
                               [self.matrix[0][1].conjugate(), self.matrix[1][1].conjugate()]])

'''
def main():
    I = QuantumGate([[Complex(1,0),Complex(0,0)],
                    [Complex(0,0),Complex(1,0)]])
    X = QuantumGate([[Complex(0,0),Complex(1,0)],
                    [Complex(1,0),Complex(0,0)]])
    R = I.tensor(X).dot(State([Complex(0,0),Complex(1,0),Complex(0,0),Complex(0,0)]))
    R[0].print()
    R[1].print()
    R[2].print()
    R[3].print()
    for i in range(len(R)):
        for j in range(len(R)):
            R[i][j].print()
            print("", end = ",")
        print()
main()
'''




























