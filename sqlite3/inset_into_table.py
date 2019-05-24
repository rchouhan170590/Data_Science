#insert the data into the table "classroom" which is present inside the "classroomDB.db" database.
import sqlite3
classroom_data = [ (1,"Ronak","M",40,23,24),
                                (2,"Rohini","F",54,34,29),
                                (3,"Mohit","M",45,34,93),
                                (4,"sunil","M",32,92,93) ]

connection = sqlite3.connect("classroomDB.db")
cursor = connection.cursor()
for student in classroom_data :
      insert_statement = """ INSERT INTO classroom
                                     (student_id,name,gender,physics_marks,chemistry_marks,mathematics_marks)
                                     VALUES
                                     ( {0},"{1}","{2}",{3},{4},{5});""".formate(student[0],student[1],student[2],student[3],student[4],student[5])
     cursor.execute(insert_statement)

connection.commit()
connection.close()