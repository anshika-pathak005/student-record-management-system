import sys, os
import sqlite3
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import customtkinter as ctk
from PIL import Image
import customtkinter as ctk

def resource_path(relative_path):
    try:
        # When using PyInstaller
        base_path = sys._MEIPASS
    except Exception:
        # When running in IDE or as .py
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class ResultManagement:
    def __init__(self,root):
        self.root = root
        # self.login_win = login_win

        # Set full screen size
        self.root.geometry("1366x750+0+0")
        self.root.title("Student Record Management System")

        self.root.config(bg='#A8D8FE')

        # validation for marks fields
        vcmd = (self.root.register(self.validate_numeric), '%P')



        # Image above buttons
        icon_img = Image.open(resource_path("images/stat.png"))
        resized_icon = icon_img.resize((170, 170))
        self.icon_image = ctk.CTkImage(light_image=resized_icon, size=(170, 170))

        self.icon_label = ctk.CTkLabel(self.root, image=self.icon_image, text="", fg_color="transparent")
        self.icon_label.place(x=600, y=0)


        self.main_frame = Frame(root, width=1200, height=540, bg="white", bd=0, highlightthickness=0)
        self.main_frame.place(x=80, y=140)

        self.title = ctk.CTkLabel(self.main_frame,
                                text="Result Management Pannel",
                                font=ctk.CTkFont(family="Segoe UI", size=25, weight="bold"),
                                text_color="white",
                                fg_color="#1a1a40",
                                corner_radius=15,
                                anchor="center",
                                width=1160,
                                height=55)
        self.title.place(x=20, y=15)

        # all the widgest and all those things


        # variables definition===================================
        self.rollNo_list = []
        self.fetch_rollNo()
        self.rollNo_var = StringVar()
        self.name_var = StringVar()
        self.course_var = StringVar()
        self.marks_obt_var = StringVar()
        self.total_marks_var = StringVar()


        # input fields-----------------------------------------------------------------------
        select_student_roll = Label(self.main_frame,text="Student Roll No.",font=("Segoe UI", 13 ,"bold"),bg="white").place(x=100,y=110)
        name_lbl = Label(self.main_frame,text="Name",font=("Segoe UI", 13 ,"bold"),bg="white").place(x=100,y=150)
        course_lbl = Label(self.main_frame,text="Course",font=("Segoe UI", 13 ,"bold"),bg="white").place(x=100,y=190)
        marks_obtained_label = Label(self.main_frame,text="Marks Obtained",font=("Segoe UI", 13 ,"bold"),bg="white").place(x=100,y=230)
        total_mark_lbl = Label(self.main_frame,text="Total Marks",font=("Segoe UI", 13 ,"bold"),bg="white").place(x=100,y=270)

        # user input here--------------------------------------------------------

        self.student_txt = ctk.CTkComboBox(self.main_frame, values=[str(rn) for rn in self.rollNo_list], variable=self.rollNo_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=250, height=35, dropdown_font=("Helvetica", 15), dropdown_fg_color="white", dropdown_text_color="black", button_color="#a6a5a5", button_hover_color="#e0e0e0")
        self.student_txt.place(x=300, y=110)

        # search button
        ctk.CTkButton(self.main_frame, text="Search", font=ctk.CTkFont("Segoe UI", 15,"bold"), fg_color="#1a1a40", hover_color="#21649A", text_color="white", corner_radius=10, cursor="hand2", width=110, height=35,command=self.search_student_roll).place(x=580, y=110)
                
        name_text = ctk.CTkEntry(self.main_frame, textvariable=self.name_var, font=("Helvetica", 15),state="readonly", corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=390, height=35).place(x=300, y=150)

        course_text = ctk.CTkEntry(self.main_frame, textvariable=self.course_var, font=("Helvetica", 15),state="readonly", corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=390, height=35).place(x=300, y=190)

        marks_obt_text = ctk.CTkEntry(self.main_frame, textvariable=self.marks_obt_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=390, height=35, validate="key",validatecommand=vcmd).place(x=300, y=230)

        total_marks_text = ctk.CTkEntry(self.main_frame, textvariable=self.total_marks_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=390, height=35,validate="key",validatecommand=vcmd).place(x=300, y=270)


        # buttons---------------------------------
        ctk.CTkButton(self.main_frame, text="Submit", font=ctk.CTkFont("Segoe UI", 15,"bold"), fg_color="#1a1a40", hover_color="#21649A", text_color="white", corner_radius=10, cursor="hand2", width=150, height=40,command=self.add_result).place(x=180, y=400)

        ctk.CTkButton(self.main_frame, text="Clear", font=ctk.CTkFont("Segoe UI",  15,"bold"), fg_color="#1a1a40", hover_color="#21649A", text_color="white", corner_radius=10, cursor="hand2", width=150, height=40,command=self.clear_data).place(x=430, y=400)


        # Right side image
        img = Image.open(resource_path("images/result3.jpeg"))
        resized_img = img.resize((380, 450), Image.LANCZOS)
        self.big_img = ctk.CTkImage(light_image=resized_img, size=(380, 450))

        # Place image inside main_frame
        self.big_img_label = ctk.CTkLabel(self.main_frame, image=self.big_img, text="", fg_color="transparent")
        self.big_img_label.place(x=750, y=70)



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
                    self.clear_data()

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
