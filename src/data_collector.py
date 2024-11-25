import random
from src.formula_gen import generate_3cnf_formula

def generate_and_save_formulas(n_values, ratios, output_file):
    """
    Generate 3CNF formulas for multiple n and m/n values and save to a file.
    
    Args:
        n_values (list): List of variable counts (n).
        ratios (list): List of m/n ratios to test.
        output_file (str): Path to save the output formulas.
    """
    with open(output_file, "w") as f:
        f.write("n,m,clauses\n")
        
        for n in n_values:
            for ratio in ratios:
                m = int(n * ratio)
                try:
                    formula = generate_3cnf_formula(n, m)
                    formula_str = "; ".join([f"({clause[0]} ∨ {clause[1]} ∨ {clause[2]})" for clause in formula])
                    f.write(f"{n},{m},{formula_str}\n")
                    print(f"Generated formula for n={n}, m={m}")
                except ValueError as e:
                    print(f"Skipping n={n}, m={m}: {e}")

if __name__ == "__main__":
    # Example inputs
    n_values = [5, 10, 20]  # List of n values to test
    ratios = [2, 4.26, 6]   # Critical m/n ratios
    output_file = "3cnf_formulas.csv"
    
    generate_and_save_formulas(n_values, ratios, output_file)
    print(f"Formulas saved to {output_file}")

