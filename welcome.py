import webbowrser
import os
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# HTML template with styling
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f2f5;
        }
        .welcome-container {
            text-align: center;
            padding: 2rem;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #1a73e8;
            margin-bottom: 1rem;
        }
        p {
            color: #5f6368;
            font-size: 1.2rem;
        }
        .form-container {
            margin-top: 1rem;
        }
        input[type="text"] {
            padding: 0.5rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            margin-right: 0.5rem;
        }
        button {
            padding: 0.5rem 1rem;
            background-color: #1a73e8;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #1557b0;
        }
    </style>
</head>
<body>
    <div class="welcome-container">
        {% if name %}
            <h1>Welcome, {{ name }}!</h1>
            <p>We're glad to have you here.</p>
            <div class="form-container">
                <form action="/" method="get">
                    <button type="submit">Enter Another Name</button>
                </form>
            </div>
        {% else %}
            <h1>Welcome!</h1>
            <form action="/" method="get">
                <input type="text" name="name" placeholder="Enter your name" required>
                <button type="submit">Submit</button>
            </form>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    name = request.args.get('name')
    return render_template_string(HTML_TEMPLATE, name=name)

if __name__ == '__main__':
    print("Starting the server...")
    print("Open your web browser and go to: http://localhost:5000")
    app.run(debug=True) 