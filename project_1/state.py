import math
import copy

class Moves:
    Up, Down, Left, Right = range(4)

class BoardState:
    def __init__(self, array):
        self.size = int(math.sqrt(len(array)))
        self.state = array
        self.zero_pos = array.index(0)

    def IsGoalState(self):
        val = 0
        for element in self.state:
            if element != val:
                return False
            val+=1
        return True

    def getPossibleMoves(self):
        possible = []
        r = int(self.zero_pos / self.size)
        c = self.zero_pos % self.size

        if r != 0:
            possible.append(Moves.Up)
        if c != 0:
            possible.append(Moves.Left)
        if r != self.size - 1:
            possible.append(Moves.Down)
        if c != self.size - 1:
            possible.append(Moves.Right)
        return possible

    def getSuccessorStates(self):
        states = []
        moves = self.getPossibleMoves()
        r = int(self.zero_pos / self.size)
        c = self.zero_pos % self.size

        for move in moves:
            # Simple assignment only does a shallow copy of the array so
            # using a deepcopy
            temp_state = copy.deepcopy(self.state)
            if move == Moves.Up:
                temp = temp_state[self.zero_pos - self.size]
                temp_state[self.zero_pos] = temp
                temp_state[self.zero_pos - self.size] = 0
            elif move == Moves.Down:
                temp = temp_state[self.zero_pos + self.size]
                temp_state[self.zero_pos] = temp
                temp_state[self.zero_pos + self.size] = 0

            elif move == Moves.Left:
                temp = temp_state[self.zero_pos - 1]
                temp_state[self.zero_pos] = temp
                temp_state[self.zero_pos - 1] = 0

            elif move == Moves.Right:
                temp = temp_state[self.zero_pos + 1]
                temp_state[self.zero_pos] = temp
                temp_state[self.zero_pos + 1] = 0

            states.append((BoardState(temp_state), move))
        return states

    # Added Printing feature for debugging purposes
    def print_state(self):
        print self.state
