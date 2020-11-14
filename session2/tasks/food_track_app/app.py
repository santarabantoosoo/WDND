from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/view')
def view():
    return render_template('day.html')

@app.route('/food')
def food():
    return render_template('add_food.html')