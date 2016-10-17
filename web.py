from flask import Flask, render_template, request
import giphypop
import os
app = Flask(__name__)

g = giphypop.Giphy()

def search_term(searchterm):
    return "GIFs tagged with {}".format(searchterm)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    searchterm = request.values.get('searchterm')
    results = g.search(searchterm)
    tag = search_term(searchterm)
    return render_template('results.html', searchterm=searchterm, tag=tag, results=results)

@app.route('/about')
def about():
    return render_template('about.html')

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)