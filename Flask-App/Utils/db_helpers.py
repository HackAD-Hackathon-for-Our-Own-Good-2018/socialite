import MySQLdb, MySQLdb.cursors
import dbconfig 

def addToDatabase(netid, fname, pname, things, alrmet, year, fb, ig, wa):

    alrmet = alrmet.split(',')
    for i in range(len(alrmet)):
        alrmet[i] = alrmet[i].strip()
    alrmet = ",".join(alrmet)
    print(alrmet)

    try:
        connection = MySQLdb.connect(host = 'localhost', 
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

        cur = connection.cursor()
        result = cur.execute(sql_query, params)
        connection.commit()
        print("Inserted successfully")

    except (MySQLdb.Error, MySQLdb.Warning) as error:
        connection.rollback()
        print("Something went wrong in the insertion", error)

    connection.close()
    


def getFromDatabase():
    try:
        connection = MySQLdb.connect(host='localhost',
        db='socialite',
        user=dbconfig.USERNAME,
        passwd=dbconfig.PASSWORD,
        cursorclass = MySQLdb.cursors.DictCursor)

        query = "select * from user_data"
        cur = connection.cursor()
        cur.execute(query)
        records = cur.fetchall()
        # print(records)

        userDictionary = {}

        # Make the netid as a key for all data for each user
        # Store all users in userDictionary with netid as key
        
        for record in records:
            # print(record)
            userDictionary[record['net_id']] = record
        
        # print(userDictionary)

        return userDictionary



    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print ("Error while connecting to MySQL", e)
        return None

    connection.close()



def updateDatabase(n1, n1_dont_match):
    
    try:
        p1_dont_match = ",".join(n1_dont_match)

        print n1, p1_dont_match
        query = "update user_data set already_met = %s where net_id = %s ;"

        connection = MySQLdb.connect(host='localhost',
        db='socialite',
        user=dbconfig.USERNAME,
        passwd=dbconfig.PASSWORD)

        cur = connection.cursor()
        cur.execute(query,[p1_dont_match, n1])

        print("Update complete")

        connection.commit()
        connection.close()

    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print("Error in DB: ", e)