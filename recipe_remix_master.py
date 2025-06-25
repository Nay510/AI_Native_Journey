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
            "Fill a large pot with water and bring to a boil. Add salt to taste.",
            "Cook spaghetti according to package directions until al dente. Reserve 1 cup of pasta water.",
            "In a large skillet, cook guanciale over medium heat until crispy and golden brown.",
            "Remove skillet from heat and add hot pasta to the pan with guanciale.",
            "In a bowl, whisk together eggs, grated cheese, and black pepper.",
            "Quickly pour egg mixture over hot pasta, stirring constantly to create a creamy sauce.",
            "Add reserved pasta water gradually if needed to achieve desired consistency.",
            "Serve immediately with extra cheese and black pepper on top."
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
            "Preheat oven to 400°F (200°C). Line a baking sheet with parchment paper.",
            "Cook quinoa according to package directions. Set aside to keep warm.",
            "Toss sweet potato cubes with 1 tablespoon olive oil, salt, pepper, cumin, and paprika.",
            "Spread sweet potatoes on baking sheet and roast for 25-30 minutes until tender.",
            "In a skillet, heat remaining olive oil and cook garlic for 30 seconds until fragrant.",
            "Add chickpeas and cook for 5-7 minutes until golden and slightly crispy.",
            "Massage kale with lemon juice and salt until softened.",
            "Assemble bowls with quinoa, roasted sweet potatoes, crispy chickpeas, and kale.",
            "Top with sliced avocado and serve immediately."
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
            "Slice chicken breast into thin strips and marinate with 1 tablespoon soy sauce and cornstarch for 10 minutes.",
            "Heat 1 tablespoon vegetable oil in a wok or large skillet over high heat.",
            "Add chicken and stir-fry for 5-7 minutes until cooked through. Remove to a plate.",
            "Add remaining oil to the same pan and cook garlic and ginger for 30 seconds until fragrant.",
            "Add broccoli and bell peppers, stir-fry for 2-3 minutes until crisp-tender.",
            "Return chicken to pan and add remaining soy sauce, sesame oil, rice vinegar, honey, and red pepper flakes.",
            "Toss everything together for 1-2 minutes until sauce coats all ingredients.",
            "Serve immediately over steamed rice or noodles."
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
            "Preheat oven to 400°F (200°C). Line a baking sheet with parchment paper.",
            "Pat salmon fillets dry and place skin-side down on the prepared baking sheet.",
            "Drizzle each fillet with olive oil and season with salt, pepper, oregano, and thyme.",
            "Sprinkle minced garlic over each fillet and arrange lemon slices on top.",
            "Scatter cherry tomatoes and kalamata olives around the salmon.",
            "Bake for 12-15 minutes until salmon flakes easily with a fork.",
            "Let rest for 5 minutes, then garnish with fresh parsley and feta cheese.",
            "Serve immediately with additional lemon wedges."
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
            "Preheat oven to 375°F (190°C). Line baking sheets with parchment paper.",
            "In a medium bowl, whisk together flour, baking soda, and salt. Set aside.",
            "In a large bowl, cream together softened butter, brown sugar, and white sugar until light and fluffy.",
            "Add eggs one at a time, beating well after each addition. Beat in vanilla extract.",
            "Gradually add dry ingredients to wet ingredients, mixing until just combined.",
            "Fold in chocolate chips and walnuts (if using) until evenly distributed.",
            "Drop rounded tablespoons of dough onto prepared baking sheets, spacing 2 inches apart.",
            "Bake for 9-11 minutes until edges are golden brown but centers are still soft.",
            "Cool on baking sheets for 5 minutes, then transfer to wire racks to cool completely."
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
            "Store in an airtight container to keep them fresh"
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

