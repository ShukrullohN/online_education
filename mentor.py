from classes import Base
import project
from db_connect import Database


def back(email, password):
    back = input("""
            0. back
                >>> """)
    if back == "0":
        return mentor(email, password)

    else:
        print("Error")
        return course(email, password)

def course_insert(email, password):

    name = input("Name: ")
    description = input("description: ")
    rating = input("rating: ")
    active_Students = input("active_Students: ")
    mentor_id = input("mentor_id: ")
    lenguage_id = input("lenguage_id: ")
    price = input("price: ")
    course_status_id = input("course_status_id: ")
    support_date = input("support_date: ")
    spec = Course(name, description, rating, active_Students, mentor_id, lenguage_id, price, course_status_id, support_date)
    print(spec.insert("course"))
    return back(email, password)

def course_list(email, password):
    data = Course.select("course")
    for i in data:
        print(f"""
                ID: {i[0]}
                Name: {i[1]}
                description: {i[2]}
                rating: {i[3]}
                Mentor First Name: {i[4]}
                Mentor Last Name: : {i[5]}
                Status: {i[6]}
                Lenguage: {i[7]}
                Price: {i[8]}
                            """)

    return back(email, password)

def course_update(email, password):
    column_name = input("Column Name: ")
    old_data = input("Now Data: ")
    new_data = input("New Data: ")
    if column_name == "speciality_id":
        print(Base.update_id("course", column_name, old_data, new_data))
    else:
        print(Base.update("course", column_name, old_data, new_data))
    return course(email, password)


def course_delete(email, password):
    column_name = input("Column Name: ")
    data = input("Data: ")
    if column_name == "speciality_id":
        print(Base.delete_id("course", column_name, data))

    else:
        print(Base.delete("course", column_name, data))

    return course(email, password)


def course(email, password):
    services = input("""
            1. List
            2. Insert
            3. Update
            4. Delete
            0. back
                >>> """)

    if services == "1":
        return course_list(email, password)

    elif services == "2":
        return course_insert(email, password)

    elif services == "3":
        return course_update(email, password)

    elif services == "4":
        return course_delete(email, password)

def speciality_insert(email, password):

    name = input("Name: ")
    query = f"INSERT INTO speciality(name) VALUES('{name}');"
    print(Database.connect(query, "insert"))
    return back(email, password)


def speciality_list(email, password):
    data = Base.select("speciality")
    for i in data:
        print(f"""
                ID: {i[0]}
                Name: {i[1]}
            """)

    return back(email, password)

def speciality_update(email, password):
    column_name = input("Column Name: ")
    old_data = input("Now Data: ")
    new_data = input("New Data: ")
    if column_name == "speciality_id":
        print(Base.update_id("speciality", column_name, old_data, new_data))
    else:
        print(Base.update("speciality", column_name, old_data, new_data))
    return speciality(email, password)


def speciality_delete(email, password):
    column_name = input("Column Name: ")
    data = input("Data: ")
    if column_name == "speciality_id":
        print(Base.delete_id("speciality", column_name, data))

    else:
        print(Base.delete("speciality", column_name, data))

    return speciality(email, password)


def speciality(email, password):
    services = input("""
            1. List
            2. Insert
            3. Update
            4. Delete
            0. back
                >>> """)

    if services == "1":
        return speciality_list(email, password)

    elif services == "2":
        return speciality_insert(email, password)

    elif services == "3":
        return speciality_update(email, password)

    elif services == "4":
        return speciality_delete(email, password)

    elif services == "0":
        return mentor(email, password)

    else:
        return speciality(email, password)

def profile_list(email, password):
    data = Base.select("mentor")
    for i in data:
        print(f"""
        first_name: {i[1]}
        last_name: {i[2]}
        email: {i[3]}
        password: {i[4]}
        headline: {i[5]}
        bio: {i[6]}
        contact_url: {i[7]}
        """)

        return mentor(email, password)

def profile_update(email, password):
    column_name = input("Column Name: ")
    old_data = input("Now Data: ")
    new_data = input("New Data: ")
    if column_name == "profile_id":
        print(Base.update_id("mentor", column_name, old_data, new_data))
    else:
        print(Base.update("mentor", column_name, old_data, new_data))
    return profile(email, password)

def profile_delete(email, password):
    column_name = input("Column Name: ")
    data = input("Data: ")
    if column_name == "profile_id":
        print(Base.delete_id("mentor", column_name, data))

    else:
        print(Base.delete("mentor", column_name, data))

    return profile(email, password)


def profile(email, password):
    print("Profile page")
    ser = input("""
        1. Edit
        2. Back
            >>> """)
    if ser == "2":
        return mentor(email, password)

    elif ser == "1":
        services = input("""
        1. List
        2. Update
        3. Delete
        0. back
            >>> """)
        
        if services == "1":
            return profile_list(email, password)

        elif services == "2":
            return profile_update(email, password)   

        elif services == "3":
            return profile_delete(email, password)


        elif services == "0":
            return mentor(email, password)   

        else:
            print("Error!")    
            return profile(email, password) 
    
    else:
        print("Error!")
        return profile(email, password)


def log_out(email, password):
    print("Log out page")
    ser = input("""
        1. Log out
        2. Back
            >>> """)
    if ser == "2":
        return mentor(email, password)
    elif ser == "1":
        data = Base.select("mentor")
        id = data[0][0]
        Base.delete_id("mentor", "mentor_id", id)
        return project.enter()

            

def mentor(email, password):
    print("mentor Page")
    services = input("""
        1. Specialitys
        2. Courses
        3. Profile
        4. Log Out
            >>> """)

    if services == "1":
        return speciality(email, password) 

    elif services == "2":
        return course(email, password)

    elif services == "3":
        return profile(email, password)

    elif services == "4":
        return log_out(email, password)

    else:
        return mentor(email, password)

