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



class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")
        
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white",
                          fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        # Ảnh trên
        img_top = Image.open(r"Pictures\student.png")
        img_top = img_top.resize((1530, 720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)
        
        dev_lbl = Label(f_lbl, text="Email: voaiquoc2001@gmail.com ", font=("times new roman", 20, "bold"), fg="blue"
                          )
        dev_lbl.place(x=550, y=260)
        
        dev_lbl = Label(f_lbl, text="Phone: 0967 -784 -548", font=("times new roman", 20, "bold"), fg="blue"
                          )
        dev_lbl.place(x=550, y=300)
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()