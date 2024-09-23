import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import numpy as np

class Train:
    # This is the constructor
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")  # 0+0 is starting point of x and y axis for application
        self.root.title("Train Data")

        title_label = Label(self.root, text="Train Data Window",
                            font=("Times New Roman", 25, "bold"),
                            bg="white", fg="blue")
        title_label.place(x=-200, y=0, width=1920, height=40)

        img = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\rvce.jpg")
        img = img.resize((799, 250), Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.photoimg = ImageTk.PhotoImage(img)  # ImageTK sets the image
        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=40, width=799, height=250)

        building_img = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\building.jpg")
        building_img = building_img.resize((799, 250), Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.photoimg1 = ImageTk.PhotoImage(building_img)  # ImageTK sets the image
        first_label = ttk.Label(self.root, image=self.photoimg1)
        first_label.place(x=799, y=40, width=799, height=250)

        # TRAIN BUTTON
        btn3_label = Button(self.root, text="Click Here For Attendance", command=self.train_classifier, font=("Times New Roman", 20, "bold"), bg="orange",fg="blue")
        btn3_label.place(x=-220, y=315, width=1900, height=50, anchor=W)

        bottom_face = Image.open(r"D:\My_Programs\Python\Auto Attendance\images\bottom_face.jpg")
        bottom_face = bottom_face.resize((1550, 455), Image.ANTIALIAS)  # ANTIALIAS converts high level image to low level image
        self.photoimg2 = ImageTk.PhotoImage(bottom_face)  # ImageTK sets the image
        bottom_label = Label(self.root, image=self.photoimg2)
        bottom_label.place(x=0, y=330, width=1550, height=455)

    @staticmethod
    def train_classifier():
        dataset_dir = "Photos_Data"
        path =[os.path.join(dataset_dir, image) for image in os.listdir(dataset_dir)] # list of images
        faces = []      # list of all the faces
        ids = []        # list of all the ids
        for image in path:    # loop to get all the images from the folder path
            img = Image.open(image).convert('L')        # converting the images to GRAY SCALE
            imageNp = np.array(img, 'uint8')
            # storing the images as an array for converting into grid
            id1 = int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)     # adding the faces into faces list
            ids.append(id1)          # adding the id1 into the ids list
            cv2.imshow("Training Data", imageNp)  # 1 param winname and 2 param is image to be shown
            if cv2.waitKey(1) == 13:
                return
        ids = np.array(ids)  # converting into numpy array

        # ========== TRAINING CLASSIFIER =========
        clf = cv2.face.LBPHFaceRecognizer_create()   # declaring the lbph algorithm
        clf.train(faces, ids)
        clf.write("classifier.xml")# training the faces and ids
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Dataset Trained Successfully")
            
            
