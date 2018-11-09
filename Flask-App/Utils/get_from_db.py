# import mysql.connector
# from mysql.connector import Error
# import dbconfig 




# try:
#    connection = mysql.connector.connect(host='localhost',
#                              database='socialite',
#                              user=dbconfig.USERNAME,
#                              password=dbconfig.PASSWORD)
#    sql_select_Query = "select * from user_data"
#    cursor = connection .cursor()
#    cursor.execute(sql_select_Query)
#    records = cursor.fetchall()
#    print("Total number of rows in python_developers is - ", cursor.rowcount)
#    print ("Printing each row's column values i.e.  developer record")
#    userList = []
#    for row in records:
#        user = []
#        for element in row:
#            user.append(element)
#        userList.append(user)
#    cursor.close()


#    print(userList)
#    print(userList[0][1])
   
# except Error as e :
#     print ("Error while connecting to MySQL", e)



import MySQLdb, MySQLdb.cursors
import dbconfig
    

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

getFromDatabase()
