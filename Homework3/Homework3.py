import sqlite3
from os.path import join, split

conn = sqlite3.connect("Courses.sq")

# create a query
cmd = "select * from Courses"

# create a cursor
crs = conn.cursor()

# send a query and receive query result
crs.execute(cmd)

Courses = crs.fetchall()

for row in Courses:
    print(row)

cmd2 = """
        select Courses.department, 
        Courses.course_num, 
        Courses.course_name,
        PreReqs.prereq1,
        PreReqs.prereq2 
        from Courses, PreReqs 
        where PreReqs.course_id = Courses.course_id
        """

crs.execute(cmd2)

Courses2 = crs.fetchall()
#prereqIds = set()

for row in Courses2:
    print(row[0] + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]))

year = input("Enter the year: ")
sem = input("Enter the semester: ")

if year is Courses.years:
    print(Courses)

if sem is Courses.semester:
    print(Courses)

grade = input("Enter a letter grade: ")

if grade is Courses.grade:
    print(Courses)

courseIid = input("Enter the course id: ")

if id is Courses.courseId:
    print(Courses)