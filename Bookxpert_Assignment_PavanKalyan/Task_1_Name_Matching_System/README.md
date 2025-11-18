## Name Matching System – Task 1 (Bookxpert Assignment)
### Project Overview

The Name Matching System is a Python-based application that identifies the most similar names from a large dataset based on a user’s input.
It applies text preprocessing and fuzzy similarity matching to return:

####  Best Match

#### Top 10 Similar Names with Similarity Scores

This project is lightweight, runs fully locally, and is color-enhanced for a better terminal experience.

## Project Workflow / Steps
###  Data Preparation

A dataset of 30 name groups, each containing 5–6 similar or variant names, is stored directly inside preprocess.py.

* Total names: 160+ unique entries.

* Variants include:

* Spelling variations

* Nicknames

* Surname-based variations

* Phonetic variations

###  Preprocessing (preprocess.py)
What this file does:

✔ Stores the entire name dataset
✔ Cleans the names for uniformity
✔ Removes noise before similarity comparison

* Key steps in preprocessing:

* Convert names to lowercase

Remove:

* Extra spaces

* Characters like , . - _

* Normalize multi-word names

##### Functions inside this file:
* preprocess_name(name)

* Cleans a single name string.

* get_cleaned_names()

* Returns a list of all cleaned names — used by the similarity engine.

* No third-party libraries are required for preprocessing.

###  Similarity Matching (similarity.py)
What this file does:

✔ Loads cleaned names
✔ Uses RapidFuzz library to compute fuzzy similarity scores

✔ Provides:

* Best match

* Top N matches

#### Why Use Fuzzy Matching?

Fuzzy matching is used because users often enter names that may have spelling mistakes, variations, or multiple possible formats. Traditional exact matching fails in such cases, but fuzzy matching compares how similar two strings are rather than checking if they are identical. This ensures the system can still find the closest match even when the input is:

* Misspelled

* Partially typed

* Phonetically different

* Has spacing or casing variations

* Using fuzzy matching improves accuracy, flexibility, and provides a more human-like search experience.

##### Functions inside similarity.py:
* ✔ get_similarity_scores(input_name, limit=10)

* Returns a ranked list of similar names based on:

* WRatio algorithm

* Higher score = more similarity

* ✔ get_best_match(input_name)

* Returns the highest scoring name only.

Library Used:

* rapidfuzz → faster and more accurate than fuzzywuzzy

###  Main Program (main.py)
Responsibilities of this file:

*  ✔ Handles user interaction
✔ Displays color-coded results
✔ Runs the application in a loop
✔ Asks the user to search again or exit

Color-coded Output:

* Yellow → Headings

* Cyan → Dividers

* Red → Errors

* Green → Success messages

* Magenta → Best match

Flow:

* Show system header

* Ask user for a name

* Fetch best match + top matches

* Display results

* Ask user whether to continue or exit

###  Project Structure
```
Task_1_Name_Matching_System/
│
├── preprocess.py       # Dataset + cleaning logic
├── similarity.py       # Similarity engine using RapidFuzz
├── main.py             # Main application (UI + loop)
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```
###  Requirements
Install Python Packages:
```
pip install colorama rapidfuzz
```

Or:

```
pip install -r requirements.txt
```

Requirements File Contents:
```
rapidfuzz
colorama 
```

###  How to Run the Project

Step 1: Navigate to the folder
```
cd Task_1_Name_Matching_System
```
Step 2 (Optional): Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux
```
Step 3: Install dependencies
```
pip install -r requirements.txt
```
Step 4: Run the application
```
python main.py
```
###  Sample Output
```
========================================
             NAME MATCHING SYSTEM
========================================

Enter a name to search: Geetha

#### BEST MATCH
geeta → 96%

#### TOP SIMILAR MATCHES
1. geeta → 96%
2. geetha → 92%
3. gita → 88%
4. geetanjali → 80%
...

```

###  Technologies Used

Python 3

RapidFuzz – Fuzzy similarity scoring

Colorama – Color output in console


### Conclusion

This project demonstrates:

* Effective text preprocessing

* Fuzzy matching techniques

* Modular Python project design

* Terminal-based interactive UI

This completes Task 1 of the Bookxpert AI Developer Assignment.