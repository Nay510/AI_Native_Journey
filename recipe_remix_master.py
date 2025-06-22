import json
import requests

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

def generate_recipe(ingredients):
    """
    Generates a basic recipe based on provided ingredients.
    """
    print(f"\nAI is thinking up a recipe with {ingredients}...\n")
    prompt = (f"Generate a simple, clear recipe using ONLY the following ingredients: {ingredients}. "
              f"Include brief instructions and suggested serving size. "
              f"Format it clearly with a recipe name, ingredients list, and steps.")
    return call_gemini_api(prompt)

def remix_recipe(current_recipe, modifications):
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

def run_recipe_remix_master():
    """
    Runs the AI Recipe Remix Master.
    """
    print("Welcome to the AI Recipe Remix Master!")
    print("I'll help you generate and remix recipes based on your ingredients and preferences.")
    print("Type 'quit' to exit at any time.\n")

    current_recipe = ""

    while True:
        if not current_recipe:
            ingredients_input = input("Enter a comma-separated list of ingredients you have (e.g., chicken, broccoli, pasta): ").strip()
            if ingredients_input.lower() == 'quit':
                print("Exiting Recipe Remix Master. Goodbye!")
                break
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