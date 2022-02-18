from fileinput import filename
from flask import Flask,render_template,url_for
import requests

ENDPOINT_JSON = 'https://api.npoint.io/e656843f0522549867e2'

app = Flask(import_name=__name__)

def load_json():
    response = requests.get(ENDPOINT_JSON)
    data = response.json()
    return data

def styles_project():
    url_for('static', filename='assets/img/about-bg.jpg')
    url_for('static', filename='assets/img/contact-bg.jpg')
    url_for('static', filename='assets/img/home-bg.jpg')
    url_for('static', filename='assets/img/post-bg.jpg')
    url_for('static', filename='assets/img/post-sample-image.jpg')
    url_for('static', filename='assets/favicon.ico')
    url_for('static', filename='css/styles.css')

@app.route('/')
def main():
    styles_project()
    data = load_json()
    return render_template('index.html', data=data)

@app.route('/about')
def about():
    styles_project()
    return render_template('about.html')

@app.route('/contact')
def contact():
    styles_project()
    return render_template('contact.html')

@app.route('/post/<int:id>')
def post(id):
    styles_project()
    data = load_json()
    
    return render_template('post.html',data=data,id=id)

if __name__ == '__main__':
    
    app.run(debug=True)