import mysql.connector


#mysql server detail
db_connection=mysql.connector.connect(host="localhost",user="root",password="s@kshi@2706",database="test_db")


#create cursor to execute queries
#cursor=db_connection.cursor()


#create database
#create_database_query="CREATE DATABASE test_db"
#cursor.execute(create_database_query)


#commit the chenges 
#db_connection.commit()

#close the cursor and the connection
#cursor.close()
#db_connection.close()


#Creating table
cursor=db_connection.cursor()

#table query
#create_table_query="""CREATE TABLE test_table(
#id INT AUTO_INCREMENT PRIMARY KEY,
#name VARCHAR(50),
#age INT
#)"""

#query execution

#cursor.execute(create_table_query)
#db_connection.commit()

#insert data into table
#insert_data_query = """
#INSERT INTO test_table (name, age) VALUES (%s, %s)"""
#data_to_insert = ("Sakshi",19 )
#cursor.execute(insert_data_query, data_to_insert)

#db_connection.commit()

#update the table

#update_data_query = """UPDATE test_table SET age = %s WHERE name = %s"""

#new_age =20
#name_to_update = "Sakshi"
#cursor.execute(update_data_query, (new_age, name_to_update))

#db_connection.commit()


#delete from table

delete_data_query = """
DELETE FROM test_table WHERE name = %s
"""
name_to_delete = "Sakshi"
cursor.execute(delete_data_query, (name_to_delete,))
db_connection.commit()

cursor.close()
db_connection.close()