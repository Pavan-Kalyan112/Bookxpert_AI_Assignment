# 30 groups × 5–6 names here

names_list = [
    "Geeta", "Geetha", "Gita", "Geetika", "Geetanjali", "Geetha Devi",
    "Ramesh", "Ramesh Kumar", "Ramesh Babu", "Ramesh Chandra", "Rameshwar", "Ramash",
    "Suresh", "Suresh Reddy", "Suresh Kumar", "Sureesh", "Suresha", "Suresh Babu",
    "Mahesh", "Mahesh Kumar", "Maheshwari", "Maheswar", "Mahes", "Mahesh Babu",
    "Manoj", "Manoj Kumar", "Manu", "Manohar", "Manoj Reddy", "Manoj Varma",
    "Ravi", "Ravi Teja", "Ravindra", "Ravindran", "Ravikiran", "Ravi Shankar",
    "Lakshmi", "Laxmi", "Lakshmi Devi", "Lakshmika", "Lakshmana", "Laksmita",
    "Praveen", "Praveen Kumar", "Pravin", "Pravina", "Praveena", "Praveenkumar",
    "Kiran", "Kiran Kumar", "Keerun", "Kiraan", "Kirun", "Kiran Reddy",
    "Keerthi", "Keerthana", "Keerthi Priya", "Kirti", "Kirthana", "Kerti",
    "Anil", "Anil Kumar", "Aneel", "Aniel", "Anil Kumar Reddy", "Anil Rao",
    "Anita", "Anitha", "Anitha Devi", "Anithaa", "Aneetha", "Anita Kumari",
    "Sunitha", "Sunita", "Suneetha", "Suneeta", "Sunitha Devi", "Sunit",
    "Sunil", "Sunil Kumar", "Sunil Reddy", "Suneel", "Suneal", "Sunill",
    "Vijay", "Vijaya", "Vijay Kumar", "Vijayan", "Vijai", "Vijay Dev",
    "Shiva", "Shivam", "Shivani", "Shivansh", "Shivan", "Shiva Kumar",
    "Asha", "Ashi", "Ashima", "Aashika", "Aashima", "Asha Devi",
    "Rohit", "Rohith", "Rohit Kumar", "Rohit Reddy", "Rohith Varma", "Rohit Sharma",
    "Deepak", "Deepak Kumar", "Deepu", "Deepesh", "Dipak", "Deepak Singh",
    "Priya", "Priyanka", "Priyadarshini", "Preeya", "Prya", "Priyashree",
    "Rahul", "Rahul Kumar", "Rahul Reddy", "Rahool", "Ragul", "Rahul Varma",
    "Aruna", "Arun", "Arunra", "Arun Kumar", "Arunesh", "Aruna Devi",
    "Karthik", "Kartik", "Karthikeyan", "Karthika", "Kartikeya", "Karthik Reddy",
    "Sahana", "Sahna", "Sahini", "Sahana Devi", "Saahna", "Sahanika",
    "Meena", "Meenakshi", "Meenal", "Mina", "Minakshi", "Meenamma",
    "Arjun", "Arjuna", "Arjun Kumar", "Arjun Reddy", "Arjunraj", "Arjunan",
    "Kavya", "Kaavya", "Kavyashree", "Kavitha", "Kavita", "Kaviya",
    "Sneha", "Snehitha", "Sneh", "Sneeha", "Snehita", "Snehaa",
    "Teja", "Tejas", "Tejaswi", "Tejash", "Tej", "Tejendra",
    "Varun", "Varun Kumar", "Varunsai", "Varundev", "Varunan", "Varrun"
]

# Preprocessing function
def preprocess_name(name: str) -> str:
    """Cleans a name by lowercasing, trimming spaces, removing symbols."""
    if not isinstance(name, str):
        return ""

    clean_name = name.lower().strip()

    # Remove commas, dots, hyphens, underscores
    for ch in [",", ".", "-", "_"]:
        clean_name = clean_name.replace(ch, "")

    clean_name = " ".join(clean_name.split())  # remove extra spaces
    return clean_name

# Generate a cleaned version of the names_list
def get_cleaned_names() -> list:
    """Returns a list of cleaned/preprocessed names from the dataset."""
    return [preprocess_name(n) for n in names_list]

# Print count to verify dataset quality
if __name__ == "__main__":
    cleaned = get_cleaned_names()
    print(f"Total names: {len(cleaned)}")  
    print("Sample cleaned names:", cleaned[:10])
