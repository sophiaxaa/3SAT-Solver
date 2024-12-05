from dpll import random_kcnf, dpll
from exhaustive_search import exhaustive_search

if __name__ == "__main__":
    n_literals = 5
    n_conjuncts = 5

    # Generate a random CNF
    cnf = random_kcnf(n_literals, n_conjuncts)

    # Run DPLL
    print("\nRunning DPLL:")
    sat, assignments = dpll(cnf)
    print("DPLL Result:", sat, assignments)

    # Run Exhaustive Search
    print("\nRunning Exhaustive Search:")
    literals = [chr(i) for i in range(65, 65 + n_literals)]
    sat, assignments = exhaustive_search(cnf, literals)
    print("Exhaustive Search Result:", sat, assignments)
