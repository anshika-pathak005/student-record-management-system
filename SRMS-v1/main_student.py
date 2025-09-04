from tkinter import *
from PIL import Image,ImageTk
import customtkinter as ctk
from tkinter import ttk,messagebox
import sqlite3
import re

class StudentManagement:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x530+80+150") #so that it start for top-right and get the whole widht
        self.root.title("Student Result Management System")
        self.root.config(bg='white')
        self.root.focus_force()

        # validation for marks fields
        vcmd = (self.root.register(self.validate_numeric), '%P')

        # the title
        title = Label(self.root, text="Student Management Panel",font=("Helvetica", 20, "bold"), bg="#1a1a40", fg="white")
        title.place(relx=0.5, y=15, anchor="n", width=1300, height=50)

        # variable to fetch the values
        self.roll_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.dob_var = StringVar()
        self.contact_var = StringVar()
        self.adm_date_var = StringVar()
        self.course_var = StringVar()
        self.state_var = StringVar()
        self.city_var = StringVar()
        self.pin_var = StringVar()

# =======================COLUMN-1==========================================================

        # input fields
        roll_num = Label(self.root,text="Roll No.",font=("Helvetica", 13 ),bg="white").place(x=20,y=110)
        name_lbl = Label(self.root,text="Name",font=("Helvetica", 13),bg="white").place(x=20,y=150)
        email_lbl = Label(self.root,text="Email",font=("Helvetica", 13),bg="white").place(x=20,y=190)
        gender_lbl = Label(self.root,text="Gender",font=("Helvetica", 13),bg="white").place(x=20,y=230)

        state_lbl = Label(self.root,text="State",font=("Helvetica", 13),bg="white").place(x=20,y=270)
        state_text = ctk.CTkEntry(self.root, textvariable=self.state_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=150, height=35).place(x=140, y=270)

        city_lbl = Label(self.root,text="City",font=("Helvetica", 13),bg="white").place(x=300,y=270)
        city_text = ctk.CTkEntry(self.root, textvariable=self.city_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=130, height=35).place(x=350, y=270)

        pin_lbl = Label(self.root,text="Pin",font=("Helvetica", 13),bg="white").place(x=495,y=270)
        pin_text = ctk.CTkEntry(self.root, textvariable=self.pin_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=130, height=35,validate="key",validatecommand=vcmd).place(x=540, y=270)


        address_lbl = Label(self.root,text="Address",font=("Helvetica", 13),bg="white").place(x=20,y=310)
        
        # user input here--------------------------------------------------------

        self.roll_no_text = ctk.CTkEntry(self.root, textvariable=self.roll_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="gray", border_width=1, text_color="black", width=200, height=35,validate="key",validatecommand=vcmd)
        self.roll_no_text.place(x=140, y=110)
        # binding of prefill_data function
        self.roll_no_text.bind("<Return>", self.prefill_data_from_roll)


        name_txt = ctk.CTkEntry(self.root,textvariable=self.name_var,font=("Helvetica", 15),corner_radius=5, fg_color="white", border_color="gray", border_width=1,text_color="black", width=200, height=35).place(x=140,y=150)


        email_txt = ctk.CTkEntry(self.root, textvariable=self.email_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=200, height=35).place(x=140, y=190)


        self.gender_txt = ctk.CTkComboBox(self.root, values=["Male", "Female", "Other"], variable=self.gender_var, font=("Helvetica", 15),state='readonly', corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=200, height=35, dropdown_font=("Helvetica", 15), dropdown_fg_color="white", dropdown_text_color="black", button_color="#a6a5a5", button_hover_color="#e0e0e0")
        self.gender_txt.place(x=140, y=230)


        self.address_txt = ctk.CTkTextbox(self.root, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="gray", border_width=1, text_color="black", width=535, height=100)
        self.address_txt.place(x=140, y=310)

