from flask import Flask, render_template, request
import requests

app = Flask(__name__)

POSTS_URL = "https://api.npoint.io/43a583d3b3d6654debfc"
posts = requests.get(POSTS_URL).json()

@app.route('/')
def home():
    return render_template('index.html', all_posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        print(data)
        return "<h1>Form submission successful!</h1>"
    return render_template("contact.html")

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in posts:
        if post['id'] == index:
            requested_post = post
    return render_template('post.html', post=requested_post)

# @app.route('/form-entry')
# def recieve_data():
#     return "<h1>Form submission successful!</h1>"

if __name__ == '__main__':
    app.run(debug=True)