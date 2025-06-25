# 🍽️ AI Recipe Remix Master

A powerful recipe generation and transformation tool that helps you create delicious meals from your available ingredients and transform them into world cuisines!

## 🌐 Access URLs

### Local Access
- **Primary URL**: http://localhost:8000
- **Alternative**: http://127.0.0.1:8000

### Network Access (for other devices)
- **Your Computer**: http://192.168.3.206:8000
- **Any device on your network**: http://[YOUR_IP]:8000

## 🚀 How to Start

1. **Start the server**:
   ```bash
   python3 server.py
   ```

2. **Open your browser** and go to one of the URLs above

3. **The browser should open automatically** when you start the server

## ✨ Features

### 🍳 Recipe Generation
- **Find recipes by ingredients**: Enter what you have and get matching recipes
- **Random recipes**: Get surprise recipes from our curated database
- **Fallback generation**: Creates recipes even when ingredients don't match the database

### 🌍 Cuisine Transformations
Transform any recipe into 10 different world cuisines:
- 🇲🇽 **Mexican** - Bold flavors, corn-based ingredients, spicy elements
- 🇯🇵 **Asian** - Umami flavors, quick cooking methods  
- 🇮🇳 **Indian** - Complex spice blends, vegetarian-friendly options
- 🇬🇷 **Mediterranean** - Fresh vegetables, olive oil, healthy fats
- 🇫🇷 **French** - Rich sauces, sophisticated flavor combinations
- 🇹🇭 **Thai** - Sweet, sour, salty, and spicy balance
- 🇯🇵 **Japanese** - Umami, seasonal ingredients, precise techniques
- 🇬🇷 **Greek** - Fresh herbs, olive oil, Mediterranean ingredients
- 🇨🇳 **Chinese** - Balance, texture, five fundamental tastes
- 🇮🇹 **Italian** - Fresh ingredients, olive oil, herbs

### 🔄 Recipe Remixing
- **Make it spicy**: Add heat to any recipe
- **Make it vegan**: Transform to plant-based versions
- **Use less oil**: Create healthier versions
- **Add ingredients**: Customize with your preferences

## 📱 How to Use

1. **Enter ingredients** in the input field (comma-separated)
2. **Click "Find Recipe"** to get a matching recipe
3. **Click "Random Recipe"** for a surprise
4. **Click "Cuisine Transformations"** to see available cuisines
5. **Select a cuisine** to transform your recipe
6. **Add modifications** like "make it spicy" or "add mushrooms"

## 🎯 Example Usage

### Finding a Recipe
```
Ingredients: chicken, broccoli, pasta
→ Finds: Quick Chicken Stir-Fry
```

### Cuisine Transformation
```
Recipe: Classic Spaghetti Carbonara
Transform: "make it mexican"
→ Result: Mexican Style Carbonara with lime, cilantro, jalapeños
```

### Recipe Remixing
```
Recipe: Any recipe
Modification: "make it spicy"
→ Result: Adds red pepper flakes and cayenne pepper
```

## 🛠️ Technical Details

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python HTTP Server
- **Port**: 8000
- **Browser Support**: All modern browsers

## 📁 Files

- `recipe-remix-master.html` - Main web application
- `server.py` - HTTP server to host the application
- `recipe_remix_master.py` - Python command-line version
- `README.md` - This file

## 🔧 Troubleshooting

### Server won't start
- Make sure Python 3 is installed
- Check if port 8000 is available
- Try a different port by editing `server.py`

### Can't access from other devices
- Check your firewall settings
- Make sure devices are on the same network
- Use the correct IP address

### Browser doesn't open automatically
- Manually open: http://localhost:8000
- Or use: http://192.168.3.206:8000

## 🎉 Enjoy Cooking!

The Recipe Remix Master is designed to make cooking fun and creative. Experiment with different cuisines and modifications to discover new flavors and techniques!

---

**Created with ❤️ for food lovers everywhere**