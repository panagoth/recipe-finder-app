
# Recipe Finder App

**Recipe Finder** is a simple web application built with Python and Flask that allows users to search for meals based on a specific ingredient. It uses the [TheMealDB API](https://www.themealdb.com/api.php) to fetch and display recipe data.

---

### Features

- Search for recipes by ingredient (e.g., "chicken", "salmon")
- Displays recipe name, image, and a direct link to full instructions
- Responsive design using Bootstrap for clean and simple UI
- Error handling for invalid or empty search results

---

### Technologies Used

- Python 3
- Flask
- HTML / Jinja2 Templates
- Bootstrap 5
- TheMealDB Public API

---

### What I Learned

By building this project, I:
- Gained practical experience in developing a Flask application
- Learned how to interact with third-party APIs and parse JSON data
- Improved my skills in structuring small Python web projects
- Practiced using Jinja2 templating and Bootstrap for dynamic UI

---

### How It Works

1. User enters an ingredient into the search box.
2. The app sends a request to TheMealDB API.
3. The API returns a list of recipes containing the ingredient.
4. The app displays each recipe with image, title, and a link to the full recipe.
