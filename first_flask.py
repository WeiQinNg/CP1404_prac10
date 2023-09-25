from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! :)'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f/<float:celsius>')
@app.route('/f/<int:celsius>')
def f(celsius):
    # return str(convert_to_fahrenheit(celsius))
    fahrenheit = convert_to_fahrenheit(celsius)
    return f"{celsius} Celsius is {fahrenheit} Fahrenheit."


def convert_to_fahrenheit(celsius):
    """Calculate fahrenheit using celsius."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
