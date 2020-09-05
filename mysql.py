
import MySQLdb

# Open database connection
db = MySQLdb.connect("host","user","password","dbname" )


# prepare a cursor object using cursor() method
cursor = db.cursor()


sql = "SELECT * FROM tablename"

try:
        # Execute the SQL command
        cursor.execute(sql)

        results = cursor.fetchall()
        print  results
except:
        print "Error: unable to fecth data"

# disconnect from server
db.close()
