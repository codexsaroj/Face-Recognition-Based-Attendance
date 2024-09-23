import cx_Freeze
import sys
import os
from cx_Freeze import setup

base = None
if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Saroj\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Saroj\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [
    cx_Freeze.Executable("login.py", base=base)]

setup(
    name="Auto Attendance",
    options={"build.exe": {"packages": ["tkinter", "os"],
                           "include_files": ['tcl86t.dll',
                                             'tk86t.dll', 'images', 'Photos_Data', 'Database', 'Attendance']}},
    version="1.0",
    description="Auto Attendance System",
    executables=executables
)
