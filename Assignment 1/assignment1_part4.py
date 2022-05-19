#Roman Melnik - 2693934
#CIS 490 - Professor Essa
#Assignment 1 - Part 4

from automata.fa.dfa import DFA

#3a, string ends with 'ab'
dfa = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q0'},
        'q1': {'a': 'q1', 'b': 'q2'},
        'q2': {'a': 'q1', 'b': 'q0'}
    },
    initial_state='q0',
    final_states={'q2'}
)

if dfa.accepts_input(input("Enter string for part 3a: ")):
    print("Part 3a: Accepted")
else:
    print("Part 3a: Rejected")

#3b, string starts and ends with 'b'
dfa = DFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q3', 'b': 'q1'},
        'q1': {'a': 'q1', 'b': 'q2'},
        'q2': {'a': 'q1', 'b': 'q2'},
        'q3': {'a': 'q3', 'b': 'q3'}
    },
    initial_state='q0',
    final_states={'q2'}
)

if dfa.accepts_input(input("Enter string for part 3b: ")):
    print("Part 3b: Accepted")
else:
    print("Part 3b: Rejected")

#3c, string has an odd number of both 'a' and 'b'
dfa = DFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q3'},
        'q1': {'a': 'q0', 'b': 'q2'},
        'q2': {'a': 'q3', 'b': 'q1'},
        'q3': {'a': 'q2', 'b': 'q0'}
        },
    initial_state='q0',
    final_states={'q2'}
)

if dfa.accepts_input(input("Enter string for part 3c: ")):
    print("Part 3c: Accepted")
else:
    print("Part 3c: Rejected")
