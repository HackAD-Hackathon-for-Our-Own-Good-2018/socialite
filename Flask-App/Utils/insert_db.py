import mysql.connector
from mysql.connector import Error
import dbconfig 


def addToDatabase(netid, fname, pname, things, alrmet, year, fb, ig, wa):

    alrmet = alrmet.split(',')
    for i in range(len(alrmet)):
        alrmet[i] = alrmet[i].strip()
    alrmet = ",".join(alrmet)
    print(alrmet)

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
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        params = [netid, fname, pname, things, alrmet, year, fb, ig, wa]

        cursor = connection.cursor()
        result = cursor.execute(sql_query, params)
        connection.commit()
        print("Inserted successfully")

    except mysql.connector.Error as error:
        connection.rollback()
        print("Something went wrong in the insertion", error)

    cursor.close()

addToDatabase("sj2538", "Shantanu Jain", "Shanty", "I don't like potato", "abs123, qwe12", "Sophomore", 1, 1, 1)