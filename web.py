from flask import Flask, render_template, request
import giphypop
import os
app = Flask(__name__)

g = giphypop.Giphy()

# Function that populates the field on the top of the results page indicating the search term used to generate the search results
def search_term(searchterm):
    return "GIFs tagged with {}".format(searchterm)

# Index page
@app.route('/')
def index():
    return render_template('index.html')

# Results page; defined terms / functions below are pulling the search term from the Index form to the results page and are then used to pull from the giphy API
@app.route('/results')
def results():
    searchterm = request.values.get('searchterm')
    results = g.search(searchterm)
    tag = search_term(searchterm)
    return render_template('results.html', searchterm=searchterm, tag=tag, results=results)

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Essentials to deploy to Heroku
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
