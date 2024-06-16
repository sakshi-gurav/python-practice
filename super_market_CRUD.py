import mysql.connector

#mysql server detail
db_connection=mysql.connector.connect(host="localhost",user="root",password="s@kshi@2706",database="Super_Market")

#create cursor to execute quries
cursor=db_connection.cursor()


#create database
#create_database_query="CREATE DATABASE Super_Market";
#cursor.execute(create_database_query)

#commit the chenges 
#db_connection.commit()

#close the cursor and the connection
#cursor.close()
#db_connection.close()


#create table
#create_table_query = """CREATE TABLE product(
#id INT AUTO_INCREMENT PRIMARY KEY,
#name varchar (255),
#category varchar(255),
# price int
#)
# """

#query execution

#cursor.execute(create_table_query)
#db_connection.commit()


#insert data into table
insert_data_query = """
INSERT INTO product (name,category,price) VALUES (%s,%s, %s)"""
data_to_insert = ("cakes","bakery",44 )
data_to_insert1 = ("milk","dairy",66 )

cursor.execute(insert_data_query, data_to_insert,data_to_insert1)

db_connection.commit()