# =======================COLUMN-2==========================================================

        # input fields
        dob_lbl = Label(self.root,text="D.O.B.",font=("Helvetica", 13 ),bg="white").place(x=380,y=110)
        contact_lbl = Label(self.root,text="Contact",font=("Helvetica", 13),bg="white").place(x=380,y=150)
        adm_date_lbl = Label(self.root,text="Adm. Date",font=("Helvetica", 13),bg="white").place(x=380,y=190)
        course_lbl = Label(self.root,text="Course",font=("Helvetica", 13),bg="white").place(x=380,y=230)


        # user input here--------------------------------------------------------

        self.dob_text = ctk.CTkEntry(self.root, textvariable=self.dob_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="gray", border_width=1, text_color="black", width=200, height=35)
        self.dob_text.place(x=470, y=110)


        contact_txt = ctk.CTkEntry(self.root,textvariable=self.contact_var,font=("Helvetica", 15),corner_radius=5, fg_color="white", border_color="gray", border_width=1,text_color="black", width=200, height=35,validate="key",validatecommand=vcmd).place(x=470,y=150)


        adm_date_text = ctk.CTkEntry(self.root, textvariable=self.adm_date_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=200, height=35).place(x=470, y=190)


        # defining a list to store all the cources that we have
        self.course_list = []
        # will do function call to fetch the cources that we have
        self.fetch_course()

        self.course_txt = ctk.CTkComboBox(self.root, values=self.course_list, variable=self.course_var, font=("Helvetica", 15),state='readonly', corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=200, height=35, dropdown_font=("Helvetica", 15), dropdown_fg_color="white", dropdown_text_color="black", button_color="#a6a5a5", button_hover_color="#e0e0e0")
        self.course_txt.place(x=470, y=230)


# ================================functional buttons========================================

        # buttons

        self.save_btn = Button(self.root,text="Save",font=("Helvetica", 12),bg='#0a2645',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.add)
        self.save_btn.place(x=130,y=450,width=110,height=40)

        self.update_btn = Button(self.root,text="Update",font=("Helvetica", 12),bg='#0a2645',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.update,state='disabled')
        self.update_btn.place(x=250,y=450,width=110,height=40)

        self.delete_btn = Button(self.root,text="Delete",font=("Helvetica", 12),bg='#0a2645',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.delete_data,state="disabled")
        self.delete_btn.place(x=370,y=450,width=110,height=40)

        self.clear_btn = Button(self.root,text="Clear",font=("Helvetica", 12),bg='#0a2645',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.clear_data)
        self.clear_btn.place(x=490,y=450,width=110,height=40)

