import json
import requests
import random
from typing import List, Dict, Optional

# Recipe database using list of dictionaries
RECIPE_DATABASE = [
    {
        "name": "Classic Spaghetti Carbonara",
        "ingredients": [
            {"item": "spaghetti", "amount": 1, "unit": "pound", "notes": "or 16 oz"},
            {"item": "eggs", "amount": 4, "unit": "large", "notes": "room temperature"},
            {"item": "pecorino romano cheese", "amount": 1, "unit": "cup", "notes": "freshly grated"},
            {"item": "guanciale", "amount": 8, "unit": "ounces", "notes": "or pancetta, cubed"},
            {"item": "black pepper", "amount": 1, "unit": "teaspoon", "notes": "freshly ground"},
            {"item": "salt", "amount": 1, "unit": "teaspoon", "notes": "for pasta water"}
        ],
        "instructions": [
            "Bring a large pot of salted water to boil and cook spaghetti according to package directions.",
            "Meanwhile, cook guanciale in a large skillet over medium heat until crispy, about 8-10 minutes.",
            "In a bowl, whisk together eggs, cheese, and black pepper.",
            "Drain pasta, reserving 1 cup of pasta water.",
            "Add hot pasta to the skillet with guanciale, remove from heat.",
            "Quickly stir in egg mixture, adding pasta water as needed for creaminess.",
            "Serve immediately with extra cheese and pepper."
        ],
        "prep_time": 10,
        "cook_time": 20,
        "servings": 4,
        "difficulty": "medium",
        "cuisine": "italian",
        "tags": ["pasta", "quick", "classic"]
    },
    {
        "name": "Vegetarian Buddha Bowl",
        "ingredients": [
            {"item": "quinoa", "amount": 1, "unit": "cup", "notes": "uncooked"},
            {"item": "sweet potato", "amount": 1, "unit": "large", "notes": "cubed"},
            {"item": "chickpeas", "amount": 1, "unit": "can", "notes": "15 oz, drained"},
            {"item": "kale", "amount": 2, "unit": "cups", "notes": "chopped"},
            {"item": "avocado", "amount": 1, "unit": "medium", "notes": "sliced"},
            {"item": "olive oil", "amount": 2, "unit": "tablespoons", "notes": "extra virgin"},
            {"item": "lemon", "amount": 1, "unit": "medium", "notes": "juiced"},
            {"item": "garlic", "amount": 2, "unit": "cloves", "notes": "minced"},
            {"item": "salt", "amount": 1, "unit": "teaspoon", "notes": "to taste"},
            {"item": "black pepper", "amount": 1, "unit": "teaspoon", "notes": "to taste"}
        ],
        "instructions": [
            "Cook quinoa according to package directions, about 15 minutes.",
            "Preheat oven to 400°F (200°C).",
            "Toss sweet potato cubes with 1 tbsp olive oil, salt, and pepper. Roast for 25-30 minutes.",
            "In a skillet, heat remaining oil and sauté chickpeas with garlic until golden, about 5 minutes.",
            "Massage kale with lemon juice and a pinch of salt until softened.",
            "Assemble bowls: quinoa base, topped with sweet potato, chickpeas, kale, and avocado.",
            "Drizzle with olive oil and season to taste."
        ],
        "prep_time": 15,
        "cook_time": 30,
        "servings": 2,
        "difficulty": "easy",
        "cuisine": "vegetarian",
        "tags": ["healthy", "bowl", "vegetarian", "gluten-free"]
    },
    {
        "name": "Quick Chicken Stir-Fry",
        "ingredients": [
            {"item": "chicken breast", "amount": 1, "unit": "pound", "notes": "sliced thin"},
            {"item": "broccoli", "amount": 2, "unit": "cups", "notes": "florets"},
            {"item": "bell peppers", "amount": 2, "unit": "medium", "notes": "sliced"},
            {"item": "soy sauce", "amount": 3, "unit": "tablespoons", "notes": "low sodium"},
            {"item": "sesame oil", "amount": 1, "unit": "tablespoon", "notes": ""},
            {"item": "garlic", "amount": 3, "unit": "cloves", "notes": "minced"},
            {"item": "ginger", "amount": 1, "unit": "tablespoon", "notes": "fresh, grated"},
            {"item": "cornstarch", "amount": 1, "unit": "teaspoon", "notes": ""},
            {"item": "vegetable oil", "amount": 2, "unit": "tablespoons", "notes": "for cooking"}
        ],
        "instructions": [
            "Slice chicken into thin strips and toss with 1 tbsp soy sauce and cornstarch.",
            "Heat vegetable oil in a wok or large skillet over high heat.",
            "Stir-fry chicken until golden, about 5-7 minutes. Remove from pan.",
            "Add garlic and ginger, stir for 30 seconds until fragrant.",
            "Add vegetables and stir-fry for 3-4 minutes until crisp-tender.",
            "Return chicken to pan, add remaining soy sauce and sesame oil.",
            "Toss everything together and serve hot over rice."
        ],
        "prep_time": 15,
        "cook_time": 15,
        "servings": 4,
        "difficulty": "easy",
        "cuisine": "asian",
        "tags": ["quick", "stir-fry", "chicken", "healthy"]
    },
    {
        "name": "Mediterranean Salmon",
        "ingredients": [
            {"item": "salmon fillets", "amount": 4, "unit": "6-ounce", "notes": "skin-on"},
            {"item": "lemon", "amount": 2, "unit": "medium", "notes": "sliced"},
            {"item": "olive oil", "amount": 2, "unit": "tablespoons", "notes": "extra virgin"},
            {"item": "garlic", "amount": 4, "unit": "cloves", "notes": "minced"},
            {"item": "oregano", "amount": 1, "unit": "teaspoon", "notes": "dried"},
            {"item": "thyme", "amount": 1, "unit": "teaspoon", "notes": "dried"},
            {"item": "cherry tomatoes", "amount": 1, "unit": "cup", "notes": "halved"},
            {"item": "kalamata olives", "amount": 1/2, "unit": "cup", "notes": "pitted"},
            {"item": "salt", "amount": 1, "unit": "teaspoon", "notes": "to taste"},
            {"item": "black pepper", "amount": 1, "unit": "teaspoon", "notes": "to taste"}
        ],
        "instructions": [
            "Preheat oven to 400°F (200°C).",
            "Place salmon fillets on a baking sheet lined with parchment paper.",
            "Drizzle with olive oil and season with salt, pepper, oregano, and thyme.",
            "Top each fillet with minced garlic, lemon slices, tomatoes, and olives.",
            "Bake for 12-15 minutes until salmon flakes easily with a fork.",
            "Serve with additional lemon wedges and fresh herbs."
        ],
        "prep_time": 10,
        "cook_time": 15,
        "servings": 4,
        "difficulty": "easy",
        "cuisine": "mediterranean",
        "tags": ["fish", "healthy", "baked", "mediterranean"]
    },
    {
        "name": "Chocolate Chip Cookies",
        "ingredients": [
            {"item": "all-purpose flour", "amount": 2.25, "unit": "cups", "notes": ""},
            {"item": "butter", "amount": 1, "unit": "cup", "notes": "softened"},
            {"item": "brown sugar", "amount": 3/4, "unit": "cup", "notes": "packed"},
            {"item": "white sugar", "amount": 3/4, "unit": "cup", "notes": "granulated"},
            {"item": "eggs", "amount": 2, "unit": "large", "notes": "room temperature"},
            {"item": "vanilla extract", "amount": 2, "unit": "teaspoons", "notes": ""},
            {"item": "chocolate chips", "amount": 2, "unit": "cups", "notes": "semi-sweet"},
            {"item": "baking soda", "amount": 1, "unit": "teaspoon", "notes": ""},
            {"item": "salt", "amount": 1, "unit": "teaspoon", "notes": ""}
        ],
        "instructions": [
            "Preheat oven to 375°F (190°C). Line baking sheets with parchment paper.",
            "Cream together butter, brown sugar, and white sugar until light and fluffy.",
            "Beat in eggs one at a time, then stir in vanilla extract.",
            "In a separate bowl, whisk together flour, baking soda, and salt.",
            "Gradually mix dry ingredients into wet ingredients until just combined.",
            "Fold in chocolate chips.",
            "Drop rounded tablespoons of dough onto prepared baking sheets.",
            "Bake for 9-11 minutes until edges are golden brown.",
            "Cool on baking sheets for 5 minutes, then transfer to wire racks."
        ],
        "prep_time": 20,
        "cook_time": 10,
        "servings": 24,
        "difficulty": "easy",
        "cuisine": "american",
        "tags": ["dessert", "baking", "cookies", "chocolate"]
    }
]

