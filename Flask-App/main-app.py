from flask import Flask, request

app = Flask(__name__)

@app.route('/add-to-db')
def addToDb():
    
    
    return "Success"
