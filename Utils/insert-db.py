import mysql.connector
from mysql.connector import Error
import dbconfig 


def addToDatabase(netid, fname, pname, things, alrmet, year, fb, ig, wa):
    try:
        connection = mysql.connector.connect(host = 'localhost', 
            database = 'socialite',
            user = dbconfig.USERNAME, 
            password = dbconfig.PASSWORD)

        sql_query = '''
            INSERT INTO `user_data` (`net_id`, 
            `full_name`, 
            `pref_name`, 
            `3_things`, 
            `already_met`, 
            `class_year`, 
            `check_fb`, 
            `check_ig`, 
            `check_wa`)
            VALUES ('{netid}', '{fname}', '{pname}', '{things}', '{alrmet}', '{year}', '{fb}', '{ig}', '{wa}')
        '''.format(netid = netid, 
        fname = fname,
        pname = pname, 
        things = things, 
        alrmet = alrmet, 
        year = year, 
        fb = fb, 
        ig = ig, 
        wa = wa )

        cursor = connection.cursor()
        result = cursor.execute(sql_query)
        connection.commit()
        print("Inserted successfully")

    except mysql.connector.Error as error:
        connection.rollback()
        print("Something went wrong in the insertion", error)

addToDatabase("ns3774", "Navya Suri","Nav", "I love potatoes", "qw123, er234", "Sophomore", 1, 1, 1)

