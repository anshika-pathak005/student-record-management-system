from tkinter import *
from PIL import Image,ImageTk
import customtkinter as ctk
from tkinter import ttk,messagebox
import sqlite3

class ViewResultManagement:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x530+80+150") #so that it start for top-right and get the whole widht
        self.root.title("Student Result Management System")
        self.root.config(bg='white')
        self.root.focus_force()
        # the title
        # our title
        title = Label(self.root, text="Student Result Overview",font=("Helvetica", 20, "bold"), bg="#1a1a40", fg="white")
        title.place(relx=0.5, y=15, anchor="n", width=1300, height=50)

        # variables
        self.search_student_roll_var = StringVar()
        self.result_id = ""

        # input fields-----------------------------------------------------------------------
        search_student_roll = Label(self.root,text="Enter Student Roll No.",font=("Helvetica", 13 ),bg="white").place(x=250,y=110)
        self.search_student_roll_text = ctk.CTkEntry(self.root, textvariable=self.search_student_roll_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="grey", border_width=1, text_color="black", width=250, height=35)
        self.search_student_roll_text.place(x=450, y=105)

        search_btn = Button(self.root,text="Search",font=("Helvetica", 12),bg='#0a2645',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.search_student_roll).place(x=730,y=105,width=110,height=35)
        cleat_btn = Button(self.root,text="Clear",font=("Helvetica", 12),bg='#0a2645',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.clear_data).place(x=860,y=105,width=110,height=35)


        # next making the lables to show the result details

        rollNo_lbl = Label(self.root,text="Roll No.",font=("Helvetica", 13 ),bg="white").place(x=150,y=230,width=150,height=50)
        name_lbl = Label(self.root,text="Name",font=("Helvetica", 13 ),bg="white").place(x=300,y=230,width=150,height=50)
        course_lbl = Label(self.root,text="Course",font=("Helvetica", 13 ),bg="white").place(x=450,y=230,width=150,height=50)
        marks_obt_lbl = Label(self.root,text="Marks Obtained",font=("Helvetica", 13 ),bg="white").place(x=600,y=230,width=150,height=50)
        total_marks_lbl = Label(self.root,text="Total Marks",font=("Helvetica", 13 ),bg="white").place(x=750,y=230,width=150,height=50)
        percentage_lbl = Label(self.root,text="Percentage",font=("Helvetica", 13 ),bg="white").place(x=900,y=230,width=150,height=50)


        self.rollNo = Label(self.root,font=("Helvetica", 13 ),bg="white", bd=1,relief=GROOVE)
        self.rollNo.place(x=150,y=280,width=150,height=50)
        self.name = Label(self.root,font=("Helvetica", 13 ),bg="white", bd=1,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)
        self.course = Label(self.root,font=("Helvetica", 13 ),bg="white", bd=1,relief=GROOVE)
        self.course.place(x=450,y=280,width=150,height=50)
        self.marks_obt = Label(self.root,font=("Helvetica", 13 ),bg="white", bd=1,relief=GROOVE)
        self.marks_obt.place(x=600,y=280,width=150,height=50)
        self.total_marks = Label(self.root,font=("Helvetica", 13 ),bg="white", bd=1,relief=GROOVE)
        self.total_marks.place(x=750,y=280,width=150,height=50)
        self.percentage = Label(self.root,font=("Helvetica", 13 ),bg="white", bd=1,relief=GROOVE)
        self.percentage.place(x=900,y=280,width=150,height=50)
      
        # delete button
        self.delete_btn = Button(self.root,text="Delete",font=("Helvetica", 12),bg='#0a2645',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.delete_data,state="disabled")
        self.delete_btn.place(x=535,y=430,width=110,height=35)


        # funtions ==================================================================

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