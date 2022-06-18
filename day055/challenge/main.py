from flask import Flask
import random
app = Flask(__name__)

NUMBER = random.randint(0, 10)


def high():
    return '<h1 style="color: red;">Too high, try again!</h1>' \
           '<img src="https://media.giphy.com/media/3o7abAHdYvZdBNnGZq/giphy.gif">'


def low():
    return '<h1 style="color: blue;">Too low, try again!</h1>' \
           '<img src="https://media.giphy.com/media/xJtkGEZQ0NWcp8jg8Z/giphy.gif">'


def right():
    return '<h1 style="color: green;">You found me!</h1>' \
           '<img src="https://media.giphy.com/media/2yuRoYBGY027wAPYML/giphy.gif">'


@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3boPPdHk2ueo8/giphy.gif">'


@app.route('/<int:guessed>')
def guess(guessed):
    if guessed < NUMBER:
        return low()
    if guessed > NUMBER:
        return high()
    return right()


if __name__ == "__main__":
    app.run(debug=True)
