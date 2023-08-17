from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search']
    movies = search_movies(search_term)
    return render_template('index.html', movies=movies)

def search_movies(search_term):
    api_key = '531179d8'
    response = requests.get(f'http://www.omdbapi.com/?apikey={api_key}&s={search_term}')
    data = response.json()
    if 'Search' in data:
        return data['Search']
    return []

if __name__ == '__main__':
    app.run(debug=True)
