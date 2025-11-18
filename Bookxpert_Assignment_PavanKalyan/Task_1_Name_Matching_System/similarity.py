# similarity.py
"""
This module handles:
1. Loading cleaned names from preprocess.py
2. Calculating similarity scores using RapidFuzz
3. Returning best matches + ranked results
"""

# Imports
from rapidfuzz import process, fuzz
from preprocess import get_cleaned_names, preprocess_name


# Load cleaned names once (improves performance)
CLEANED_NAMES = get_cleaned_names()


# Similarity Function
def get_similarity_scores(input_name: str, limit: int = 10):
    """
    Takes a user-input name and returns a ranked list of similar names.

    Parameters:
    - input_name (str): The name entered by the user.
    - limit (int): Number of top matches to return.

    Returns:
    - List of tuples: (matched_name, similarity_score, index)
    """

    if not input_name or not isinstance(input_name, str):
        return []

    # Preprocess user input
    clean_input = preprocess_name(input_name)

    # Use RapidFuzz fuzzy matching
    results = process.extract(
        clean_input,
        CLEANED_NAMES,
        scorer=fuzz.WRatio,
        limit=limit
    )

    return results


# Best Match Function
def get_best_match(input_name: str):
    """
    Returns the single most similar name.

    Example return:
    ("geeta", 96)
    """
    results = get_similarity_scores(input_name, limit=1)
    return results[0] if results else None


# Debugging / Test Run
if __name__ == "__main__":
    print("🔍 Debug Test for similarity.py")
    test_name = "Geetha"
    print(f"\nInput: {test_name}")

    matches = get_similarity_scores(test_name)
    print("\nTop Matches:")
    for name, score, _ in matches:
        print(f"- {name} → {score}%")

    best = get_best_match(test_name)
    print("\nBest Match:", best)
