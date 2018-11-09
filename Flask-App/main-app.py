from flask import Flask, request, render_template, url_for
import Utils.db_helpers, os

html_path = os.path.abspath("form/index.html")

app = Flask(__name__)

@app.route('/')
def show_page():
    

    
    # Display form index here
    print("should work")

    return render_template("index.html")

@app.route('/add-to-db', methods=['POST'])
def addToDb():

    print request.data

    print "success"
    
    # Construct args here

    # Use addToDatabase(netid, fname, pname, things, alrmet, year, fb, ig, wa)

    # Construct return message based on success of insertion

    return "Success"



