import sqlite3
def create_database():
    con = sqlite3.connect(database = "RMS.db")
    # next ill make the cursor , which helps to run any query
    cur = con.cursor()

    # table for courses
    # cur.execute("CREATE TABLE IF NOT EXISTS course(c_id INTEGER PRIMARY KEY AUTOINCREMENT, name text, duration text,charges text,description text)")
    # con.commit()


    # table for students
    # cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,dob text,contact text,admission text,course text,state text,city text,pin text,address text)")
    # con.commit()


    # table for results of the student
    # cur.execute("CREATE TABLE IF NOT EXISTS result(rNo INTEGER PRIMARY KEY AUTOINCREMENT, roll text, name text,course text,marks_obt text,total_marks text, percentage text)")
    # con.commit()

    # table for login
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    con.commit()

    # closing the connection
    con.close()

create_database()
