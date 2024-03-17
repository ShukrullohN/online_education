import student
import mentor
from classes import Base
from db_connect import Database
def enter():
    se = input("""
        1. Login
        2. Register
    """)
    
    if se == "1":
        return login()

    elif se =="2":
        return register()
    
    else:
        print("Error!")
        return enter()

def login():
    sr = input("""
        1. Student
        2. Mentor
    """)
    if sr == "1":
        email = input("Enter email:")
        password = input("Enter password: ")
        data = Base.select("student")
        for i in data:
            if i[3] == email and i[4] == password:
                return student.student(email, password)
            else:
                print("Error")
                return enter()

    elif sr == "2":
        email = input("Enter email:")
        password = input("Enter password: ")
        data = Base.select("mentor")
        for i in data:
            if i[3] == email and i[4] == password:
                return mentor.mentor(email, password)
            else:
                print("Error")
                return enter()        
    
def register():
    first_name = input("First name :")
    last_name = input("Last name :")
    email = input("email:")
    password = input("password :")
    contact_url = input("contact_url: ")
    
    query = f"insert into student(first_name, last_name, email, password, contact_url) values('{first_name}', '{last_name}', '{email}', '{password}', '{contact_url}');"
    print(Database.connect(query, "insert"))
    return student.student(email, password)




if __name__ == "__main__":
    enter()