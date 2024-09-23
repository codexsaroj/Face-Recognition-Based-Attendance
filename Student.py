from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from mysql.connector.locales.eng import client_error
import mysql.connector
import cv2

global conn
class Student:
    # This is the constructor
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")  # 0+0 is starting point of x and y axis for application
        self.root.title("Auto Attendance System")

        # THESE VARIABLES ARE USED TO GET THE VALUE FROM THEIR RESPECTIVE COMBOBOX(INPUT FIELDS) THROUGH TEXT VARIABLES

        self.var_id = StringVar()
        self.var_dept = StringVar()
        self.var_name = StringVar()
        self.var_rollno = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_section = StringVar()
        self.var_phno = StringVar()
        self.var_email = StringVar()

        # first_image
        img = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\rvce.jpg")
        img = img.resize((512, 130), Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.photoimg = ImageTk.PhotoImage(img)  # ImageTK sets the image

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=510, y=0, width=512, height=130)

        # logo
        img1 = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\student1.jpeg")
        img1 = img1.resize((510, 130), Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.photoimg1 = ImageTk.PhotoImage(img1)  # this sets the image

        second_label = Label(self.root, image=self.photoimg1)
        second_label.place(x=0, y=0, width=510, height=130)

        # third image
        img2 = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\student2.jpg")
        img2 = img2.resize((515, 130), Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.photoimg2 = ImageTk.PhotoImage(img2)  # this sets the image

        third_label = Label(self.root, image=self.photoimg2)
        third_label.place(x=1022, y=0, width=515, height=130)

        bg_img = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\bg1.png")
        bg_img = bg_img.resize((1920, 950), Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.backimg = ImageTk.PhotoImage(bg_img)  # this sets the image

        backimg_label = Label(self.root, image=self.backimg)
        backimg_label.place(x=0, y=130, width=1900, height=950)

        # placing the text below headers
        title_label = Label(backimg_label, text="STUDENT   DATABASE",
                            font=("Times New Roman", 30, "bold"),
                            bg="#6dd5ed", fg="green")
        title_label.place(x=-200, y=0, width=1920, height=30)

        main_frame = Frame(backimg_label, bd=2)
        main_frame.place(x=0, y=35, width=1850, height=920)

        # left label
        Left_frame = LabelFrame(main_frame, bd=2, relief="solid", text="Student Details",
                                font=("Times New Roman", 15, "bold"))
        Left_frame.place(x=10, y=10, width=740, height=600)

        # Left frame image
        left_frame_img = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\hand.jpg")
        left_frame_img = left_frame_img.resize((745, 130),
                                               Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.left_img = ImageTk.PhotoImage(left_frame_img)  # this sets the image

        left_img_label = Label(Left_frame, image=self.left_img)
        left_img_label.place(x=15, y=0, width=705, height=130)

        # CURRENT COURSE
        current_course_frame = LabelFrame(Left_frame, bd=1, relief=RIDGE, text="Current Course Information",
                                          font=("Times New Roman", 15, "bold"))
        current_course_frame.place(x=10, y=140, width=715, height=120)

        # LABEL FOR DEPARTMENT
        dept_label = Label(current_course_frame, text="Department:", font=("Times New Roman", 13, "bold"),
                           bg="white")  # Label helps to put text on window or frame
        dept_label.grid(row=0, column=0, padx=10,
                        sticky=W)  # grid is used to combine any text field with the option values

        dept_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dept,
                                  font=("Times New Roman", 12, "normal"), width=17, state="read only")
        dept_combo["values"] = ("Select Departments", "CSE", "CSSE", "ECE", "EEE", "CIVIL", "ME", "IT")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1, padx=2, pady=10,
                        sticky=W)  # grid is used to combine any text field with the option values

        # COURSE
        course_label = Label(current_course_frame, text="Course:", font=("Times New Roman", 13, "bold"),
                             bg="white")  # Label helps to put text on window or frame
        course_label.grid(row=0, column=2, padx=10,
                          sticky=W)  # grid is used to combine any text field with the option values

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course,
                                    font=("Times New Roman", 12, "normal"), width=17, state="read only")
        course_combo["values"] = ("Select Course", "B.Tech", "M.Tech", "Phd", "Pfd")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10,
                          sticky=W)  # grid is used to combine any text field with the option values

        # LABEL FOR YEAR
        year_label = Label(current_course_frame, text="Year:", font=("Times New Roman", 13, "bold"),
                           bg="white")  # Label helps to put text on window or frame
        year_label.grid(row=1, column=0, padx=10,
                        sticky=W)  # grid is used to combine any text field with the option values

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,
                                  font=("Times New Roman", 12, "normal"), width=17, state="read only")
        year_combo["values"] = ("Select Year", "I Year", "II Year", "III Year", "IV Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10,
                        sticky=W)  # grid is used to combine any text field with the option values

        # LABEL FOR SEMESTER
        sem_label = Label(current_course_frame, text="Semester:", font=("Times New Roman", 13, "bold"),
                          bg="white")  # Label helps to put text on window or frame
        sem_label.grid(row=1, column=2, padx=10,
                       sticky=W)  # grid is used to combine any text field with the option values

        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester,
                                 font=("Times New Roman", 12, "normal"), width=17, state="read only")
        sem_combo["values"] = ("Select Semester", "I", "II")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10,
                       sticky=W)  # grid is used to combine any text field with the option values

        # CLASS FRAME
        class_frame = LabelFrame(Left_frame, bd=1, relief=RIDGE, text="Class Information", font=(
            "Times New Roman", 15, "bold"))  # LabelFrame is used to create frame with text on it
        class_frame.place(x=10, y=260, width=715, height=302)

        # STUDENT NAMe
        student_name = Label(class_frame, text="Name:", font=("Times New Roman", 13, "bold"), bg="white")
        student_name.grid(row=0, column=0, padx=10, sticky=W)

        student_name_entry = ttk.Entry(class_frame, width=20, textvariable=self.var_name, font=("Times New Roman", 13))
        student_name_entry.grid(row=0, column=1, padx=10, sticky=W)

        # ROLL NO
        roll_no = Label(class_frame, text="Roll No:", font=("Times New Roman", 13, "bold"), bg="white")
        roll_no.grid(row=0, column=2, padx=10, sticky=W)

        roll_no_entry = ttk.Entry(class_frame, width=20, textvariable=self.var_rollno, font=("Times New Roman", 13))
        roll_no_entry.grid(row=0, column=3, padx=10, sticky=W)

        # SECTION
        section = Label(class_frame, text="Section:", font=("Times New Roman", 13, "bold"), bg="white")
        section.grid(row=1, column=0, padx=10, pady=15, sticky=W)

        section_entry = ttk.Entry(class_frame, width=20, textvariable=self.var_section, font=("Times New Roman", 13))
        section_entry.grid(row=1, column=1, padx=10, pady=15, sticky=W)

        # Gender
        gender = Label(class_frame, text="Gender:", font=("Times New Roman", 13, "bold"), bg="white")
        gender.grid(row=1, column=2, padx=10, sticky=W)

        self.var_gen_radio = StringVar()
        male_radio_btn = ttk.Radiobutton(class_frame, variable=self.var_gen_radio, text="Male", value="Male")
        male_radio_btn.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        female_radio_button = ttk.Radiobutton(class_frame, variable=self.var_gen_radio, text="Female", value="Female")
        female_radio_button.grid(row=1, column=3, padx=80, pady=10, sticky=W)

        # Phone NO
        phno = Label(class_frame, text="Phone No:", font=("Times New Roman", 13, "bold"), bg="white")
        phno.grid(row=2, column=0, padx=10, sticky=W)

        phno_entry = ttk.Entry(class_frame, width=20, textvariable=self.var_phno, font=("Times New Roman", 13))
        phno_entry.grid(row=2, column=1, padx=10, sticky=W)

        # Email
        email = Label(class_frame, text="Email:", font=("Times New Roman", 13, "bold"), bg="white")
        email.grid(row=2, column=2, padx=10, sticky=W)

        email_entry = ttk.Entry(class_frame, width=20, textvariable=self.var_email, font=("Times New Roman", 13))
        email_entry.grid(row=2, column=3, padx=10, sticky=W)

        # Radio Buttons
        self.var_radio1 = StringVar()
        radio_button1 = ttk.Radiobutton(class_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radio_button1.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        radio_button2 = ttk.Radiobutton(class_frame, variable=self.var_radio1, text="Photo Sample Not Taken",
                                        value="No")
        radio_button2.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # LABEL FOR ID
        student_id = Label(class_frame, text="ID:", font=("Times New Roman", 13, "bold"),
                           bg="white")  # Label helps to put text on window or frame
        student_id.grid(row=3, column=2, padx=10, pady=15,
                        sticky=W)  # grid is used to combine any text field with the option values

        id_entry = ttk.Entry(class_frame, width=20, textvariable=self.var_id, font=("Times New Roman", 13))
        id_entry.grid(row=3, column=3, padx=10, pady=15, sticky=W)

        # Buttons Frame
        button_frame = Frame(class_frame, bd=1, relief=RAISED)  # Frame is used to create a frame without text on it
        button_frame.place(x=15, y=160, width=680, height=40)

        save_btn = Button(button_frame, text="Save", command=self.data_add, width=15,
                          font=("Times New Roman", 14, "bold"), bg="orange", fg="blue", cursor="hand2")
        save_btn.grid(row=0, column=0)

        update_btn = Button(button_frame, text="Update", command=self.update_data, width=14,
                            font=("Times New Roman", 14, "bold"), bg="orange", fg="blue", cursor="hand2")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(button_frame, text="Delete", width=14, command=self.delete_data,
                            font=("Times New Roman", 14, "bold"), bg="orange", fg="blue", cursor="hand2")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(button_frame, text="Reset", width=15, command=self.reset_data,
                           font=("Times New Roman", 14, "bold"), bg="orange", fg="blue", cursor="hand2")
        reset_btn.grid(row=0, column=3)

        button_frame1 = Frame(class_frame, bd=1, relief="solid")
        button_frame1.place(x=15, y=200, width=681, height=40)

        take_photo_sample = Button(button_frame1, text="Take Photo Sample", width=30, command=self.generate_dataset,
                                   font=("Times New Roman", 14, "bold"), bg="orange", fg="blue", cursor="hand2")
        take_photo_sample.grid(row=0, column=0)

        update_photo_sample = Button(button_frame1, text="Update Photo Sample", width=30, command = self.generate_dataset,
                                     font=("Times New Roman", 14, "bold"), bg="orange", fg="blue", cursor="hand2")
        update_photo_sample.grid(row=0, column=1)

        # Right Frame
        Right_frame = LabelFrame(main_frame, bd=2, relief="solid", text="Student Details",
                                 font=("Times New Roman", 15, "bold"))
        Right_frame.place(x=770, y=10, width=750, height=600)

        # Right Frame Image
        Right_frame_img = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\hand.jpg")
        Right_frame_img = Right_frame_img.resize((745, 130),
                                                 Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.right_img = ImageTk.PhotoImage(Right_frame_img)  # this sets the image

        right_img_label = Label(Right_frame, image=self.right_img)
        right_img_label.place(x=15, y=0, width=715, height=130)

        # SEARCH FRAME
        self.var_combosearch = StringVar()
        search_frame = LabelFrame(Right_frame, bd=1, relief=RIDGE, text="Search System",
                                  font=("Times New Roman", 15, "bold"))
        search_frame.place(x=10, y=140, width=725, height=90)

        search_label = Label(search_frame, text="Search By:", width=8, font=("Times New Roman", 16, "bold"), bg="green",
                             fg="white")
        search_label.grid(row=0, column=0, padx=10, sticky=W)

        search_combo = ttk.Combobox(search_frame, textvariable=self.var_combosearch, font=("Times New Roman", 15),
                                    width=12, state="read only", )
        search_combo["values"] = ("RollNo", "ID")
        search_combo.set('Select')
        search_combo.grid(row=0, column=1, pady=10, sticky=W)

        self.var_search = StringVar()
        search_entry = ttk.Entry(search_frame, width=15, textvariable=self.var_search, font=("Times New Roman", 13))
        search_entry.grid(row=0, column=2, padx=10, sticky=W)

        search_btn = Button(search_frame, text="Search", width=12, command=self.search_data,
                            font=("Times New Roman", 13, "bold"), bg="blue",
                            fg="white", cursor="hand2")
        search_btn.grid(row=0, column=3, padx=6)

        show_all_btn = Button(search_frame, text="Show All", width=12, command=self.fetch_data,
                              font=("Times New Roman", 13, "bold"), bg="blue",
                              fg="white", cursor="hand2")
        show_all_btn.grid(row=0, column=4, padx=5)

        # Table Frame
        table_frame = Frame(Right_frame, bd=1, relief=RAISED)
        table_frame.place(x=10, y=245, width=725, height=320)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column=(
            "id", "dept", "name", "roll_no", "course", "year", "semester", "section", "gender", "phno", "email",
            "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # HEADER
        self.student_table.heading("id", text="ID")
        self.student_table.heading("dept", text="Department")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll_no", text="Roll No")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("section", text="Section")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("phno", text="Phone No")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("photo", text="Photo Sample")
        self.student_table["show"] = "headings"

        self.student_table.column("id", width=100)
        self.student_table.column("dept", width=100)
        self.student_table.column("name", width=150)
        self.student_table.column("roll_no", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=80)
        self.student_table.column("semester", width=80)
        self.student_table.column("section", width=80)
        self.student_table.column("gender", width=100)
        self.student_table.column("phno", width=100)
        self.student_table.column("email", width=150)
        self.student_table.column("photo", width=120)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # FUNCTION TO ADD DATA INTO DATABASE
    def data_add(self):
        if self.var_rollno.get() == "":
            messagebox.showerror("Error", "Please Fill Out The All The Fields!!", parent=self.root)
        else:  # CONNECTING TO OUR DATABASE
            global conn
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Crockroz434",
                                               database="face_recognition", auth_plugin='mysql_native_password')
                # CURSOR IS USED TO EXECUTE BELOW SQL STATEMENTS TO COMMUNICATE WITH DATABASE
                new_cursor = conn.cursor()
                new_cursor.execute("INSERT INTO `student` VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_id.get(),
                    self.var_dept.get(),
                    self.var_name.get(),
                    self.var_rollno.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_section.get(),
                    self.var_gen_radio.get(),
                    self.var_phno.get(),
                    self.var_email.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Details stored successfully!!", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due to {str(e)}", parent=self.root)

    # TO FETCH THE DATA FROM DATABASE INTO THE TABLE
    def fetch_data(self):
        global conn
        conn = mysql.connector.connect(host="localhost", user="root", password="Crockroz434",
                                       database="face_recognition", auth_plugin='mysql_native_password')
        new_cursor = conn.cursor()
        new_cursor.execute("SELECT * FROM `student`")
        mydata = new_cursor.fetchall()

        if len(mydata) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in mydata:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ======= Get Cursor ============ to get the focused data into entry fields from table
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        mydata = content["values"]

        self.var_id.set(mydata[0]),
        self.var_dept.set(mydata[1]),
        self.var_name.set(mydata[2]),
        self.var_rollno.set(mydata[3]),
        self.var_course.set(mydata[4]),
        self.var_year.set(mydata[5]),
        self.var_semester.set(mydata[6]),
        self.var_section.set(mydata[7]),
        self.var_gen_radio.set(mydata[8]),
        self.var_phno.set(mydata[9]),
        self.var_email.set(mydata[10]),
        self.var_radio1.set(mydata[11])

    #  UPDATE FUNCTION BUTTON
    def update_data(self):
        if self.var_rollno.get() == "":
            messagebox.showerror("Error", "Please Fill Out The All The Fields!!", parent=self.root)
        else:
            global conn
            try:
                Update = messagebox.askyesno("Update", "Are you sure you want to update?", parent=self.root)
                if Update > 0:  # 1 means yes  and 0 means no
                    conn = mysql.connector.connect(host="localhost", user="root", password="Crockroz434",
                                                   database="face_recognition", auth_plugin='mysql_native_password')
                    new_cursor = conn.cursor()
                    new_cursor.execute(
                        "UPDATE student SET `Dept`=%s, `Name`=%s,`RollNo`=%s, `Course`=%s, `Year`=%s, `Semester`=%s, `Section`=%s, `Gender`=%s, `Phone`=%s, `Email`=%s, `Photo Sample`=%s WHERE `ID`=%s",
                        (
                            self.var_dept.get(),
                            self.var_name.get(),
                            self.var_rollno.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_section.get(),
                            self.var_gen_radio.get(),
                            self.var_phno.get(),
                            self.var_email.get(),
                            self.var_radio1.get(),
                            self.var_id.get()
                        ))
                else:
                    if not Update:
                        return 0
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Data updated successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due to {str(e)}", parent=self.root)
    # ======== DELETE BUTTON FUNCTION
    def delete_data(self):
        if self.var_rollno.get() == "":
            messagebox.showerror("Error", "Roll No missing!!", parent=self.root)
        else:
            global conn
            try:
                delete = messagebox.askyesno("Delete", "Are you sure you want to delete?", parent=self.root)
                if delete > 0:  # 1 means yes  and 0 means no
                    conn = mysql.connector.connect(host="localhost", user="root", password="Crockroz434",
                                                   database="face_recognition", auth_plugin='mysql_native_password')
                    new_cursor = conn.cursor()
                    sql = "DELETE FROM `student` WHERE `RollNo`=%s"
                    val = (self.var_rollno.get(),)
                    new_cursor.execute(sql, val)
                else:
                    if not delete:
                        return 0
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Data deleted successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due to {str(e)}")

    # =====RESET BUTTON FUNCTION======
    def reset_data(self):
        self.var_id.set(""),
        self.var_dept.set("Select Departments"),
        self.var_name.set(""),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_section.set(""),
        self.var_gen_radio.set(""),
        self.var_phno.set(""),
        self.var_email.set(""),
        self.var_radio1.set(""),
        self.var_rollno.set("")

    # =========Search data=======
    def search_data(self):
        if self.var_combosearch.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "Select at least one option!!", parent=self.root)
        else:
            global conn
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Crockroz434",
                                               database="face_recognition", auth_plugin='mysql_native_password')
                new_cursor = conn.cursor()
                new_cursor.execute(
                    "SELECT * FROM `student` WHERE " + str(self.var_combosearch.get()) + " LIKE '%" + str(
                        self.var_search.get()) + "%'")
                data = new_cursor.fetchall()
                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                else:
                    messagebox.showerror("Missing", "Sorry, Student not found", parent=self.root)
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", "Sorry, Student not found {error}".format(error=str(e)), parent=self.root)

    @staticmethod
    def crop_face(img, face_classifier):
        image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(image, 1.1, 4)  # 1.1=scaling factor and 4=minimum neighbour
        for (x, y, w, h) in faces:
            crop_face = img[y:y + h, x:x + w]
            return crop_face

    # ============ TAKING PHOTO SAMPLE ===============
    def generate_dataset(self):
        roll = str(self.var_rollno.get())
        photo_id = str(self.var_id.get())
        if self.var_rollno.get() == "":
            messagebox.showerror("Error", "Please Fill Out The All The Fields!!", parent=self.root)
        else:
            global conn
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Crockroz434",
                                               database="face_recognition", auth_plugin='mysql_native_password')
                new_cursor = conn.cursor()
                new_cursor.execute("SELECT * FROM `student`")
                my_result = new_cursor.fetchall()
                id1 = 0
                for x in my_result:
                    id1 += 1
                new_cursor.execute(
                    "UPDATE `student` SET `ID`=%s, `Dept`=%s, `Name`=%s, `Course`=%s, `Year`=%s, `Semester`=%s, `Section`=%s, `Gender`=%s, `Phone`=%s, `Email`=%s, `Photo Sample`=%s WHERE `RollNo`=%s",
                    (
                        self.var_id.get(),
                        self.var_dept.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_section.get(),
                        self.var_gen_radio.get(),
                        self.var_phno.get(),
                        self.var_email.get(),
                        self.var_radio1.get(),
                        self.var_rollno.get()
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ========LOADING THE IMAGES ==========
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                # FUNCTION TO CROP THE FACE IMAGES
                cam = cv2.VideoCapture(0)  # it opens up the camera 1 for external cam and 0 for webcam
                img_id = 0  # For the number of photo samples taken
                while True:
                    ret, myframe = cam.read()  # it reads the video file
                    if self.crop_face(myframe,
                                      face_classifier) is not None:  # this means there is some data inside myframe
                        img_id += 1
                        cap_face = cv2.resize(self.crop_face(myframe, face_classifier),
                                              (450, 450))  # Resizing the captured faces
                        cap_face = cv2.cvtColor(cap_face, cv2.COLOR_BGR2GRAY)
                        photo_path = "Photos_Data/{}.{}.{}.jpg".format(roll, photo_id, img_id)
                        cv2.imwrite(photo_path, cap_face)
                        cv2.putText(cap_face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", cap_face)

                    # it will display a frame for 1ms, after which display will be automatically closed.
                    if cv2.waitKey(1) == 13 or int(img_id) == 200:
                        break
                cam.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Dataset generated successfully!!")
            except Exception as e:
                messagebox.showerror("Error", "Unable to connect to database due to {error}".format(error=str(e)), parent=self.root)


