# Import csv, sqlite3 and time modules
import csv, sqlite3 , time
 
# record start time
start = time.time()
 
con = sqlite3.connect("./sqlite_employees.db") # sqlite connection
cur = con.cursor()

with open('employees.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['emp_id'],i['emp_name'], i['dob'], i['role'], i['dept']) for i in dr]

cur.executemany("INSERT INTO employee_details (emp_id, emp_name, emp_dob, emp_role, emp_dept) VALUES (?,?,?,?,?);", to_db)
con.commit()
con.close()

# print the difference between start and end time in milli. secs record end time
end = time.time()
print("The time of execution of python program is :",(end-start) * 10**3, "ms")
