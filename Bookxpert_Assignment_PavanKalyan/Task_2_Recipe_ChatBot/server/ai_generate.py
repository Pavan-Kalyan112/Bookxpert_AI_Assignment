from transformers import pipeline
import torch
import logging
from typing import List, Dict, Any, Optional
import random
import re

logger = logging.getLogger(__name__)

class RecipeGenerator:
    def __init__(self):
        try:
            logger.info("Initializing Recipe Generator...")
            self.generator = pipeline(
                'text-generation', 
                model='gpt2',
                device=0 if torch.cuda.is_available() else -1,
                model_kwargs={"cache_dir": "./model_cache"}
            )
            logger.info("Recipe Generator initialized successfully")
            
            self.culinary_terms = {
                'eggs': ['whisked', 'beaten', 'poached', 'scrambled', 'fried', 'soft-boiled', 'hard-boiled'],
                'onions': ['diced', 'sliced', 'caramelized', 'sautéed', 'minced', 'pickled', 'roasted'],
                'chicken': ['diced', 'sliced', 'grilled', 'roasted', 'shredded', 'baked'],
                'beef': ['diced', 'sliced', 'ground', 'cubed', 'shredded'],
                'fish': ['filleted', 'whole', 'steamed', 'grilled', 'baked', 'pan-seared'],
                'rice': ['cooked', 'steamed', 'fried', 'boiled', 'pilaf'],
                'pasta': ['cooked', 'al dente', 'baked', 'stir-fried'],
                'potatoes': ['diced', 'mashed', 'roasted', 'boiled', 'sliced', 'wedges'],
                'tomatoes': ['diced', 'sliced', 'cherry', 'sun-dried', 'pureed'],
                'cheese': ['grated', 'sliced', 'crumbled', 'shredded', 'melted'],
                'mushrooms': ['sliced', 'whole', 'stuffed', 'sautéed', 'grilled'],
                'spinach': ['fresh', 'sautéed', 'steamed', 'chopped', 'baby'],
                'carrots': ['diced', 'julienned', 'sliced', 'shredded', 'baby'],
                'broccoli': ['florets', 'steamed', 'roasted', 'stir-fried'],
                'bell peppers': ['diced', 'sliced', 'stuffed', 'roasted', 'grilled'],
                'zucchini': ['sliced', 'spiralized', 'diced', 'grilled'],
                'garlic': ['minced', 'sliced', 'chopped', 'crushed', 'roasted'],
                'ginger': ['grated', 'minced', 'sliced', 'julienned'],
                'herbs': ['fresh', 'chopped', 'torn', 'whole'],
                'spices': ['ground', 'whole', 'toasted', 'crushed'],
                'nuts': ['chopped', 'toasted', 'sliced', 'whole', 'crushed']
            }
            
            self.cooking_methods = [
                "sauté", "roast", "bake", "grill", "steam", "poach", 
                "simmer", "stir-fry", "braise", "sear", "glaze", "broil",
                "deep-fry", "pan-fry", "stew", "boil", "blanch", "gratin"
            ]
            
            self.herbs_spices = {
                'eggs': ['chives', 'dill', 'parsley', 'basil', 'thyme', 'paprika', 'black pepper'],
                'onions': ['thyme', 'rosemary', 'garlic', 'cumin', 'coriander', 'chili flakes'],
                'chicken': ['rosemary', 'thyme', 'sage', 'oregano', 'garlic', 'paprika'],
                'beef': ['thyme', 'rosemary', 'garlic', 'black pepper', 'mustard', 'oregano'],
                'fish': ['dill', 'lemon zest', 'parsley', 'fennel', 'tarragon', 'chives'],
                'pasta': ['basil', 'oregano', 'parsley', 'red pepper flakes', 'garlic'],
                'rice': ['saffron', 'turmeric', 'cumin', 'coriander', 'bay leaves'],
                'vegetables': ['thyme', 'rosemary', 'oregano', 'basil', 'dill', 'parsley']
            }
            
        except Exception as e:
            logger.error(f"Failed to initialize Recipe Generator: {str(e)}")
            raise

    def _is_english(self, text: str) -> bool:
        """Check if text contains only English characters"""
        try:
            return all(ord(c) < 128 for c in text)
        except:
            return False

    def _validate_parameters(self, ingredients: str, cooking_time: Optional[int], difficulty: Optional[str]) -> None:
        """Validate input parameters"""
        if not ingredients or not isinstance(ingredients, str):
            raise ValueError("Ingredients must be a non-empty string")
        
        if cooking_time is not None and (not isinstance(cooking_time, int) or cooking_time < 1):
            raise ValueError("Cooking time must be a positive integer")
            
        if difficulty and difficulty.lower() not in ['easy', 'medium', 'hard']:
            raise ValueError("Difficulty must be one of: easy, medium, hard")

    def _enhance_ingredients(self, ingredients: List[str]) -> Dict[str, str]:
        """Add preparation details to ingredients"""
        enhanced = {}
        for ing in ingredients:
            ing_lower = ing.lower().strip()
            prep = ""
            
            # Find matching culinary term
            for key, preps in self.culinary_terms.items():
                if key in ing_lower:
                    prep = random.choice(preps)
                    break
                    
            enhanced[ing] = f"{prep} {ing}" if prep else ing
            
        return enhanced

    def _generate_chef_notes(self, ingredients: List[str]) -> str:
        """Generate professional chef's notes"""
        notes = []
        ing_lower = [i.lower() for i in ingredients]
        
        if any(x in ' '.join(ing_lower) for x in ['egg', 'chicken', 'meat', 'fish']):
            notes.append("For best results, make sure all proteins are properly cooked to the recommended internal temperature.")
            
        if any(x in ' '.join(ing_lower) for x in ['pasta', 'rice']):
            notes.append("Save some pasta/rice water before draining - the starchy water helps create a silky sauce.")
            
        if 'garlic' in ' '.join(ing_lower):
            notes.append("Add garlic towards the end of cooking to preserve its flavor and prevent burning.")
            
        if len(notes) > 2:
            notes = random.sample(notes, 2)
            
        return "\n".join([f"👨‍🍳 Chef's Note: {note}" for note in notes])

    def _suggest_pairings(self, ingredients: List[str]) -> str:
        """Suggest food and drink pairings"""
        pairings = []
        main_ingredients = [i.lower() for i in ingredients]
        
        if any(x in ' '.join(main_ingredients) for x in ['chicken', 'turkey']):
            pairings.extend([
                "🍷 Wine Pairing: A crisp Chardonnay or light Pinot Noir",
                "🥗 Side Suggestion: Roasted vegetables or a fresh garden salad"
            ])
        elif any(x in ' '.join(main_ingredients) for x in ['beef', 'lamb']):
            pairings.extend([
                "🍷 Wine Pairing: A bold Cabernet Sauvignon or Malbec",
                "🥔 Side Suggestion: Creamy mashed potatoes or roasted root vegetables"
            ])
        elif any(x in ' '.join(main_ingredients) for x in ['fish', 'seafood']):
            pairings.extend([
                "🍷 Wine Pairing: A dry Riesling or Sauvignon Blanc",
                "🍋 Serving Suggestion: Fresh lemon wedges and a light aioli"
            ])
        elif any(x in ' '.join(main_ingredients) for x in ['pasta', 'risotto']):
            pairings.extend([
                "🍷 Wine Pairing: A Chianti or Sangiovese for tomato-based, Pinot Grigio for cream-based",
                "🍞 Serving Suggestion: Garlic bread or a fresh baguette"
            ])
            
        return "\n".join(pairings[:2])

    def _get_cooking_instructions(self, difficulty: Optional[str]) -> str:
        """Get cooking instructions based on difficulty"""
        if difficulty == "easy":
            return "This recipe uses simple techniques and minimal ingredients for quick preparation."
        elif difficulty == "hard":
            return "This recipe involves advanced techniques and multiple preparation steps for experienced cooks."
        return "This recipe uses standard cooking techniques suitable for most home cooks."

    def generate_recipe(self, ingredients: str, category: Optional[str] = None, 
                       cooking_time: Optional[int] = None, difficulty: Optional[str] = None) -> str:
        try:
            # Validate inputs
            self._validate_parameters(ingredients, cooking_time, difficulty)
            
            # Clean and process ingredients
            ingredient_list = [i.strip() for i in ingredients.split(',') if i.strip()]
            if not ingredient_list:
                return self._get_fallback_recipe(ingredients)
                
            enhanced_ingredients = self._enhance_ingredients(ingredient_list)
            
            # Build prompt with all parameters
            prompt_parts = [f"Create a{' ' + difficulty if difficulty else ''} recipe in English only"]
            
            if category and category.lower() != 'all':
                prompt_parts.append(f"for {category.lower()}")
                
            prompt_parts.append(f"using these ingredients: {', '.join(ingredient_list)}")
            
            if cooking_time:
                prompt_parts.append(f"that takes no more than {cooking_time} minutes to prepare and cook")
                
            prompt = " ".join(prompt_parts) + "\n\nRespond in English only.\n\nTitle: "
            
            result = self.generator(
                prompt,
                max_length=1000,
                num_return_sequences=1,
                temperature=0.9,
                do_sample=True,
                top_p=0.95,
                pad_token_id=50256,
                no_repeat_ngram_size=2,
                early_stopping=True
            )
            
            recipe = result[0]['generated_text']
            
            # Ensure English output
            if not self._is_english(recipe):
                logger.warning("Non-English characters detected, using fallback recipe")
                return self._get_fallback_recipe(ingredients)
            
            # Format the recipe
            formatted_recipe = self._format_recipe(recipe, ingredient_list, enhanced_ingredients, difficulty)
            
            # Add professional touches
            chef_notes = self._generate_chef_notes(ingredient_list)
            pairings = self._suggest_pairings(ingredient_list)
            
            if chef_notes:
                formatted_recipe += f"\n\n{chef_notes}"
            if pairings:
                formatted_recipe += f"\n\n{pairings}"
                
            return formatted_recipe.strip()
            
        except Exception as e:
            logger.error(f"Error generating recipe: {str(e)}")
            return self._get_fallback_recipe(ingredients)

    def _format_recipe(self, recipe: str, original_ingredients: List[str], 
                      enhanced_ingredients: Dict[str, str], difficulty: Optional[str] = None) -> str:
        """Format the recipe with proper sections and styling"""
        sections = {
            "Description": "",
            "Ingredients": "",
            "Instructions": "",
            "Prep Time": "15 minutes",
            "Cook Time": "30 minutes",
            "Servings": "2-4",
            "Difficulty": difficulty.capitalize() if difficulty else "Medium"
        }
        
        # Extract or generate each section
        lines = recipe.split('\n')
        current_section = None
        
        for line in lines:
            line_lower = line.lower().strip()
            
            if "ingredient" in line_lower:
                current_section = "Ingredients"
                continue
            elif "instruction" in line_lower or "direction" in line_lower:
                current_section = "Instructions"
                continue
            elif "time" in line_lower:
                current_section = "Cook Time"
                continue
            elif "serving" in line_lower:
                current_section = "Servings"
                continue
            elif "description" in line_lower:
                current_section = "Description"
                continue
            elif "difficulty" in line_lower:
                current_section = "Difficulty"
                continue
                
            if current_section and current_section in sections:
                if not sections[current_section]:
                    sections[current_section] = line.strip()
                else:
                    sections[current_section] += "\n" + line.strip()
        
        # Build the formatted recipe
        formatted = []
        
        # Title and Description
        title = next((line for line in lines if line.strip() and ":" not in line), "Delicious Recipe")
        formatted.append(f"# {title.strip()}\n")
        
        if sections["Description"]:
            formatted.append(f"*{sections['Description']}*\n")
        
        # Cooking Info
        formatted.append("## ⏱️ Cooking Information")
        formatted.append(f"- ⏱️ Prep Time: {sections['Prep Time']}")
        formatted.append(f"- 🔥 Cook Time: {sections['Cook Time']}")
        formatted.append(f"- 🍽️ Servings: {sections['Servings']}")
        formatted.append(f"- ⚡ Difficulty: {sections['Difficulty']}")
        
        # Ingredients
        formatted.append("\n## 🛒 Ingredients")
        if sections["Ingredients"]:
            formatted.append(sections["Ingredients"])
        else:
            # Generate ingredients list if not provided
            formatted.extend([f"- {enhanced_ingredients.get(ing, ing)}" for ing in original_ingredients])
            formatted.append("- Salt and pepper to taste")
            formatted.append("- 1-2 tablespoons olive oil or butter")
        
        # Instructions
        formatted.append("\n## 👨‍🍳 Instructions")
        if sections["Instructions"]:
            # Ensure instructions are properly numbered
            instructions = [i.strip() for i in sections["Instructions"].split('\n') if i.strip()]
            for i, step in enumerate(instructions, 1):
                if not step[0].isdigit():
                    step = f"{i}. {step}"
                formatted.append(step)
        else:
            formatted.extend([
                "1. Prepare all ingredients as specified.",
                "2. Heat oil in a pan over medium heat.",
                "3. Cook the ingredients, stirring occasionally, until done.",
                "4. Season with salt and pepper to taste.",
                "5. Serve hot and enjoy!"
            ])
        
        return "\n".join(formatted)

    def _get_fallback_recipe(self, ingredients: str) -> str:
        """Generate a fallback recipe if generation fails"""
        return f"""# Quick and Easy Recipe with {ingredients}

*This simple yet delicious recipe makes the most of your available ingredients.*

## ⏱️ Cooking Information
- ⏱️ Prep Time: 10 minutes
- 🔥 Cook Time: 15 minutes
- 🍽️ Servings: 2-4
- ⚡ Difficulty: Easy

## 🛒 Ingredients
- {ingredients}
- 1-2 tablespoons olive oil
- Salt and pepper to taste
- Fresh herbs (optional, for garnish)

## 👨‍🍳 Instructions
1. Prepare all ingredients as needed.
2. Heat olive oil in a pan over medium heat.
3. Add the {ingredients.split(',')[0].strip()} and cook until starting to soften.
4. Add remaining ingredients and cook until everything is heated through.
5. Season with salt and pepper to taste.
6. Garnish with fresh herbs if desired and serve immediately.

👨‍🍳 Chef's Note: For extra flavor, try adding a splash of lemon juice or a sprinkle of your favorite herbs and spices. You can also top with some grated cheese or a drizzle of olive oil before serving.

🍷 Wine Pairing: A crisp white wine or light red would pair nicely with this dish.
"""