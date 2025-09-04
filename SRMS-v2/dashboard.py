# i will be using tkinter to make the gui of my project

import sys, os
import sqlite3
from tkinter import *
from PIL import Image,ImageTk
from course import CourseManagement
from student import StudentManagement
from result import ResultManagement
from view_result import ViewResultManagement
from tkinter import ttk,messagebox
import customtkinter as ctk

def resource_path(relative_path):
    try:
        # When using PyInstaller
        base_path = sys._MEIPASS
    except Exception:
        # When running in IDE or as .py
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class StudentManagementSystem:
    def __init__(self,root,login_win,first_name):
        self.root = root
        self.login_win = login_win
        self.first_name = first_name
        self.root.geometry("1366x750+0+0") #so that it start for top-right and get the whole widht
        self.root.title("Student Record Management System")
        self.root.config(bg='#A8D8FE')
        self.root.protocol("WM_DELETE_WINDOW",self.exit_app)

        image = Image.open(resource_path("images/dash.png"))
        resized_image = image.resize((100, 100))
        self.logo = ctk.CTkImage(light_image=resized_image, size=(100, 100))

        # title logo2
        image2 = Image.open(resource_path("images/username.png"))
        resized_image2 = image2.resize((100, 100))
        self.logo2 = ctk.CTkImage(light_image=resized_image2, size=(100, 100))


        # title 1
        title = ctk.CTkLabel(root,
                            text="Dashboard",
                            font=ctk.CTkFont(family="Segoe UI", size=35, weight="bold"),
                            text_color="#1a1a40",
                            fg_color="white",
                            corner_radius=15,
                            anchor="w",
                            padx=10,
                            width=900,
                            compound=LEFT,
                            image= self.logo,
                            height=100)
        title.place(x=20, y=15)

        # title 2
        title = ctk.CTkLabel(root,
                            text=f"Hello! {self.first_name}",
                            font=ctk.CTkFont(family="Segoe UI", size=35, weight="bold"),
                            text_color="#1a1a40",
                            fg_color="white",
                            anchor="w",
                            padx=10,
                            width=450,
                            compound=LEFT,
                            image= self.logo2,
                            height=100)
        title.place(x=890, y=15)


        # buttons


        course_btn = ctk.CTkButton(
                            master=self.root,
                           text="Course",
                           font=ctk.CTkFont("Segoe UI", 17, "bold"),
                           fg_color="#1a1a40",             # normal background
                           hover_color="#21649A",          # on hover
                           text_color="white",
                           corner_radius=10,               # makes it rounded
                           cursor="hand2", width=200, height=50,
                           command=self.add_course
                           )
        course_btn.place(x=20, y=150)

        student_button = ctk.CTkButton(
                            master=self.root,
                           text="Student",
                           font=ctk.CTkFont("Segoe UI", 17, "bold"),
                           fg_color="#1a1a40",             # normal background
                           hover_color="#21649A",          # on hover
                           text_color="white",
                           corner_radius=10,               # makes it rounded
                           cursor="hand2", width=200, height=50,
                           command=self.add_student
                           )
        student_button.place(x=240, y=150)

        result_btn = ctk.CTkButton(
                            master=self.root,
                           text="Result",
                           font=ctk.CTkFont("Segoe UI", 17, "bold"),
                           fg_color="#1a1a40",             # normal background
                           hover_color="#21649A",          # on hover
                           text_color="white",
                           corner_radius=10,               # makes it rounded
                           cursor="hand2", width=200, height=50,
                           command=self.add_result
                           )
        result_btn.place(x=460, y=150)

        view_result = ctk.CTkButton(
                            master=self.root,
                           text="View Result",
                           font=ctk.CTkFont("Segoe UI", 17, "bold"),
                           fg_color="#1a1a40",             # normal background
                           hover_color="#21649A",          # on hover
                           text_color="white",
                           corner_radius=10,               # makes it rounded
                           cursor="hand2", width=200, height=50,
                           command=self.view_result
                           )
        view_result.place(x=680, y=150)

        logout_btn = ctk.CTkButton(
                            master=self.root,
                           text="Logout",
                           font=ctk.CTkFont("Segoe UI", 17, "bold"),
                           fg_color="#1a1a40",             # normal background
                           hover_color="#21649A",          # on hover
                           text_color="white",
                           corner_radius=10,               # makes it rounded
                           cursor="hand2", width=200, height=50,
                           command=self.logout_user
                           )
        logout_btn.place(x=900, y=150)

        exit_btn = ctk.CTkButton(
                            master=self.root,
                           text="Exit",
                           font=ctk.CTkFont("Segoe UI", 17, "bold"),
                           fg_color="#1a1a40",             # normal background
                           hover_color="#21649A",          # on hover
                           text_color="white",
                           corner_radius=10,               # makes it rounded
                           cursor="hand2", width=200, height=50,
                           command=self.exit_app
                           )
        exit_btn.place(x=1120, y=150)


        # # main logo

        # Load and resize the image
        image = Image.open(resource_path("images/main-logo.jpg"))
        resized_image = image.resize((750, 500))
        self.background_img = ctk.CTkImage(light_image=resized_image, size=(750, 500))

        # Display the image using CTkLabel
        self.bg_label = ctk.CTkLabel(self.root, image=self.background_img, text="", width=750, height=500)
        self.bg_label.place(relx=0.6, rely=0.65, anchor="e")

        icon_img = Image.open(resource_path("images/stat.png"))  # Replace with your image path
        resized_icon_img = icon_img.resize((170, 170))
        icon_ctk_img = ctk.CTkImage(light_image=resized_icon_img, size=(170, 170))

        # Image above buttons
        self.icon_label = ctk.CTkLabel(self.root, image=icon_ctk_img, text="", fg_color="transparent")
        self.icon_label.place(x=1000, y=200)  # Position as needed


        # Buttons shifted slightly downward
        self.course_lbl = ctk.CTkButton(self.root, text="Total Course\n[0]", width=350, height=80,
            font=ctk.CTkFont("Segoe UI", 18, "bold"), fg_color="#1a1a40", hover_color="#2b6cb0",
            text_color="white", corner_radius=10, cursor="hand2", command=self.show_all_courses_window)
        self.course_lbl.place(x=900, y=340)

        self.student_lbl = ctk.CTkButton(self.root, text="Total Students\n[0]", width=350, height=80,
            font=ctk.CTkFont("Segoe UI", 18, "bold"), fg_color="#1a1a40", hover_color="#2b6cb0",
            text_color="white", corner_radius=10, cursor="hand2", command=self.show_all_students_window)
        self.student_lbl.place(x=900, y=450)

        self.result_lbl = ctk.CTkButton(self.root, text="Total Results\n[0]", width=350, height=80,
            font=ctk.CTkFont("Segoe UI", 18, "bold"), fg_color="#1a1a40", hover_color="#2b6cb0",
            text_color="white", corner_radius=10, cursor="hand2", command=self.show_all_results_window)
        self.result_lbl.place(x=900, y=560)

        # showing the data in button
        self.update_details()

