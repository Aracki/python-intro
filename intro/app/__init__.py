print('init.py from app/')

from flask import Flask

app = Flask(__name__)


@app.route('/raca')
def raca():
    return "raca"
