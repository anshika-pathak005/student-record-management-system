# i will be using tkinter to make the gui of my project

import sys, os
import sqlite3
from tkinter import *
from PIL import Image,ImageTk
from main_course import CourseManagement
from main_student import StudentManagement
from main_result import ResultManagement
from view_result import ViewResultManagement
from tkinter import ttk,messagebox

def resource_path(relative_path):
    try:
        # When using PyInstaller
        base_path = sys._MEIPASS
    except Exception:
        # When running in IDE or as .py
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class ResultManagementSystem:
    def __init__(self,root,login_win):
        self.root = root
        self.login_win = login_win
        self.root.geometry("1366x750+0+0") #so that it start for top-right and get the whole widht
        # self.root.overrideredirect(True)
        self.root.title("Student Result Management System")
        self.root.config(bg='white')

        base_path = os.path.dirname(os.path.abspath(__file__))

        # title logo
        # image = Image.open("images/logo.jpg")  # PNG recommended
        # resized_image = image.resize((50, 50))  # Resize (width, height)
        # self.logo = ImageTk.PhotoImage(resized_image)
        image = Image.open(resource_path("images/logo.jpg"))  # PNG recommended
        resized_image = image.resize((50, 50))  # Resize (width, height)
        self.logo = ImageTk.PhotoImage(resized_image)


        # our title
        title = Label(self.root, text="Student Result Management System",padx=10,compound=LEFT,image= self.logo, font=("Helvetica", 25, "bold"), bg="white", fg="#1a1a40")
        # title.pack(pady=20)
        title.place(x=0,y=0,relwidth=1,height=50)

        # menu
        menu_frame = LabelFrame(self.root,text="Menus",font=("Arial", 15, "bold"),bg="white")
        menu_frame.place(x=10,y=70,width=1330,height=90)

        # buttons
        course_btn = Button(menu_frame,text="Course",font=("Helvetica", 12, "bold"),bg='#1a1a40',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.add_course).place(x = 20,y=5,width=200,height=40)

        student_btn = Button(menu_frame,text="Student",font=("Helvetica", 12, "bold"),bg='#1a1a40',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.add_student).place(x = 240,y=5,width=200,height=40)

        result_btn = Button(menu_frame,text="Result",font=("Helvetica", 12, "bold"),bg='#1a1a40',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.add_result).place(x = 460,y=5,width=200,height=40)

        view_btn = Button(menu_frame,text="View Result",font=("Helvetica", 12, "bold"),bg='#1a1a40',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.view_result).place(x = 680,y=5,width=200,height=40)

        logout_btn = Button(menu_frame,text="Logout",font=("Helvetica", 12, "bold"),bg='#1a1a40',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.logout_user).place(x = 900,y=5,width=200,height=40)

        exit_btn = Button(menu_frame,text="Exit",font=("Helvetica", 12, "bold"),bg='#1a1a40',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.exit_app).place(x = 1120,y=5,width=190,height=40)

        # main logo image
        # self.background_img = Image.open("images/main-logo.jpg")
        # self.background_img = self.background_img.resize((500,400),Image.Resampling.LANCZOS)
        # self.background_img = ImageTk.PhotoImage(self.background_img)
        self.background_img = Image.open(resource_path("images/main-logo.jpg"))
        self.background_img = self.background_img.resize((500, 400), Image.Resampling.LANCZOS)
        self.background_img = ImageTk.PhotoImage(self.background_img)


        self.bg_lable = Label(self.root,image=self.background_img).place(relx=0.5, rely=0.55, anchor="center",width=500,height=400)

        # main buttons
        self.course_lbl = Label(self.root,text="Total Course\n[0]",font=("Helvetica", 18),bg="#1a1a40",fg="white",bd='0',cursor='hand2')
        self.course_lbl.place(x = 225,y=620,width=280,height=70)

        self.student_lbl = Label(self.root,text="Total Students\n[0]",font=("Helvetica", 18),bg="#1a1a40",fg="white",bd='0',cursor='hand2')
        self.student_lbl.place(x = 535,y=620,width=280,height=70)

        self.result_lbl = Label(self.root,text="Total Results\n[0]",font=("Helvetica", 18),bg="#1a1a40",fg="white",bd='0',cursor='hand2')
        self.result_lbl.place(x = 845,y=620,width=280,height=70)

        self.update_details()
    
       # create footer in future

    # updation of details
    def update_details(self):
        con = sqlite3.connect(database = "RMS.db")
        cur = con.cursor()

        try:
            # for courses
            cur.execute("select * from course")
            count_course = cur.fetchall()
            #update
            self.course_lbl.config(text=f"Total Course\n[{str(len(count_course))}]") 

            # for student
            cur.execute("select * from student")
            count_student = cur.fetchall()
            #update
            self.student_lbl.config(text=f"Total Students\n[{str(len(count_student))}]")

            # for reault
            cur.execute("select * from result")
            count_result = cur.fetchall()
            #update
            self.result_lbl.config(text=f"Total Result\n[{str(len(count_result))}]")


            # for dynamic updation
            self.course_lbl.after(200,self.update_details)
        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")

    # course button --> open course window
    def add_course(self):
        # Check if window exists and is still open
        if hasattr(self, 'course_window') and self.course_window.winfo_exists():
            self.course_window.deiconify()  # Restore if minimized
            self.course_window.lift()       # Bring to front
            self.course_window.focus_force()  # Take focus
            return

        # Otherwise, create new window
        self.course_window = Toplevel(self.root)
        self.new_object = CourseManagement(self.course_window)


    # student button --> open student window
    def add_student(self):
        # Check if window exists and is still open
        if hasattr(self, 'student_window') and self.student_window.winfo_exists():
            self.student_window.deiconify()  # Restore if minimized
            self.student_window.lift()       # Bring to front
            self.student_window.focus_force()  # Take focus
            return

        # Otherwise, create new window
        self.student_window = Toplevel(self.root)
        self.new_object = StudentManagement(self.student_window)


    # result button --> open result window
    def add_result(self):
        # Check if window exists and is still open
        if hasattr(self, 'result_window') and self.result_window.winfo_exists():
            self.result_window.deiconify()  # Restore if minimized
            self.result_window.lift()       # Bring to front
            self.result_window.focus_force()  # Take focus
            return

        # Otherwise, create new window
        self.result_window = Toplevel(self.root)
        self.new_object = ResultManagement(self.result_window)
 

    # view result button --> open view result window
    def view_result(self):
        # Check if window exists and is still open
        if hasattr(self, 'view_result_window') and self.view_result_window.winfo_exists():
            self.view_result_window.deiconify()  # Restore if minimized
            self.view_result_window.lift()       # Bring to front
            self.view_result_window.focus_force()  # Take focus
            return

        # Otherwise, create new window
        self.view_result_window = Toplevel(self.root)
        self.new_object = ViewResultManagement(self.view_result_window)


    def logout_user(self):
        confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=self.root)
        if confirm:
            self.root.destroy() #close dashboard
            self.login_win.deiconify()  # Show login again
            self.login_win.focus_force() #focus lofgin


    def exit_app(self):
        confirm = messagebox.askyesno("Exit", "Are you sure you want to exit the application?", parent=self.root)
        if confirm:
            try:
                if self.login_win.winfo_exists():
                    self.login_win.destroy()
            except:
                pass  # Already destroyed, ignore

            try:
                if self.root.winfo_exists():
                    self.root.destroy()
            except:
                pass  # Already destroyed, ignore


if __name__ == "__main__":
    root = Tk()
    obj = ResultManagementSystem(root,root)
    root.mainloop() #so that our window stays on looping