# =============================funtions========================================================

    # updation of details
    def update_details(self):
        con = sqlite3.connect(database = "RMS.db")
        cur = con.cursor()

        try:
            # for courses
            cur.execute("select * from course")
            count_course = cur.fetchall()
            #update
            self.course_lbl.configure(text=f"Total Course\n[{str(len(count_course))}]") 

            # for student
            cur.execute("select * from student")
            count_student = cur.fetchall()
            #update
            self.student_lbl.configure(text=f"Total Students\n[{str(len(count_student))}]")

            # for result
            cur.execute("select * from result")
            count_result = cur.fetchall()
            #update
            self.result_lbl.configure(text=f"Total Result\n[{str(len(count_result))}]")


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

        # Otherwise open course window
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

    # click logout to get logout from the system
    def logout_user(self):
        confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=self.root)
        if confirm:
            self.root.destroy() #close dashboard
            self.login_win.deiconify()  # Show login again
            self.login_win.focus_force() #focus lofgin

    # click exit to exit the whole application
    def exit_app(self):
        confirm = messagebox.askyesno("Exit", "Are you sure you want to exit the application?", parent=self.root)
        if confirm:
            try:
                if self.login_win.winfo_exists():
                    self.login_win.destroy()
            except:
                pass 

            try:
                if self.root.winfo_exists():
                    self.root.destroy()
            except:
                pass  

    # total student window
    def show_all_students_window(self):
        win = Toplevel(self.root)
        win.title("All Students")
        win.geometry("900x500+250+180")
        win.config(bg="white")

        title = ctk.CTkLabel(win,
                            text="All Registered Students",
                            font=ctk.CTkFont(family="Segoe UI", size=25, weight="bold"),
                            text_color="white",
                            fg_color="#1a1a40",
                            corner_radius=10,
                            anchor="center",
                            width=880,   
                            height=55)
        title.place(x=10, y=15)

        # Table Frame with .place()
        table_frame = Frame(win, bd=0, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=85, width=880, height=400)  # Adjust height accordingly

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,
            columns=("roll", "name", "email", "gender", "dob", "contact", "course"),
            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("roll", text="Roll No", anchor="center")
        self.student_table.heading("name", text="Name", anchor="center")
        self.student_table.heading("email", text="Email", anchor="center")
        self.student_table.heading("gender", text="Gender", anchor="center")
        self.student_table.heading("dob", text="DOB", anchor="center")
        self.student_table.heading("contact", text="Contact", anchor="center")
        self.student_table.heading("course", text="Course", anchor="center")

        self.student_table["show"] = "headings"
        self.student_table.column("roll", width=100, anchor="center")
        self.student_table.column("name", width=150, anchor="center")
        self.student_table.column("email", width=150, anchor="center")
        self.student_table.column("gender", width=100, anchor="center")
        self.student_table.column("dob", width=100, anchor="center")
        self.student_table.column("contact", width=100, anchor="center")
        self.student_table.column("course", width=100, anchor="center")

        self.student_table.pack(fill=BOTH, expand=True)

        # Load data from DB
        self.fetch_student_data()

    # ṭotal student fetching
    def fetch_student_data(self):
        con = sqlite3.connect("RMS.db") 
        cur = con.cursor()
        try:
            cur.execute("SELECT roll, name, email, gender, dob, contact, course FROM student")
            rows = cur.fetchall()
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching data:\n{str(ex)}", parent=self.root)
        finally:
            con.close()


    # total course  window
    def show_all_courses_window(self):
        win = Toplevel(self.root)
        win.title("All Courses")
        win.geometry("900x500+250+180")
        win.config(bg="white")

        title = ctk.CTkLabel(win,
                            text="All Registered Courses",
                            font=ctk.CTkFont(family="Segoe UI", size=25, weight="bold"),
                            text_color="white",
                            fg_color="#1a1a40",
                            corner_radius=10,
                            anchor="center",
                            width=880,
                            height=55)
        title.place(x=10, y=15)

        # Table Frame with .place()
        table_frame = Frame(win, bd=0, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=85, width=880, height=400)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.course_table = ttk.Treeview(table_frame,
            columns=("cid", "name", "duration", "charges"),
            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.course_table.xview)
        scroll_y.config(command=self.course_table.yview)

        self.course_table.heading("cid", text="Course ID", anchor="center")
        self.course_table.heading("name", text="Course Name", anchor="center")
        self.course_table.heading("duration", text="Duration", anchor="center")
        self.course_table.heading("charges", text="Charges", anchor="center")

        self.course_table["show"] = "headings"
        self.course_table.column("cid", width=100, anchor="center")
        self.course_table.column("name", width=300, anchor="center")
        self.course_table.column("duration", width=150, anchor="center")
        self.course_table.column("charges", width=100, anchor="center")

        self.course_table.pack(fill=BOTH, expand=True)

        # Load data from DB
        self.fetch_course_data()

    # ṭotal course fetching form db
    def fetch_course_data(self):
        con = sqlite3.connect("RMS.db") 
        cur = con.cursor()
        try:
            cur.execute("SELECT c_id, name, duration, charges FROM course")
            rows = cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching course data:\n{str(ex)}", parent=self.root)
        finally:
            con.close()


    # total results window
    def show_all_results_window(self):
        try:
            win = Toplevel(self.root)
            win.geometry("900x500+250+180")
            win.title("Declared Results")
            win.config(bg="white")

            # CTkLabel for Title
            title = ctk.CTkLabel(win,
                                text="All Declared Results",
                                font=ctk.CTkFont(family="Segoe UI", size=25, weight="bold"),
                                text_color="white",
                                fg_color="#1a1a40",
                                corner_radius=15,
                                width=860,
                                height=55,
                                anchor="center")
            title.place(x=20, y=15)

            # Frame for Table
            table_frame = Frame(win, bg="white")
            table_frame.place(x=20, y=90, width=860, height=380)

            scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
            scroll_y = Scrollbar(table_frame, orient=VERTICAL)

            self.resultTable = ttk.Treeview(table_frame,
                                            columns=("roll", "name", "course", "marks", "total", "percent"),
                                            xscrollcommand=scroll_x.set,
                                            yscrollcommand=scroll_y.set)

            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=self.resultTable.xview)
            scroll_y.config(command=self.resultTable.yview)

            # self.resultTable.heading("rno", text="Result ID")
            self.resultTable.heading("roll", text="Roll No")
            self.resultTable.heading("name", text="Name")
            self.resultTable.heading("course", text="Course")
            self.resultTable.heading("marks", text="Marks Obtained")
            self.resultTable.heading("total", text="Total Marks")
            self.resultTable.heading("percent", text="Percentage")
            self.resultTable["show"] = "headings"

            for col in ("roll", "name", "course", "marks", "total", "percent"):
                self.resultTable.column(col, width=120, anchor="center")

            self.resultTable.pack(fill=BOTH, expand=1)

            self.fetch_result_data()
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")

    # total result fetching from db
    def fetch_result_data(self):
        try:
            con = sqlite3.connect("RMS.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM result")
            rows = cur.fetchall()
            self.resultTable.delete(*self.resultTable.get_children())
            for row in rows:
                self.resultTable.insert('', END, values=row[1:])
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = StudentManagementSystem(root,root,first_name="Anshika")
    root.mainloop() #so that our window stays on looping