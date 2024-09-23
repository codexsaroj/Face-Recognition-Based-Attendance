import pymysql
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import main
from tkinter import messagebox

global Frame_login1
class Login:
    def __init__(self, root):
        self.root = root
        root.iconphoto(False, ImageTk.PhotoImage(file='D:\My_Programs\Python\Auto Attendance\images\login2.jpg'))
        self.root.title("Login System")

        self.root.geometry("1920x1080+0+0")

        # =======REGISTRATION VARIABLES
        self.username = StringVar()
        self.email = StringVar()
        self.passwd = StringVar()
        self.cnfm_passwd = StringVar()

        # ===== LOGIN VARIABLES
        self.login_password = StringVar()
        self.login_username = StringVar()

    def loginform(self):
        Frame_login = Frame(self.root, bg="white")

        Frame_login.place(x=0, y=0, height=1080, width=1920)

        # Background Image
        bg_img = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\bg7.jpg")
        bg_img = bg_img.resize((1920, 950), Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.backimg = ImageTk.PhotoImage(bg_img)  # this sets the image

        backimg_label = ttk.Label(self.root, image=self.backimg)
        backimg_label.place(x=0, y=0, width=1920, height=950)

        inside_img = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\bg7.jpg")
        inside_img = inside_img.resize((455, 450),
                                       Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.insideimg = ImageTk.PhotoImage(inside_img)

        text_label = Label(backimg_label, image=self.insideimg, text="WELCOME\nTO\nAUTO\nATTENDANCE", compound='center',
                           font=('calibri', 60, "bold"), fg="white")
        text_label.place(x=900, y=120)

        # LOGIN FRAME
        frame_input = Frame(self.root, bg='white', bd=2)

        frame_input.place(x=420, y=130, height=450, width=350)

        label1 = Label(frame_input, text="Login Here", font=('impact', 32, 'bold'), fg="black", bg='white')

        label1.place(x=75, y=20)

        label2 = Label(frame_input, text="Username", font=("arial old style", 20, "bold"),

                       fg='orangered', bg='white')

        label2.place(x=30, y=95)

        login_email = ttk.Entry(frame_input, textvariable=self.login_username, font=("times new roman", 15, "bold"))

        login_email.place(x=30, y=145, width=270, height=35)

        label3 = Label(frame_input, text="Password", font=("arial old style", 20, "bold"),

                       fg='orangered', bg='white')

        label3.place(x=30, y=195)

        login_password = ttk.Entry(frame_input, textvariable=self.login_password, font=("times new roman", 15, "bold"))

        login_password.place(x=30, y=245, width=270, height=35)

        # ===== LOGIN BUTTON=========
        btn2 = Button(frame_input, text="Login", command=self.login, cursor="hand2",

                      font=("times new roman", 15), fg="white", bg="orange",

                      bd=0, width=15, height=1)

        btn2.place(x=90, y=320)

        # ========= REGISTER BUTTON ============
        btn3 = Button(frame_input, command=self.Register, text="Create New Account"

                      , cursor="hand2", font=("sans-ascii", 13), bg='green', fg="white")

        btn3.place(x=65, y=380, width=230)

    def login(self):

        if self.login_username.get() == "" or self.login_password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="Crockroz434",
                                      database="face_recognition")
                cur = con.cursor()
                cur.execute("SELECT * FROM `register` WHERE `username`=%s AND `password`=%s",
                            (
                                self.login_username.get(),
                                self.login_password.get())
                            )
                row = cur.fetchone()
                if row is None:
                    root_icon = PhotoImage(file=f"D:\My_Programs\Python\Auto Attendance\images\invalid.png")
                    root.iconphoto(False, root_icon)
                    messagebox.showerror('Invalid', 'Invalid Username or Password!!', parent=self.root)
                    self.loginclear()
                else:
                    self.main_page()
                    con.close()

            except Exception as es:
                messagebox.showerror('Error', f'Error Due to : {str(es)}', parent=self.root)

    def Register(self):
        # ====== REGISTRATION MAIN FRAME =========
        global Frame_login1
        self.new_window = Toplevel(self.root)
        self.app = Login(self.new_window)
        Frame_login1 = Frame(self.new_window, bg="white")

        Frame_login1.place(x=0, y=0, height=810, width=1920)

        # ========= REGISTRATION BACKGROUND IMAGE =======
        register_img = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\b13.jpg")
        register_img = register_img.resize((1920, 810),
                                           Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.regimg = ImageTk.PhotoImage(register_img)  # this sets the image

        regimg_label = Label(Frame_login1, image=self.regimg)
        regimg_label.place(x=0, y=0, width=1920, height=810)

        #   ==== REGISTRATION INNER FRAME
        frame_input2 = Frame(self.new_window, bg='white')

        frame_input2.place(x=320, y=130, height=450, width=630)

        label1 = Label(frame_input2, text="Register Here", font=('impact', 32, 'bold'),

                       fg="black", bg='white')

        label1.place(x=45, y=20)

        # ======== USERNAME========
        label2 = Label(frame_input2, text="Username", font=("arial old style", 20, "bold"),

                       fg='orangered', bg='white')

        label2.place(x=30, y=95)

        username = ttk.Entry(frame_input2, textvariable=self.username, font=("times new roman", 15, "bold"))

        username.place(x=30, y=145, width=270, height=35)


        # ========== EMAIL ===========
        label4 = Label(frame_input2, text="Email-id", font=("arial old style", 20, "bold"),fg='orangered', bg='white')

        label4.place(x=330, y=95)

        email = ttk.Entry(frame_input2, textvariable=self.email, font=("times new roman", 15, "bold"))

        email.place(x=330, y=145, width=270, height=35)

        # =========== PASSWORD ===============
        label3 = Label(frame_input2, text="Password", font=("arial old style", 20, "bold"), fg='orangered', bg='white')

        label3.place(x=30, y=195)

        password = ttk.Entry(frame_input2, textvariable=self.passwd, font=("times new roman", 15, "bold"))

        password.place(x=30, y=245, width=270, height=35)

        # ========== CONFIRM PASSWORD =============
        label5 = Label(frame_input2, text="Confirm Password",

                       font=("arial old style", 20, "bold"), fg='orangered', bg='white')

        label5.place(x=330, y=195)

        cnfm_passwd = ttk.Entry(frame_input2, textvariable=self.cnfm_passwd, font=("times new roman", 15, "bold"))

        cnfm_passwd.place(x=330, y=245, width=270, height=35)


        # ======== REGISTER BUTTON ===========
        btn2 = Button(frame_input2, command=self.register, text="Register"

                      , cursor="hand2", font=("times new roman", 15), fg="white",

                      bg="orangered", bd=0, width=15, height=1)

        btn2.place(x=90, y=340)


    # =========== REGISTRATION FUNCTION ===============
    def register(self):
        if self.username.get() == "" or self.passwd.get() == "" or self.email.get() == "" or self.cnfm_passwd.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.new_window)
        elif len(self.passwd.get()) < 8:
            messagebox.showerror("Invalid", "Length of password must be greater than 8", parent=self.root)
        elif self.passwd.get() != self.cnfm_passwd.get():
            messagebox.showerror("Error", "Password and Confirm Password Should Be Same", parent=self.root)
        else:
            try:
                global Frame_login1

                con = pymysql.connect(host="localhost", user="root", password="Crockroz434",
                                      database="face_recognition")
                new_cursor = con.cursor()
                new_cursor.execute("SELECT * FROM `register` WHERE `email`=%s",
                                   (
                                       str(self.email.get()))
                                   )
                row = new_cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User already exists!!", parent=self.root)
                    self.regclear()
                else:
                    new_cursor.execute("INSERT INTO `register` VALUES(%s,%s,%s,%s)",
                                       (self.username.get(), self.email.get(), self.passwd.get(),
                                        self.cnfm_passwd.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration Successful", parent=self.root)
                    self.regclear()
                    self.new_window.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}"
                                     , parent=self.new_window)

    def regclear(self):
        self.username.set("")
        self.passwd.set("")
        self.email.set("")
        self.cnfm_passwd.set("")

    def loginclear(self):
        self.login_username.set("")
        self.login_password.set("")

    def main_page(self):
        self.new_window = Toplevel(self.root)
        self.app = main.Face_Recognition_System(self.new_window)


if __name__ == '__main__':
    root = Tk()
    # Creating an object for the class
    obj = Login(root)
    obj.loginform()
    root.mainloop()