# Fallback recipe templates for when API is not available
FALLBACK_RECIPES = {
    "pasta": {
        "name": "Simple Pasta Dish",
        "ingredients": [
            {"item": "pasta", "amount": 1, "unit": "pound", "notes": "any type"},
            {"item": "olive oil", "amount": 2, "unit": "tablespoons", "notes": "extra virgin"},
            {"item": "garlic", "amount": 3, "unit": "cloves", "notes": "minced"},
            {"item": "salt", "amount": 1, "unit": "teaspoon", "notes": "to taste"},
            {"item": "black pepper", "amount": 1, "unit": "teaspoon", "notes": "to taste"},
            {"item": "parmesan cheese", "amount": 1/2, "unit": "cup", "notes": "grated, optional"}
        ],
        "instructions": [
            "Bring a large pot of salted water to a boil.",
            "Cook pasta according to package directions until al dente.",
            "In a large skillet, heat olive oil over medium heat.",
            "Add minced garlic and cook for 1-2 minutes until fragrant.",
            "Add cooked pasta to the skillet and toss to coat with oil and garlic.",
            "Season with salt and black pepper to taste.",
            "Serve hot with grated parmesan cheese on top."
        ],
        "prep_time": 5,
        "cook_time": 15,
        "total_time": 20,
        "servings": 4,
        "difficulty": "easy",
        "cuisine": "italian",
        "tags": ["pasta", "quick", "simple", "dinner"]
    },
    "chicken": {
        "name": "Simple Chicken Dish",
        "ingredients": [
            {"item": "chicken breast", "amount": 1, "unit": "pound", "notes": "sliced into strips"},
            {"item": "olive oil", "amount": 2, "unit": "tablespoons", "notes": "for cooking"},
            {"item": "garlic", "amount": 2, "unit": "cloves", "notes": "minced"},
            {"item": "salt", "amount": 1, "unit": "teaspoon", "notes": "to taste"},
            {"item": "black pepper", "amount": 1, "unit": "teaspoon", "notes": "to taste"},
            {"item": "herbs", "amount": 1, "unit": "tablespoon", "notes": "dried oregano, thyme, or rosemary"}
        ],
        "instructions": [
            "Heat olive oil in a large skillet over medium-high heat.",
            "Season chicken strips with salt, black pepper, and herbs.",
            "Add chicken to the hot skillet and cook for 5-7 minutes per side until golden brown.",
            "Add minced garlic and cook for 1 minute until fragrant.",
            "Continue cooking until chicken is cooked through (no pink in center).",
            "Remove from heat and let rest for 5 minutes before serving."
        ],
        "prep_time": 10,
        "cook_time": 15,
        "total_time": 25,
        "servings": 4,
        "difficulty": "easy",
        "cuisine": "american",
        "tags": ["chicken", "quick", "healthy", "dinner"]
    },
    "vegetables": {
        "name": "Simple Vegetable Dish",
        "ingredients": [
            {"item": "mixed vegetables", "amount": 4, "unit": "cups", "notes": "broccoli, carrots, bell peppers, etc."},
            {"item": "olive oil", "amount": 2, "unit": "tablespoons", "notes": "extra virgin"},
            {"item": "garlic", "amount": 2, "unit": "cloves", "notes": "minced"},
            {"item": "salt", "amount": 1, "unit": "teaspoon", "notes": "to taste"},
            {"item": "black pepper", "amount": 1, "unit": "teaspoon", "notes": "to taste"},
            {"item": "lemon", "amount": 1, "unit": "medium", "notes": "juiced"}
        ],
        "instructions": [
            "Heat olive oil in a large skillet over medium heat.",
            "Add minced garlic and cook for 30 seconds until fragrant.",
            "Add mixed vegetables and stir-fry for 5-7 minutes until crisp-tender.",
            "Season with salt and black pepper to taste.",
            "Add lemon juice and toss to combine.",
            "Serve immediately while vegetables are still bright and crisp."
        ],
        "prep_time": 10,
        "cook_time": 10,
        "total_time": 20,
        "servings": 4,
        "difficulty": "easy",
        "cuisine": "vegetarian",
        "tags": ["vegetables", "healthy", "quick", "side dish"]
    }
}

