import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import sqlite3 as sql


# Connect Database



def enter_data():
    accepted = accept_var.get()
    
    if accepted=="Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            title = title_combobox.get()
            dob = dob_cal.get()
            gender = gender_combobox.get()
            telephone = telephone_entry.get()
            
            # Course info
            registration_status = reg_status_var.get()
            course = course_combobox.get()
            email =email_entry.get()
         
            
            print("First name: ", firstname, "Last name: ", lastname)
            print("Title: ", title, "DOB: ", dob, "Gender: ", gender, "Telephone: ", telephone)
            print("Course: ", course, "# Email: ", email)
            print("Registration status", registration_status)
            print("------------------------------------------")
            
            # Create Table
            conn = sql.connect('Python/Python Personal Project/Data Entry Project/student.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data 
                    (firstname TEXT, lastname TEXT, title TEXT, dob INT, gender TEXT, telephone TEXT,
                    registration_status TEXT, course TEXT, email INT)
            '''
            conn.execute(table_create_query)
            
            # Insert Data
            data_insert_query = '''INSERT INTO Student_Data (firstname, lastname, title, 
            dob, gender, telephone, registration_status, course, email) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (firstname, lastname, title,
                                  dob, gender,telephone, registration_status, course, email)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()

            
                
        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms")

window = tkinter.Tk()
window.title("Student Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame =tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Mrs.","Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

dob_label = tkinter.Label(user_info_frame, text="DOB")
dob_cal=DateEntry(user_info_frame,selectmode='day')
dob_label.grid(row=2, column=0)
dob_cal.grid(row=3, column=0)


gender_label = tkinter.Label(user_info_frame, text="Gender")
gender_combobox = ttk.Combobox(user_info_frame, values=["Male", "Female"])
gender_label.grid(row=2, column=1)
gender_combobox.grid(row=3, column=1)

telephone_label = tkinter.Label(user_info_frame, text="Telephone")
telephone_entry = ttk.Entry(user_info_frame)
telephone_label.grid(row=2, column=2)
telephone_entry.grid(row=3, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

course_label = tkinter.Label(courses_frame, text= "# Course Name")
course_combobox = ttk.Combobox(courses_frame, values=["Data Analytics", "Software Development", "IT Technician", "Networking"])
course_label.grid(row=0, column=1)
course_combobox.grid(row=1, column=1)

email_label = tkinter.Label(courses_frame, text="# Email")
email_entry = tkinter.Entry(courses_frame)
email_label.grid(row=0, column=3)
email_entry.grid(row=1, column=3)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=20, pady=8)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
 
window.mainloop()