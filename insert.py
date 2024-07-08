import sqlite3

conn = sqlite3.connect ('example.db')
print("Opened database successfully")


conn.execute("INSERT INTO EMPLOYEE VALUES (1 , 'MARY' , 'KAMAU', 45, 34000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (2 , 'JAMES' , 'WEKESA', 25, 131000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (3 , 'ANNE' , 'NDUTA', 35, 211000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (4 , 'JOHN' , 'WERE', 28, 34000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (5, 'JANE' , 'KADZO', 23, 34000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (6 , 'PAUL' , 'SALIM', 31, 34000.00)")
conn.commit()

print("successfully added records")
conn.close()