def call_gemini_api(prompt_text):
    """
    Helper function to call the Gemini API with a given prompt.
    """
    apiKey = "" # If you want to use models other than gemini-2.0-flash, provide an API key here. Otherwise, leave this as-is.
    apiUrl = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={apiKey}"

    chat_history = []
    chat_history.append({"role": "user", "parts": [{"text": prompt_text}]})
    payload = {"contents": chat_history}

    try:
        response = requests.post(apiUrl,
                                 headers={'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        response.raise_for_status() # Raise an exception for HTTP errors
        result = response.json()

        if result.get("candidates") and result["candidates"][0].get("content") and \
           result["candidates"][0]["content"].get("parts") and result["candidates"][0]["content"]["parts"][0].get("text"):
            text = result["candidates"][0]["content"]["parts"][0]["text"]
            return text
        else:
            return "Failed to get a valid response from the AI. Unexpected API response structure."
    except requests.exceptions.RequestException as e:
        return f"Failed to connect to the AI service: {e}. Please ensure you have network access and a valid API key (if required)."
    except json.JSONDecodeError:
        return "Failed to parse API response. Invalid JSON received."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def format_recipe(recipe: Dict) -> str:
    """
    Format a recipe dictionary into a readable string.
    """
    formatted = f"🍽️ {recipe['name']}\n\n"
    
    # Ingredients section
    formatted += "📋 Ingredients:\n"
    for ingredient in recipe['ingredients']:
        amount = ingredient['amount']
        unit = ingredient['unit']
        item = ingredient['item']
        notes = ingredient.get('notes', '')
        
        if isinstance(amount, float) and amount.is_integer():
            amount = int(amount)
        
        formatted += f"- {amount} {unit} {item}"
        if notes:
            formatted += f" ({notes})"
        formatted += "\n"
    
    # Instructions section
    formatted += f"\n👨‍🍳 Instructions:\n"
    for i, instruction in enumerate(recipe['instructions'], 1):
        formatted += f"{i}. {instruction}\n"
    
    # Additional info
    formatted += f"\n⏱️ Prep Time: {recipe['prep_time']} minutes\n"
    formatted += f"🔥 Cook Time: {recipe['cook_time']} minutes\n"
    formatted += f"👥 Servings: {recipe['servings']}\n"
    formatted += f"📊 Difficulty: {recipe['difficulty'].title()}\n"
    formatted += f"🌍 Cuisine: {recipe['cuisine'].title()}\n"
    
    if recipe.get('tags'):
        formatted += f"🏷️ Tags: {', '.join(recipe['tags'])}\n"
    
    return formatted

def find_recipes_by_ingredients(ingredients: List[str]) -> List[Dict]:
    """
    Find recipes that contain any of the specified ingredients.
    """
    matching_recipes = []
    ingredients_lower = [ing.lower() for ing in ingredients]
    
    for recipe in RECIPE_DATABASE:
        recipe_ingredients = [ing['item'].lower() for ing in recipe['ingredients']]
        
        # Check if any of the user's ingredients match recipe ingredients
        matches = [ing for ing in ingredients_lower if any(ing in recipe_ing or recipe_ing in ing for recipe_ing in recipe_ingredients)]
        
        if matches:
            recipe_copy = recipe.copy()
            recipe_copy['matching_ingredients'] = matches
            recipe_copy['match_score'] = len(matches)
            matching_recipes.append(recipe_copy)
    
    # Sort by match score (most matches first)
    matching_recipes.sort(key=lambda x: x['match_score'], reverse=True)
    return matching_recipes

def generate_recipe(ingredients: str) -> str:
    """
    Generates a recipe based on provided ingredients.
    """
    ingredients_list = [ing.strip().lower() for ing in ingredients.split(',')]
    
    # First try to find matching recipes in our database
    matching_recipes = find_recipes_by_ingredients(ingredients_list)
    
    if matching_recipes:
        # Use the best matching recipe
        best_match = matching_recipes[0]
        print(f"\nFound a recipe that matches your ingredients: {best_match['name']}")
        print(f"Matching ingredients: {', '.join(best_match['matching_ingredients'])}")
        return format_recipe(best_match)
    
    # If no matches found, use AI to generate a recipe
    print(f"\nAI is thinking up a recipe with {ingredients}...\n")
    prompt = (f"Generate a simple, clear recipe using ONLY the following ingredients: {ingredients}. "
              f"Include brief instructions and suggested serving size. "
              f"Format it clearly with a recipe name, ingredients list, and steps.")
    return call_gemini_api(prompt)

def remix_recipe(current_recipe: str, modifications: str) -> str:
    """
    Remixes an existing recipe based on user-specified modifications.
    """
    print(f"\nAI is remixing the recipe with '{modifications}'...\n")
    prompt = (f"Take the following recipe:\n\n{current_recipe}\n\n"
              f"Now, remix this recipe by incorporating the following changes: '{modifications}'. "
              f"Provide the updated recipe. Focus on making the changes clear and integrating them smoothly. "
              f"If a requested change doesn't make sense for the ingredients, explain why briefly. "
              f"Always return a complete, updated recipe, not just the changes.")
    return call_gemini_api(prompt)

def get_random_recipe() -> str:
    """
    Returns a random recipe from the database.
    """
    recipe = random.choice(RECIPE_DATABASE)
    return format_recipe(recipe)

def search_recipes_by_tag(tag: str) -> List[Dict]:
    """
    Search recipes by tag.
    """
    tag_lower = tag.lower()
    matching_recipes = []
    
    for recipe in RECIPE_DATABASE:
        if tag_lower in [t.lower() for t in recipe.get('tags', [])]:
            matching_recipes.append(recipe)
    
    return matching_recipes

def search_recipes_by_cuisine(cuisine: str) -> List[Dict]:
    """
    Search recipes by cuisine type.
    """
    cuisine_lower = cuisine.lower()
    matching_recipes = []
    
    for recipe in RECIPE_DATABASE:
        if cuisine_lower in recipe['cuisine'].lower():
            matching_recipes.append(recipe)
    
    return matching_recipes

def run_recipe_remix_master():
    """
    Runs the AI Recipe Remix Master.
    """
    print("Welcome to the Enhanced AI Recipe Remix Master!")
    print("I'll help you find and remix recipes based on your ingredients and preferences.")
    print("Type 'quit' to exit at any time.")
    print("Type 'random' to get a random recipe from our database.")
    print("Type 'search [tag]' to search recipes by tag (e.g., 'search quick').")
    print("Type 'cuisine [type]' to search by cuisine (e.g., 'cuisine italian').\n")

    current_recipe = ""

    while True:
        if not current_recipe:
            ingredients_input = input("Enter a comma-separated list of ingredients you have (e.g., chicken, broccoli, pasta): ").strip()
            
            if ingredients_input.lower() == 'quit':
                print("Exiting Recipe Remix Master. Goodbye!")
                break
            elif ingredients_input.lower() == 'random':
                current_recipe = get_random_recipe()
                print("\n--- Random Recipe ---")
                print(current_recipe)
                print("----------------------\n")
                continue
            elif ingredients_input.lower().startswith('search '):
                tag = ingredients_input[7:].strip()
                matching_recipes = search_recipes_by_tag(tag)
                if matching_recipes:
                    print(f"\nFound {len(matching_recipes)} recipes with tag '{tag}':")
                    for i, recipe in enumerate(matching_recipes, 1):
                        print(f"{i}. {recipe['name']} ({recipe['cuisine']})")
                    
                    choice = input(f"\nEnter a number (1-{len(matching_recipes)}) to view a recipe, or press Enter to continue: ").strip()
                    if choice.isdigit() and 1 <= int(choice) <= len(matching_recipes):
                        current_recipe = format_recipe(matching_recipes[int(choice) - 1])
                        print("\n--- Selected Recipe ---")
                        print(current_recipe)
                        print("----------------------\n")
                else:
                    print(f"No recipes found with tag '{tag}'.")
                continue
            elif ingredients_input.lower().startswith('cuisine '):
                cuisine = ingredients_input[8:].strip()
                matching_recipes = search_recipes_by_cuisine(cuisine)
                if matching_recipes:
                    print(f"\nFound {len(matching_recipes)} {cuisine} recipes:")
                    for i, recipe in enumerate(matching_recipes, 1):
                        print(f"{i}. {recipe['name']}")
                    
                    choice = input(f"\nEnter a number (1-{len(matching_recipes)}) to view a recipe, or press Enter to continue: ").strip()
                    if choice.isdigit() and 1 <= int(choice) <= len(matching_recipes):
                        current_recipe = format_recipe(matching_recipes[int(choice) - 1])
                        print("\n--- Selected Recipe ---")
                        print(current_recipe)
                        print("----------------------\n")
                else:
                    print(f"No {cuisine} recipes found.")
                continue
            
            if not ingredients_input:
                print("Please enter some ingredients to get started.")
                continue

            current_recipe = generate_recipe(ingredients_input)
            if current_recipe.startswith("Failed to"):
                print(f"Error: {current_recipe}")
                current_recipe = "" # Reset to allow re-entry of ingredients
                continue
        else:
            print("\n--- Current Recipe ---")
            print(current_recipe)
            print("----------------------\n")

        mod_input = input(
            "How would you like to remix this recipe? (e.g., 'make it vegan', 'add a spicy kick', 'use less oil', 'add mushrooms', 'quit' to exit): "
        ).strip()

        if mod_input.lower() == 'quit':
            print("Exiting Recipe Remix Master. Goodbye!")
            break

        if not mod_input:
            print("No modification specified. Displaying current recipe again.")
            continue

        updated_recipe = remix_recipe(current_recipe, mod_input)

        if updated_recipe.startswith("Failed to"):
            print(f"Error: {updated_recipe}")
            print("Please try modifying the recipe again.")
        else:
            current_recipe = updated_recipe # Update the current recipe to the new, remixed version
            print("\n--- Remixed Recipe ---")
            print(current_recipe)
            print("----------------------\n")

if __name__ == "__main__":
    run_recipe_remix_master() 