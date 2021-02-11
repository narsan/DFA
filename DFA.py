class DFA:
    current_state = None

    def __init__(self, states, alphabet, transition_function, firstState, finalStates):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = firstState
        self.accept_states = finalStates
        self.current_state = firstState
        return

    # function that go to the next state

    def transition(self, input_value):
        if ((self.current_state, input_value) not in self.transition_function.keys()):
            self.current_state = None
            return
        self.current_state = self.transition_function[(self.current_state, input_value)]
        return
    # this function check if the state is one of the final states

    def if_final_state(self):
        return self.current_state in finalStates

    # using this function we can back to first state

    def start_over(self):
        self.current_state = self.start_state
        return
    # do the transition by getting the input

    def run_by_inp(self, input_list):
        self.start_over()
        for inp in input_list:
            self.transition(inp)
            continue
        return self.if_final_state()

    pass


#  this function defined to have the ability of adding into dictionary

class MyDictionary(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

# main


tf = MyDictionary()
# reading from file
try:
    f = open("DFA_Input_1.txt", "r")
except FileNotFoundError:
    print("Wrong file or file path")

inp1 = input()
alphabet = str(f.readline()).split()
states = str(f.readline()).split()
tmp = str(f.readline()).split()
firstState = tmp[0]
finalStates = str(f.readline()).split()
line = f.readlines()
n = line.__len__()

for i in range(n):
    temp = str(line[i]).split()
    tf.add((temp[0], temp[1]), temp[2])

d = DFA(states, alphabet, tf, firstState, finalStates)
inp_program = list(inp1)
print(d.run_by_inp(inp_program))
f.close()



