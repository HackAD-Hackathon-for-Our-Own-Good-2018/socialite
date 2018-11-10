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
    data = request.form.to_dict()
    # print request.form['net_id']

    netid = request.form['net_id']
    things = request.form['3_things']
    fname = request.form['full_name']
    pname = request.form['pref_name']
    alrmet = request.form['already_met']
    year = request.form['year']

    ig = False
    if 'check_ig' in data.keys():
        ig = True
    fb = False
    if 'check_fb' in data.keys():
        fb = True
    wa = False
    if 'check_wa' in data.keys():
        wa = True



    print "success"
    print (netid, fname, pname, things, alrmet, year, fb, ig, wa)
    
    # Construct args here

    return Utils.db_helpers.addToDatabase(netid, fname, pname, things, alrmet, year, fb, ig, wa)

    # Construct return message based on success of insertion
