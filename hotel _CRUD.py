import mysql.connector

#my server detail
db_connection=mysql.connector.connect(host="localhost",user="root",password="s@kshi@2706",database="hotel");

#create cursor queries
cursor=db_connection.cursor()

#create database
#create_database_query="CREATE DATABASE Hotel";
#cursor.execute(create_database_query)

#commit the chenges
#db_connection.commit()

#CLOSE the cursor and the connection
#cursur.close()
#db_connection.close()

#create table
#create_table_query = """CREATE TABLE Staff(
#id INT,
#fullname varchar (255),
#position varchar(255),
#salary INT
#)
#"""

 #query execution

#cursor.execute(create_table_query)
#db_connection.commit()

#INSERT DATA INTO table
#insert_data_query="""
#INSERT INTO Staff(id,fullname,position,salary) VALUES (%s,%s, %s,%s)"""

#data_to_insert = [(1,"sakshi gurav","employee",8000),(2,"shruti kadam","employee",8000),(2,"shruti kadam","employee",8000)]

#cursor.executemany(insert_data_query, data_to_insert)

#db_connection.commit()

#create table
#create_table_query = """CREATE TABLE Booking(
#bookingid INT,
#guestid INT,
#room_number INT,
#price INT
#)
#"""

 #query execution

#cursor.execute(create_table_query)
#db_connection.commit()

#INSERT DATA INTO table
insert_data_query="""
INSERT INTO Booking(bookingid,guestid,room_number,price) VALUES (%s,%s, %s,%s)"""

data_to_insert = [(23,45,23,1800),(25,67,12,2000),(14,34,10,3000)]

cursor.executemany(insert_data_query, data_to_insert)

db_connection.commit()

