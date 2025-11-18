# main.py
"""
Main execution file for the Name Matching System.

This script:
1. Takes user input
2. Finds the most similar names using similarity.py
3. Displays best match + ranked list of matches
"""

# Imports
from similarity import get_similarity_scores, get_best_match
from colorama import Fore, Style, init

# Initialize colors for Windows
init(autoreset=True)

def run_name_matching():
    print(Fore.CYAN + "========================================")
    print(Fore.YELLOW + "       NAME MATCHING SYSTEM")
    print(Fore.CYAN + "========================================")

    while True:
        # User input
        name = input(Fore.GREEN + "\nEnter a name to search: ").strip()

        if not name:
            print(Fore.RED + "\n Error: Please enter a valid name.")
            continue

        # Best match
        best = get_best_match(name)
        if not best:
            print(Fore.RED + "\n No match found.")
            continue

        best_name, best_score, _ = best

        print(Fore.CYAN + "\n----------------------------------------")
        print(Fore.YELLOW + " BEST MATCH")
        print(Fore.CYAN + "----------------------------------------")
        print(Fore.MAGENTA + f"{best_name}  →  {best_score}%")

        # Top matches
        matches = get_similarity_scores(name, limit=10)

        print(Fore.CYAN + "\n----------------------------------------")
        print(Fore.YELLOW + " TOP SIMILAR MATCHES")
        print(Fore.CYAN + "----------------------------------------")

        for idx, (match, score, _) in enumerate(matches, start=1):
            print(Fore.WHITE + f"{idx}. {match:<20}  →  {score}%")

        print(Fore.CYAN + "\n========================================")
        print(Fore.GREEN + "         ✔ SEARCH COMPLETED")
        print(Fore.CYAN + "========================================")

        # Ask if they want to continue
        choice = input(Fore.BLUE + "\nDo you want to search another name? (yes/no): ").strip().lower()

        if choice not in ["yes", "y"]:
            print(Fore.YELLOW + "\n👋 Exiting the system. Goodbye!")
            break


if __name__ == "__main__":
    run_name_matching()
