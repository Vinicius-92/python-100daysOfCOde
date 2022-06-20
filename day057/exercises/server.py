from flask import Flask, render_template
import random
import datetime
import requests
app = Flask(__name__)

CURRENT_YEAR = datetime.date.today().year


@app.route('/')
def hello_world():
    rand = random.randint(1, 10)
    return render_template("index.html", number=rand, year=CURRENT_YEAR)


@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
