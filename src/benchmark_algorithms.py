import time
import matplotlib.pyplot as plt
import csv
from dpll import random_kcnf, dpll
from exhaustive_search import exhaustive_search

def conduct_experiments(n_values, k_values, repetitions=2):
    results = []

    for n in n_values:
        print(f"Running experiments for n={n}...")
        literals = [chr(i) for i in range(65, 65 + n)]
        for k in k_values:
            m = int(k * n)  # Number of clauses
            print(f"  Testing ratio k={k} (m={m})...")
            dpll_times, exhaustive_times, match_count, total_count = [], [], 0, 0

            for i in range(repetitions):
                print(f"    Repetition {i + 1}/{repetitions}...")
                cnf = random_kcnf(n, m)

                # dpll tests
                start = time.time()
                sat_dpll, _ = dpll(cnf)
                dpll_time = time.time() - start
                dpll_times.append(dpll_time)

                # exhaustive search tests
                start = time.time()
                sat_exhaustive, _ = exhaustive_search(cnf, literals)
                exhaustive_time = time.time() - start
                exhaustive_times.append(exhaustive_time)

                # compare
                match = sat_dpll == sat_exhaustive
                if match:
                    match_count += 1

                total_count += 1

                # summary
                results.append({
                    "n": n,
                    "k": k,
                    "m": m,
                    "sat": sat_dpll,
                    "dpll_time": dpll_time,
                    "exhaustive_time": exhaustive_time,
                    "match": match
                })

            print(f"    Average DPLL Time: {sum(dpll_times) / repetitions:.6f}s")
            print(f"    Average Exhaustive Time: {sum(exhaustive_times) / repetitions:.6f}s")
            print(f"    Match Rate: {match_count / total_count:.2%}")

    return results

def save_results_to_csv(results, filename="experiment_results.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["n", "k", "m", "SAT", "DPLL Time", "Exhaustive Time", "Match"])
        for result in results:
            writer.writerow([
                result["n"], result["k"], result["m"], result["sat"],
                f"{result['dpll_time']:.6f}", f"{result['exhaustive_time']:.6f}", result["match"]
            ])
    print(f"Results saved to {filename}")

def plot_results(results):
    n_values = sorted(set([r['n'] for r in results]))
    for n in n_values:
        subset = [r for r in results if r['n'] == n]
        k_values = sorted(set([r['k'] for r in subset]))
        satisfiability_rates = [
            sum(1 for r in subset if r['k'] == k and r['sat']) / len([r for r in subset if r['k'] == k])
            for k in k_values
        ]

        plt.plot(k_values, satisfiability_rates, label=f"n={n}")

    plt.axvline(4.26, color='red', linestyle='--', label="Critical Ratio (4.26)")
    plt.xlabel("Clause-to-Variable Ratio (k)")
    plt.ylabel("Satisfiability Rate")
    plt.title("3SAT Phase Transition - Satisfiability Trends")
    plt.legend()
    plt.annotate("More SAT formulas", xy=(3.5, 0.9), xytext=(3.0, 0.8),
                 arrowprops=dict(facecolor='green', shrink=0.05))
    plt.annotate("Fewer SAT formulas", xy=(4.5, 0.3), xytext=(5.0, 0.5),
                 arrowprops=dict(facecolor='blue', shrink=0.05))
    plt.show(block=False)
    plt.pause(30)  # time for graph to display
    plt.close()

if __name__ == "__main__":
    # define ranges for n and k
    n_values = [10, 15]  # smaller n for faster execution 
    k_values = [3.0, 4.0, 4.26, 5.0]
    repetitions = 2 

    # experiments
    print("Starting experiments...")
    results = conduct_experiments(n_values, k_values, repetitions=repetitions)

    
    save_results_to_csv(results)

    # graph
    plot_results(results)
    print("All experiments completed.")

