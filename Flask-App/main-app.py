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

    print request.form.to_dict()
    # print request.form['net_id']

    netid = request.form['net_id']
    things = request.form['3_things']
    fname = request.form['full_name']
    pname = request.form['pref_name']
    alrmet = request.form['already_met']
    year = request.form['year']

    ig = False
    ig = True if 'check_ig' in request.form
    fb = False
    fb = True if 'check_fb' in request.form
    wa = False
    wa = True if 'check_wa' in request.form



    print "success"
    
    # Construct args here

    # Use addToDatabase(netid, fname, pname, things, alrmet, year, fb, ig, wa)

    # Construct return message based on success of insertion

    return "Success"