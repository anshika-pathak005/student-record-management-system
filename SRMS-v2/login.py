import sys, os
import sqlite3
from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from tkinter import ttk,messagebox
import customtkinter as ctk
from PIL import Image
import customtkinter as ctk
from PIL import Image, ImageDraw
import customtkinter as ctk
from register import Register
from dashboard import StudentManagementSystem
from customtkinter import CTkImage

# this funtion is used for rounding the image
def make_rounded_image_preserve_aspect(path, container_size, radius=10, bg_color="white"):
    container_width, container_height = container_size

    # Load original image
    img = Image.open(path).convert("RGBA")

    # Calculate resize while keeping 3:4 ratio
    img_ratio = 4 / 5
    if container_width / container_height > img_ratio:
        new_height = container_height
        new_width = int(new_height * img_ratio)
    else:
        new_width = container_width
        new_height = int(new_width / img_ratio)

    # Resize image maintaining aspect ratio
    img = img.resize((new_width, new_height), Image.LANCZOS)

    # Create mask
    mask = Image.new("L", (new_width, new_height), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, new_width, new_height), radius=radius, fill=255)

    img.putalpha(mask)

    # Create background image (same size as container)
    bg = Image.new("RGB", (container_width, container_height), bg_color)

    # Calculate position to center image
    x_offset = (container_width - new_width) // 2
    y_offset = (container_height - new_height) // 2

    bg.paste(img, (x_offset, y_offset), img)

    return ImageTk.PhotoImage(bg)

def resource_path(relative_path):
    try:
        # When using PyInstaller
        base_path = sys._MEIPASS
    except Exception:
        # When running in IDE or as .py
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class LoginUser:
    def __init__(self,root,login_win):
        self.root = root
        self.login_win = login_win

        # Set full screen size
        self.root.geometry("1366x750+0+0")

        self.root.title("Login")
        self.root.config(bg='#A8D8FE')

        image = Image.open(resource_path("images/login dash.png"))
        resized_image = image.resize((100, 70))
        self.logo = CTkImage(light_image=resized_image, size=(100, 70))




        # title
        title = ctk.CTkLabel(root,
                            text=" Welcome to Our Student Record Management System",
                            font=ctk.CTkFont(family="Segoe UI", size=25,weight="bold"),
                            text_color="white",
                            fg_color="#1a1a40",
                            corner_radius=15,
                            anchor="n",
                            padx=10,
                            width=1300,
                            compound=LEFT,
                            image= self.logo,
                            height=70)
        title.place(x=20, y=15)


        # Frame dimensions
        frame_width = 800
        frame_height = 480

        # Calculate centered x, y
        x_pos = (1366 - frame_width) // 2
        y_pos = (850- frame_height) // 2

        # Main centered frame
        self.center_frame = Frame(self.root, width=frame_width, height=frame_height, bg="white")
        self.center_frame.place(x=x_pos, y=y_pos)

        # Left frame (half of 900 = 450)
        self.left_frame = Frame(self.center_frame, width=400, height=480, bg="white")
        self.left_frame.place(x=0, y=0)

        # Right frame
        self.right_frame = Frame(self.center_frame, width=400, height=480, bg="white")
        self.right_frame.place(x=400, y=0)


# fo the left frame -> image

        self.left_image = make_rounded_image_preserve_aspect(
            resource_path("images/main-login.jpg"),
            container_size=(410, 420),   # Label or frame space
            radius=15,
            bg_color="white"
        )

        self.left_img_label = Label(self.left_frame, image=self.left_image, bg="#A8D8FE", bd=0)
        self.left_img_label.place(x=-10, y=30, width=410, height=420)

# for the right part -> data

        # variable
        self.username_var = StringVar()
        self.new_pass_var = StringVar()

        title = Label(self.right_frame, text=" Login ", font=("Segoe UI", 30,"bold","underline"), bg="white", fg="#1a1a40")
        title.place(relx=0.4, y=20, anchor="n", width=500, height=50)


        # Labels inside the frame
        username_label = Label(self.right_frame, text="Username", font=("Segoe UI", 13,"bold"), bg="white")
        username_label.place(x=30, y=130)

        pass_label = Label(self.right_frame, text="Password", font=("Segoe UI", 13,"bold"), bg="white")
        pass_label.place(x=30, y=190)


        # Entry boxes inside the frame
        self.username_txt = ctk.CTkEntry(self.right_frame, textvariable=self.username_var, font=("Helvetica", 15),corner_radius=5, fg_color="white", border_color="gray", border_width=1,text_color="black", width=200, height=35)
        self.username_txt.place(x=140, y=130)

        self.new_pass_txt = ctk.CTkEntry(self.right_frame, textvariable=self.new_pass_var, font=("Helvetica", 15),corner_radius=5, fg_color="white", border_color="gray", border_width=1,text_color="black", width=200, height=35,show="●")
        self.new_pass_txt.place(x=140, y=190)

        # Login button inside the frame

        self.login_btn = ctk.CTkButton(self.right_frame, text="Login", font=ctk.CTkFont("Segoe UI", 15,"bold"),
                                    fg_color="#1a1a40", hover_color="#21649A", text_color="white",
                                    corner_radius=10, cursor="hand2", width=110, height=40,command=self.login_user)
        self.login_btn.place(x=140, y=300)

        # for registration
        bottom_frame = Frame(self.right_frame, bg="white")
        bottom_frame.place(relx=0.5, rely=1.0, anchor="s", y=-30)

        label1 = Label(bottom_frame, text="Don't have an account? ", font=("Segoe UI", 12), bg="white")
        label1.pack(side=LEFT)

        register_link = Label(bottom_frame, text="Register here", font=("Segoe UI", 12, "underline"), fg="blue", bg="white", cursor="hand2")
        register_link.pack(side=LEFT)
        register_link.bind("<Button-1>", lambda e: self.open_register())

# =======================================Funtions=====================================================


    def open_register(self):
        # Check if window exists and is still open
        if hasattr(self, 'register_win') and self.register_win.winfo_exists():
            self.register_win.deiconify()  # Restore if minimized
            self.register_win.lift()       # Bring to front
            self.register_win.focus_force()  # Take focus
            return

        # Otherwise, create new window
        # self.root.withdraw()
        self.register_win = Toplevel(self.root)
        self.register_win.grab_set()
        self.new_object = Register(self.register_win,self)           

    # to login the user
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
                # getting the username
                full_name = row[1]
                first_name = full_name.strip().split()[0].capitalize()

                self.username_var.set("")
                self.new_pass_var.set("")
                # messagebox.showinfo("Success", f"Welcome {username}!", parent=self.root)

                if hasattr(self, 'dashboard') and self.dashboard.winfo_exists():
                    self.dashboard.deiconify()  # Restore if minimized
                    self.dashboard.lift()       # Bring to front
                    self.dashboard.focus_force()  # Take focus
                    return

                # Otherwise, open the dashboard
                self.dashboard = Toplevel(self.root)
                self.new_object = StudentManagementSystem(self.dashboard,self.root,first_name)

                self.root.withdraw()  # Hide login window



        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)

    

if __name__ == "__main__":
    root = Tk()
    obj = LoginUser(root,root)
    root.mainloop() #so that our window stays on looping
