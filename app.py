
from flask import Flask, request, Response, render_template

app = Flask(__name__)

@app.route('/')
def default_page():
    return "Hello World"

if __name__ == '__main__':
    app.run()
