from flask import Flask, request
import Utils.insert_db

app = Flask(__name__)

@app.route('/add-to-db')
def addToDb():
    
    # Construct args here

    # Use addToDatabase(netid, fname, pname, things, alrmet, year, fb, ig, wa)

    # Construct return message based on success of insertion
    return "Success"