# =========================================================================================
# ===========================Right side of the window======================================
        # search bar
        roll_no_search = Label(self.root,text="Search Roll No.",font=("Helvetica", 13 ),bg="white").place(x=700,y=110)

        self.var_search_rollNo = StringVar()
        rollNo_search_bar = ctk.CTkEntry(self.root, textvariable=self.var_search_rollNo, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=180, height=35,validate="key",validatecommand=vcmd).place(x=840, y=105)

        search_btn = Button(self.root,text="Search",font=("Helvetica", 12),bg='#0a2645',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.search_student_roll).place(x=1040,y=105,width=110,height=35)


        # listbox to show all of the details-----------------------------------------------------
        self.course_frame = Frame(self.root,bd=1,relief="flat")
        self.course_frame.place(x=700,y=170,width=470,height=340)
        # scrollBars for the frame
        scrollX = Scrollbar(self.course_frame,orient=HORIZONTAL)
        scrollY = Scrollbar(self.course_frame,orient=VERTICAL)

        # creating table
        self.course_table = ttk.Treeview(self.course_frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)

        # pack the scroll bars
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)
        # configure the scrollbars
        scrollX.config(command=self.course_table.xview)
        scrollY.config(command=self.course_table.yview)

        # setting the headings
        self.course_table.heading("roll", text="Roll No")
        self.course_table.heading("name", text="Name")
        self.course_table.heading("email", text="Email")
        self.course_table.heading("gender", text="Gender")
        self.course_table.heading("dob", text="DOB")
        self.course_table.heading("contact", text="Contact")
        self.course_table.heading("admission", text="Admission Date")
        self.course_table.heading("course", text="Course")
        self.course_table.heading("state", text="State")
        self.course_table.heading("city", text="City")
        self.course_table.heading("pin", text="PIN Code")
        self.course_table.heading("address", text="Address")

        # to hide the default column
        self.course_table['show'] = "headings"

        # defining width and alignment of the columns
        self.course_table.column("roll", width=80, anchor='center')
        self.course_table.column("name", width=120, anchor='center')
        self.course_table.column("email", width=150, anchor='center')
        self.course_table.column("gender", width=80, anchor='center')
        self.course_table.column("dob", width=100, anchor='center')
        self.course_table.column("contact", width=100, anchor='center')
        self.course_table.column("admission", width=100, anchor='center')
        self.course_table.column("course", width=100, anchor='center')
        self.course_table.column("state", width=100, anchor='center')
        self.course_table.column("city", width=100, anchor='center')
        self.course_table.column("pin", width=80, anchor='center')
        self.course_table.column("address", width=200, anchor='center')

        self.course_table.pack(fill=BOTH,expand=1) 
        self.show_data() # show the data soon as window appears

        # update button functioning
        self.course_table.bind("<ButtonRelease-1>",self.get_data)

    # -------------------------------functionss---------------------------------------------

    # validation
    def validate_numeric(self, value):
        return value.isdigit() or value == ""

    # function for save button
    def add(self):
        con = sqlite3.connect(database = "RMS.db")
        cur = con.cursor()

        try:
            cur.execute("select * from student where roll=?",(self.roll_var.get(),))
            row = cur.fetchone()
            if row != None: #this means entered roll no is already in my db
                messagebox.showerror("Error","Student with this Roll Number is already enrolled. Please use a unique Roll Number!",parent=self.root)
                return
            
            if (
                self.roll_var.get().strip() == "" or
                self.name_var.get().strip() == "" or
                self.email_var.get().strip() == "" or
                self.contact_var.get().strip() == "" or
                self.course_var.get().strip() == ""
            ):
                messagebox.showerror(
                    "Missing Fields",
                    "Please fill all required fields before submitting:\n\n"
                    "• Roll no.\n"
                    "• Name\n"
                    "• Email\n"
                    "• Contact Number\n"
                    "• Course\n",
                    parent=self.root
                )
                return

            # email format check if it is okay or not
            email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            if not re.match(email_pattern, self.email_var.get().strip()):
                messagebox.showerror("Invalid Email", "Please enter a valid email address.", parent=self.root)
                return

            # contact number check , only 10 digits ar allowed
            if not self.contact_var.get().strip().isdigit() or len(self.contact_var.get().strip()) != 10:
                messagebox.showerror("Invalid Contact", "Contact number must be a 10-digit number.", parent=self.root)
                return
            
            
            # after everythin is good then add student
            cur.execute("insert into student (roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                self.roll_var.get(),
                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.dob_var.get(),
                self.contact_var.get(),
                self.adm_date_var.get(),
                self.course_var.get(),
                self.state_var.get(),
                self.city_var.get(),
                self.pin_var.get(),
                self.address_txt.get("1.0",END)
            ))
            con.commit()
            
            messagebox.showinfo("Success","Student has been added Successfully!",parent=self.root)
            self.show_data() #show data when  new course added
            self.clear_data() #clear data after addition

        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")
 

    # function for showing all of the data to the frame or table
    def show_data(self):
        con = sqlite3.connect(database = "RMS.db")
        cur = con.cursor()

        try:
            cur.execute("select * from student")
            rows = cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())

            # inserting all the data froom the db to the frame on my window
            for row in rows:
                self.course_table.insert('',END,values=row)
 
        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")
 

    # whenever any entry is clicked all the data should be available to the form for editing
    def get_data(self,event):
        self.roll_no_text.configure(state='readonly') #course name cannot be changed once created
        selected_row = self.course_table.focus()
        content = self.course_table.item(selected_row)

        row = content["values"] # now this row has the vlues of the selected row from our table

        self.roll_var.set(row[0]),
        self.name_var.set(row[1]),
        self.email_var.set(row[2]),
        self.gender_var.set(row[3]),
        self.dob_var.set(row[4]),
        self.contact_var.set(row[5]),
        self.adm_date_var.set(row[6]),
        self.course_var.set(row[7]),
        self.state_var.set(row[8]),
        self.city_var.set(row[9]),
        self.pin_var.set(row[10]),
        self.address_txt.delete("1.0",END)
        self.address_txt.insert(END,row[11])
        self.update_btn.config(state="normal")
        self.delete_btn.config(state="normal")


    # main function for update button
    def update(self):

        con = sqlite3.connect(database = "RMS.db")
        cur = con.cursor()

        try:
            if self.roll_var.get() == "":
                messagebox.showerror("Error","Enter/Select the Student's Roll No. first!",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.roll_var.get(),))
                row = cur.fetchone()
                if row == None: #this means the roll no entered is not in my database
                    messagebox.showerror("Error","No such Student with this Roll no. exists to update!",parent=self.root)
                else: 
                    # Ask for confirmation before updating
                    confirm = messagebox.askyesno("Confirm Update", "Are you sure you want to update this student's details?", parent=self.root)
                    if not confirm:
                        return
    
                    # if fields are filled then update
                    cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where roll=?",(
                        self.name_var.get(),
                        self.email_var.get(),
                        self.gender_var.get(),
                        self.dob_var.get(),
                        self.contact_var.get(),
                        self.adm_date_var.get(),
                        self.course_var.get(),
                        self.state_var.get(),
                        self.city_var.get(),
                        self.pin_var.get(),
                        self.address_txt.get("1.0",END),
                        self.roll_var.get()

                    ))
                    con.commit()
                    
                    messagebox.showinfo("Success","Student Details has been updated Successfully!",parent=self.root)
                    self.show_data() #show data when  new course added
                    self.clear_data()

        except Exception as e:
            messagebox.showerror("Error",f"Error due to  {str(e)}")
 

    # function for clear button
    def clear_data(self):
        self.show_data() #before clearing show the data
        self.roll_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.dob_var.set("")
        self.contact_var.set("")
        self.adm_date_var.set("")
        self.course_var.set("")
        self.state_var.set("")
        self.city_var.set("")
        self.pin_var.set("")
        self.address_txt.delete("1.0",END)
        self.roll_no_text.configure(state=NORMAL)#so that user can type his course again
        self.var_search_rollNo.set("")
        self.update_btn.config(state="disabled")
        self.delete_btn.config(state="disabled")



    # function for delete button
    def delete_data(self):
        con = sqlite3.connect(database = "RMS.db")
        cur = con.cursor()

        try:
            if self.roll_var.get() == "":
                messagebox.showerror("Error","Enter/Select the Student's Roll No. first!",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.roll_var.get(),))
                row = cur.fetchone()
                if row == None:  #this means the course entered is not in my database
                    messagebox.showerror("Error","No such Roll no. exists to delete!",parent=self.root)
                else: 
                    op = messagebox.askyesno(" Confirm","Are you sure you want to delete this student?",parent=self.root)
                    # if user says yes
                    if op == True:
                        cur.execute("delete from student where roll=?",(self.roll_var.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student data has been deleted Successfully!",parent=self.root)
                        self.clear_data() #so that all values of the input boxes are cleared
                        self.delete_btn.config(state="disabled") #disable the delete button again
                    # if user said no then do not do anything
                

        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")


    # function for the search button
    def search_student_roll(self):
        con = sqlite3.connect(database = "RMS.db")
        cur = con.cursor()
        try:
            cur.execute(f"select * from student where roll=?",(self.var_search_rollNo.get(),))
            rows = cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())

            # if no student found
            if not rows:
                messagebox.showinfo("No Result", "No student found with this Roll Number!",parent=self.root)
                return

            # otherwises inserting all the data froom the db to the frame on my window
            for row in rows:
                self.course_table.insert('',END,values=row)
 
        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")
 

    # function to fetch the cources
    def fetch_course(self):
        con = sqlite3.connect(database = "RMS.db")
        cur = con.cursor()

        try:
            cur.execute("select name from course")
            rows = cur.fetchall()

            if len(rows) > 0:
                for row in rows:
                    self.course_list.append(row[0])

        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")
 

    # as soon as user enteres hi roll no and presses enter fill all of his data
    def prefill_data_from_roll(self,event):
       
        roll = self.roll_var.get()
        if roll == "":
            return

        con = sqlite3.connect("RMS.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM student WHERE roll=?", (self.roll_var.get(),))
        row = cur.fetchone()

        if row:
            self.name_var.set(row[1])
            self.email_var.set(row[2])
            self.gender_var.set(row[3])
            self.dob_var.set(row[4])
            self.contact_var.set(row[5])
            self.adm_date_var.set(row[6])
            self.course_var.set(row[7])
            self.state_var.set(row[8])
            self.city_var.set(row[9])
            self.pin_var.set(row[10])
            self.address_txt.delete("1.0", END)
            self.address_txt.insert("1.0", row[11])

            self.original_data = row[1:]
            self.update_btn.config(state="normal")
            self.delete_btn.config(state="normal")

if __name__ == "__main__":
    root = Tk()
    obj = StudentManagement(root)
    root.mainloop() #so that our window stays on looping