# Cuisine transformation mappings
CUISINE_TRANSFORMATIONS = {
    "italian": {
        "spices": ["oregano", "basil", "rosemary", "thyme", "parmesan", "garlic"],
        "techniques": ["sauté", "braise", "simmer", "al dente"],
        "ingredients": ["olive oil", "tomatoes", "mozzarella", "pasta", "wine"],
        "description": "Italian cuisine focuses on fresh ingredients, olive oil, herbs, and simple preparation methods."
    },
    "mexican": {
        "spices": ["cumin", "chili powder", "oregano", "cayenne", "lime", "cilantro"],
        "techniques": ["grill", "braise", "slow cook", "char"],
        "ingredients": ["corn", "beans", "tortillas", "avocado", "jalapeños"],
        "description": "Mexican cuisine features bold flavors, corn-based ingredients, and spicy elements."
    },
    "asian": {
        "spices": ["ginger", "soy sauce", "sesame oil", "garlic", "chili", "lemongrass"],
        "techniques": ["stir-fry", "steam", "braise", "deep fry"],
        "ingredients": ["rice", "noodles", "tofu", "bamboo shoots", "water chestnuts"],
        "description": "Asian cuisine emphasizes balance, umami flavors, and quick cooking methods."
    },
    "indian": {
        "spices": ["turmeric", "cumin", "coriander", "cardamom", "ginger", "garam masala"],
        "techniques": ["curry", "tandoor", "slow cook", "temper"],
        "ingredients": ["rice", "lentils", "yogurt", "ghee", "naan"],
        "description": "Indian cuisine is known for its complex spice blends and vegetarian-friendly options."
    },
    "mediterranean": {
        "spices": ["oregano", "thyme", "rosemary", "lemon", "garlic", "olive oil"],
        "techniques": ["grill", "roast", "braise", "simmer"],
        "ingredients": ["olive oil", "tomatoes", "feta", "chickpeas", "fish"],
        "description": "Mediterranean cuisine emphasizes fresh vegetables, olive oil, and healthy fats."
    },
    "french": {
        "spices": ["thyme", "tarragon", "parsley", "shallots", "wine", "butter"],
        "techniques": ["braise", "sauté", "reduce", "deglaze"],
        "ingredients": ["butter", "wine", "shallots", "herbs", "cream"],
        "description": "French cuisine focuses on technique, rich sauces, and sophisticated flavor combinations."
    },
    "thai": {
        "spices": ["lemongrass", "fish sauce", "lime", "chili", "coconut milk", "basil"],
        "techniques": ["stir-fry", "curry", "steam", "grill"],
        "ingredients": ["rice", "coconut milk", "fish sauce", "lime", "peanuts"],
        "description": "Thai cuisine balances sweet, sour, salty, and spicy flavors with fresh herbs."
    },
    "japanese": {
        "spices": ["miso", "soy sauce", "dashi", "wasabi", "ginger", "mirin"],
        "techniques": ["steam", "grill", "tempura", "sushi"],
        "ingredients": ["rice", "noodles", "tofu", "seaweed", "mushrooms"],
        "description": "Japanese cuisine emphasizes umami, seasonal ingredients, and precise techniques."
    },
    "greek": {
        "spices": ["oregano", "lemon", "garlic", "dill", "mint", "olive oil"],
        "techniques": ["grill", "roast", "braise", "simmer"],
        "ingredients": ["olive oil", "feta", "yogurt", "lamb", "phyllo"],
        "description": "Greek cuisine features fresh herbs, olive oil, and Mediterranean ingredients."
    },
    "chinese": {
        "spices": ["soy sauce", "ginger", "garlic", "five spice", "star anise", "sesame oil"],
        "techniques": ["stir-fry", "steam", "braise", "deep fry"],
        "ingredients": ["rice", "noodles", "soy sauce", "bamboo shoots", "water chestnuts"],
        "description": "Chinese cuisine emphasizes balance, texture, and the five fundamental tastes."
    }
}

