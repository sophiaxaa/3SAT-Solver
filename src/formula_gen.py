import random

def generate_3cnf_formula(n,m):
    """
        Generate a random 3CNF formula 

        Args:
        n (int): number of variables
        m (int): number of clauses 

        Returns:
            list of tuples, with each tuple representing a clause
    """

    variables = list(range(1, n+1))
    clause_pool = []

    #generate all possible three literal clauses

    for i in variables:
        for j in variables:
            for k in variables: 
                if len({i, j, k}) == 3:
                    for signs in [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), 
                                  (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]:
                        clause_pool.append((i * signs[0], j * signs[1], k * signs[2]))

    #randomly select m clauses 
    if m > len(clause_pool):
         raise ValueError("requested more clauses than possible combinations.")
    formula = random.sample(clause_pool, m)

    return formula

if __name__ == "__main__":
    #test usage
    n = 5
    m = 10
    formula = generate_3cnf_formula(n,m)
    print("generated 3CNF formula: ")
    for clause in formula:
        print(f"({clause[0]} ∨ {clause[1]} ∨ {clause[2]})")
