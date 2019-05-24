#create table called "classroom" in database "classroomDB.db"
#On jupyter notebook 



import sqlite3

#open connection
connection = sqlite3.connect("classroomDB.db")

#open cursor
cursor = connection.cursor()

#query for creating table
create_table = """
                         CREATE TABLE classroom (
                           student_id INTEGER PRIMARY KEY,
                           name VARCHAR(20),
                           gender VARCHAE(1),
                           physics_marks INTEGER,
                           chemistr_marks INTEGER,
                           mathematics_marks INTEGER
                          ); """

#execute query
cursor.execute(create_table)

#commit change
connection.commit()
connection.close()
