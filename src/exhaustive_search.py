from itertools import product

def exhaustive_search(cnf, literals):
    # generate all truth assignments 
    for assignment in product([False, True], repeat=len(literals)):
        assignment_map = dict(zip(literals, assignment))
        if is_satisfiable(cnf, assignment_map):
            return True, assignment_map
    return False, None

def is_satisfiable(cnf, assignment_map):
    for clause in cnf:
        if not any(assignment_map.get(lit, not val) == val for lit, val in clause):
            return False
    return True
