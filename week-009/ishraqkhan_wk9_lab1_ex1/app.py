from flask import Flask, render_template

app = Flask('exercise1')

def home():
    return render_template("index.html")

app.add_url_rule('/', 'home', home)

app.run(debug=True)