def format_instructions_concise(instructions: List[str]) -> str:
    """
    Format instructions in a concise, numbered format.
    """
    formatted_instructions = []
    for i, instruction in enumerate(instructions, 1):
        # Remove any existing numbering or formatting
        clean_instruction = instruction.strip()
        if clean_instruction.startswith('**'):
            # Remove markdown formatting
            clean_instruction = clean_instruction.replace('**', '').strip()
        
        # Make the instruction more concise
        if len(clean_instruction) > 100:
            # Split long instructions into shorter steps
            sentences = clean_instruction.split('. ')
            if len(sentences) > 1:
                for j, sentence in enumerate(sentences):
                    if sentence.strip():
                        formatted_instructions.append(f"{i + j}. {sentence.strip()}")
                i += len(sentences) - 1
            else:
                formatted_instructions.append(f"{i}. {clean_instruction}")
        else:
            formatted_instructions.append(f"{i}. {clean_instruction}")
    
    return '\n'.join(formatted_instructions)

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
    
    # Instructions section with concise formatting
    formatted += f"\n👨‍🍳 Instructions:\n"
    formatted += format_instructions_concise(recipe['instructions'])
    formatted += "\n"
    
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
    
    # If no matches found, try to use fallback recipes based on ingredient types
    print(f"\nNo exact matches found. Creating a recipe with {ingredients}...\n")
    
    # Determine the best fallback recipe based on ingredients
    fallback_key = "vegetables"  # default
    if any(ing in ["pasta", "spaghetti", "penne", "fettuccine", "linguine"] for ing in ingredients_list):
        fallback_key = "pasta"
    elif any(ing in ["chicken", "poultry", "breast", "thigh"] for ing in ingredients_list):
        fallback_key = "chicken"
    
    # Get the fallback recipe and customize it with the provided ingredients
    fallback_recipe = FALLBACK_RECIPES[fallback_key].copy()
    
    # Customize the recipe name and ingredients based on provided ingredients
    ingredient_names = [ing.title() for ing in ingredients_list]
    fallback_recipe["name"] = f"Simple {' '.join(ingredient_names[:3])} Dish"
    
    # Add the provided ingredients to the recipe
    custom_ingredients = []
    for ing in ingredients_list:
        if ing not in ["salt", "pepper", "oil", "olive oil", "garlic"]:
            custom_ingredients.append({"item": ing, "amount": 1, "unit": "cup", "notes": "as needed"})
    
    # Add basic cooking ingredients
    basic_ingredients = [
        {"item": "olive oil", "amount": 2, "unit": "tablespoons", "notes": "for cooking"},
        {"item": "garlic", "amount": 2, "unit": "cloves", "notes": "minced"},
        {"item": "salt", "amount": 1, "unit": "teaspoon", "notes": "to taste"},
        {"item": "black pepper", "amount": 1, "unit": "teaspoon", "notes": "to taste"}
    ]
    
    fallback_recipe["ingredients"] = custom_ingredients + basic_ingredients
    
    # Customize instructions based on the main ingredients
    if fallback_key == "pasta":
        fallback_recipe["instructions"] = [
            "Bring a large pot of salted water to a boil.",
            "Cook pasta according to package directions until al dente.",
            "In a large skillet, heat olive oil over medium heat.",
            "Add minced garlic and cook for 1-2 minutes until fragrant.",
            "Add your main ingredients and cook for 3-5 minutes until heated through.",
            "Add cooked pasta to the skillet and toss to combine.",
            "Season with salt and black pepper to taste.",
            "Serve hot with grated cheese on top if desired."
        ]
    elif fallback_key == "chicken":
        fallback_recipe["instructions"] = [
            "Heat olive oil in a large skillet over medium-high heat.",
            "Season chicken with salt and black pepper.",
            "Add chicken to the hot skillet and cook for 5-7 minutes per side until golden brown.",
            "Add minced garlic and cook for 1 minute until fragrant.",
            "Add your other ingredients and cook for 3-5 minutes until heated through.",
            "Continue cooking until chicken is cooked through (no pink in center).",
            "Remove from heat and let rest for 5 minutes before serving."
        ]
    else:  # vegetables
        fallback_recipe["instructions"] = [
            "Heat olive oil in a large skillet over medium heat.",
            "Add minced garlic and cook for 30 seconds until fragrant.",
            "Add your main ingredients and stir-fry for 5-7 minutes until crisp-tender.",
            "Season with salt and black pepper to taste.",
            "Add any additional seasonings or herbs as desired.",
            "Serve immediately while vegetables are still bright and crisp."
        ]
    
    return format_recipe(fallback_recipe)

