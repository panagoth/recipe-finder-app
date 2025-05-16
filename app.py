from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Homepage with search form
@app.route('/')
def index():
    return render_template('index.html')

# Handle form submission
@app.route('/results', methods=['POST'])
def results():
    ingredient = request.form['ingredient']
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}"
    response = requests.get(url)
    data = response.json()
    meals = data.get('meals')

    return render_template('results.html', meals=meals, ingredient=ingredient)

if __name__ == '__main__':
    app.run(debug=True)
