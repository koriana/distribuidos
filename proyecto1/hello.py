#!/usr/bin/python

import MySQLdb
from flask import render_template
from flask import Flask
app = Flask(__name__)

# Open database connection
db = MySQLdb.connect("localhost","root","zhangyixing","hola" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
#cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
#data = cursor.fetchone()


# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM ubicacion"
try:
   # Execute the SQL command
   cursor.execute(sql)
   canthijos = cursor.rowcount
   
   print canthijos
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      pid = row[0]
      lat = row[1]
      lng = row[2]

      # Now print fetched result
      print "pid=%d,lat=%s,lng=%s" % \
             (pid, lat, lng )
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()


@app.route('/')
def index():
    return str(tuple(results))
    
@app.route('/hello/')
def hello():
    return render_template('prueba.html', results=results, canthijos=canthijos)
    

app.debug = True
if __name__ == '__main__':
    app.run(host='0.0.0.0')
