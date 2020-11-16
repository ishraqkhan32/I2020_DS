from flask import Flask, render_template, request
import math

app = Flask('exercise2')

@app.route('/sqrt/<int:num>')
def sqrt(num):
    result = float(math.sqrt(num))
    return render_template('sqrt.html', sqrt=result)

@app.route('/user/<username>')
def welcome_user(username):
    username = username.title()
    return render_template('welcome.html', user=username)

@app.route('/req', methods=['GET'])
def req():  
    data = request.url
    print(data)
    return render_template('request.html', data=data)

app.run()