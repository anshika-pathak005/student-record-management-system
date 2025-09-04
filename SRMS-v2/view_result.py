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


class ViewResultManagement:
    def __init__(self,root):
        self.root = root
        # self.login_win = login_win

        # Set full screen size
        self.root.geometry("1366x750+0+0")
        self.root.title("Student Record Management System")

        self.root.config(bg='#A8D8FE')


        # Image above buttons
        icon_img = Image.open(resource_path("images/stat.png"))
        resized_icon = icon_img.resize((170, 170))
        self.icon_image = ctk.CTkImage(light_image=resized_icon, size=(170, 170))

        self.icon_label = ctk.CTkLabel(self.root, image=self.icon_image, text="", fg_color="transparent")
        self.icon_label.place(x=600, y=0)


        self.main_frame = Frame(root, width=1200, height=540, bg="white", bd=0, highlightthickness=0)
        self.main_frame.place(x=80, y=140)

        self.title = ctk.CTkLabel(self.main_frame,
                                text="Result Overview",
                                font=ctk.CTkFont(family="Segoe UI", size=25, weight="bold"),
                                text_color="white",
                                fg_color="#1a1a40",
                                corner_radius=15,
                                anchor="center",
                                width=1160,
                                height=55)
        self.title.place(x=20, y=15)

        # all the widgest and all those things


        # variables
        self.search_student_roll_var = StringVar()
        self.result_id = ""

        # input fields-----------------------------------------------------------------------
        search_student_roll = Label(self.main_frame,text="Enter Student Roll No.",font=("Helvetica", 13 ),bg="white").place(x=350,y=140)
        self.search_student_roll_text = ctk.CTkEntry(self.main_frame, textvariable=self.search_student_roll_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=250, height=35)
        self.search_student_roll_text.place(x=550, y=135)

        search_btn = Button(self.main_frame,text="Search",font=("Helvetica", 12),bg='#0a2645',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.search_student_roll).place(x=830,y=135,width=110,height=35)

        cleat_btn = Button(self.main_frame,text="Clear",font=("Helvetica", 12),bg='#0a2645',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.clear_data).place(x=960,y=135,width=110,height=35)


        # next making the lables to show the result details

        rollNo_lbl = Label(self.main_frame,text="Roll No.",font=("Helvetica", 13 ),bg="white").place(x=250,y=230,width=150,height=50)
        name_lbl = Label(self.main_frame,text="Name",font=("Helvetica", 13 ),bg="white").place(x=400,y=230,width=150,height=50)
        course_lbl = Label(self.main_frame,text="Course",font=("Helvetica", 13 ),bg="white").place(x=550,y=230,width=150,height=50)
        marks_obt_lbl = Label(self.main_frame,text="Marks Obtained",font=("Helvetica", 13 ),bg="white").place(x=700,y=230,width=150,height=50)
        total_marks_lbl = Label(self.main_frame,text="Total Marks",font=("Helvetica", 13 ),bg="white").place(x=850,y=230,width=150,height=50)
        percentage_lbl = Label(self.main_frame,text="Percentage",font=("Helvetica", 13 ),bg="white").place(x=1000,y=230,width=150,height=50)


        self.rollNo = Label(self.main_frame,font=("Helvetica", 13 ),bg="white", bd=1,relief=GROOVE)
        self.rollNo.place(x=250,y=280,width=150,height=50)
        self.name = Label(self.main_frame,font=("Helvetica", 13 ),bg="white", bd=1,relief=GROOVE)
        self.name.place(x=400,y=280,width=150,height=50)
        self.course = Label(self.main_frame,font=("Helvetica", 13 ),bg="white", bd=1,relief=GROOVE)
        self.course.place(x=550,y=280,width=150,height=50)
        self.marks_obt = Label(self.main_frame,font=("Helvetica", 13 ),bg="white", bd=1,relief=GROOVE)
        self.marks_obt.place(x=700,y=280,width=150,height=50)
        self.total_marks = Label(self.main_frame,font=("Helvetica", 13 ),bg="white", bd=1,relief=GROOVE)
        self.total_marks.place(x=850,y=280,width=150,height=50)
        self.percentage = Label(self.main_frame,font=("Helvetica", 13 ),bg="white", bd=1,relief=GROOVE)
        self.percentage.place(x=1000,y=280,width=150,height=50)


        # delete button
        self.delete_btn = Button(self.main_frame,text="Delete",font=("Helvetica", 12),bg='#0a2645',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',state="disabled",command=self.delete_data)
        self.delete_btn.place(x=635,y=430,width=110,height=35)

        # Background image on the left side
        img = Image.open(resource_path("images/view_result.png"))
        resized_img = img.resize((220, 450), Image.LANCZOS)
        self.big_img = ctk.CTkImage(light_image=resized_img, size=(220, 450))

        # Place image inside main_frame
        self.big_img_label = ctk.CTkLabel(self.main_frame, image=self.big_img, text="", fg_color="transparent")
        self.big_img_label.place(x=10, y=90)




    # getting or searching the result of the student for a particular roll no.
    def search_student_roll(self):
        con = sqlite3.connect(database = "RMS.db")
        cur = con.cursor()

        try:
            cur.execute("select * from result where roll=?",(self.search_student_roll_var.get(),))
            row = cur.fetchone()
         
            if self.search_student_roll_var.get() == "":
                messagebox.showerror("Error","Enter the Roll No. first!",parent=self.root)
                return
            
            if row != None:
                self.result_id = row[0]
                self.rollNo.config(text=row[1])
                self.name.config(text=row[2])
                self.course.config(text=row[3])
                self.marks_obt.config(text=row[4])
                self.total_marks.config(text=row[5])
                self.percentage.config(text=row[6]+"%")
                # enble delete button now because data is fethched
                self.delete_btn.config(state="normal") 
            else:
                messagebox.showinfo("No Result", "No Student Result found with this Roll Number!",parent=self.root)

 
        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")
 

    # clear data
    def clear_data(self):
        self.result_id = ""
        self.rollNo.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks_obt.config(text="")
        self.total_marks.config(text="")
        self.percentage.config(text="")
        self.search_student_roll_text.delete(0, 'end')
        self.delete_btn.config(state="disabled")  


    # delete the student result
    def delete_data(self):
        con = sqlite3.connect(database = "RMS.db")
        cur = con.cursor()

        try:
            if self.search_student_roll_text.get().strip() == "":
                messagebox.showerror("Error","Enter the Roll No. first!",parent=self.root)
                return
        
            else:
                cur.execute("select * from result where rNo=?",(self.result_id,))
                row = cur.fetchone()
                if row == None:  #this means that particular result id or roll no entered is not in my database
                    messagebox.showerror("Error","No such Roll No. exists to delete!",parent=self.root)

                else:                     
                    op = messagebox.askyesno("Confirm","Do you really want to delete the Result?",parent=self.root)
                    # if user says yes
                    if op == True:
                        cur.execute("delete from result where rNo=?",(self.result_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result has been deleted Successfullyl!",parent=self.root)
                        self.clear_data() #so that value of the input
                    # if user said no then do not do anything
                

        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")
 





if __name__ == "__main__":
    root = Tk()
    obj = ViewResultManagement(root)
    root.mainloop() #so that our window stays on looping
