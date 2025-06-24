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
            "**Pasta Water Setup**: Fill a large pot (at least 6 quarts) with cold water and place it on the stove. Add 1 tablespoon of salt per 4 quarts of water (about 2 tablespoons total for a large pot). The water should taste like seawater - this is crucial for flavoring the pasta. Bring to a rolling boil over high heat (this will take about 8-10 minutes).",
            "**Pasta Cooking**: Once water is boiling vigorously (large bubbles breaking the surface), add spaghetti all at once. Stir immediately with tongs to prevent sticking. Cook according to package directions (usually 8-10 minutes for al dente). To test doneness, bite a piece - it should be firm but not crunchy, with a slight resistance in the center. Reserve 1 cup of the hot pasta water before draining - this starchy water is essential for creating the creamy sauce.",
            "**Guanciale Preparation**: While pasta cooks, cut guanciale into 1/4-inch cubes. Heat a large skillet (12-inch or larger) over medium heat (325°F/163°C) for 2 minutes. Add guanciale cubes in a single layer and cook undisturbed for 3-4 minutes until bottom is golden brown. Stir and continue cooking for another 4-5 minutes until all pieces are crispy and golden brown. Guanciale should be rendered and crispy, with about 2-3 tablespoons of golden fat remaining in the pan. Remove from heat but keep the rendered fat in the pan.",
            "**Egg Mixture Preparation**: In a medium bowl, crack 4 large eggs at room temperature (cold eggs can cause scrambling). Add 1 cup freshly grated pecorino romano cheese and 1 teaspoon freshly ground black pepper. Whisk vigorously until well combined and slightly frothy. The mixture should be smooth with no lumps. Set aside at room temperature.",
            "**Pasta Assembly**: When pasta is done, drain it quickly in a colander, shaking to remove excess water. Immediately add the hot pasta to the skillet with guanciale and rendered fat. Working quickly, toss pasta with tongs to coat evenly with the fat. The pasta should glisten with the fat coating.",
            "**Sauce Creation**: Remove skillet from heat completely (this is crucial to prevent scrambled eggs). Immediately pour in the egg mixture, stirring constantly in a circular motion with tongs or a wooden spoon. The heat from the pasta should gently cook the eggs into a creamy sauce. If eggs start to scramble, remove from heat immediately and stir faster.",
            "**Sauce Adjustment**: Add reserved pasta water gradually, starting with 1/4 cup. Stir constantly until absorbed, then add more as needed. You'll likely use 1/2 to 3/4 cup total. The sauce should be silky and creamy, coating each strand of pasta without being runny. If it's too thick, add more water; if too thin, cook briefly over low heat.",
            "**Final Seasoning**: Taste and adjust seasoning. Add more salt if needed (remember the pasta water was salted), and more black pepper for heat. The dish should be well-seasoned but not overly salty.",
            "**Serving**: Serve immediately in warm bowls while hot. The pasta should be creamy and steaming. Garnish with extra grated pecorino cheese and freshly ground black pepper on top. Do not let it sit - the sauce will thicken and become gluey."
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
            "**Oven Setup**: Preheat oven to 400°F (200°C). Line a large baking sheet (18x13 inches) with parchment paper for easy cleanup and even cooking. The parchment prevents sticking and ensures even browning.",
            "**Quinoa Preparation**: Measure 1 cup quinoa and rinse thoroughly in a fine-mesh strainer under cold running water for 2-3 minutes until water runs clear (this removes the bitter saponin coating). Drain well. In a medium saucepan, combine rinsed quinoa with 2 cups cold water and 1/4 teaspoon salt. Bring to a boil over high heat, then reduce to low heat, cover, and simmer for 15-20 minutes. Quinoa is done when all water is absorbed and you can see little white 'tails' on the grains. Fluff with a fork and set aside covered to keep warm.",
            "**Sweet Potato Preparation**: Wash and peel 1 large sweet potato. Cut into 1-inch cubes (uniform size ensures even cooking). Place cubes in a large bowl and toss with 1 tablespoon olive oil, 1/2 teaspoon salt, 1/2 teaspoon black pepper, 1/2 teaspoon ground cumin, and 1/2 teaspoon smoked paprika. Use your hands to ensure even coating. Spread cubes in a single layer on the prepared baking sheet, leaving space between pieces for even roasting.",
            "**Sweet Potato Roasting**: Place baking sheet in preheated oven on the middle rack. Roast for 15 minutes, then remove from oven and flip each cube with a spatula (this ensures even browning on all sides). Return to oven and roast for another 10-15 minutes until tender and slightly caramelized. Sweet potatoes should be fork-tender with golden edges and slightly crispy corners when done. Total roasting time: 25-30 minutes.",
            "**Chickpea Preparation**: While sweet potatoes roast, drain and rinse 1 can (15 oz) chickpeas in a colander. Pat dry with paper towels to remove excess moisture (this helps them crisp up). Heat remaining 1 tablespoon olive oil in a large skillet over medium heat (325°F/163°C) for 1 minute until oil is hot but not smoking.",
            "**Garlic and Chickpea Cooking**: Add 2 cloves minced garlic to the hot oil and cook for exactly 30 seconds, stirring constantly, until fragrant but not browned (garlic should smell aromatic, not burnt). Immediately add dried chickpeas and cook for 5-7 minutes, stirring occasionally, until golden and slightly crispy. Chickpeas should have a golden-brown exterior and be slightly crunchy but not hard. Remove from heat and set aside.",
            "**Kale Preparation**: Wash 2 cups kale thoroughly under cold water. Remove tough stems by holding the stem and pulling the leaves off with your other hand. Tear leaves into bite-sized pieces. In a large bowl, combine kale with juice from 1 medium lemon (about 2 tablespoons) and remaining 1/2 teaspoon salt. Massage kale with your hands for 2-3 minutes until leaves are softened and reduced in volume by about half. Kale should be dark green, tender, and slightly wilted but not mushy.",
            "**Bowl Assembly**: Divide warm quinoa evenly between 2 large bowls (about 1 cup each). Arrange roasted sweet potatoes, crispy chickpeas, and massaged kale in separate sections on top of the quinoa for visual appeal. Slice 1 medium avocado and arrange slices on top. The bowl should look colorful and appetizing with distinct sections.",
            "**Final Seasoning**: Drizzle each bowl with 1 teaspoon additional olive oil and season with remaining black pepper to taste. The dish should be well-seasoned but not overly salty. Serve immediately while warm for best flavor and texture."
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
            "**Chicken Preparation**: Place 1 pound chicken breast on a cutting board. Using a sharp knife, slice chicken breast into thin, uniform strips (about 1/4 inch thick and 2-3 inches long). Cut against the grain (across the muscle fibers) for tender results. Place strips in a medium bowl and add 1 tablespoon soy sauce and 1 teaspoon cornstarch. Use your hands to toss and coat evenly. Let marinate at room temperature for 10 minutes (this tenderizes the chicken and helps it brown better).",
            "**Vegetable Preparation**: While chicken marinates, prepare all vegetables: Cut 2 cups broccoli into small florets (about 1-inch pieces) and trim any tough stems. Slice 2 medium bell peppers into thin strips (1/4 inch wide and 2-3 inches long). Mince 3 cloves garlic finely (you should have about 1 tablespoon). Peel and grate 1 tablespoon fresh ginger (if using fresh, peel the skin first with a spoon). Have everything ready before cooking starts - stir-frying is fast-paced.",
            "**High Heat Setup**: Heat 1 tablespoon vegetable oil in a wok or large skillet (12-inch or larger) over high heat for 2-3 minutes until very hot. The oil should shimmer and start to smoke slightly (about 450°F/232°C). The pan should be smoking hot for authentic stir-fry texture. If using an electric stove, you may need to preheat longer.",
            "**Chicken Cooking**: Add marinated chicken strips in a single layer (don't overcrowd - cook in batches if needed). Let cook undisturbed for 2-3 minutes until bottom is golden brown, then stir-fry for another 3-4 minutes until chicken is opaque throughout with no pink centers. Chicken should be golden brown and cooked through. Remove chicken to a clean plate and set aside. The pan should still be very hot.",
            "**Aromatics**: Add remaining 1 tablespoon vegetable oil to the same pan (it should still be very hot). Immediately add minced garlic and grated ginger, stir for exactly 30 seconds until fragrant (they should smell aromatic, not burnt). If they start to brown too quickly, reduce heat slightly.",
            "**Vegetable Cooking**: Add broccoli florets and bell pepper strips to the pan. Stir-fry for 2-3 minutes, tossing constantly with tongs or a spatula, until vegetables are crisp-tender but still bright in color. Broccoli should be bright green and slightly crunchy, peppers should be softened but not mushy. If vegetables start to stick, add 1-2 tablespoons water.",
            "**Sauce Assembly**: Return cooked chicken to the pan. Add remaining 2 tablespoons soy sauce, 1 tablespoon sesame oil, 1 tablespoon rice vinegar, 1 teaspoon honey, and 1/4 teaspoon red pepper flakes (if using). Toss everything together for 1-2 minutes until sauce coats all ingredients evenly and chicken is heated through.",
            "**Final Touch**: Taste and adjust seasoning if needed. The dish should be well-seasoned with a balance of salty, sweet, and umami flavors. Serve immediately over steamed rice or noodles while hot. The dish should be steaming and aromatic with vegetables still bright and crisp."
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
            "**Oven Setup**: Preheat oven to 400°F (200°C). Line a large baking sheet (18x13 inches) with parchment paper for easy cleanup and even cooking. The parchment prevents sticking and ensures even heat distribution. Position oven rack in the middle for even cooking.",
            "**Salmon Preparation**: Remove 4 salmon fillets from packaging and pat completely dry with paper towels (this ensures proper seasoning adherence and crispy skin). Check for and remove any pin bones with clean tweezers if present (run your finger along the flesh to feel for small bones). Place fillets on a clean cutting board skin-side down.",
            "**Pan Preparation**: Place salmon fillets skin-side down on the prepared baking sheet, spacing them evenly (about 2 inches apart) for proper air circulation. Don't overcrowd the pan - this ensures even cooking and crispy skin. The fillets should not touch each other.",
            "**Seasoning**: Drizzle each fillet with 1/2 tablespoon olive oil (2 tablespoons total divided among 4 fillets). Season generously with salt and pepper on both sides (about 1/4 teaspoon each per fillet). Sprinkle 1/4 teaspoon dried oregano and 1/4 teaspoon dried thyme evenly over the top of each fillet. The seasoning should be visible but not overwhelming.",
            "**Topping Assembly**: Distribute 4 cloves minced garlic evenly over each fillet (about 1 clove per fillet). Slice 2 medium lemons into thin rounds and place 2-3 slices on each fillet. Halve 1 cup cherry tomatoes and scatter over fillets. Halve 1/2 cup kalamata olives and distribute evenly. Arrange toppings for visual appeal - the dish should look colorful and appetizing.",
            "**Baking**: Place baking sheet in preheated oven on the middle rack. Bake for 12-15 minutes, depending on thickness (thicker fillets need longer). Salmon is done when it flakes easily with a fork and reaches 145°F (63°C) internal temperature. The flesh should be opaque and slightly pink in the center, not translucent. If you don't have a thermometer, the fish should flake easily when pressed with a fork.",
            "**Resting**: Remove from oven and let rest for 5 minutes on the baking sheet to allow juices to redistribute. This prevents the salmon from drying out when cut and ensures moist, tender fish. Don't cover - this would make the skin soggy.",
            "**Garnishing**: While salmon rests, chop 1/4 cup fresh parsley finely. Garnish each fillet with fresh parsley and 2 tablespoons crumbled feta cheese if desired. The dish should look colorful and appetizing with bright herbs and white cheese.",
            "**Serving**: Serve immediately with additional lemon wedges and your choice of side dishes. The salmon should be moist and flavorful with crispy skin and tender flesh. The dish should be hot and aromatic."
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
            "**Oven Setup**: Preheat oven to 375°F (190°C). Line 2 large baking sheets (18x13 inches) with parchment paper or silicone baking mats for easy removal and even baking. Position oven racks in the upper and lower thirds of the oven for even baking if making multiple batches.",
            "**Dry Ingredients**: In a medium bowl, measure 2.25 cups all-purpose flour by spooning flour into the measuring cup and leveling with a knife (don't scoop directly from the bag - this compacts the flour). Add 1 teaspoon baking soda and 1 teaspoon fine sea salt. Whisk together until well combined and no lumps remain. This ensures even distribution of leavening agents. Set aside.",
            "**Butter Preparation**: Ensure 1 cup (2 sticks) unsalted butter is softened to room temperature (about 65-70°F). Butter should be soft enough to leave an indentation when pressed but not melted. If butter is too cold, microwave in 10-second intervals until soft. If too soft, refrigerate briefly.",
            "**Butter Creaming**: In a large bowl using an electric mixer fitted with paddle attachment, cream together softened butter, 3/4 cup packed brown sugar, and 3/4 cup granulated white sugar on medium speed (speed 4-5) until light and fluffy (about 3-4 minutes). The mixture should be pale yellow and airy when done. Scrape down the sides of the bowl with a rubber spatula halfway through.",
            "**Egg Addition**: Add 2 large eggs one at a time, beating well after each addition on medium speed (about 30 seconds per egg). Scrape down the sides of the bowl after each egg to ensure even mixing. The mixture should be smooth and well combined with no streaks of egg visible.",
            "**Vanilla Addition**: Beat in 2 teaspoons pure vanilla extract until well combined (about 30 seconds). Use pure vanilla extract for best flavor - imitation vanilla will give an artificial taste.",
            "**Dry Ingredient Incorporation**: Gradually add the dry ingredients to the wet ingredients in 3 additions, mixing on low speed (speed 2) until just combined after each addition. Do not overmix - this develops gluten and makes cookies tough. The dough should be soft but not sticky. If dough is too sticky, add 1-2 tablespoons flour.",
            "**Chocolate Addition**: Add 2 cups semi-sweet chocolate chips and 1 cup chopped walnuts (if using) to the dough. Fold in gently with a rubber spatula until evenly distributed throughout the dough. Don't use the mixer for this step - it would break up the chocolate chips.",
            "**Cookie Formation**: Using a 1.5-tablespoon cookie scoop or rounded tablespoon, drop dough onto prepared baking sheets, spacing cookies about 2 inches apart for proper spreading. Don't overcrowd the baking sheets - cookies need space to spread. You should get about 12 cookies per sheet.",
            "**Baking**: Bake for 9-11 minutes, rotating baking sheets halfway through (top to bottom and front to back) for even baking, until edges are golden brown but centers are still soft. Cookies should be slightly underdone when removed from oven - they will continue cooking on the hot baking sheet. If you prefer crispier cookies, bake 1-2 minutes longer.",
            "**Cooling**: Remove from oven and let cookies cool on baking sheets for exactly 5 minutes (this allows them to set without becoming too hard). Then transfer to wire racks to cool completely. Don't try to move cookies too soon - they will fall apart. Store in an airtight container at room temperature for up to 1 week."
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
            "**Broth Preparation**: Pour 6 cups vegetable broth into a medium saucepan and heat over low heat until warm (about 150°F/65°C). Keep warm throughout cooking - cold broth will shock the rice and prevent proper cooking. The broth should be steaming but not boiling. Cover with a lid to maintain temperature.",
            "**Mushroom Preparation**: Clean 1 pound mixed mushrooms by gently wiping with a damp paper towel (don't rinse under water - they absorb too much moisture). Slice mushrooms into 1/4-inch thick pieces. Heat 1 tablespoon olive oil and 1 tablespoon butter in a large, heavy-bottomed pot (Dutch oven works well) over medium heat (325°F/163°C) for 1 minute until butter is melted and oil is hot.",
            "**Mushroom Cooking**: Add sliced mushrooms to the hot oil and butter. Cook for 8-10 minutes, stirring occasionally, until mushrooms are deeply browned and all moisture has evaporated. Mushrooms should be golden brown and slightly crispy, with no liquid remaining in the pan. Remove mushrooms to a clean plate and set aside. Don't wash the pan - the browned bits add flavor.",
            "**Aromatics**: In the same pot, add remaining 1 tablespoon olive oil and 1 tablespoon butter. Heat over medium heat until butter is melted. Add 1 medium onion, finely diced, and cook for 5 minutes, stirring occasionally, until translucent and soft (onion should be clear, not browned). The onion should be very soft and sweet.",
            "**Garlic Addition**: Add 3 cloves minced garlic to the softened onions and cook for exactly 1 minute, stirring constantly, until fragrant (garlic should smell aromatic, not burnt). If garlic starts to brown too quickly, reduce heat slightly.",
            "**Rice Toasting**: Add 1.5 cups arborio rice to the pot and stir for 2-3 minutes until rice is translucent around the edges (this toasts the rice and enhances flavor). Rice should have a pearly appearance and smell slightly nutty. Don't let it brown - just toast until translucent.",
            "**Wine Deglazing**: Pour in 1/2 cup dry white wine and stir constantly until liquid is completely absorbed (about 2 minutes). The wine should be completely absorbed before adding broth. The rice should smell slightly alcoholic and be slightly sticky.",
            "**Broth Addition**: Begin adding warm broth 1/2 cup at a time, stirring constantly with a wooden spoon in a figure-8 motion. Allow each addition to be completely absorbed before adding more. This slow process creates the creamy texture. The rice should always be covered with liquid but not swimming in it.",
            "**Cooking Process**: Continue adding broth and stirring for 18-20 minutes until rice is creamy and al dente (firm but not hard in the center). The risotto should be creamy but still have some bite. You may not need all 6 cups of broth - stop when rice is done. The mixture should be thick and creamy, not soupy.",
            "**Final Assembly**: Remove from heat and immediately stir in remaining 1 tablespoon butter, 1 cup grated parmesan cheese, cooked mushrooms, and 1 teaspoon fresh thyme. The heat from the risotto will melt the cheese and butter. Stir until cheese is melted and mixture is creamy.",
            "**Resting**: Cover pot with a lid and let rest for 2 minutes (this allows flavors to meld and cheese to fully incorporate). Don't stir during this time - let it rest undisturbed.",
            "**Final Seasoning**: Uncover and stir gently. Taste and season with salt and pepper to taste (remember the broth and cheese are salty). The risotto should be well-seasoned but not overly salty. If it's too thick, add a splash of warm broth.",
            "**Serving**: Serve immediately in warm bowls while hot. The risotto should be creamy and steaming. Garnish with extra parmesan cheese on top. Risotto thickens as it cools, so serve immediately for best texture."
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
    },
    {
        "name": "Vegan Chocolate Avocado Mousse",
        "ingredients": [
            {"item": "ripe avocados", "amount": 2, "unit": "large", "notes": "very ripe, soft to touch"},
            {"item": "dark chocolate", "amount": 6, "unit": "ounces", "notes": "70% cocoa, dairy-free"},
            {"item": "maple syrup", "amount": 1/3, "unit": "cup", "notes": "pure maple syrup"},
            {"item": "cocoa powder", "amount": 2, "unit": "tablespoons", "notes": "unsweetened"},
            {"item": "vanilla extract", "amount": 1, "unit": "teaspoon", "notes": "pure vanilla extract"},
            {"item": "almond milk", "amount": 1/4, "unit": "cup", "notes": "unsweetened"},
            {"item": "salt", "amount": 1/8, "unit": "teaspoon", "notes": "fine sea salt"},
            {"item": "fresh berries", "amount": 1, "unit": "cup", "notes": "for garnish (strawberries, raspberries)"},
            {"item": "coconut whipped cream", "amount": 1/2, "unit": "cup", "notes": "optional, for topping"}
        ],
        "instructions": [
            "**Chocolate Melting**: Chop 6 ounces dark chocolate into small, uniform pieces (about 1/4-inch chunks) for even melting. Place in a heatproof bowl. Create a double boiler by filling a medium saucepan with 1 inch of water and bringing to a gentle simmer over medium heat (water should bubble but not boil vigorously). Place the bowl of chocolate over the simmering water, ensuring the bottom of the bowl doesn't touch the water. Stir chocolate constantly with a rubber spatula until completely melted and smooth (about 3-5 minutes). Remove from heat and let cool for 5 minutes to room temperature.",
            "**Avocado Preparation**: Cut 2 large ripe avocados in half lengthwise and remove pits. Scoop flesh into a food processor or high-powered blender. Avocados should be very ripe (dark green to black skin, soft when gently squeezed) for the smoothest texture. If avocados aren't ripe enough, the mousse will have a grainy texture.",
            "**Base Mixture**: Add 1/3 cup pure maple syrup, 2 tablespoons unsweetened cocoa powder, 1 teaspoon pure vanilla extract, 1/4 cup unsweetened almond milk, and 1/8 teaspoon fine sea salt to the food processor with the avocados. Process on high speed for 2-3 minutes, scraping down the sides with a rubber spatula every 30 seconds, until completely smooth and creamy. The mixture should be velvety with no lumps or avocado chunks visible.",
            "**Chocolate Incorporation**: With the food processor running on low speed, slowly pour the cooled melted chocolate through the feed tube in a steady stream. Continue processing for 1-2 minutes until chocolate is fully incorporated and the mixture is smooth and glossy. The mousse should be thick and creamy, similar to traditional chocolate mousse consistency.",
            "**Taste Testing**: Stop the processor and taste the mousse. If it needs more sweetness, add 1-2 tablespoons additional maple syrup and process for 30 seconds. If it's too thick, add 1-2 tablespoons additional almond milk and process briefly. The mousse should be rich and chocolatey with a subtle avocado undertone.",
            "**Chilling**: Transfer mousse to a clean bowl and cover tightly with plastic wrap, pressing the wrap directly onto the surface of the mousse to prevent a skin from forming. Refrigerate for at least 2 hours, or up to 24 hours, until well chilled and set. The mousse will firm up slightly as it chills.",
            "**Garnish Preparation**: While mousse chills, wash and dry 1 cup fresh berries. Hull strawberries if using, and cut larger berries in half for easier eating. Keep berries refrigerated until ready to serve.",
            "**Serving**: Remove mousse from refrigerator 10 minutes before serving to allow it to soften slightly. Spoon mousse into 4-6 serving glasses or bowls, creating a smooth, rounded top. Garnish each serving with fresh berries and a dollop of coconut whipped cream if desired. The mousse should be smooth, creamy, and decadent with a rich chocolate flavor.",
            "**Storage**: Cover any remaining mousse tightly and refrigerate for up to 3 days. The mousse will keep well but may darken slightly over time due to avocado oxidation."
        ],
        "prep_time": 20,
        "cook_time": 0,
        "total_time": 140,
        "servings": 4,
        "difficulty": "easy",
        "cuisine": "vegan",
        "tags": ["dessert", "vegan", "chocolate", "healthy", "gluten-free"],
        "tips": [
            "Use very ripe avocados for the smoothest texture",
            "Melt chocolate slowly to prevent burning",
            "Chill thoroughly for best consistency",
            "Serve with fresh berries for contrast"
        ]
    },
    {
        "name": "Classic New York Cheesecake",
        "ingredients": [
            {"item": "graham crackers", "amount": 1.5, "unit": "cups", "notes": "crushed into fine crumbs"},
            {"item": "butter", "amount": 1/3, "unit": "cup", "notes": "unsalted, melted"},
            {"item": "sugar", "amount": 1/4, "unit": "cup", "notes": "granulated, for crust"},
            {"item": "cream cheese", "amount": 4, "unit": "8-ounce packages", "notes": "full-fat, room temperature"},
            {"item": "sugar", "amount": 1.25, "unit": "cups", "notes": "granulated, for filling"},
            {"item": "eggs", "amount": 4, "unit": "large", "notes": "room temperature"},
            {"item": "egg yolks", "amount": 2, "unit": "large", "notes": "room temperature"},
            {"item": "vanilla extract", "amount": 2, "unit": "teaspoons", "notes": "pure vanilla extract"},
            {"item": "lemon juice", "amount": 1, "unit": "tablespoon", "notes": "fresh squeezed"},
            {"item": "sour cream", "amount": 1, "unit": "cup", "notes": "full-fat, room temperature"},
            {"item": "salt", "amount": 1/4, "unit": "teaspoon", "notes": "fine sea salt"},
            {"item": "fresh berries", "amount": 2, "unit": "cups", "notes": "for garnish (strawberries, blueberries)"}
        ],
        "instructions": [
            "**Oven Setup**: Preheat oven to 350°F (175°C). Position oven rack in the center. Wrap the outside of a 9-inch springform pan with heavy-duty aluminum foil (this prevents water from seeping in during water bath baking). The foil should extend up the sides of the pan by at least 2 inches. Grease the inside of the pan with butter or non-stick cooking spray.",
            "**Crust Preparation**: Place 1.5 cups graham cracker crumbs in a medium bowl. Add 1/4 cup granulated sugar and stir to combine. Pour in 1/3 cup melted butter and mix with a fork until all crumbs are evenly moistened. The mixture should hold together when pressed but not be soggy. If too dry, add 1 tablespoon additional melted butter.",
            "**Crust Formation**: Press the crumb mixture firmly and evenly into the bottom of the prepared springform pan using the bottom of a measuring cup or glass. Press the crumbs up the sides of the pan about 1 inch to create a rim. The crust should be compact and even. Bake the crust for 10 minutes until lightly golden and fragrant. Remove from oven and let cool completely on a wire rack while preparing the filling.",
            "**Cream Cheese Preparation**: Ensure 4 packages (32 ounces total) cream cheese are at room temperature (about 70°F) for at least 2 hours. Room temperature cream cheese is crucial for a smooth, lump-free filling. Cut cream cheese into 1-inch cubes and place in a large mixing bowl.",
            "**Cream Cheese Beating**: Using an electric mixer fitted with paddle attachment, beat cream cheese on medium speed (speed 4) for 2-3 minutes until completely smooth and creamy. Scrape down the sides and bottom of the bowl with a rubber spatula every 30 seconds to ensure even mixing. The cream cheese should be completely smooth with no lumps.",
            "**Sugar Addition**: Gradually add 1.25 cups granulated sugar while continuing to beat on medium speed. Beat for 2-3 minutes until sugar is completely dissolved and mixture is light and fluffy. The mixture should be pale yellow and airy. Scrape down the bowl again to ensure even mixing.",
            "**Egg Incorporation**: Add 4 large eggs and 2 large egg yolks one at a time, beating well after each addition on medium speed (about 30 seconds per egg). Scrape down the bowl after each egg. The mixture should remain smooth and creamy throughout this process. Don't overbeat - this can incorporate too much air and cause cracking.",
            "**Flavoring**: Beat in 2 teaspoons pure vanilla extract, 1 tablespoon fresh lemon juice, and 1/4 teaspoon fine sea salt until well combined (about 30 seconds). The lemon juice adds brightness and helps balance the richness.",
            "**Sour Cream Addition**: Add 1 cup room temperature sour cream and beat on low speed just until combined (about 30 seconds). Don't overmix at this stage - overmixing can cause the cheesecake to crack during baking.",
            "**Water Bath Setup**: Bring a large pot of water to a boil. Place the springform pan in a large roasting pan or baking dish. Pour the cheesecake batter into the cooled crust, smoothing the top with a rubber spatula. Carefully pour boiling water into the roasting pan around the springform pan until it reaches halfway up the sides of the springform pan.",
            "**Baking**: Bake for 60-75 minutes until the center is almost set but still slightly jiggly when gently shaken. The edges should be set and slightly golden. The center should have a slight wobble but not be liquid. If the top starts to brown too quickly, tent with aluminum foil.",
            "**Cooling**: Turn off the oven and leave the cheesecake in the oven with the door slightly ajar for 1 hour. This gradual cooling prevents cracking. Remove from water bath and let cool completely on a wire rack for 2 hours. Cover and refrigerate for at least 4 hours, or overnight, before serving.",
            "**Serving**: Remove from refrigerator 30 minutes before serving. Run a thin knife around the edge of the pan to loosen, then remove the springform ring. Garnish with fresh berries and serve in thin slices. The cheesecake should be creamy, smooth, and perfectly set."
        ],
        "prep_time": 30,
        "cook_time": 75,
        "total_time": 285,
        "servings": 12,
        "difficulty": "medium",
        "cuisine": "american",
        "tags": ["dessert", "cheesecake", "baking", "classic", "indulgent"],
        "tips": [
            "Use room temperature ingredients for smooth texture",
            "Don't overmix the filling to prevent cracking",
            "Use a water bath for even baking",
            "Cool gradually to prevent cracks"
        ]
    },
    {
        "name": "Vegan Apple Cinnamon Muffins",
        "ingredients": [
            {"item": "all-purpose flour", "amount": 2, "unit": "cups", "notes": "spooned and leveled"},
            {"item": "baking powder", "amount": 2, "unit": "teaspoons", "notes": ""},
            {"item": "baking soda", "amount": 1/2, "unit": "teaspoon", "notes": ""},
            {"item": "salt", "amount": 1/2, "unit": "teaspoon", "notes": "fine sea salt"},
            {"item": "cinnamon", "amount": 2, "unit": "teaspoons", "notes": "ground"},
            {"item": "nutmeg", "amount": 1/4, "unit": "teaspoon", "notes": "ground"},
            {"item": "applesauce", "amount": 1/2, "unit": "cup", "notes": "unsweetened"},
            {"item": "coconut oil", "amount": 1/3, "unit": "cup", "notes": "melted and cooled"},
            {"item": "maple syrup", "amount": 1/2, "unit": "cup", "notes": "pure maple syrup"},
            {"item": "vanilla extract", "amount": 1, "unit": "teaspoon", "notes": "pure vanilla extract"},
            {"item": "almond milk", "amount": 1/2, "unit": "cup", "notes": "unsweetened"},
            {"item": "apples", "amount": 2, "unit": "medium", "notes": "peeled, cored, and diced into 1/4-inch pieces"},
            {"item": "brown sugar", "amount": 1/4, "unit": "cup", "notes": "for topping"},
            {"item": "cinnamon", "amount": 1, "unit": "teaspoon", "notes": "for topping"}
        ],
        "instructions": [
            "**Oven Setup**: Preheat oven to 375°F (190°C). Line a 12-cup muffin tin with paper liners or grease generously with coconut oil. Position oven rack in the center for even baking. The oven should be fully preheated before adding muffins.",
            "**Dry Ingredients**: In a large bowl, measure 2 cups all-purpose flour by spooning flour into the measuring cup and leveling with a knife. Add 2 teaspoons baking powder, 1/2 teaspoon baking soda, 1/2 teaspoon fine sea salt, 2 teaspoons ground cinnamon, and 1/4 teaspoon ground nutmeg. Whisk together until well combined and no lumps remain. This ensures even distribution of leavening agents and spices.",
            "**Apple Preparation**: Peel, core, and dice 2 medium apples into 1/4-inch pieces. Use firm, tart apples like Granny Smith or Honeycrisp for best texture and flavor. The apples should be uniform in size for even distribution throughout the muffins. Set aside in a small bowl.",
            "**Wet Ingredients**: In a medium bowl, combine 1/2 cup unsweetened applesauce, 1/3 cup melted and cooled coconut oil, 1/2 cup pure maple syrup, 1 teaspoon pure vanilla extract, and 1/2 cup unsweetened almond milk. Whisk together until smooth and well combined. The coconut oil should be liquid but not hot to avoid cooking the ingredients.",
            "**Batter Assembly**: Make a well in the center of the dry ingredients. Pour the wet ingredients into the well and gently fold together with a rubber spatula until just combined. The batter should be thick but not dry. Don't overmix - this develops gluten and makes muffins tough. A few small lumps are okay.",
            "**Apple Addition**: Gently fold in the diced apples until evenly distributed throughout the batter. The apples should be well distributed but not broken up. The batter should be thick enough to hold the apple pieces in suspension.",
            "**Muffin Formation**: Using a 1/4-cup measuring cup or large spoon, divide batter evenly among the 12 muffin cups, filling each about 3/4 full. The muffins should be uniform in size for even baking. Don't overfill - muffins need room to rise.",
            "**Topping Preparation**: In a small bowl, combine 1/4 cup brown sugar and 1 teaspoon ground cinnamon. Mix well with a fork until evenly combined. Sprinkle about 1 teaspoon of the mixture evenly over each muffin. The topping should be evenly distributed for consistent flavor.",
            "**Baking**: Bake for 18-22 minutes, rotating the muffin tin halfway through (front to back) for even baking, until a toothpick inserted into the center of a muffin comes out clean with just a few moist crumbs. The muffins should be golden brown on top and spring back when lightly pressed. If muffins are browning too quickly, tent with aluminum foil for the last 5 minutes.",
            "**Cooling**: Remove from oven and let muffins cool in the tin for 5 minutes. Then transfer to a wire rack to cool completely. Don't try to remove muffins too soon - they will stick to the liners. The muffins should be firm but tender when cooled.",
            "**Serving**: Serve warm or at room temperature. The muffins should be moist, tender, and full of apple and cinnamon flavor. Store in an airtight container at room temperature for up to 3 days, or freeze for up to 2 months."
        ],
        "prep_time": 20,
        "cook_time": 20,
        "total_time": 40,
        "servings": 12,
        "difficulty": "easy",
        "cuisine": "vegan",
        "tags": ["dessert", "vegan", "muffins", "breakfast", "apple", "cinnamon"],
        "tips": [
            "Use room temperature ingredients for best results",
            "Don't overmix the batter to keep muffins tender",
            "Use firm apples for better texture",
            "Let muffins cool completely before storing"
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