import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="myusername",
  password="mypassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE projet_python_airport")
