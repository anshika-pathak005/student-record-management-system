from tkinter import *
from PIL import Image,ImageTk
import customtkinter as ctk
from tkinter import ttk,messagebox
import sqlite3

class Register:
    def __init__(self, root):
        self.root = root

        window_width = 480
        window_height = 450

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.root.resizable(False, False)

        self.root.title("Register Page")
        self.root.config(bg='white')
        self.root.focus_force()


        title = Label(self.root, text="Register",font=("Helvetica", 20, "bold"), bg="#1a1a40", fg="white")
        title.place(relx=0.5, y=15, anchor="n", width=1300, height=50)

        # variable
        self.username_var = StringVar()
        self.new_pass_var = StringVar()
        self.confirm_pass_var = StringVar()

        # user entry
        username = Label(self.root,text="New Username",font=("Helvetica", 13 ),bg="white").place(x=30,y=110)
        new_pass = Label(self.root,text="New Password",font=("Helvetica", 13),bg="white").place(x=30,y=160)
        confirm_pass = Label(self.root,text="Confirm Password",font=("Helvetica", 13),bg="white").place(x=30,y=210)

        self.username_txt = ctk.CTkEntry(self.root, textvariable=self.username_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="gray", border_width=1, text_color="black", width=230, height=35)
        self.username_txt.place(x=200, y=105)
        self.new_pass_txt = ctk.CTkEntry(self.root, textvariable=self.new_pass_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="gray", border_width=1, text_color="black", width=230, height=35,show="●")
        self.new_pass_txt.place(x=200, y=155)
        self.confirm_pass_txt = ctk.CTkEntry(self.root, textvariable=self.confirm_pass_var, font=("Helvetica", 15), corner_radius=5, fg_color="white", border_color="gray", border_width=1, text_color="black", width=230, height=35,show="●")
        self.confirm_pass_txt.place(x=200, y=205)

        
        self.register_btn = Button(self.root,text="Register",font=("Helvetica", 12),bg='#0a2645',fg="white",bd='0',activebackground='#2b6cb0',activeforeground="white",cursor='hand2',command=self.register_user)
        self.register_btn.place(x=180,y=320,width=110,height=40)

        # function

    def register_user(self):

        username = self.username_var.get().strip()
        password = self.new_pass_var.get().strip()
        confirm = self.confirm_pass_var.get().strip()

        if username == "" or password == "" or confirm == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
            return

        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match!", parent=self.root)
            return

        try:
            con = sqlite3.connect("RMS.db")
            cur = con.cursor()

            # Check if username already exists
            cur.execute("SELECT * FROM users WHERE username = ?", (username,))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Username already exists!", parent=self.root)
            else:
                cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                con.commit()
                messagebox.showinfo("Success", "Account created successfully!", parent=self.root)
                self.root.destroy()  # Close register window
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop() #so that our window stays on looping