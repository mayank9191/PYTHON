# Explore the ‘Flask’ module and create a web server using Flask & Python.

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello,World</p>"


app.run()

# Flask is a lightweight web framework for Python, often referred to as a microframework because it does not require particular tools or libraries. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. Flask is based on Werkzeug WSGI toolkit and Jinja2 template engine.
