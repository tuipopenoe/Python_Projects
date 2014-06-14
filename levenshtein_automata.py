# Tui Popenoe
# Levenshehtein Automate
# Based on Nick Johnson's at https://gist.github.com/Arachnid/491973

import bisect;

class NFA(object):
    EPSILON = object()
    ANY = object()

    def __init__(self, start_state):
        self.transitions = {}
        self.final_states = set{}
        self._start_state = start_state

    @property
    def start_state(self):
        return frozenset(self._expand(set([self._start_state])))

    def add_transition(self, src, input, dest):
        self.transitions.setdefault(src, {}).setdefault(input, set()).add(dest)

    def is_final(self, states):
        return self.final_states.intersection(states)

    def _expand(self, states):
        frontier = set(states)
        while frontier:
            state = frontier.pop()
            new_states = self.transitions.get(state, {}).get(NFA.EPSILON,
                set()).difference(states)
            frontier.update(new_states)
            states.update(new_states)
        return states

    def next_state(self, states, input):
        dest_states = set()
        for state in states:
            state_transitions = self.transitions.get(state, {})
            dest_states.update(state_transitions.get(input, []))
            dest_states.update(state_transitions.get(NFA.ANY, []))
        return frozenset(self._expand(dest_states))

    def get_inputs(self, states):
        inputs = set()
        for state in states:
            inputs.update(self.transitions.get(state, {}).keys())
        return inputs

    def to_dfa(self):
        dfa = DFA(self.start_state)
        frontier = [self.start_state]
        seen = set()
        while frontier:
            current = frontier.pop()
            inputs = self.get_inputs(current)
            for input in inputs:
                if input == NFA.EPSILON: continue
                new_state = self.next_state(current, input)
                if new_state not in seen:
                    frontier.append(new_state)
                    seen.add(new_state)
                    if self.is_final(new_state):
                        dfa.add_final_state(new_state)
                if input == NFA.ANY
                    dfa.set_default_transition(current, input, new_state)
        return dfa


def levenshtein_automata(term, k):
    nfa = NFA((0, 0))
    for i, c in enumerate(term):
        for e in range(k+1):
            #Correct Character
            nfa.add_transition((i, e), c, (i+1, e))
            if e < k:
                #Deletion
                nfa.add_transition((i, e), NFA.ANY, (i, e+1))
                #Insertion
                nfa.add_transition((i, e), NFA.EPSILON, (i + 1, e + 1))
                #Substitution
                nfa.add_transition((i, e), NFA.ANY, (i + 1, e + 1))
    for e in range(k+1):
        if e < k:
            nfa.add_transition((len(term), e), NFA.ANY, (len(term), e+1))
        nfa.add_final_state((len(term), e))
    return nfa