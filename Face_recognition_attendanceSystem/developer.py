from cProfile import label
from cgitb import text
import imp
from logging import root
from multiprocessing import parent_process
from tkinter import *
from tkinter import ttk
from turtle import title, width
from unicodedata import name
from PIL import Image, ImageTk
from pip import main
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")
        
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white",
                          fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        # Ảnh trên
        img_top = Image.open(r"Pictures\student.png")
        img_top = img_top.resize((1530, 720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        # Frame
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=600)
        
        img_top1 = Image.open(r"Pictures\student.png")
        img_top1 = img_top.resize((200,200), Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=300, y=0, width=200, height=200)
        
        # Developer info
        
        dev_lbl = Label(main_frame, text="Software written by ", font=("times new roman", 20, "bold"), bg="white"
                          )
        dev_lbl.place(x=0, y=0)
        dev_lbl = Label(main_frame, text="Quoc, Hai, Dai ", font=("times new roman", 20, "bold"), bg="white"
                          )
        dev_lbl.place(x=0, y=40)

       
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()