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



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")

        # ==========variable =================================
        # ========== dep","course", "year", "sem", "id", "name", "adr", "gender", "email", "phone" "roll"====
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_adr = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_roll = StringVar()
        self.var_radio1 = StringVar()


        # picture 1
        img1 = Image.open(r"D:\DoAnChuyenNganh\Pictures\3.jpeg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=130)
        # picture2
        img2 = Image.open(r"D:\DoAnChuyenNganh\Pictures\2.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # picture3
        img3 = Image.open(r"D:\DoAnChuyenNganh\Pictures\4.jpg")
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # picture4
        img4 = Image.open(r"D:\DoAnChuyenNganh\Pictures\2.jpg")
        img4 = img4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white",
                          fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)

        # left label frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"D:\DoAnChuyenNganh\Pictures\student.png")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # current course

        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current course information",
                                          font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=150)

        # Department

        dep_label = Label(current_course_frame, text="Môn học", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 13, "bold"),
                                 state="readonly")
        dep_combo["values"] = ("Chon mon hoc", "QTDACNTT", "Lập trình Python", "Web server", "Đồ án", "Thiết kế PM")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Khoá học", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course,
                                    font=("times new roman", 13, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Chọn khoá học", "K41", "K42", "K43", "K44")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Năm", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,
                                  font=("times new roman", 13, "bold"), state="readonly",
                                  width=20)
        year_combo["values"] = ("Chọn năm", "2019-20", "2020-21", "2021-22", "2022-23")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester

        Semester_label = Label(current_course_frame, text="Chọn học kỳ", font=("times new roman", 13, "bold"),
                               bg="white")
        Semester_label.grid(row=1, column=2, padx=10, sticky=W)

        Semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem,
                                      font=("times new roman", 13, "bold"), state="readonly",
                                      width=20)
        Semester_combo["values"] = ("Chọn học kỳ", "Học kỳ 1", "Học kỳ 2")
        Semester_combo.current(0)
        Semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student information

        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information",
                                         font=("times new roman", 12, "bold"))
        class_Student_frame.place(x=5, y=250, width=720, height=300)

        # Mã SV

        studentId_label = Label(class_Student_frame, text="Mã Hs/Sv", font=("times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(class_Student_frame, textvariable=self.var_id, width=20,
                                    font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Họ tên SV
        studentName_label = Label(class_Student_frame, text="Tên Hs/Sv", font=("times new roman", 13, "bold"),
                                  bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame, textvariable=self.var_name, width=20,
                                      font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Địa chỉ
        address_label = Label(class_Student_frame, text="Địa chỉ", font=("times new roman", 13, "bold"),
                              bg="white")
        address_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_Student_frame, textvariable=self.var_adr, width=20,
                                  font=("times new roman", 13, "bold"))
        address_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Giới tính

        gender_label = Label(class_Student_frame, text="Giới tính", font=("times new roman", 13, "bold"),
                             bg="white")
        gender_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        #gender_entry = ttk.Entry(class_Student_frame, textvariable=self.var_gender, width=20,
                                # font=("times new roman", 13, "bold"))
        #gender_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_gender,
                                  font=("times new roman", 13, "bold"), state="readonly",
                                  width=18)
        gender_combo["values"] = ("Chọn giới tính", "Nam", "Nữ", "Khác")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)


        # Email

        email_label = Label(class_Student_frame, text="Email", font=("times new roman", 13, "bold"),
                            bg="white")
        email_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_Student_frame, textvariable=self.var_email, width=20,
                                font=("times new roman", 13, "bold"))
        email_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Phone

        phone_label = Label(class_Student_frame, text="SĐT", font=("times new roman", 13, "bold"),
                            bg="white")
        phone_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_Student_frame, textvariable=self.var_phone, width=20,
                                font=("times new roman", 13, "bold"))
        phone_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Vai trò trong lớp học

        roll_no_label = Label(class_Student_frame, text="Chức vụ", font=("times new roman", 13, "bold"),
                              bg="white")
        roll_no_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_Student_frame, textvariable=self.var_roll, width=20,
                                  font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # radio Buttons

        radiobtn1 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="Take Photo Sample",
                                    value="Yes")
        radiobtn1.grid(row=4, column=0)

        radiobtn2 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="No Photo Sample",
                                    value="No")
        radiobtn2.grid(row=4, column=1)

        # buttons frame
        btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=180, width=715, height=35)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=("times new roman", 13, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=17, font=("times new roman", 13, "bold"), bg="blue",
                            fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=17, font=("times new roman", 13, "bold"), bg="blue",
                            fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command= self.reset_data,width=17, font=("times new roman", 13, "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=215, width=715, height=35)

        take_photo_btn = Button(btn_frame1,command=self.generate_dataset, text="Take Photo Sample", width=35, font=("times new roman", 13, "bold"),
                                bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=35,
                                  font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)

        # Right label frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)

        img_right = Image.open(r"D:\DoAnChuyenNganh\Pictures\student.png")
        img_right = img_right.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # ===== Search System =====
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                  font=("times new roman", 13, "bold"))
        Search_frame.place(x=5, y=135, width=710, height=70)

        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 13, "bold"),
                             bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 13, "bold"), state="readonly", width=20)
        search_combo["values"] = ("Chọn...", "Tên Hs/Sv", "Mã Hs/Sv")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(Search_frame, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(Search_frame, text="Search", width=11, font=("times new roman", 12, "bold"), bg="blue",
                            fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(Search_frame, text="Show All", width=11, font=("times new roman", 12, "bold"), bg="blue",
                             fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)

        # ====== Table Farme =======

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=(
        "dep", "course", "year", "sem", "id", "name", "adr", "gender", "email", "phone", "roll", "photo"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Môn học")
        self.student_table.heading("course", text="Khoá học")
        self.student_table.heading("year", text="Năm")
        self.student_table.heading("sem", text="Học kỳ")
        self.student_table.heading("id", text="Mã Hs/Sv")
        self.student_table.heading("name", text="Tên Hs/Sv")
        self.student_table.heading("adr", text="Địa chỉ")
        self.student_table.heading("gender", text="Giới tính")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Số điện thoại")
        self.student_table.heading("roll", text="Vai trò")
        self.student_table.heading("photo", text="Tình trạng mẫu ảnh")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("adr", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ===========Functions  decrations =========
    def add_data(self):
        if self.var_dep.get() == " Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", " All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username = "root", password ="123456", database ="face_recognizer" )
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_adr.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_roll.get(),
                    self.var_radio1.get()


                    )
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Đã xong", "Dữ liệu sinh viên/ học sinh đã được thêm", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent = self.root)



    #=========== fetch data =============
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="123456", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data :
                self.student_table.insert("", END, values= i)
            conn.commit()
        conn.close()

    #============= get cursor ============
    def get_cursor(self, event = ""):
        cursor_focus =  self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_adr.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_roll.set(data[10]),
        self.var_radio1.set(data[11])


    #======= Update ===========
    def update_data(self):
        if self.var_dep.get() == " Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", " All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", " Bạn muốn cập nhật?", parent = self.root)
                if Update >0 :
                    conn = mysql.connector.connect(host="localhost", username="root", password="123456", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set dep=%s, course=%s,Year=%s,Sem=%s,Name=%s,Address=%s,Gender=%s,Email=%s,SDT=%s,Roll=%s,Photo_Sample=%s where Student_Id=%s", (

                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_adr.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_roll.get(),
                        self.var_radio1.get(),
                        self.var_id.get(),


                            )
                        )
                else:
                    if not Update:
                        return
                messagebox.showinfo("Thành công", " Thông tin đã được cập nhật", parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi", f"Due to :{str(es)}", parent = self.root)

    #===========    delete Function ====
    def delete_data(self):
        if self.var_id.get() =="":
            messagebox.showerror("Error", "Student id must be required", parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete page", "Bạn muốn xoá Student này?", parent = self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="123456",database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_Id=%s"
                    val= (self.var_id.get(), )
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", " Đã xoá Student này", parent = self.root)
            except Exception as es:
                messagebox.showerror("Lỗi", f"Due to :{str(es)}", parent = self.root)


    #==== Reset Function =====
    def reset_data(self):
        self.var_dep.set("Chọn môn học")
        self.var_course.set("Khoá học")
        self.var_year.set("Chọn năm")
        self.var_sem.set("Chọn học kỳ")
        self.var_id.set("")
        self.var_name.set("")
        self.var_adr.set("")
        self.var_gender.set("Chọn giới tính")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_roll.set("")
        self.var_radio1.set("")


    # ===== Chụp ảnh =======

    def generate_dataset(self):
        if self.var_dep.get() == " Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", " All Fields are required", parent=self.root)
        else:
            try:

                conn = mysql.connector.connect(host="localhost", username="root", password="123456", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult =  my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id +=1
                my_cursor.execute("update student set dep=%s, course=%s,Year=%s,Sem=%s,Name=%s,Address=%s,Gender=%s,Email=%s,SDT=%s,Roll=%s,Photo_Sample=%s where Student_Id=%s",
                    (

                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_adr.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_roll.get(),
                        self.var_radio1.get(),
                        self.var_id.get() == id+1
                        

                    )
                )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ================ Load  predifiend data on face frontals from Opencv ============
                sampleNum=0
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    
                    gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3,5)
                    
                    #scaling factor = 1.3
                    #minium neighbor = 5

                    for (x,y,w,h) in faces:
                        #cv2.rectangle(img, (x,y), (x+w, y +h), (255,0,0),2)
                        face_cropped = img[y:y+h,x:x+w]
                        return  face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id +=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGRA2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".png"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) ==50:
                        break
                cap.release() 
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets complete!!!")
            except Exception as es:
                messagebox.showerror("Lỗi", f"Due to :{str(es)}", parent = self.root)
                

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()