import tkinter.messagebox
from tkinter import *
import tkinter
import login
from PIL import Image, ImageTk
from time import strftime
from Student import Student
from train_data import Train
from attendance import Attendance
from face_recognition import FaceRecognition
import os


class Face_Recognition_System:
    # This is the constructor
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")  # 0+0 is starting point of x and y axis for application
        self.root.title("Auto Attendance System")
        root.iconphoto(False, ImageTk.PhotoImage(file=r'D:\My_Programs\Python\Auto Attendance\images\face3.jpg'))


        # first_image
        img = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\logo1.jpg")
        img = img.resize((512, 130), Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.photoimg = ImageTk.PhotoImage(img)  # this sets the image

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=510, y=0, width=512, height=130)

        # logo
        img1 = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\face.jpg")
        img1 = img1.resize((510, 130), Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.photoimg1 = ImageTk.PhotoImage(img1)  # this sets the image

        second_label = Label(self.root, image=self.photoimg1)
        second_label.place(x=0, y=0, width=510, height=130)

        # third image
        img2 = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\face2.jpg")
        img2 = img2.resize((515, 130), Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.photoimg2 = ImageTk.PhotoImage(img2)  # this sets the image

        third_label = Label(self.root, image=self.photoimg2)
        third_label.place(x=1022, y=0, width=515, height=130)

        # Background Image
        bg_img = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\bg1.png")
        bg_img = bg_img.resize((1920, 950), Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.backimg = ImageTk.PhotoImage(bg_img)  # this sets the image

        backimg_label = Label(self.root, image=self.backimg)
        backimg_label.place(x=0, y=130, width=1920, height=950)

        # placing the text below headers
        title_label = Label(backimg_label, text="WELCOME TO AUTO ATTENDANCE SYSTEM",
                            font=("Times New Roman", 30, "bold"),
                            bg="#6dd5ed", fg="blue")
        title_label.place(x=-130, y=0, width=1900, height=30)

        # ===============Time============
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_label, font=('times new roman', 14, 'bold'), background='white', foreground='blue')
        lbl.place(x=130, y=0, width=110, height=25)
        time()

        # BUTTON1
        student_image = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\stn.png")
        student_image = student_image.resize((230, 230),
                                             Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.btnimg1 = ImageTk.PhotoImage(student_image)

        button1 = Button(backimg_label, image=self.btnimg1, command=self.student_details, cursor="hand2")
        button1.place(x=200, y=60, width=230, height=230)

        btn1_label = Button(backimg_label, text="STUDENT DETAILS", command=self.student_details,
                            font=("Times New Roman", 14, "bold"), bg="#6dd5ed", fg="blue", cursor="hand2")
        btn1_label.place(x=200, y=290, width=230, height=50)

        # BUTTON2
        face_recognize = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\face3.jpg")
        face_recognize = face_recognize.resize((230, 230),
                                               Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.btnimg2 = ImageTk.PhotoImage(face_recognize)

        button2 = Button(backimg_label, command=self.face_recognition, image=self.btnimg2, cursor="hand2")
        button2.place(x=630, y=60, width=230, height=230)

        btn2_label = Button(backimg_label, text="FACE DETECTOR", command=self.face_recognition,
                            font=("Times New Roman", 14, "bold"), bg="#6dd5ed", fg="blue")
        btn2_label.place(x=630, y=290, width=230, height=50)

        student_image = Image.open
        # BUTTON3
        attendance = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\att3.png")

        attendance = attendance.resize((230, 230),
                                       Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.btnimg3 = ImageTk.PhotoImage(attendance)

        button3 = Button(backimg_label, command=self.attendance, image=self.btnimg3, cursor="hand2")
        button3.place(x=1055, y=60, width=230, height=230)

        btn3_label = Button(backimg_label, text="ATTENDANCE", command=self.attendance,
                            font=("Times New Roman", 14, "bold"), bg="#6dd5ed", fg="blue")
        btn3_label.place(x=1055, y=290, width=230, height=50)

        # BUTTON4
        train_data = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\td.jpg")
        train_data = train_data.resize((230, 230),
                                       Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image

        self.btnimg4 = ImageTk.PhotoImage(train_data)

        button4 = Button(backimg_label, command=self.data_train, image=self.btnimg4)
        button4.place(x=200, y=370, width=230, height=230)

        btn4_label = Button(backimg_label, text="TRAIN DATA", command=self.data_train,
                            font=("Times New Roman", 14, "bold"), bg="#6dd5ed",
                            fg="blue")

        btn4_label.place(x=200, y=600, width=230, height=50)

        # BUTTON5
        photos = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\ph1.jpg")
        photos = photos.resize((230, 230), Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.btnimg5 = ImageTk.PhotoImage(photos)

        button5 = Button(backimg_label, image=self.btnimg5, command=self.open_images)
        button5.place(x=630, y=370, width=230, height=230)

        btn5_label = Button(backimg_label, text="PHOTOS", command=self.open_images,
                            font=("Times New Roman", 14, "bold"), bg="#6dd5ed", fg="blue")
        btn5_label.place(x=630, y=600, width=230, height=50)

        # BUTTON6
        exit_opt = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\log1.png")
        exit_opt = exit_opt.resize((230, 230),
                                   Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.btnimg6 = ImageTk.PhotoImage(exit_opt)

        button6 = Button(backimg_label, command=self.logout, image=self.btnimg6)
        button6.place(x=1055, y=370, width=230, height=230)

        btn6_label = Button(backimg_label, text="LOGOUT", command=self.logout, font=("calibri", 14, "bold"),
                            bg="#6dd5ed", fg="blue")
        btn6_label.place(x=1055, y=600, width=230, height=50)


    # FUNCTION FOR CALLING ALL BUTTONS THROUGH MAIN WINDOW
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def open_images(self):
        os.startfile(r"D:\My_Programs\Python\Auto Attendance\Photos_Data")

    def data_train(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognition(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def logout(self):
        self.logout = tkinter.messagebox.askyesno("Exit", "Do you really want to logout?", parent=self.root)
        if self.logout > 0:
            self.new_window = Toplevel(self.root)
            self.app = login.Login(self.new_window)
            self.root.destroy()
        else:
            return
