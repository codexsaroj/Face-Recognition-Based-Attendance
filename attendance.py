from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tempfile import NamedTemporaryFile
import shutil
from tkinter import messagebox
from tkinter import filedialog
import os
import csv

alldata = []
global mydata

class Attendance:
    # This is the constructor
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")  # 0+0 is starting p130t of x and y axis for application
        self.root.title("Auto Attendance System")

        self.var_id = StringVar()
        self.var_dept = StringVar()
        self.var_name = StringVar()
        self.var_rollno = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_status = StringVar()

        # first_image
        img = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\rvce.jpg")
        img = img.resize((800, 140), Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.photoimg = ImageTk.PhotoImage(img)  # ImageTK sets the image

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=800, height=140)

        # logo
        img1 = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\student1.jpeg")
        img1 = img1.resize((800, 140), Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.photoimg1 = ImageTk.PhotoImage(img1)  # this sets the image

        second_label = Label(self.root, image=self.photoimg1)
        second_label.place(x=800, y=0, width=800, height=140)

        # BACKGROUND IMAGE
        bg_img = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\bg1.png")
        bg_img = bg_img.resize((1920, 950), Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.backimg = ImageTk.PhotoImage(bg_img)  # this sets the image

        backimg_label = Label(self.root, image=self.backimg)
        backimg_label.place(x=0, y=140, width=1920, height=950)

        # placing the text below headers
        title_label = Label(backimg_label, text="STUDENT ATTENDANCE DETAILS",
                            font=("Times New Roman", 30, "bold"),
                            bg="#6dd5ed", fg="green")
        title_label.place(x=-200, y=0, width=1920, height=30)

        # MAIN FRAME
        main_frame = Frame(backimg_label, bd=2)
        main_frame.place(x=0, y=31, width=1850, height=920)

        # left label
        Left_frame = LabelFrame(main_frame, bd=2, relief="solid", text="Attendance", fg="green",
                                font=("Times New Roman", 15, "bold"))
        Left_frame.place(x=10, y=5, width=740, height=600)

        # Left frame image
        left_frame_img = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\hand.jpg")
        left_frame_img = left_frame_img.resize((745, 130),
                                               Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.left_img = ImageTk.PhotoImage(left_frame_img)  # this sets the image

        left_img_label = Label(Left_frame, image=self.left_img)
        left_img_label.place(x=15, y=0, width=705, height=130)

        # ATTENDANCE FRAME
        left_att_frame = Frame(Left_frame, bd=1, relief=RIDGE)
        left_att_frame.place(x=10, y=140, width=715, height=420)

        # LABEL FOR ID
        student_id = Label(left_att_frame, text="ID:", font=("Times New Roman", 13, "bold"),
                           bg="white")  # Label helps to put text on window or frame
        student_id.grid(row=0, column=0, padx=20, pady=15,
                        sticky=W)  # grid is used to combine any text field with the option values

        id_entry = ttk.Entry(left_att_frame, width=20, textvariable=self.var_id, font=("Times New Roman", 13))
        id_entry.grid(row=0, column=1, pady=15, sticky=W)

        # STUDENT NAMe
        student_name = Label(left_att_frame, text="Name:", font=("Times New Roman", 13, "bold"), bg="white")
        student_name.grid(row=0, column=2, padx=10, sticky=W)

        student_name_entry = ttk.Entry(left_att_frame, width=20, textvariable=self.var_name,
                                       font=("Times New Roman", 13))
        student_name_entry.grid(row=0, column=3, padx=10, sticky=W)

        # ROLL NO
        roll_no = Label(left_att_frame, text="Roll No:", font=("Times New Roman", 13, "bold"), bg="white")
        roll_no.grid(row=1, column=0, padx=20, pady=15, sticky=W)

        roll_no_entry = ttk.Entry(left_att_frame, width=20, textvariable=self.var_rollno, font=("Times New Roman", 13))
        roll_no_entry.grid(row=1, column=1, pady=15, sticky=W)

        # LABEL FOR DEPARTMENT
        dept_label = Label(left_att_frame, text="Department:", font=("Times New Roman", 13, "bold"),
                           bg="white")  # Label helps to put text on window or frame
        dept_label.grid(row=1, column=2, padx=10, pady=15,
                        sticky=W)  # grid is used to combine any text field with the option values

        dept_combo = ttk.Combobox(left_att_frame, textvariable=self.var_dept,
                                  font=("Times New Roman", 12, "normal"), width=20, state="read only")
        dept_combo["values"] = ("Select Departments", "CSE", "CSSE", "ECE", "EEE", "CIVIL", "ME", "IT")
        dept_combo.current(0)
        dept_combo.grid(row=1, column=3, padx=10, pady=15,
                        sticky=W)

        # Time
        date = Label(left_att_frame, text="Date:", font=("Times New Roman", 13, "bold"), bg="white")
        date.grid(row=2, column=0, padx=20, pady=15, sticky=W)

        date_entry = ttk.Entry(left_att_frame, width=20, textvariable=self.var_date, font=("Times New Roman", 13))
        date_entry.grid(row=2, column=1, pady=15, sticky=W)

        # time
        time = Label(left_att_frame, text="Time:", font=("Times New Roman", 13, "bold"), bg="white")
        time.grid(row=2, column=2, padx=10, pady=15, sticky=W)

        time_entry = ttk.Entry(left_att_frame, width=20, textvariable=self.var_time, font=("Times New Roman", 13))
        time_entry.grid(row=2, column=3, padx=10, pady=15, sticky=W)

        # LABEL FOR Status
        att_status = Label(left_att_frame, text="Attendance Status:", font=("Times New Roman", 13, "bold"),
                           bg="white")  # Label helps to put text on window or frame
        att_status.grid(row=3, column=1, padx=30, pady=15,
                        sticky=W)  # grid is used to combine any text field with the option values

        att_status = ttk.Combobox(left_att_frame, textvariable=self.var_status,
                                  font=("Times New Roman", 12, "normal"), width=20, state="read only")
        att_status["values"] = ("Status", "Present", "Absent")
        att_status.current(0)
        att_status.grid(row=3, column=2, padx=0, pady=15,
                        sticky=W)

        # Buttons Frame
        button_frame = Frame(left_att_frame, bd=1, relief=RAISED)  # Frame is used to create a frame without text on it
        button_frame.place(x=10, y=260, width=680, height=40)

        import_cvs = Button(button_frame, text="Import CSV", width=15, command=self.import_csv,
                            font=("Times New Roman", 14, "bold"), bg="orange", fg="blue", cursor="hand2")
        import_cvs.grid(row=0, column=0)

        export_csv = Button(button_frame, text="Export CSV", width=14, command=self.export_csv,
                            font=("Times New Roman", 14, "bold"), bg="orange", fg="blue", cursor="hand2")
        export_csv.grid(row=0, column=1)

        update = Button(button_frame, text="Update", width=14, command=self.update_data,
                        font=("Times New Roman", 14, "bold"), bg="orange", fg="blue", cursor="hand2")
        update.grid(row=0, column=2)

        reset_btn = Button(button_frame, text="Reset", width=15, command=self.reset_data,
                           font=("Times New Roman", 14, "bold"), bg="orange", fg="blue", cursor="hand2")
        reset_btn.grid(row=0, column=3)

        # Right Frame
        Right_frame = LabelFrame(main_frame, bd=2, relief="solid", text="Attendance Information", fg="green",
                                 font=("Times New Roman", 15, "bold"))
        Right_frame.place(x=770, y=5, width=740, height=600)

        table_frame = Frame(Right_frame, bd=1, relief=RAISED)
        table_frame.place(x=10, width=725, height=560)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.attendance_table = ttk.Treeview(table_frame,
                                             column=("id", "name", "roll", "dept", "date", "time", "status"),
                                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("id", text="ID")
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("roll", text="Roll No")
        self.attendance_table.heading("dept", text="Department")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("time", text="Time")
        self.attendance_table.heading("status", text="Status")
        self.attendance_table["show"] = "headings"

        self.attendance_table.column("id", width=70)
        self.attendance_table.column("name", width=150)
        self.attendance_table.column("roll", width=100)
        self.attendance_table.column("dept", width=100)
        self.attendance_table.column("date", width=100)
        self.attendance_table.column("time", width=100)
        self.attendance_table.column("status", width=80)

        self.attendance_table.pack(fill=BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease>", self.get_cursor)

    # FUNCTION TO FETCH DATA
    def fetchData(self, rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("", END, values=i)

    # This will help to import the data from the user.csv file
    def import_csv(self):
        global alldata
        alldata.clear()
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(), title="Opening CSV",
                                               filetypes=(("CSV File", ".csv"), ("All file", "*.*")), parent=self.root)
        try:
            with open(file_name) as fln:
                readfile = csv.reader(fln, delimiter=",")
                for data in readfile:
                    alldata.append(data)
                self.fetchData(alldata)
        except Exception as e:
            if file_name is None:
                messagebox.showerror("Empty", "No file imported", parent=self.root)

    # This will help to export the csv file
    def export_csv(self):
        try:
            if len(alldata) < 1:
                messagebox.showerror("Error", "No data in the file!", parent=self.root)
                return False
            file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Opening CSV",
                                                     filetypes=(("CSV File", ".csv"), ("All file", "*.*")),
                                                     parent=self.root)
            with open(file_name, mode="w", newline="") as op:
                export_file = csv.writer(op, delimiter=",")
                for i in alldata:
                    export_file.writerow(i)
                messagebox.showinfo("Export",
                                    "All data got exported to " + os.path.basename(file_name) + " successfully")

        except Exception as e:
            messagebox.showerror("Error", "Unsuccessful due to {error}".format(error=str(e)), parent=self.root)

    @staticmethod
    def is_Null(list):
        if len(list) == 0:
            messagebox.showerror("Empty", "No data in the table!!")

    def get_cursor(self, event=""):
        global mydata
        try:
            cursor_focus = self.attendance_table.focus()
            content = self.attendance_table.item(cursor_focus)
            mydata = content["values"]

            self.var_id.set(mydata[0]),
            self.var_name.set(mydata[1]),
            self.var_rollno.set(mydata[2]),
            self.var_dept.set(mydata[3]),
            self.var_date.set(mydata[4]),
            self.var_time.set(mydata[5]),
            self.var_status.set(mydata[6]),
        except Exception as e:
            self.is_Null(mydata)

        # ====UPDATE BUTTON FUNCTION======

    def update_data(self):
        try:
            if len(alldata) < 1:
                messagebox.showerror("Error", "No data in the file!", parent=self.root)
                return False
            file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Opening CSV",
                                                     filetypes=(("CSV File", ".csv"), ("All file", "*.*")),
                                                     parent=self.root)
            tempfile = NamedTemporaryFile(mode='w', delete=False)

            fields = ['ID', 'Name', 'Roll No', 'Department', 'Date', 'Time', 'Status']

            with open(file_name, 'r+', encoding='ascii') as csvfile, tempfile:
                reader = csv.DictReader(csvfile, fieldnames=fields)
                writer = csv.DictWriter(tempfile, fieldnames=fields)
                for row in reader:
                    if row['ID'] == str(self.var_id.get()):
                        print('updating row', row['ID'])
                        row['Name'], row['Roll No'], row['Department'], row['Date'], row['Time'], row[
                            'Status'] = (
                            self.var_name.get(), self.var_rollno.get(), self.var_dept.get(), self.var_date.get()
                            , self.var_time.get(), self.var_status.get())

                    row = {'ID': row['ID'], 'Name': row['Name'], 'Roll No': row['Roll No'],
                           'Department': row['Department'], 'Date': row['Date']
                        , 'Time': row['Time'], 'Status': row['Status']}
                    writer.writerow(row)
            shutil.move(tempfile.name, file_name)
            messagebox.showinfo("Success", "Updation Successful")
        except Exception as e:
            messagebox.showerror("Error", f"{str(e)}", parent=self.root)

    # ========RESET BUTTON FUNCTION
    def reset_data(self):
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_rollno.set(""),
        self.var_dept.set("Select Departments"),
        self.var_date.set("dd/mm/yy"),
        self.var_status.set("Status"),
        self.var_time.set("")

