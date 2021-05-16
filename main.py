import requests
from flask import Flask, render_template


app = Flask(__name__)

blog_url = "https://api.npoint.io/ed99320662742443cc5b"
response = requests.get(blog_url)
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<num>')
def post(num):
    for p in all_posts:
        if p['id'] == int(num):
            return render_template('post.html', posts=p)


if __name__ == "__main__":
    app.run(debug=True)
