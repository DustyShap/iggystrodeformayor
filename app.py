from flask import Flask, render_template, url_for, redirect, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/issues')
def issues():
    return render_template('issues.html')
