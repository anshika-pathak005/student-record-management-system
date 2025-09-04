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
from customtkinter import CTkImage

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


class Register:
    def __init__(self,root,login_win):
        self.root = root
        self.login_win = login_win

        # Set full screen size
        self.root.geometry("1366x750+0+0")
        self.root.title("Login")
        self.root.config(bg='#A8D8FE')

# title logo
        image = Image.open(resource_path("images/login dash.png"))
        resized_image = image.resize((100, 70))
        self.logo = CTkImage(light_image=resized_image, size=(100, 70))




        # title
        title = ctk.CTkLabel(root,
                            text="  Welcome to Our Student Record Management System",
                            font=ctk.CTkFont(family="Segoe UI", size=25, weight="bold"),
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
        frame_width = 900
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
        self.right_frame = Frame(self.center_frame, width=450, height=480, bg="white")
        self.right_frame.place(x=400, y=0)


# fo the left frame -> image

        self.left_image = make_rounded_image_preserve_aspect(
            resource_path("images/reg.jpg"),
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
        self.confirm_pass_var = StringVar()

        title = Label(self.right_frame, text=" Register ", font=("Segoe UI", 25,"bold","underline"), bg="white", fg="#1a1a40")
        title.place(relx=0.4, y=20, anchor="n", width=500, height=50)


        # Labels inside the frame
        username_label = Label(self.right_frame, text="New Username", font=("Segoe UI", 13,"bold"), bg="white")
        username_label.place(x=30, y=130)

        pass_label = Label(self.right_frame, text="New Password", font=("Segoe UI", 13,"bold"), bg="white")
        pass_label.place(x=30, y=190)

        confirm_pass_label = Label(self.right_frame, text="Confirm Password", font=("Segoe UI", 13,"bold"), bg="white")
        confirm_pass_label.place(x=30, y=250)


        # Entry boxes inside the frame
        self.username_txt = ctk.CTkEntry(self.right_frame, textvariable=self.username_var, font=("Helvetica", 15),corner_radius=5, fg_color="white", border_color="gray", border_width=1,text_color="black", width=220, height=35)
        self.username_txt.place(x=200, y=130)

        self.new_pass_txt = ctk.CTkEntry(self.right_frame, textvariable=self.new_pass_var, font=("Helvetica", 15),corner_radius=5, fg_color="white", border_color="gray", border_width=1,text_color="black", width=220, height=35,show="●")
        self.new_pass_txt.place(x=200, y=190)

        self.new_pass_txt = ctk.CTkEntry(self.right_frame, textvariable=self.confirm_pass_var, font=("Helvetica", 15),corner_radius=5, fg_color="white", border_color="gray", border_width=1,text_color="black", width=220, height=35,show="●")
        self.new_pass_txt.place(x=200, y=250)

        # Login button inside the frame

        self.register_btn = ctk.CTkButton(self.right_frame, text="Register", font=ctk.CTkFont("Segoe UI", 15,"bold"),
                                    fg_color="#1a1a40", hover_color="#21649A", text_color="white",
                                    corner_radius=10, cursor="hand2", width=110, height=40,command=self.register_user)
        self.register_btn.place(x=140, y=330)

        # for registration
        bottom_frame = Frame(self.right_frame, bg="white")
        bottom_frame.place(relx=0.5, rely=1.0, anchor="s", y=-30)

        label1 = Label(bottom_frame, text="Already have an account? ", font=("Segoe UI", 12), bg="white")
        label1.pack(side=LEFT)

        register_link = Label(bottom_frame, text="Login here", font=("Segoe UI", 12, "underline"), fg="blue", bg="white", cursor="hand2")
        register_link.pack(side=LEFT)
        register_link.bind("<Button-1>", lambda e: self.open_login())

# functions===============================================================================

    def open_login(self):
        self.root.destroy()
        self.login_win.root.deiconify()

    def register_user(self):

        username = self.username_var.get().strip()
        password = self.new_pass_var.get().strip()
        confirm = self.confirm_pass_var.get().strip()

        if username == "" or password == "" or confirm == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
            return
        
        if len(password) < 8:
            messagebox.showerror("Error", "Password length should be atleast 8!", parent=self.root)
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
    obj = Register(root,root)
    root.mainloop() #so that our window stays on looping
