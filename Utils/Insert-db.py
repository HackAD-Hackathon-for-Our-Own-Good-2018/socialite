import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import dbconfig 


def addToDatabase(netid, pname, things, alrmet, year, fb, ig, wa):
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
            VALUES ({netid}, {fname}, {pname}, {things}, {alrmet}, {year}, {fb}, {ig}, {wa}})
        '''.format(netid = netid, 
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

    except:
        connection.rollback()
        print("Something went wrong in the insertion")

