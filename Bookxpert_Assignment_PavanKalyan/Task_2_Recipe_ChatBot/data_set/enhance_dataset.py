import json
import random
from pathlib import Path
from typing import List, Dict, Any

def load_existing_recipes(input_path: str) -> List[Dict[str, str]]:
    """Load existing recipes from JSONL file."""
    recipes = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                recipes.append(json.loads(line.strip()))
            except json.JSONDecodeError:
                continue
    return recipes

def generate_enhanced_recipe(base_recipe: Dict[str, str]) -> Dict[str, str]:
    """Enhance a single recipe with more details."""
    ingredients = [i.strip() for i in base_recipe['input'].split(',')]
    
    # Recipe templates for different cuisines
    cuisines = ["Indian", "Italian", "Chinese", "Mexican", "Mediterranean"]
    cuisine = random.choice(cuisines)
    
    # Generate detailed recipe
    recipe = {
        "instruction": "Create a detailed recipe with the given ingredients. Include title, ingredients with quantities, step-by-step instructions, cooking time, and number of servings.",
        "input": ", ".join(ingredients),
        "output": generate_recipe_output(ingredients, cuisine)
    }
    return recipe

def generate_recipe_output(ingredients: List[str], cuisine: str) -> str:
    """Generate detailed recipe output."""
    # Common recipe components
    proteins = ["chicken", "paneer", "tofu", "fish", "egg", "dal", "beans"]
    veggies = ["onion", "tomato", "potato", "carrot", "beans", "peas", "spinach"]
    
    # Determine recipe type
    has_protein = any(p in " ".join(ingredients).lower() for p in proteins)
    has_veggie = any(v in " ".join(ingredients).lower() for v in veggies)
    
    # Generate recipe details
    title = f"{cuisine} Style {ingredients[0].title()} " + (
        "Stir Fry" if has_veggie else "Dish"
    )
    
    # Generate ingredients list with quantities
    ingredients_list = []
    for ing in ingredients:
        ing = ing.strip().lower()
        if ing in proteins:
            ingredients_list.append(f"- 200g {ing}")
        elif ing in veggies:
            ingredients_list.append(f"- 1 medium {ing}, chopped")
        elif ing == "rice":
            ingredients_list.append("- 1 cup basmati rice")
        elif ing == "pasta":
            ingredients_list.append("- 200g pasta")
        else:
            ingredients_list.append(f"- 1 tbsp {ing}")
    
    # Add common ingredients
    if cuisine == "Indian":
        ingredients_list.extend([
            "- 2 tbsp oil",
            "- 1 tsp cumin seeds",
            "- 1/2 tsp turmeric powder",
            "- 1 tsp coriander powder",
            "- Salt to taste"
        ])
    elif cuisine == "Italian":
        ingredients_list.extend([
            "- 2 tbsp olive oil",
            "- 2 cloves garlic, minced",
            "- 1 tsp dried oregano",
            "- 1/2 tsp red chili flakes",
            "- Salt and pepper to taste"
        ])
    
    # Generate instructions
    instructions = [
        "Heat oil in a pan over medium heat.",
        "Add whole spices and let them splutter.",
        "Add chopped vegetables and sauté until soft.",
        "Add main ingredients and mix well.",
        "Cook for 5-7 minutes, stirring occasionally.",
        "Adjust seasoning and serve hot."
    ]
    
    # Format final output
    return f"""Title: {title}

Ingredients:
""" + "\n".join(ingredients_list) + """

Instructions:
""" + "\n".join(f"{i+1}. {step}" for i, step in enumerate(instructions)) + f"""

Time: {random.randint(15, 45)} minutes
Servings: {random.randint(2, 4)}
Cuisine: {cuisine}
Dietary Info: {"Vegetarian" if not has_protein else "Non-vegetarian"}, {random.choice(["Gluten-free", "Nut-free", "Dairy-free"])}"""

def main():
    input_path = Path("D:/Bookxpert_Assignment_PavanKalyan/Task_2_Recipe_ChatBot/data_set/recipes_finetune.jsonl")
    output_path = Path("D:/Bookxpert_Assignment_PavanKalyan/Task_2_Recipe_ChatBot/data_set/recipes_enhanced.jsonl")
    
    # Load existing recipes
    print("Loading existing recipes...")
    existing_recipes = load_existing_recipes(input_path)
    
    # Generate enhanced recipes
    print(f"Enhancing {len(existing_recipes)} recipes...")
    enhanced_recipes = [generate_enhanced_recipe(r) for r in existing_recipes]
    
    # Save enhanced recipes
    print(f"Saving {len(enhanced_recipes)} enhanced recipes to {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        for recipe in enhanced_recipes:
            f.write(json.dumps(recipe, ensure_ascii=False) + '\n')
    
    print("Dataset enhancement complete!")

if __name__ == "__main__":
    main()
