from tkinter import *
from PIL import Image,ImageTk
import customtkinter as ctk
from tkinter import ttk,messagebox
import sqlite3

class ResultManagement:
    def __init__(self,root):
        self.root = root
        self.root.geometry("750x530+280+150") #so that it start for top-right and get the whole widht
        self.root.title("Student Result Management System")
        self.root.config(bg='white')
        self.root.focus_force()

        # validation for marks fields
        vcmd = (self.root.register(self.validate_numeric), '%P')

        # the title
        title = Label(self.root, text="Result Entry Panel",font=("Helvetica", 20, "bold"), bg="#1a1a40", fg="white")
        title.place(relx=0.5, y=15, anchor="n", width=1300, height=50)

        # variables definition===================================
        self.rollNo_list = []
        self.fetch_rollNo()
        self.rollNo_var = StringVar()
        self.name_var = StringVar()
        self.course_var = StringVar()
        self.marks_obt_var = StringVar()
        self.total_marks_var = StringVar()

        # input fields-----------------------------------------------------------------------
        select_student_roll = Label(self.root,text="Student Roll No.",font=("Helvetica", 13 ),bg="white").place(x=100,y=110)
        name_lbl = Label(self.root,text="Name",font=("Helvetica", 13),bg="white").place(x=100,y=150)
        course_lbl = Label(self.root,text="Course",font=("Helvetica", 13),bg="white").place(x=100,y=190)
        marks_obtained_label = Label(self.root,text="Marks Obtained",font=("Helvetica", 13),bg="white").place(x=100,y=230)
        total_mark_lbl = Label(self.root,text="Total Marks",font=("Helvetica", 13),bg="white").place(x=100,y=270)

        # user input here--------------------------------------------------------

        self.student_txt = ctk.CTkComboBox(self.root, values=[str(rn) for rn in self.rollNo_list], variable=self.rollNo_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=250, height=35, dropdown_font=("Helvetica", 15), dropdown_fg_color="white", dropdown_text_color="black", button_color="#a6a5a5", button_hover_color="#e0e0e0")
        self.student_txt.place(x=300, y=110)

        # search button
        search_btn = Button(self.root,text="Search",font=("Helvetica", 12),bg='#0a2645',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.search_student_roll).place(x=580,y=110,width=110,height=35)

        name_text = ctk.CTkEntry(self.root, textvariable=self.name_var, font=("Helvetica", 15),state="readonly", corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=390, height=35).place(x=300, y=150)

        course_text = ctk.CTkEntry(self.root, textvariable=self.course_var, font=("Helvetica", 15),state="readonly", corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=390, height=35).place(x=300, y=190)

        marks_obt_text = ctk.CTkEntry(self.root, textvariable=self.marks_obt_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=390, height=35, validate="key",validatecommand=vcmd).place(x=300, y=230)

        total_marks_text = ctk.CTkEntry(self.root, textvariable=self.total_marks_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=390, height=35,validate="key",validatecommand=vcmd).place(x=300, y=270)


        # buttons---------------------------------
        submit_btn = Button(self.root,text="Submit",font=("Helvetica", 12),bg='#0a2645',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.add_result).place(x=180,y=400,width=150,height=40)
        clear_btn = Button(self.root,text="Clear",font=("Helvetica", 12),bg='#0a2645',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.clear_data).place(x=430,y=400,width=150,height=40)

    # functions ================================================================

    # validation
    def validate_numeric(self, value):
        return value.isdigit() or value == ""


    # fetching the roll no of students, enrolled in our system
    def fetch_rollNo(self):
        con = sqlite3.connect(database = "RMS.db")
        cur = con.cursor()

        try:
            cur.execute("select roll from Student")
            rows = cur.fetchall()

            if len(rows) > 0:
                for row in rows:
                    self.rollNo_list.append(row[0])

        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")
 

    # getting or searching all the data of the student for a particular roll no.
    def search_student_roll(self):
        con = sqlite3.connect(database = "RMS.db")
        cur = con.cursor()

        # if we search any course in the search bar then , it will look into the database and will return the course which is like that course means jiska name similar ho, now it will first delete all the entries from the table , and insert only those rows which have similar name as searched course name

        try:
            cur.execute("select name,course from student where roll=?",(self.rollNo_var.get(),))
            row = cur.fetchone()
         
            if self.rollNo_var.get() == "":
                messagebox.showerror("Error","Select/Enter the Roll No. first!",parent=self.root)
            elif row != None:
                # Check name
                if row[0] == "":
                    self.name_var.set("N/A")
                else:
                    self.name_var.set(row[0])

                # Check course
                if row[1] == "":
                    self.course_var.set("N/A")
                else:
                    self.course_var.set(row[1])
            else:
                messagebox.showinfo("No Result", "No student found with this Roll Number!",parent=self.root)

 
        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")
 

    def add_result(self):

        if (self.rollNo_var.get() == "" or 
            self.name_var.get() == "" or 
            self.course_var.get() == "" or 
            self.marks_obt_var.get() == "" or 
            self.total_marks_var.get() == ""):
            
            messagebox.showerror("Error", "Please fill all the fields before submitting!", parent=self.root)
            return


        con = sqlite3.connect(database = "RMS.db")
        cur = con.cursor()

        try:
            if self.name_var.get() == "":
                messagebox.showerror("Error","Roll Number and Name are required!",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.rollNo_var.get(),self.course_var.get()))
                row = cur.fetchone()
                if row != None: #this means entered result and course name is already in my result db
                    messagebox.showerror("Error","Result for this student and course already exists!",parent=self.root)
                else: 
                    # calculate percentage
                    percentage = (int(self.marks_obt_var.get()) * 100 )/int(self.total_marks_var.get())
                    # means agr nhi hua record result db me to main ye result db me add kar dungi
                    cur.execute("insert into result (roll, name,course,marks_obt,total_marks, percentage) values(?,?,?,?,?,?)",(
                        self.rollNo_var.get(),
                        self.name_var.get(),
                        self.course_var.get(),
                        self.marks_obt_var.get(),
                        self.total_marks_var.get(),
                        str(percentage)
                    ))
                    con.commit()
                    
                    messagebox.showinfo("Success","Result has been added Successfully!",parent=self.root)

        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")
 
    def clear_data(self):
        self.rollNo_var.set(""),
        self.name_var.set(""),
        self.course_var.set(""),
        self.marks_obt_var.set(""),
        self.total_marks_var.set("")


if __name__ == "__main__":
    root = Tk()
    obj = ResultManagement(root)
    root.mainloop() #so that our window stays on looping