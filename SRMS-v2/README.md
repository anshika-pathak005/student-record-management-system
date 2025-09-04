# Student Record Management System – Version 2

This is the **second and improved version** of my Student Record Management System (SRMS).  
Unlike Version 1, which was a simple learning phase project, this version was **completely designed and thought out by me** with a modern user interface and additional validations.  
It is built using **Python (CustomTkinter)** and **SQLite**, and is also available as an **executable (.exe)** for easy use.

## Features

- **User Authentication**
  - Registration and login system with password protection.  
  - Strong validations for fields (email, roll no, contact, DOB, pin code).  

- **Dashboard**
  - Modern design with real-time statistics (students, courses, results).  
  - Navigation to all modules.  

- **Student Management**
  - Add, update, delete, and search students.  
  - Validations prevent incorrect input.  

- **Course Management**
  - Add, update, delete courses.  
  - Duplicate course names are not allowed.  

- **Result Management**
  - Enter student results by roll number.  
  - Percentage automatically calculated.  
  - Prevents duplicate entries.  

- **View Results**
  - Search and view results by roll number in a clean window.  

- **Database**
  - SQLite database (`RMS.db`) with 4 tables:  
    - **User** → stores login/registration details  
    - **Student** → stores student information  
    - **Course** → stores course details  
    - **Result** → stores marks and calculated percentage  

## Folder Structure
```
── SRMS-v2/
│
├── README.md # This README
├── login.py # Main entry file (start the application here)
├── dashboard.py # Dashboard module (navigation + real-time stats)
├── register.py # User registration module with validations
├── student.py # Student management (CRUD + validation)
├── course.py # Course management (CRUD + duplicate prevention)
├── result.py # Result management (add/update + percentage calculation)
├── view_result.py # View results by roll number
├── create_db.py # Creates SQLite tables
├── RMS.db # SQLite database file
└── images/ # Icons and UI images
```
## Screenshots
## How to Run

### Option 1 – Run from Source Code
1. Make sure **Python 3.x** is installed.  
2. Download this folder (or the whole repository).  
3. Ensure `RMS.db` is in the same folder as the `.py` files.  
4. Open a terminal/command prompt inside the folder and run:  
   ```bash
   python login.py
The application will open, and data will be stored inside RMS.db.

###Option 2 – Run the Executable (Recommended)
Download SRMS-v2-Executable.zip from the releases folder.

Extract the .zip.

Keep SRMS.exe and RMS.db in the same folder.

Double-click SRMS.exe to launch the application.

## Acknowledgment

This version was entirely my own design and implementation.
I improved upon the first version with better UI, validations, and additional functionality, and packaged it into an executable for real-world usability.
