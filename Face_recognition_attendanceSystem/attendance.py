from cProfile import label
from cgitb import text
import imp
from importlib.resources import contents, path
from logging import root
from multiprocessing import parent_process
from re import I
from select import select
from tkinter import *
from tkinter import ttk
from turtle import title, width
from unicodedata import name
from PIL import Image, ImageTk
from matplotlib.pyplot import clf, gray
from pip import main
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np




mydata = []
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
    # ================== varaibles ===================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        
        
    # picture 1
        img1 = Image.open(r"Pictures\3.jpeg")
        img1 = img1.resize((800, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=800, height=200)
        # picture2
        img2 = Image.open(r"Pictures\2.jpg")
        img2 = img2.resize((800, 200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=800, y=0, width=800, height=200)
        
        
        # bg img
        img4 = Image.open(r"Pictures\2.jpg")
        img4 = img4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=200, width=1530, height=710)

        
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white",
                          fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)
        
        
        

        # left label frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)
        
        img_left = Image.open(r"D:\DoAnChuyenNganh\Pictures\student.png")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)
        
        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=720, height=370)
        
        # khung Label entry
        
        
            #Department
        dep_label = Label(left_inside_frame, text="Môn học:", font=("times new roman", 11, "bold"), bg="white")
        dep_label.grid(row=1, column=2)

        atten_dep = ttk.Entry(left_inside_frame, textvariable=self.var_atten_dep , width=22,  font=("times new roman", 11, "bold"))
        atten_dep.grid(row=1, column=3, pady=8)
           
            #Roll
        rollLabel_label = Label(left_inside_frame, text="Vai trò:", font=("times new roman", 11, "bold"),
                                  bg="white")
        rollLabel_label.grid(row=0, column=2, padx=4, pady=8)

        atten_roll = ttk.Entry(left_inside_frame, textvariable= self.var_atten_roll , width=22, font=("times new roman", 11, "bold"))
        atten_roll.grid(row=0, column=3, pady=8)   
           
            # Attendance ID
        attendanceId_label = Label(left_inside_frame, text="AttendanceId:", font=("times new roman", 11, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame,  width=20, textvariable=self.var_atten_id , font=("times new roman", 11, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        
        
            #Name
        Name_label = Label(left_inside_frame, text="Tên Hs/Sv:", font=("times new roman", 11, "bold"),
                                  bg="white")
        Name_label.grid(row=1, column=0)

        atten_name = ttk.Entry(left_inside_frame, textvariable= self.var_atten_name ,width=22,  font=("times new roman", 11, "bold"))
        atten_name.grid(row=1, column=1, pady=8)
        
            
        
            #time
        
        time_label = Label(left_inside_frame, text="Thời gian:", font=("times new roman", 11, "bold"), bg="white")
        time_label.grid(row=2, column=0)

        atten_time = ttk.Entry(left_inside_frame, textvariable= self.var_atten_time ,width=22,  font=("times new roman", 11, "bold"))
        atten_time.grid(row=2, column=1, pady=8)
        
            #Date
        datelabel = Label(left_inside_frame, text="Ngày:", font=("times new roman", 11, "bold"), bg="white")
        datelabel.grid(row=2, column=2)

        atten_date = ttk.Entry(left_inside_frame, textvariable= self.var_atten_date , width=22,  font=("times new roman", 11, "bold"))
        atten_date.grid(row=2, column=3, pady=8)

            #Attendance
        attendanceLabel = Label(left_inside_frame, text=" Trạng thái:", font=("times new roman", 11, "bold"), bg="white")
        attendanceLabel.grid(row=3, column=0)
        
        self.atten_status = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance ,width=20, font=("times new roman", 11, "bold"), state="readonly")
        self.atten_status["values"] = ("Trạng thái","Có mặt","Vắng mặt")
        self.atten_status.grid(row=3, column=1,pady=8)
        self.atten_status.current(0)
        
        
        # button frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=715, height=35)

        save_btn = Button(btn_frame, text="Nhập file",command= self.importCsv , width=17, font=("times new roman", 13, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Xuất file", command=self.exportCsv,width=17, font=("times new roman", 13, "bold"), bg="blue",
                            fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Cập nhật" ,width=17, font=("times new roman", 13, "bold"), bg="blue",
                            fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command= self.reset_data ,width=17, font=("times new roman", 13, "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=0, column=3)
        

        
        
        # Right label frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=455)
    

        # ========== Scroll bar ==============
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable =  ttk.Treeview(table_frame, column =("department", "roll", "id", "name","time","date","attendance"),xscrollcommand=scroll_x.set, yscrollcommand= scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        
        self.AttendanceReportTable.heading("department", text="Môn học")
        self.AttendanceReportTable.heading("roll", text="Vai trò")
        self.AttendanceReportTable.heading("id", text="Mã số")        
        self.AttendanceReportTable.heading("name", text="Tên") 
        self.AttendanceReportTable.heading("time", text="Thời gian")
        self.AttendanceReportTable.heading("date", text="Ngày")
        self.AttendanceReportTable.heading("attendance", text="Điểm danh")
        
        self.AttendanceReportTable["show"] = "headings"
        
        
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("name", width=100)    
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    # =========== Tìm data ==============
    
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
                self.AttendanceReportTable.insert("", END, values=i)
    
    # Import Csv/ Nhập file
    
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir = os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*csv"), ("ALl File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
        
    # Export Csv/ Xuất file
    def exportCsv(self):
        try:
            if len(mydata) <1:
                messagebox.showerror("No Data", "Không có dữ liệu để xuất ra", parent= self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir = os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*csv"), ("ALl File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="" ) as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", " Dữ liệu của bạn được xuất tới "+ os.path.basename(fln)+" thành công")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}", parent = self.root)
            
    def get_cursor(self, event = ""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_dep.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_id.set(rows[2])
        self.var_atten_name.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])    
        self.var_atten_attendance.set(rows[6])    
        
    # ========Reset data =======
    def reset_data(self):
        self.var_atten_dep.set("")
        self.var_atten_roll.set("")
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")    
        self.var_atten_attendance.set("")   
    
    
    
        
            
            
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()    