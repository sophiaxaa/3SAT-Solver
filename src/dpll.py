import random
import time

def __select_literal(cnf):
    for c in cnf:
        for literal in c:
            return literal[0]

def dpll(cnf, assignments={}):
    if len(cnf) == 0:
        return True, assignments

    if any([len(c) == 0 for c in cnf]):
        return False, None

    l = __select_literal(cnf)

    new_cnf = [c for c in cnf if (l, True) not in c]
    new_cnf = [c.difference({(l, False)}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{l: True}})
    if sat:
        return sat, vals

    new_cnf = [c for c in cnf if (l, False) not in c]
    new_cnf = [c.difference({(l, True)}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{l: False}})
    if sat:
        return sat, vals

    return False, None

def random_kcnf(n_literals, n_conjuncts, k=3):
    literals = [chr(i) for i in range(65, 65 + n_literals)] 
    result = []
    for _ in range(n_conjuncts):
        conj = set()
        for _ in range(k):
            literal = random.choice(literals)
            conj.add((literal, bool(random.randint(0, 1))))  
        result.append(conj)
    return result

if __name__ == "__main__":

    n_literals = 5  # Example number of literals
    n_conjuncts = 5  # Example number of conjunctions

    # Generate a random CNF
    cnf = random_kcnf(n_literals, n_conjuncts)

    print("Random CNF:")
    for clause in cnf:
        print(clause)

    # Time DPLL execution
    start = time.time()
    sat, assignments = dpll(cnf)
    stop = time.time()

    print("\nDPLL Result:")
    print("Satisfiable:", sat)
    if sat:
        print("Assignments:", assignments)
    
    print(f"\nDPLL Execution Time: {stop - start:.6f} seconds")
