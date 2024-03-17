from classes import Base
def back(email, password):
    back = input("""
        0. Back
    """)
    if back == "0":
        return student(email, password)

   
    
def profile(email, password):
    services = input("""
        1. Edit
        2. Back
    """)
    if services == "1":
        ser = input("""
        1. First_name
        2. Last_name
        3. email
        4. Password
        5. Contact
        6. Back
              """)
        if ser == "1":
            old_data = input("Enter old data")
            new_data = input("Enter new data")

            data = Base.update("student", "first_name", old_data, new_data)
            return profile(email, password)

        elif ser == "2":
            old_data = input("Enter old data")
            new_data = input("Enter new data")
            
            data = Base.update("student", "last_name", old_data, new_data)
            return profile(email, password)

        elif ser == "3":
            old_data = input("Enter old data")
            new_data = input("Enter new data")
            data = Base.update("student", "email", old_data, new_data)
            return profile(email, password)

        elif ser == "4":
            old_data = input("Enter old data")
            new_data = input("Enter new data")
            data = Base.update("student", "password", old_data, new_data)
            return profile(email, password)

        elif ser == "5":
            old_data = input("Enter old data")
            new_data = input("Enter new data")
            data = Base.update("student", "contact_url", old_data, new_data)
            return profile(email, password)                
        
        elif ser == "6":
            return student(email, password)

        else:
            print("Error")
            return student(email, password)    
       
    elif services == "2":
        return student(email, password)
    else:
        print("Error")
        return profile(email, password)
def speciality(email, password):
    data = Base.select("speciality")
    for i in data:
        print(f"""
        ID: {i[0]}
        Name: {i[1]}
        """)
    return back(email, password)


def courses(email, password):
    data = Base.select("course")
    for i in data:
        print(f"""
        ID: {i[0]}
        name: {i[1]}
        description: {i[2]}
        rating: {i[3]}
        price: {i[7]}
        lenguage_id: {i[6]}
        last_update: {i[9]}
        """)
    
    return back(email, password)
    
def log_out(email, password):
    ser = input("""
        Are you sure to log out
        1. Yes
        2. Back
    """)      
    if ser == "1":
        Base.delete("student", "email", email)

def student(email, password):
    print("Student Page")
    services = input("""
        1. Specialitys
        2. Courses
        3. Profile
        4. Log Out
            >>> """)

    if services == "1":
        return speciality(email, password)

    elif services == "2":
        return courses(email, password)

    elif services == "3":
        return profile(email, password)

    elif services == "4":
        return log_out(email, password)

    else:
        return student(email, password)
    



