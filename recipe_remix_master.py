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
            "**Pasta Preparation**: Bring a large pot of salted water to a rolling boil (add 1 tbsp salt per 4 quarts water). Cook spaghetti according to package directions (usually 8-10 minutes for al dente). Pasta should be firm but not crunchy when done. Reserve 1 cup of the hot pasta water before draining - this is essential for the sauce.",
            "**Guanciale Cooking**: Meanwhile, cook guanciale in a large skillet over medium heat (325°F/163°C) until crispy and golden brown, about 8-10 minutes. Guanciale should be rendered and crispy, with golden fat remaining in the pan. Remove from heat but keep the rendered fat in the pan.",
            "**Egg Mixture**: In a medium bowl, whisk together eggs, cheese, and black pepper until well combined. Set aside at room temperature (cold eggs can cause scrambling).",
            "**Pasta Assembly**: When pasta is done, drain it quickly, reserving 1 cup of the hot pasta water. Working quickly, add the hot pasta to the skillet with guanciale and rendered fat. Toss to coat pasta with the fat.",
            "**Sauce Creation**: Remove skillet from heat and immediately pour in the egg mixture, stirring constantly in a circular motion to create a creamy sauce without scrambling the eggs. The heat from the pasta should cook the eggs gently.",
            "**Sauce Adjustment**: Add pasta water gradually (about 1/4 cup at a time) until you achieve a silky, creamy consistency. The sauce should coat the pasta evenly without being runny.",
            "**Final Touch**: Serve immediately with extra grated cheese and freshly ground black pepper on top. The dish should be creamy and hot."
        ],
        "prep_time": 15,
        "cook_time": 20,
        "total_time": 35,
        "servings": 4,
        "difficulty": "medium",
        "cuisine": "italian",
        "tags": ["pasta", "quick", "classic", "dinner"],
        "tips": [
            "Use room temperature eggs to prevent scrambling",
            "Work quickly when combining pasta and eggs",
            "Reserve pasta water - it's essential for the sauce",
            "Don't overcook the pasta - al dente is key"
        ]
    },
    {
        "name": "Vegetarian Buddha Bowl",
        "ingredients": [
            {"item": "quinoa", "amount": 1, "unit": "cup", "notes": "uncooked, rinsed"},
            {"item": "sweet potato", "amount": 1, "unit": "large", "notes": "peeled and cubed into 1-inch pieces"},
            {"item": "chickpeas", "amount": 1, "unit": "can", "notes": "15 oz, drained and rinsed"},
            {"item": "kale", "amount": 2, "unit": "cups", "notes": "chopped, stems removed"},
            {"item": "avocado", "amount": 1, "unit": "medium", "notes": "sliced"},
            {"item": "olive oil", "amount": 2, "unit": "tablespoons", "notes": "extra virgin, divided"},
            {"item": "lemon", "amount": 1, "unit": "medium", "notes": "juiced (about 2 tbsp)"},
            {"item": "garlic", "amount": 2, "unit": "cloves", "notes": "minced"},
            {"item": "salt", "amount": 1, "unit": "teaspoon", "notes": "divided"},
            {"item": "black pepper", "amount": 1, "unit": "teaspoon", "notes": "divided"},
            {"item": "cumin", "amount": 1/2, "unit": "teaspoon", "notes": "ground"},
            {"item": "paprika", "amount": 1/2, "unit": "teaspoon", "notes": "smoked"}
        ],
        "instructions": [
            "**Oven Setup**: Preheat oven to 400°F (200°C). Line a baking sheet with parchment paper for easy cleanup and even cooking.",
            "**Quinoa Preparation**: Rinse quinoa thoroughly in a fine-mesh strainer under cold running water until water runs clear (this removes bitter coating). Cook according to package directions (usually 15-20 minutes), then fluff with a fork and set aside. Quinoa should be light and fluffy when done.",
            "**Sweet Potato Preparation**: Peel sweet potato and cut into 1-inch cubes (uniform size ensures even cooking). Toss sweet potato cubes with 1 tbsp olive oil, 1/2 tsp salt, 1/2 tsp pepper, cumin, and paprika. Spread on prepared baking sheet in a single layer (don't overcrowd).",
            "**Sweet Potato Roasting**: Roast sweet potatoes for 25-30 minutes, flipping halfway through with a spatula, until tender and slightly caramelized. Sweet potatoes should be fork-tender with golden edges when done.",
            "**Chickpea Cooking**: While sweet potatoes roast, heat remaining 1 tbsp olive oil in a large skillet over medium heat (325°F/163°C). Add minced garlic and cook for exactly 30 seconds until fragrant but not browned (garlic should smell aromatic, not burnt).",
            "**Chickpea Crisping**: Add chickpeas to the skillet and cook for 5-7 minutes, stirring occasionally, until golden and slightly crispy. Chickpeas should have a golden-brown exterior and be slightly crunchy.",
            "**Kale Massaging**: In a large bowl, massage kale with lemon juice and remaining 1/2 tsp salt until leaves are softened and reduced in volume (about 2-3 minutes). Kale should be dark green and tender, not tough.",
            "**Bowl Assembly**: Divide quinoa among 2 bowls, then top with roasted sweet potatoes, crispy chickpeas, massaged kale, and sliced avocado. Arrange ingredients in sections for visual appeal.",
            "**Final Seasoning**: Drizzle with additional olive oil and season with remaining black pepper to taste. Serve immediately while warm."
        ],
        "prep_time": 20,
        "cook_time": 30,
        "total_time": 50,
        "servings": 2,
        "difficulty": "easy",
        "cuisine": "vegetarian",
        "tags": ["healthy", "bowl", "vegetarian", "gluten-free", "lunch"],
        "tips": [
            "Massage kale thoroughly to make it tender",
            "Don't overcrowd the baking sheet for crispy sweet potatoes",
            "Rinse quinoa well to remove bitter coating",
            "Use fresh lemon juice for best flavor"
        ]
    },
    {
        "name": "Quick Chicken Stir-Fry",
        "ingredients": [
            {"item": "chicken breast", "amount": 1, "unit": "pound", "notes": "sliced into thin strips"},
            {"item": "broccoli", "amount": 2, "unit": "cups", "notes": "florets, cut into bite-sized pieces"},
            {"item": "bell peppers", "amount": 2, "unit": "medium", "notes": "sliced into thin strips"},
            {"item": "soy sauce", "amount": 3, "unit": "tablespoons", "notes": "low sodium, divided"},
            {"item": "sesame oil", "amount": 1, "unit": "tablespoon", "notes": "toasted"},
            {"item": "garlic", "amount": 3, "unit": "cloves", "notes": "minced"},
            {"item": "ginger", "amount": 1, "unit": "tablespoon", "notes": "fresh, grated"},
            {"item": "cornstarch", "amount": 1, "unit": "teaspoon", "notes": ""},
            {"item": "vegetable oil", "amount": 2, "unit": "tablespoons", "notes": "for high-heat cooking"},
            {"item": "rice vinegar", "amount": 1, "unit": "tablespoon", "notes": ""},
            {"item": "honey", "amount": 1, "unit": "teaspoon", "notes": "or brown sugar"},
            {"item": "red pepper flakes", "amount": 1/4, "unit": "teaspoon", "notes": "optional, for heat"}
        ],
        "instructions": [
            "**Chicken Preparation**: Slice chicken breast into thin, uniform strips (about 1/4 inch thick) for even cooking. Cut against the grain for tender results. In a medium bowl, combine chicken with 1 tbsp soy sauce and cornstarch. Toss to coat evenly and let marinate for 10 minutes at room temperature.",
            "**Vegetable Prep**: Prepare all vegetables: cut broccoli into small florets (about 1-inch pieces), slice bell peppers into thin strips (1/4 inch wide), mince garlic finely, and grate ginger (peel first if using fresh). Have everything ready before cooking starts.",
            "**High Heat Setup**: Heat 1 tbsp vegetable oil in a wok or large skillet over high heat until very hot (oil should shimmer and smoke slightly, about 450°F/232°C). The pan should be smoking hot for authentic stir-fry texture.",
            "**Chicken Cooking**: Add chicken in a single layer (don't overcrowd) and stir-fry for 5-7 minutes until golden brown and cooked through. Chicken should be opaque throughout with no pink centers. Remove chicken to a plate and set aside.",
            "**Aromatics**: Add remaining 1 tbsp vegetable oil to the same pan. Add garlic and ginger, stir for exactly 30 seconds until fragrant (they should smell aromatic, not burnt).",
            "**Vegetable Cooking**: Add broccoli and bell peppers. Stir-fry for 3-4 minutes until vegetables are crisp-tender but still bright in color. Broccoli should be bright green and slightly crunchy, peppers should be softened but not mushy.",
            "**Sauce Assembly**: Return chicken to the pan. Add remaining 2 tbsp soy sauce, sesame oil, rice vinegar, honey, and red pepper flakes if using. Toss everything together for 1-2 minutes until sauce coats all ingredients evenly.",
            "**Final Touch**: Serve immediately over steamed rice or noodles while hot. The dish should be steaming and aromatic."
        ],
        "prep_time": 20,
        "cook_time": 15,
        "total_time": 35,
        "servings": 4,
        "difficulty": "easy",
        "cuisine": "asian",
        "tags": ["quick", "stir-fry", "chicken", "healthy", "dinner"],
        "tips": [
            "Cut chicken into uniform strips for even cooking",
            "Use high heat for authentic stir-fry texture",
            "Don't overcrowd the pan - cook in batches if needed",
            "Have all ingredients prepped before starting to cook"
        ]
    },
    {
        "name": "Mediterranean Salmon",
        "ingredients": [
            {"item": "salmon fillets", "amount": 4, "unit": "6-ounce", "notes": "skin-on, pin bones removed"},
            {"item": "lemon", "amount": 2, "unit": "medium", "notes": "1 sliced, 1 for juice"},
            {"item": "olive oil", "amount": 2, "unit": "tablespoons", "notes": "extra virgin"},
            {"item": "garlic", "amount": 4, "unit": "cloves", "notes": "minced"},
            {"item": "oregano", "amount": 1, "unit": "teaspoon", "notes": "dried"},
            {"item": "thyme", "amount": 1, "unit": "teaspoon", "notes": "dried"},
            {"item": "cherry tomatoes", "amount": 1, "unit": "cup", "notes": "halved"},
            {"item": "kalamata olives", "amount": 1/2, "unit": "cup", "notes": "pitted, halved"},
            {"item": "salt", "amount": 1, "unit": "teaspoon", "notes": "divided"},
            {"item": "black pepper", "amount": 1, "unit": "teaspoon", "notes": "divided"},
            {"item": "fresh parsley", "amount": 1/4, "unit": "cup", "notes": "chopped, for garnish"},
            {"item": "feta cheese", "amount": 1/2, "unit": "cup", "notes": "crumbled, optional"}
        ],
        "instructions": [
            "**Oven Setup**: Preheat oven to 400°F (200°C). Line a large baking sheet with parchment paper for easy cleanup and even cooking.",
            "**Salmon Preparation**: Pat salmon fillets dry with paper towels to ensure proper seasoning adherence and crispy skin. Check for and remove any pin bones with tweezers if present.",
            "**Pan Preparation**: Place salmon fillets skin-side down on the prepared baking sheet, spacing them evenly (about 2 inches apart) for proper air circulation.",
            "**Seasoning**: Drizzle each fillet with olive oil and season generously with salt and pepper on both sides. Sprinkle dried oregano and thyme evenly over the top of each fillet.",
            "**Topping Assembly**: Distribute minced garlic over each fillet, then top with lemon slices, halved cherry tomatoes, and kalamata olives. Arrange toppings evenly for visual appeal.",
            "**Baking**: Bake in preheated oven for 12-15 minutes, depending on thickness. Salmon is done when it flakes easily with a fork and reaches 145°F (63°C) internal temperature. The flesh should be opaque and slightly pink in the center.",
            "**Resting**: Remove from oven and let rest for 5 minutes to allow juices to redistribute. This prevents the salmon from drying out when cut.",
            "**Garnishing**: Garnish with fresh parsley and crumbled feta cheese if desired. The dish should look colorful and appetizing.",
            "**Serving**: Serve immediately with additional lemon wedges and your choice of side dishes. The salmon should be moist and flavorful."
        ],
        "prep_time": 15,
        "cook_time": 15,
        "total_time": 30,
        "servings": 4,
        "difficulty": "easy",
        "cuisine": "mediterranean",
        "tags": ["fish", "healthy", "baked", "mediterranean", "dinner"],
        "tips": [
            "Pat salmon dry for better seasoning adherence",
            "Don't overcook - salmon should be slightly pink in center",
            "Let salmon rest after cooking for juicier results",
            "Use fresh herbs for garnish for best flavor"
        ]
    },
    {
        "name": "Chocolate Chip Cookies",
        "ingredients": [
            {"item": "all-purpose flour", "amount": 2.25, "unit": "cups", "notes": "spooned and leveled"},
            {"item": "butter", "amount": 1, "unit": "cup", "notes": "unsalted, softened to room temperature"},
            {"item": "brown sugar", "amount": 3/4, "unit": "cup", "notes": "packed, light or dark"},
            {"item": "white sugar", "amount": 3/4, "unit": "cup", "notes": "granulated"},
            {"item": "eggs", "amount": 2, "unit": "large", "notes": "room temperature"},
            {"item": "vanilla extract", "amount": 2, "unit": "teaspoons", "notes": "pure vanilla extract"},
            {"item": "chocolate chips", "amount": 2, "unit": "cups", "notes": "semi-sweet or dark"},
            {"item": "baking soda", "amount": 1, "unit": "teaspoon", "notes": ""},
            {"item": "salt", "amount": 1, "unit": "teaspoon", "notes": "fine sea salt"},
            {"item": "walnuts", "amount": 1, "unit": "cup", "notes": "chopped, optional"}
        ],
        "instructions": [
            "**Oven Setup**: Preheat oven to 375°F (190°C). Line baking sheets with parchment paper or silicone baking mats for easy removal and even baking.",
            "**Dry Ingredients**: In a medium bowl, whisk together flour, baking soda, and salt until well combined. Set aside. This ensures even distribution of leavening agents.",
            "**Butter Creaming**: In a large bowl using an electric mixer, cream together softened butter, brown sugar, and white sugar on medium speed until light and fluffy (about 3-4 minutes). The mixture should be pale and airy when done.",
            "**Egg Addition**: Add eggs one at a time, beating well after each addition. Scrape down the sides of the bowl as needed to ensure even mixing. The mixture should be smooth and well combined.",
            "**Vanilla Addition**: Beat in vanilla extract until well combined. Use pure vanilla extract for best flavor.",
            "**Dry Ingredient Incorporation**: Gradually add the dry ingredients to the wet ingredients, mixing on low speed until just combined. Do not overmix - this makes cookies tough. The dough should be soft but not sticky.",
            "**Chocolate Addition**: Fold in chocolate chips and chopped walnuts (if using) with a rubber spatula until evenly distributed throughout the dough.",
            "**Cookie Formation**: Using a cookie scoop or rounded tablespoon, drop dough onto prepared baking sheets, spacing cookies about 2 inches apart for proper spreading. Don't overcrowd the baking sheets.",
            "**Baking**: Bake for 9-11 minutes, rotating baking sheets halfway through for even baking, until edges are golden brown but centers are still soft. Cookies should be slightly underdone when removed from oven.",
            "**Cooling**: Remove from oven and let cookies cool on baking sheets for 5 minutes before transferring to wire racks to cool completely. This prevents cookies from breaking."
        ],
        "prep_time": 25,
        "cook_time": 10,
        "total_time": 35,
        "servings": 24,
        "difficulty": "easy",
        "cuisine": "american",
        "tags": ["dessert", "baking", "cookies", "chocolate", "sweet"],
        "tips": [
            "Use room temperature ingredients for best results",
            "Don't overmix the dough - it makes cookies tough",
            "Let cookies cool on baking sheet for 5 minutes before moving",
            "Store in airtight container to maintain freshness"
        ]
    },
    {
        "name": "Creamy Mushroom Risotto",
        "ingredients": [
            {"item": "arborio rice", "amount": 1.5, "unit": "cups", "notes": "uncooked"},
            {"item": "mushrooms", "amount": 1, "unit": "pound", "notes": "mixed varieties, sliced"},
            {"item": "vegetable broth", "amount": 6, "unit": "cups", "notes": "warm, divided"},
            {"item": "white wine", "amount": 1/2, "unit": "cup", "notes": "dry white wine"},
            {"item": "onion", "amount": 1, "unit": "medium", "notes": "finely diced"},
            {"item": "garlic", "amount": 3, "unit": "cloves", "notes": "minced"},
            {"item": "parmesan cheese", "amount": 1, "unit": "cup", "notes": "freshly grated"},
            {"item": "butter", "amount": 3, "unit": "tablespoons", "notes": "unsalted, divided"},
            {"item": "olive oil", "amount": 2, "unit": "tablespoons", "notes": "extra virgin"},
            {"item": "thyme", "amount": 1, "unit": "teaspoon", "notes": "fresh, chopped"},
            {"item": "salt", "amount": 1, "unit": "teaspoon", "notes": "to taste"},
            {"item": "black pepper", "amount": 1/2, "unit": "teaspoon", "notes": "freshly ground"}
        ],
        "instructions": [
            "**Broth Preparation**: Heat vegetable broth in a medium saucepan and keep warm over low heat throughout cooking. Warm broth prevents temperature shock when added to rice.",
            "**Mushroom Cooking**: In a large, heavy-bottomed pot, heat 1 tbsp olive oil and 1 tbsp butter over medium heat (325°F/163°C). Add sliced mushrooms and cook for 8-10 minutes until golden brown and moisture has evaporated. Mushrooms should be deeply browned and slightly crispy. Remove mushrooms to a plate and set aside.",
            "**Aromatics**: In the same pot, add remaining 1 tbsp olive oil and 1 tbsp butter. Add diced onion and cook for 5 minutes until translucent and soft (onion should be clear, not browned).",
            "**Garlic Addition**: Add minced garlic and cook for exactly 1 minute until fragrant (garlic should smell aromatic, not burnt).",
            "**Rice Toasting**: Add arborio rice and stir for 2-3 minutes until rice is translucent around the edges (this toasts the rice and enhances flavor). Rice should have a pearly appearance.",
            "**Wine Deglazing**: Pour in white wine and stir constantly until liquid is absorbed (about 2 minutes). The wine should be completely absorbed before adding broth.",
            "**Broth Addition**: Begin adding warm broth 1/2 cup at a time, stirring constantly and allowing each addition to be absorbed before adding more. This slow process creates the creamy texture.",
            "**Cooking Process**: Continue this process for 18-20 minutes until rice is creamy and al dente (firm but not hard in the center). The risotto should be creamy but still have some bite.",
            "**Final Assembly**: Remove from heat and stir in remaining 1 tbsp butter, grated parmesan cheese, cooked mushrooms, and fresh thyme. The heat from the risotto will melt the cheese.",
            "**Resting**: Cover and let rest for 2 minutes, then season with salt and pepper to taste. This allows flavors to meld.",
            "**Serving**: Serve immediately with extra parmesan cheese on top. Risotto should be creamy and hot."
        ],
        "prep_time": 15,
        "cook_time": 25,
        "total_time": 40,
        "servings": 4,
        "difficulty": "medium",
        "cuisine": "italian",
        "tags": ["risotto", "mushroom", "vegetarian", "dinner", "creamy"],
        "tips": [
            "Keep broth warm throughout cooking",
            "Stir constantly for creamy texture",
            "Don't rush the process - risotto takes time",
            "Use good quality parmesan for best flavor"
        ]
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
    formatted += f"⏰ Total Time: {recipe.get('total_time', recipe['prep_time'] + recipe['cook_time'])} minutes\n"
    formatted += f"👥 Servings: {recipe['servings']}\n"
    formatted += f"📊 Difficulty: {recipe['difficulty'].title()}\n"
    formatted += f"🌍 Cuisine: {recipe['cuisine'].title()}\n"
    
    if recipe.get('tags'):
        formatted += f"🏷️ Tags: {', '.join(recipe['tags'])}\n"
    
    # Tips section
    if recipe.get('tips'):
        formatted += f"\n💡 Chef's Tips:\n"
        for tip in recipe['tips']:
            formatted += f"• {tip}\n"
    
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

def open_conversion_chart():
    """
    Opens the measurement conversion chart in the default web browser.
    """
    import webbrowser
    import os
    
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    chart_path = os.path.join(current_dir, 'measurement_conversion_chart.html')
    
    # Convert to file URL
    file_url = f"file://{chart_path}"
    
    try:
        webbrowser.open(file_url)
        print("📏 Measurement conversion chart opened in your browser!")
        print("Keep this window open to return to the recipe remix master.\n")
    except Exception as e:
        print(f"Could not open conversion chart: {e}")
        print("You can manually open 'measurement_conversion_chart.html' in your browser.\n")

def run_recipe_remix_master():
    """
    Runs the AI Recipe Remix Master.
    """
    print("Welcome to the Enhanced AI Recipe Remix Master!")
    print("I'll help you find and remix recipes based on your ingredients and preferences.")
    print("Type 'quit' to exit at any time.")
    print("Type 'random' to get a random recipe from our database.")
    print("Type 'search [tag]' to search recipes by tag (e.g., 'search quick').")
    print("Type 'cuisine [type]' to search by cuisine (e.g., 'cuisine italian').")
    print("Type 'chart' to open the measurement conversion chart.\n")

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
            elif ingredients_input.lower() == 'chart':
                open_conversion_chart()
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