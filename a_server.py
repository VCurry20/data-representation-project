from flask import Flask, jsonify, request, abort, render_template, session, url_for, g, redirect

from DAO import populationDAO ## should this be the capital one!?

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Server"


if __name__ == "__main__":
    app.run(debug=True)


