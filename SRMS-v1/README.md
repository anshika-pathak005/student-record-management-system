# Student Record Management System – Version 1

This is the **first version** of my Student Record Management System (SRMS).  
It was created during my learning phase to practice building a desktop CRUD application using **Python (Tkinter)** and **SQLite**.  
The design was simple (blue & white theme), but it covered the **core functionality** of student record management.

---

## Features

- **User Authentication**
  - Registration and login system with password protection.  

- **Dashboard**
  - Simple navigation window to access different modules.  

- **Student Management**
  - Add, update, delete, and search student records.  
  - No advanced field validations in this version.  

- **Course Management**
  - Add, update, delete courses.  
  - Duplicate course names not allowed.  

- **Result Management**
  - Enter student results by roll number.  
  - Percentage calculated automatically.  

- **View Results**
  - Search and view results by roll number in a read-only window.  

---

## Database

This version uses a **SQLite database** (`RMS.db`) with the following 4 tables:

- **User** → stores login/registration details  
- **Student** → stores student information (roll no, name, DOB, etc.)  
- **Course** → stores course details  
- **Result** → stores marks and calculated percentage  

The schema is created via `create_database.py`.

---

## Folder Structure
```
── SRMS-v1/
│
├── README.md # This README
├── login.py # Main entry file (start the application here)
├── main_dashboard.py # Dashboard module (navigation only)
├── register.py # User registration module
├── main_student.py # Student management (CRUD operations)
├── main_course.py # Course management
├── main_result.py # Result management
├── view_result.py # View results by roll number
├── create_database.py # Creates SQLite tables
├── RMS.db # SQLite database file
└── images/ # Icons and UI images
```
## How to Run

### Option 1 – Run from Source Code
1. Make sure **Python 3.x** is installed.  
2. Download this folder (or the whole repository).  
3. Ensure `RMS.db` is in the same folder as the `.py` files.  
4. Open a terminal/command prompt inside the folder and run:  
   ```bash
   python login.py
The application will open, and data will be stored inside RMS.db.

Option 2 – Run the Executable
Download SRMS-v1-Executable.zip from the releases folder.

Extract the .zip.

Keep SRMS.exe and RMS.db in the same folder.

Double-click SRMS.exe to launch the application.
##Screenshots

This version was my learning phase project — in Version 2, I redesigned the UI with CustomTkinter, added validations, and packaged it into an executable.

## Acknowledgment

This version was inspired by an online tutorial to understand the flow of a student management system.  
However, all code and design in this version were written by me, and I used the tutorial only as a learning reference.