def remix_recipe(current_recipe: str, modifications: str) -> str:
    """
    Remixes an existing recipe based on user-specified modifications.
    """
    print(f"\nRemixing the recipe with '{modifications}'...\n")
    
    # Check if this is a cuisine transformation request
    mod_lower = modifications.lower()
    cuisine_keywords = ["make it", "transform to", "convert to", "change to", "style"]
    
    for keyword in cuisine_keywords:
        if keyword in mod_lower:
            # Extract the cuisine name
            parts = mod_lower.split(keyword)
            if len(parts) > 1:
                potential_cuisine = parts[1].strip().split()[0]  # Get first word after keyword
                
                # Check if it's a valid cuisine
                if potential_cuisine in CUISINE_TRANSFORMATIONS:
                    print(f"🌍 Transforming recipe to {potential_cuisine.title()} cuisine...\n")
                    
                    # We need to parse the current recipe back to a dictionary
                    # For now, let's use a simple approach with the first recipe from database
                    # In a full implementation, you'd want to parse the current_recipe string
                    try:
                        # Try to find a matching recipe in the database
                        for recipe in RECIPE_DATABASE:
                            if recipe['name'] in current_recipe:
                                transformed_recipe = transform_cuisine(recipe, potential_cuisine)
                                return format_recipe(transformed_recipe)
                        
                        # If no exact match, use the first recipe as a template
                        transformed_recipe = transform_cuisine(RECIPE_DATABASE[0], potential_cuisine)
                        return format_recipe(transformed_recipe)
                    except Exception as e:
                        print(f"Could not transform recipe: {e}")
                        break
    
    # Try to use AI for remixing first
    prompt = (f"Take the following recipe:\n\n{current_recipe}\n\n"
              f"Now, remix this recipe by incorporating the following changes: '{modifications}'. "
              f"Provide the updated recipe. Focus on making the changes clear and integrating them smoothly. "
              f"If a requested change doesn't make sense for the ingredients, explain why briefly. "
              f"Always return a complete, updated recipe, not just the changes.")
    
    ai_result = call_gemini_api(prompt)
    
    # If AI fails, provide helpful fallback suggestions
    if ai_result.startswith("Failed to"):
        print("AI remixing is not available. Here are some manual modification suggestions:\n")
        
        if "vegan" in mod_lower or "vegetarian" in mod_lower:
            return current_recipe + "\n\n💡 VEGAN/VEGETARIAN MODIFICATIONS:\n" + \
                   "• Replace meat with tofu, tempeh, or plant-based alternatives\n" + \
                   "• Use vegetable broth instead of chicken/beef broth\n" + \
                   "• Replace dairy with plant-based alternatives (almond milk, coconut milk)\n" + \
                   "• Use nutritional yeast instead of cheese\n" + \
                   "• Add more vegetables for protein and texture"
        
        elif "spicy" in mod_lower or "hot" in mod_lower:
            return current_recipe + "\n\n🌶️ SPICY MODIFICATIONS:\n" + \
                   "• Add red pepper flakes or cayenne pepper\n" + \
                   "• Include fresh or dried chili peppers\n" + \
                   "• Use hot sauce or sriracha\n" + \
                   "• Add jalapeños or habaneros (seeded for less heat)\n" + \
                   "• Include ginger for additional heat"
        
        elif "less oil" in mod_lower or "low fat" in mod_lower:
            return current_recipe + "\n\n🥗 LOW-FAT MODIFICATIONS:\n" + \
                   "• Reduce oil by half and use non-stick pans\n" + \
                   "• Use cooking spray instead of oil\n" + \
                   "• Steam vegetables instead of sautéing\n" + \
                   "• Use broth for cooking instead of oil\n" + \
                   "• Choose leaner cuts of meat"
        
        elif "add" in mod_lower:
            # Extract what they want to add
            words = modifications.split()
            try:
                add_index = words.index("add")
                if add_index + 1 < len(words):
                    ingredient_to_add = words[add_index + 1]
                    return current_recipe + f"\n\n➕ ADDING {ingredient_to_add.upper()}:\n" + \
                           f"• Add {ingredient_to_add} during the cooking process\n" + \
                           f"• Adjust cooking time if needed\n" + \
                           f"• Consider complementary seasonings\n" + \
                           f"• Taste and adjust seasoning accordingly"
            except ValueError:
                pass
        
        # Generic modification suggestions
        return current_recipe + "\n\n🔄 MODIFICATION SUGGESTIONS:\n" + \
               "• For flavor changes: adjust herbs, spices, or seasonings\n" + \
               "• For texture: change cooking method or add crunchy elements\n" + \
               "• For health: reduce salt, oil, or add more vegetables\n" + \
               "• For serving: change portion sizes or add garnishes\n" + \
               "• For time: use pre-cut ingredients or simplify steps"
    
    return ai_result

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

