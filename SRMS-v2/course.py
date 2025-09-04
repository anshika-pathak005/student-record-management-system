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


class CourseManagement:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x750+0+0")
        self.root.title("Student Record Management System")
        self.root.config(bg='#A8D8FE')


        # Load and resize the image for the icon above the frame
        icon_img = Image.open(resource_path("images/stat.png"))
        resized_icon_img = icon_img.resize((170, 170))
        icon_ctk_img = ctk.CTkImage(light_image=resized_icon_img, size=(170, 170))

        self.icon_label = ctk.CTkLabel(self.root, image=icon_ctk_img, text="", fg_color="transparent")
        self.icon_label.place(x=600, y=10)  # Adjust x and y if needed


        # frame in which everything will be placed
        self.main_frame = Frame(root, width=1200, height=530, bg="white", bd=0, highlightthickness=0)
        self.main_frame.place(x=80, y=150)

        self.title = ctk.CTkLabel(self.main_frame,
                                text="Course Management Pannel",
                                font=ctk.CTkFont(family="Segoe UI", size=25, weight="bold"),
                                text_color="white",
                                fg_color="#1a1a40",
                                corner_radius=15,
                                anchor="center",     # Center the text
                                width=1160,
                                height=55)
        self.title.place(x=20, y=15)

        # main-frame background image
        bg_img = Image.open(resource_path("images/cources.png"))
        resized_bg_img = bg_img.resize((250, 250))
        self.background_img = ctk.CTkImage(light_image=resized_bg_img, size=(250, 250))

        self.bg_label = ctk.CTkLabel(self.main_frame, image=self.background_img, text="", width=250, height=250)
        self.bg_label.place(x=450, y=100)


        # variable to fetch the values
        self.course_var = StringVar()
        self.duration_var = StringVar() 
        self.charges_var = StringVar()

        # input fields-----------------------------------------------------------------------
        course_name = Label(self.main_frame,text="Course Name *",font=("Helvetica", 13 ),bg="white").place(x=20,y=110)
        duration_lbl = Label(self.main_frame,text="Duration *",font=("Helvetica", 13),bg="white").place(x=20,y=150)
        charges_lbl = Label(self.main_frame,text="Charges *",font=("Helvetica", 13),bg="white").place(x=20,y=190)
        description_lbl = Label(self.main_frame,text="Description",font=("Helvetica", 13),bg="white").place(x=20,y=230)


        # user input here----------------------------------------------------------------
        self.course_name_txt = ctk.CTkEntry(self.main_frame, textvariable=self.course_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="gray", border_width=1, text_color="black", width=230, height=35)
        self.course_name_txt.place(x=180, y=110)
        self.course_name_txt.bind("<Return>", self.prefill_data_from_course)


        duration_txt = ctk.CTkEntry(self.main_frame, textvariable=self.duration_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=230, height=35).place(x=180, y=150)

        charges_txt = ctk.CTkEntry(self.main_frame,textvariable=self.charges_var,font=("Helvetica", 15),corner_radius=5, fg_color="white", border_color="gray", border_width=1,text_color="black", width=230, height=35).place(x=180,y=190)

        self.description_txt = ctk.CTkTextbox(self.main_frame, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="gray", border_width=1, text_color="black", width=250, height=100)
        self.description_txt.place(x=180, y=230)

        # buttons---------------------------------------------------------------------

        # Save Button
        self.save_btn = ctk.CTkButton(self.main_frame, text="Save", font=ctk.CTkFont("Segoe UI", 15,"bold"),
                                    fg_color="#1a1a40", hover_color="#21649A", text_color="white",
                                    corner_radius=10, cursor="hand2", width=110, height=40,command=self.add_data)
        self.save_btn.place(x=120, y=400)

        # Update Button
        self.update_btn = ctk.CTkButton(self.main_frame, text="Update", font=ctk.CTkFont("Segoe UI", 15,"bold"),
                                        fg_color="#1a1a40", hover_color="#21649A", text_color="white",
                                        corner_radius=10, cursor="hand2", width=110, height=40, state="disabled",command=self.update)
        self.update_btn.place(x=250, y=400)

        # Delete Button
        self.delete_btn = ctk.CTkButton(self.main_frame, text="Delete", font=ctk.CTkFont("Segoe UI", 15,"bold"),
                                        fg_color="#1a1a40", hover_color="#21649A", text_color="white",
                                        corner_radius=10, cursor="hand2", width=110, height=40, state="disabled",command=self.delete_data)
        self.delete_btn.place(x=370, y=400)

        # Clear Button
        self.clear_btn = ctk.CTkButton(self.main_frame, text="Clear", font=ctk.CTkFont("Segoe UI", 15,"bold"),
                                    fg_color="#1a1a40", hover_color="#21649A", text_color="white",
                                    corner_radius=10, cursor="hand2", width=110, height=40,command=self.clear_data)
        self.clear_btn.place(x=490, y=400)


        # search bar---------------------------------------------------------
        course_name_search = Label(self.main_frame,text="Search Course",font=("Helvetica", 13 ),bg="white").place(x=700,y=110)

        self.var_search = StringVar()
        course_search_bar = ctk.CTkEntry(self.main_frame, textvariable=self.var_search, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=180, height=35).place(x=840, y=105)

        # Search Button
        self.search_btn = ctk.CTkButton(self.main_frame, text="Search", font=ctk.CTkFont("Segoe UI", 15,"bold"),
                                        fg_color="#1a1a40", hover_color="#21649A", text_color="white",
                                        corner_radius=10, cursor="hand2", width=110, height=35,command=self.search_course)
        self.search_btn.place(x=1040, y=105)


        # listbox to show all of the details-------------------------------------------------
        self.course_frame = Frame(self.main_frame,bd=1,relief="flat")
        self.course_frame.place(x=700,y=170,width=470,height=340)
        # scrollBars for the frame
        scrollX = Scrollbar(self.course_frame,orient=HORIZONTAL)
        scrollY = Scrollbar(self.course_frame,orient=VERTICAL)

        # creating table
        self.course_table = ttk.Treeview(self.course_frame,columns=("c_id","name","duration","charges","description"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)

        # pack the scroll bars
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)
        # configure the scrollbars
        scrollX.config(command=self.course_table.xview)
        scrollY.config(command=self.course_table.yview)

        self.course_table.heading("c_id",text="Course ID")
        self.course_table.heading("name",text="Name")
        self.course_table.heading("duration",text="Duration")
        self.course_table.heading("charges",text="Charges")
        self.course_table.heading("description",text="Description")
        # to hide the default column
        self.course_table['show'] = "headings"
        # defining widht of the columns
        self.course_table.column("c_id",width=100,anchor='center')
        self.course_table.column("name",width=100,anchor='center')
        self.course_table.column("duration",width=100,anchor='center')
        self.course_table.column("charges",width=100,anchor='center')
        self.course_table.column("description",width=200,anchor='center')

        self.course_table.pack(fill=BOTH,expand=1) 
        self.show_data() # show the data soon as window appears

        # update button functioning
        self.course_table.bind("<ButtonRelease-1>",self.get_data)

    # -------------------------------functionss---------------------------------------------

    # function for save button
    def add_data(self):
        con = sqlite3.connect(database = "RMS.db")
        cur = con.cursor()

        try:
            if self.course_var.get() == "":
                messagebox.showerror("Error","Course Name is required!",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.course_var.get(),))
                row = cur.fetchone()
                if row != None: #this means entered coursee name is already in my db
                    messagebox.showerror("Error","Course Name already exists!",parent=self.root)
                    return

                if (
                    self.course_var.get().strip() == "" or
                    self.duration_var.get().strip() == "" or
                    self.charges_var.get().strip() == ""
                ):
                    messagebox.showerror(
                        "Missing Fields",
                        "Please fill all required (*) fields",
                        parent=self.root
                    )
                    return
                
                # means if not present then ill add this course to db
                cur.execute("insert into course (name,duration,charges,description) values(?,?,?,?)",(
                    self.course_var.get(),
                    self.duration_var.get(),
                    self.charges_var.get(),
                    self.description_txt.get("1.0",END)
                ))
                con.commit()
                
                messagebox.showinfo("Success","Course has been added Successfully!",parent=self.root)
                self.show_data() #show data when  new course added
                self.clear_data() #show data when  new course added

        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")
 

    # function for showing all of the data to the frame or table
    def show_data(self):
            con = sqlite3.connect(database = "RMS.db")
            cur = con.cursor()

            try:
                cur.execute("select * from course")
                rows = cur.fetchall()
                self.course_table.delete(*self.course_table.get_children())

                # inserting all the data froom the db to the frame on my window
                for row in rows:
                    self.course_table.insert('',END,values=row)
    
            except Exception as e:
                messagebox.showerror("Error",f"Error due to {str(e)}")
 

    # whenever any entry is clicked all the data should be available to the form for editing
    def get_data(self,event):
        self.course_name_txt.configure(state='readonly') #course name cannot be changed once created
        selected_row = self.course_table.focus()
        content = self.course_table.item(selected_row)

        row = content["values"] # now this row has the vlues of the selected row from our table

        self.course_var.set(row[1])
        self.duration_var.set(row[2])
        self.charges_var.set(row[3])
        # to insert the description
        self.description_txt.delete('1.0',END)
        self.description_txt.insert(END,row[4])
        self.update_btn.configure(state="normal")
        self.delete_btn.configure(state="normal")
        # self.update_btn.config(state="normal")
        # self.delete_btn.config(state="normal")
    
    
    # main function for update button
    def update(self):
        con = sqlite3.connect(database = "RMS.db")
        cur = con.cursor()

        try:
            if self.course_var.get() == "":
                messagebox.showerror("Error","Select the course first!",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.course_var.get(),))
                row = cur.fetchone()
                if row == None: #this means the course entered is not in my database
                    messagebox.showerror("Error","No such course exists to update!",parent=self.root)

                else: 
                    # Ask for confirmation before updating
                    confirm = messagebox.askyesno("Confirm Update", "Are you sure you want to update the Course details?", parent=self.root)
                    if not confirm:
                        return
                    
                    cur.execute("update course set duration=?,charges=?,description=? where name=?",(
                        self.duration_var.get(),
                        self.charges_var.get(),
                        self.description_txt.get("1.0",END),
                        self.course_var.get()
                    ))
                    con.commit()
                    
                    messagebox.showinfo("Success","Course has been updated Successfully!",parent=self.root)
                    self.show_data() #show data when  new course added

        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")


    # function for clear button
    def clear_data(self):
        self.show_data() #before clearing show the data
        self.course_var.set("")
        self.duration_var.set("")
        self.charges_var.set("")
        self.description_txt.delete('1.0',END)
        self.course_name_txt.configure(state=NORMAL) #so that user can type his course again
        # clear the search box as well
        self.var_search.set("")
        self.update_btn.configure(state="disabled")
        self.delete_btn.configure(state="disabled")



    # function for delete button
    def delete_data(self):
        con = sqlite3.connect(database = "RMS.db")
        cur = con.cursor()

        try:
            if self.course_var.get() == "":
                messagebox.showerror("Error","Select the course first!",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.course_var.get(),))
                row = cur.fetchone()

                if row == None:  #this means the course entered is not in my database
                    messagebox.showerror("Error","No such course exists to delete!",parent=self.root)
                else: 
                    op = messagebox.askyesno("Confirm","Do you really want to delete the course?",parent=self.root)
                    # if user says yes
                    if op == True:
                        cur.execute("delete from course where name=?",(self.course_var.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course has been deleted Successfullyl!",parent=self.root)
                        self.clear_data() #so that all values of the input boxes are cleared
                    # if user said no then do not do anything
                

        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")
 

    # function for the search button
    def search_course(self):
        con = sqlite3.connect(database = "RMS.db")
        cur = con.cursor()

        # if we search any course in the search bar then , it will look into the database and will return the course which is like that course means whatever name is similar, now it will first delete all the entries from the table , and insert only those rows which have similar name as searched course name
        try:
            cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows = cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())

            # if no course matches
            if not rows:
                messagebox.showinfo("No Result", "No such cours exists!",parent=self.root)
                return  # stop further execution

            # inserting all the data froom the db to the frame on my window
            for row in rows:
                self.course_table.insert('',END,values=row)
 
        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")


    # on entering the course name,all the fields will be filled
    def prefill_data_from_course(self, event):
        course_name = self.course_var.get().strip()
        if course_name == "":
            return

        con = sqlite3.connect("RMS.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM course WHERE name=?", (course_name,))
        row = cur.fetchone()

        if row:
            self.duration_var.set(row[2])
            self.charges_var.set(row[3])
            self.description_txt.delete("1.0", END)
            self.description_txt.insert("1.0", row[4])

            self.original_course_data = row[1:]  # store original for update comparison if needed
            self.update_btn.configure(state="normal")
            self.delete_btn.configure(state="normal")



if __name__ == "__main__":
    root = Tk()
    obj = CourseManagement(root)
    root.mainloop() #so that our window stays on looping
