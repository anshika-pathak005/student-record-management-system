from tkinter import *
from PIL import Image,ImageTk
import customtkinter as ctk
from tkinter import ttk,messagebox
import sqlite3
from register import Register
from main_dashboard import ResultManagementSystem

class UserLogin:
    def __init__(self, root):
        self.root = root

        # Full screen size
        window_width = self.root.winfo_screenwidth()
        window_height = self.root.winfo_screenheight()

        self.root.geometry(f"{window_width}x{window_height}+0+0")
        self.root.resizable(False, False)

        self.root.title("Login")
        self.root.config(bg='white')
        self.root.focus_force()

        title = Label(
            self.root,
            text="Welcome to Our Student Result Management System",
            font=("Helvetica", 20, "bold"),
            bg="#1a1a40",
            fg="white"
        )
        title.place(relx=0.5, y=15, anchor="n", width=1300, height=50)


        # variable
        self.username_var = StringVar()
        self.new_pass_var = StringVar()
        self.confirm_pass_var = StringVar()

        frame_width = 380
        frame_height = 420

        frame_x = (self.root.winfo_screenwidth() // 2) - (frame_width // 2)
        frame_y = (self.root.winfo_screenheight() // 2) - (frame_height // 2)

        self.center_frame = ctk.CTkFrame(
            self.root,
            width=frame_width,
            height=frame_height,
            corner_radius=5,
            fg_color="white",
            border_color="gray",
            border_width=1
        )
        self.center_frame.place(x=frame_x, y=frame_y)

        title = Label(self.center_frame, text="Login", font=("Helvetica", 20, "bold"), bg="#1a1a40", fg="white")
        title.place(relx=0.5, y=0, anchor="n", width=500, height=50)

        # variable
        self.username_var = StringVar()
        self.new_pass_var = StringVar()
        

        # Labels inside the frame
        username_label = Label(self.center_frame, text="New Username", font=("Helvetica", 13), bg="white")
        username_label.place(x=30, y=100)

        pass_label = Label(self.center_frame, text="New Password", font=("Helvetica", 13), bg="white")
        pass_label.place(x=30, y=170)


        # Entry boxes inside the frame
        self.username_txt = ctk.CTkEntry(self.center_frame, textvariable=self.username_var, font=("Helvetica", 15),corner_radius=5, fg_color="white", border_color="gray", border_width=1,text_color="black", width=180, height=35)
        self.username_txt.place(x=150, y=95)

        self.new_pass_txt = ctk.CTkEntry(self.center_frame, textvariable=self.new_pass_var, font=("Helvetica", 15),corner_radius=5, fg_color="white", border_color="gray", border_width=1,text_color="black", width=180, height=35,show="●")
        self.new_pass_txt.place(x=150, y=165)

        # Login button inside the frame
        self.login_btn = Button(self.center_frame, text="Login", font=("Helvetica", 12),bg='#0a2645', fg="white", bd=0,activebackground='#2b6cb0', activeforeground="white", cursor='hand2',command=self.login_user)
        self.login_btn.place(x=140, y=270, width=110, height=40)


        # Add this at the bottom of your center_frame
        bottom_frame = Frame(self.center_frame, bg="white")
        bottom_frame.place(relx=0.5, rely=1.0, anchor="s", y=-25)

        label1 = Label(bottom_frame, text="Don't have an account? ", font=("Helvetica", 10), bg="white")
        label1.pack(side=LEFT)

        register_link = Label(bottom_frame, text="Register here", font=("Helvetica", 10, "underline"), fg="blue", bg="white", cursor="hand2")
        register_link.pack(side=LEFT)
        register_link.bind("<Button-1>", lambda e: self.open_register())



    # function
    def open_register(self):
        # Check if window exists and is still open
        if hasattr(self, 'register_win') and self.register_win.winfo_exists():
            self.register_win.deiconify()  # Restore if minimized
            self.register_win.lift()       # Bring to front
            self.register_win.focus_force()  # Take focus
            return

        # Otherwise, create new window
        self.register_win = Toplevel(self.root)
        self.new_object = Register(self.register_win)


    def login_user(self):
        username = self.username_var.get().strip()
        password = self.new_pass_var.get().strip()

        if username == "" or password == "":
            messagebox.showerror("Error", "Username and Password are required!", parent=self.root)
            return

        try:
            con = sqlite3.connect("RMS.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid username or password!", parent=self.root)
            else:
                self.username_var.set("")
                self.new_pass_var.set("")
                # messagebox.showinfo("Success", f"Welcome {username}!", parent=self.root)
                self.root.withdraw()  # Hide login window

                if hasattr(self, 'dashboard') and self.dashboard.winfo_exists():
                    self.dashboard.deiconify()  # Restore if minimized
                    self.dashboard.lift()       # Bring to front
                    self.dashboard.focus_force()  # Take focus
                    return

                # Otherwise, create new window
                self.dashboard = Toplevel(self.root)
                self.new_object = ResultManagementSystem(self.dashboard,self.root)


        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = UserLogin(root)
    root.mainloop() #so that our window stays on looping