# Tui Popenoe
# Levenshehtein Automate
# Based on Nick Johnson's at https://gist.github.com/Arachnid/491973

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