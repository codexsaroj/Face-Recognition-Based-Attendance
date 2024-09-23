from tkinter import *
from PIL import Image, ImageTk
from Student import Student
import mysql.connector
import webbrowser
from tkinter import ttk
from tkinter import messagebox
import cv2
from datetime import datetime

class FaceRecognition(Student):
    # This is the constructor
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.geometry("1920x1080")  # 0+0 is starting point of x and y axis for application
        self.root.title("Face Detector")


        self.var_year = StringVar()
        self.var_section = StringVar()

        title_label = Label(self.root, text="Face Detector",
                            font=("Times New Roman", 25, "bold"),
                            bg="white", fg="blue")
        title_label.place(x=-200, y=0, width=1920, height=30)

        # LEFT SIDE IMAGE
        left_img = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\face2.jpg")
        left_img = left_img.resize((799, 754),
                                   Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.photoimg = ImageTk.PhotoImage(left_img)  # ImageTK sets the image

        left_img_label = Label(self.root, image=self.photoimg)
        left_img_label.place(x=0, y=40, width=799, height=754)

        # RIGHT SIDE IMAGE
        right_img = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\face3.jpg")
        right_img = right_img.resize((799, 754),
                                     Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.photoimg1 = ImageTk.PhotoImage(right_img)  # ImageTK sets the image

        right_img_label = Label(self.root, image=self.photoimg1)
        right_img_label.place(x=799, y=40, width=799, height=754)

        # Create CSV
        create_csv_button = Button(self.root, text="Create Attendance File", command=self.create_csv,
                                    font=("Times New Roman", 20, "bold"), bg="#3D59AB",
                                    fg="white", cursor="hand2")
        create_csv_button.place(x=580, y=110, width=350, height=50, anchor=W)

        # TRAIN BUTTON
        face_detect_button = Button(self.root, text="TAKE ATTENDANCE", command=self.face_recognition,
                                    font=("Times New Roman", 20, "bold"), bg="#4169E1",
                                    fg="white", cursor="hand2")
        face_detect_button.place(x=1050, y=700, width=300, height=50, anchor=W)

        # YEAR AND SECTION
        year_combo = ttk.Combobox(self.root, textvariable=self.var_year,
                                    font=("Times New Roman", 15, "normal"), width=10, state="read only")
        year_combo["values"] = ("Select Year", "I year", "II year", "III year", "IV year")
        year_combo.current(0)
        year_combo.place(x=620, y=600, height="40")

        section_combo = ttk.Combobox(self.root, textvariable=self.var_section,
                                  font=("Times New Roman", 15, "normal"), width=10, state="read only")
        section_combo["values"] = ("Section", "A", "B", "C", "D")
        section_combo.current(0)
        section_combo.place(x=770, y=600, height="40")
        # year_combo.grid(row=0, column=3, padx=2, pady=10,
        #                   sticky=W)  # grid is used to combine any text field with the option values

        # ============ ATTENDANCE =========

    def create_csv(self):
        path = "Attendance"
        create = messagebox.askyesno("File Creation", "Do u want to create attendance file?")
        if create > 0:
            webbrowser.open(path)



    def mark_attendance(self, id1, n, r, dept):
        path = rf"Attendance\{str(self.var_year.get())}\{ str(self.var_section.get())}\{datetime.now().strftime('attendance-%d-%m-%Y.csv')}"

        with open(path, "w+") as f_output:
            pass

        with open(path, "r+") as op:
            myDataList = op.readlines()
            names_list = []
            for line in myDataList:
                entry = line.split(",")
                names_list.append(entry[0])
            if (id1 not in names_list) and (n not in names_list) and (r not in names_list) and (dept not in names_list):
                current_time = datetime.now()
                d = current_time.strftime("%d/%m/%Y")
                t = current_time.strftime("%H:%M:%S")
                op.writelines(f"{id1},{n},{r},{dept},{d},{t},Present"+"\n")

        # ========= FACE RECOGNITION ===========

    def face_recognition(self):

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, flags, minSize, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors, flags, minSize)
            coordinates = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id1, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confindence = int((100 * (1 - predict / 300)))
                conn = mysql.connector.connect(host="localhost", user="root", password="Crockroz434",
                                               database="face_recognition", auth_plugin='mysql_native_password')

                new_cursor = conn.cursor()
                new_cursor.execute("SELECT `ID` FROM `student` WHERE `ID`= "+str(id1))
                i = new_cursor.fetchone()
                i = '+'.join(i)

                new_cursor.execute("SELECT `Name` FROM `student` WHERE `ID`= " + str(id1))
                n = new_cursor.fetchone()
                n = '+'.join(n)

                new_cursor.execute(f"SELECT `RollNo` FROM `student` WHERE `ID`= " + str(id1))
                r = new_cursor.fetchone()
                r = "+".join(r)

                new_cursor.execute(f"SELECT `Dept` FROM `student` WHERE `ID`=" + str(id1))
                dept = new_cursor.fetchone()
                dept = "+".join(dept)

                if confindence > 78:
                    cv2.putText(img, f"RollNo:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 25), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    self.mark_attendance(i, n, r, dept)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown Face", (x, y - 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                coordinates = [x, y, w, h]
            return coordinates

        def recognize(img, clf, faceCascade):
            coordinates = draw_boundary(img, faceCascade, 1.3, 5, None, (30, 30), (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")  # reading the classifier file
        cam = cv2.VideoCapture(0)
        while True:
            ret, img = cam.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition System", img)
            if cv2.waitKey(1) == 13:
                break
        cam.release()
        cv2.destroyAllWindows()