def transform_cuisine(recipe: Dict, target_cuisine: str) -> Dict:
    """
    Transform a recipe to a different cuisine style.
    """
    target_cuisine = target_cuisine.lower()
    
    if target_cuisine not in CUISINE_TRANSFORMATIONS:
        return recipe  # Return original if cuisine not supported
    
    transformation = CUISINE_TRANSFORMATIONS[target_cuisine]
    transformed_recipe = recipe.copy()
    
    # Update recipe name to reflect cuisine change
    original_name = recipe['name']
    transformed_recipe['name'] = f"{target_cuisine.title()} Style {original_name}"
    
    # Update cuisine tag
    transformed_recipe['cuisine'] = target_cuisine
    
    # Transform ingredients based on cuisine
    new_ingredients = []
    for ingredient in recipe['ingredients']:
        item = ingredient['item'].lower()
        
        # Replace ingredients based on cuisine
        if target_cuisine == "mexican":
            if "pasta" in item:
                new_ingredients.append({"item": "corn tortillas", "amount": ingredient['amount'], "unit": ingredient['unit'], "notes": "or flour tortillas"})
            elif "parmesan" in item or "pecorino" in item:
                new_ingredients.append({"item": "queso fresco", "amount": ingredient['amount'], "unit": ingredient['unit'], "notes": "or cotija cheese"})
            elif "olive oil" in item:
                new_ingredients.append({"item": "vegetable oil", "amount": ingredient['amount'], "unit": ingredient['unit'], "notes": "or lard for authentic flavor"})
            else:
                new_ingredients.append(ingredient)
        
        elif target_cuisine == "asian":
            if "pasta" in item:
                new_ingredients.append({"item": "rice noodles", "amount": ingredient['amount'], "unit": ingredient['unit'], "notes": "or udon noodles"})
            elif "parmesan" in item or "pecorino" in item:
                new_ingredients.append({"item": "sesame seeds", "amount": ingredient['amount'], "unit": ingredient['unit'], "notes": "for garnish"})
            elif "olive oil" in item:
                new_ingredients.append({"item": "sesame oil", "amount": ingredient['amount'], "unit": ingredient['unit'], "notes": "or vegetable oil"})
            else:
                new_ingredients.append(ingredient)
        
        elif target_cuisine == "indian":
            if "pasta" in item:
                new_ingredients.append({"item": "basmati rice", "amount": ingredient['amount'], "unit": ingredient['unit'], "notes": "or naan bread"})
            elif "parmesan" in item or "pecorino" in item:
                new_ingredients.append({"item": "paneer", "amount": ingredient['amount'], "unit": ingredient['unit'], "notes": "fresh Indian cheese"})
            elif "olive oil" in item:
                new_ingredients.append({"item": "ghee", "amount": ingredient['amount'], "unit": ingredient['unit'], "notes": "clarified butter"})
            else:
                new_ingredients.append(ingredient)
        
        else:
            new_ingredients.append(ingredient)
    
    # Add cuisine-specific ingredients
    if target_cuisine == "mexican":
        new_ingredients.extend([
            {"item": "lime", "amount": 1, "unit": "medium", "notes": "juiced"},
            {"item": "cilantro", "amount": 1/4, "unit": "cup", "notes": "chopped"},
            {"item": "jalapeño", "amount": 1, "unit": "medium", "notes": "seeded and minced"}
        ])
    elif target_cuisine == "asian":
        new_ingredients.extend([
            {"item": "soy sauce", "amount": 2, "unit": "tablespoons", "notes": "low sodium"},
            {"item": "ginger", "amount": 1, "unit": "tablespoon", "notes": "fresh, grated"},
            {"item": "green onions", "amount": 2, "unit": "stalks", "notes": "chopped"}
        ])
    elif target_cuisine == "indian":
        new_ingredients.extend([
            {"item": "turmeric", "amount": 1/2, "unit": "teaspoon", "notes": "ground"},
            {"item": "cumin", "amount": 1/2, "unit": "teaspoon", "notes": "ground"},
            {"item": "coriander", "amount": 1/2, "unit": "teaspoon", "notes": "ground"}
        ])
    
    transformed_recipe['ingredients'] = new_ingredients
    
    # Transform instructions based on cuisine
    new_instructions = []
    for instruction in recipe['instructions']:
        new_instruction = instruction
        
        # Replace cooking techniques and methods
        if target_cuisine == "mexican":
            new_instruction = new_instruction.replace("sauté", "sauté with cumin and chili powder")
            new_instruction = new_instruction.replace("olive oil", "vegetable oil")
            new_instruction = new_instruction.replace("parmesan", "queso fresco")
        
        elif target_cuisine == "asian":
            new_instruction = new_instruction.replace("sauté", "stir-fry")
            new_instruction = new_instruction.replace("olive oil", "sesame oil")
            new_instruction = new_instruction.replace("parmesan", "sesame seeds")
        
        elif target_cuisine == "indian":
            new_instruction = new_instruction.replace("sauté", "temper with spices")
            new_instruction = new_instruction.replace("olive oil", "ghee")
            new_instruction = new_instruction.replace("parmesan", "paneer")
        
        new_instructions.append(new_instruction)
    
    # Add cuisine-specific final steps
    if target_cuisine == "mexican":
        new_instructions.append("Garnish with fresh cilantro, lime wedges, and jalapeño slices.")
    elif target_cuisine == "asian":
        new_instructions.append("Garnish with green onions and sesame seeds before serving.")
    elif target_cuisine == "indian":
        new_instructions.append("Garnish with fresh cilantro and serve with naan bread or rice.")
    
    transformed_recipe['instructions'] = new_instructions
    
    # Update tags
    if 'tags' in transformed_recipe:
        # Remove old cuisine tags and add new ones
        old_tags = [tag for tag in transformed_recipe['tags'] if tag not in ['italian', 'mediterranean', 'american']]
        transformed_recipe['tags'] = old_tags + [target_cuisine]
    
    # Update tips
    if 'tips' in transformed_recipe:
        transformed_recipe['tips'].append(f"Use authentic {target_cuisine} ingredients for best results.")
        transformed_recipe['tips'].append(f"Adjust spice levels to your preference for {target_cuisine} heat.")
    
    return transformed_recipe

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
    print("Type 'chart' to open the measurement conversion chart.")
    print("\n🌍 CUISINE TRANSFORMATIONS:")
    print("You can transform any recipe to different cuisines using:")
    print("• 'make it mexican' - Transform to Mexican cuisine")
    print("• 'make it asian' - Transform to Asian cuisine") 
    print("• 'make it indian' - Transform to Indian cuisine")
    print("• 'make it mediterranean' - Transform to Mediterranean cuisine")
    print("• 'make it french' - Transform to French cuisine")
    print("• 'make it thai' - Transform to Thai cuisine")
    print("• 'make it japanese' - Transform to Japanese cuisine")
    print("• 'make it greek' - Transform to Greek cuisine")
    print("• 'make it chinese' - Transform to Chinese cuisine")
    print("\n")

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
            "How would you like to remix this recipe? (e.g., 'make it mexican', 'add a spicy kick', 'use less oil', 'add mushrooms', 'quit' to exit): "
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