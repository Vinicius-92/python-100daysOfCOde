from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center;">Hello, World!</h1>' \
           '<p style="text-align: center;">this is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/6znpHNXfBQJnSWhwmm/giphy-downsized-large.gif">'


@app.route('/username/<name>/<int:age>')
def greeting(name, age):
    return f"Hello {name}, you're {age} years old!"


if __name__ == "__main__":
    app.run(debug=True)
