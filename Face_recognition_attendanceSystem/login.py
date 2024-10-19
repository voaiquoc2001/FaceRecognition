from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


def main():
    win= Tk()
    app=Login_Window(win)
    win.mainloop()




class Login_Window:
    
    
    
    
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.new_window=Toplevel()
        
        self.bg = ImageTk.PhotoImage(file= r"D:\DoAnChuyenNganh\codeDA\Pictures\background-đẹp-3-1.jpg")
        
        lbl_bg= Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0 ,relwidth = 1, relheight = 1)
        
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y= 170, width=340, height=450)

        img1 = Image.open(r"D:\DoAnChuyenNganh\codeDA\Pictures\login.png")
        img1 = img1.resize((100,100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg = "black", borderwidth=0)
        lblimg1.place(x=730, y =175, width=100 , height=100 )        
        
        get_str = Label(frame, text="Get Started", font=("times new roman", 20,"bold"),fg= "white",bg="black")
        get_str.place(x=95,y =100)

        # Label
        username=lbl=Label(frame, text="Username",font=("times new roman", 15,"bold"),fg= "white",bg="black")
        username.place(x=70, y = 155)

        self.txtuser =  ttk.Entry(frame,font=("times new roman", 15,"bold") )
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame, text="Password",font=("times new roman", 15,"bold"),fg= "white",bg="black")
        password.place(x=70, y = 225)

        self.txtpass =  ttk.Entry(frame,font=("times new roman", 15,"bold") )
        self.txtpass.place(x=40,y=250,width=270)

        
        # Icon image
        img2 = Image.open(r"D:\DoAnChuyenNganh\codeDA\Pictures\login1.jpg")
        img2 = img2.resize((25,25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg = "black", borderwidth=0)
        lblimg2.place(x=650, y =323, width=25 , height=25 )  


        img3 = Image.open(r"D:\DoAnChuyenNganh\codeDA\Pictures\lock.png")
        img3 = img3.resize((25,25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg = "black", borderwidth=0)
        lblimg3.place(x=650, y =394, width=25 , height=25 )
        
        # Login button
        loginbtn= Button(frame,command=self.login, text= "Login", font=("times new roman", 15,"bold"), bd=3, relief=RIDGE, fg= "white", bg= "red", activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y= 300,width=120, height=35)

        # register Button
        registerbtn= Button(frame,command= self.register_window, text= "New User Register", font=("times new roman", 10,"bold"),borderwidth= 0,fg= "white", bg= "black", activeforeground="white",activebackground="blue")
        registerbtn.place(x=15,y= 350,width=160)

        # Forget Button
        loginbtn= Button(frame,command= self.forgot_password_window ,text= "Forget Password", font=("times new roman", 10,"bold"), bd=3, borderwidth= 0,fg= "white", bg= "black", activeforeground="white",activebackground="blue")
        loginbtn.place(x=10,y= 370,width=160)
        
    def register_window(self):
        self.new_window= Toplevel(self.root)
        self.app = Register(self.new_window)   

    def login(self):
        if self.txtuser.get() =="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "all fiekd required")
        elif self.txtuser.get()=="Quoc" and self.txtpass.get()=="123456":
            messagebox.showinfo("Success", "Login Success")
        else:
            conn = mysql.connector.connect(host= "localhost",user="root",password="123456",database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.var_email.get(),
                                                                                        self.var_pass.get()
                                                                                        ))

            row = my_cursor.fetchone()
            if row!= None:
                messagebox.showerror("Error","Ivalid Username & password")
            else:
                open_main= messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window = Toplevel(self.new_window)
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
                conn.commit()
                conn.close()
            
                
    # ========== Reset Password ===============
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(host= "localhost",user="root",password="123456",database="mydata")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                self.root2.destroy()
                
    
    # =========== Forgot Password ==============
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email to reset Password!")
        else:
            conn = mysql.connector.connect(host= "localhost",user="root",password="123456",database="mydata")
            mycursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,(value),)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)

                security_Q= Label(self.root2, text= "Select Security Question", font= ("times new roman",15, "bold"),bg="white", fg="black")
                security_Q.place(x=50, y=80)
        
                self.combo_security_Q= ttk.Combobox(self.root2  , font= ("times new roman",15, "bold"),state="readonly" )
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your friend name", "Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
                

                security_A=Label(self.root2, text= "Security Answer", font= ("times new roman",15, "bold"),bg="white", fg="black")
                security_A.place(x=50,y=150)
                
                self.txt_security= ttk.Entry(self.root2, font= ("times new roman",15))
                self.txt_security.place(x=50, y=180,width=250)
                
                
                new_password=Label(self.root2, text= "New Password", font= ("times new roman",15, "bold"),bg="white", fg="black")
                new_password.place(x=50,y=220)
                
                self.txt_newpass= ttk.Entry(self.root2, font= ("times new roman",15))
                self.txt_newpass.place(x=50, y=250,width=250)
                
                # ==== Login Btn =======
                
                btn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                btn.place(x=100,y=290)
            
            
            
            
            
class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        # ================ variable ==============
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        


        # ========= Bg image =========
        self.bg = ImageTk.PhotoImage(file=r"D:\DoAnChuyenNganh\codeDA\Pictures\Re.jpg")

        bg_lbl=Label(self.root, image=self.bg)
        bg_lbl.place(x=0,y=0, relwidth=1, relheight=1)
        
        # =========== Left image =========
        self.bg1 = ImageTk.PhotoImage(file=r"D:\DoAnChuyenNganh\codeDA\Pictures\regs1.jpg")

        left_lbl=Label(self.root, image=self.bg1)
        left_lbl.place(x=50,y=100, width=470, height=550)

        frame =Frame(self.root, bg="white")
        frame.place(x=520,y=100,width=800, height=550)
        
        register_lbl= Label(frame, text= "REGISTER HERE", font= ("times new roman",20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)


        # ============= label and entry ===============
        
            # ====== Row 1=======
        fname= Label(frame, text= "First Name", font= ("times new roman",15, "bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry = ttk.Entry(frame ,textvariable= self.var_fname ,font= ("times new roman",15, "bold"))
        fname_entry.place(x=50, y=130,width=250)

        l_name= Label(frame, text= "Last Name", font= ("times new roman",15, "bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)
        
        self.txt_lname= ttk.Entry(frame,textvariable= self.var_lname ,font= ("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)
        
            # ========= Row 2 =======
        contact= Label(frame, text= "Contact No", font= ("times new roman",15, "bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact = ttk.Entry(frame, textvariable= self.var_contact,font= ("times new roman",15))
        self.txt_contact.place(x=50, y=200,width=250)

        email= Label(frame, text= "Email", font= ("times new roman",15, "bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        
        self.txt_email= ttk.Entry(frame,textvariable= self.var_email ,font= ("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)
        
        
            # ========= Row 3 ========
        
        security_Q= Label(frame, text= "Select Security Question", font= ("times new roman",15, "bold"),bg="white", fg="black")
        security_Q.place(x=50, y=240)
        
        
        
        
        self.combo_security_Q= ttk.Combobox(frame ,textvariable= self.var_securityQ , font= ("times new roman",15, "bold"),state="readonly" )
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your friend name", "Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        
        
        security_A=Label(frame, text= "Security Answer", font= ("times new roman",15, "bold"),bg="white", fg="black")
        security_A.place(x=370,y=240)
        
        self.txt_security= ttk.Entry(frame, textvariable= self.var_securityA,font= ("times new roman",15))
        self.txt_security.place(x=370, y=270,width=250)
        
        
        
            # ========= Row 4 ========
        
        pswd = Label(frame, text= "Password", font= ("times new roman",15, "bold"),bg="white", fg="black")
        pswd.place(x=50,y=310)
        
        self.txt_pswd = ttk.Entry(frame, textvariable= self.var_pass , font= ("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pwsd = Label(frame, text= "Confirm Password", font= ("times new roman",15, "bold"),bg="white", fg="black")
        confirm_pwsd.place(x=370, y=310)
        
        self.txt_confirm_pswd = ttk.Entry(frame,textvariable= self.var_confpass ,font= ("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        
        
            # ============ check button =============
        self.var_check= IntVar()
        checkbtn= Checkbutton(frame , variable= self.var_check ,text="I Agree The Terms & Conditions",font= ("times new roman",12, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)
        
            # ============= Buttons ============
        img = Image.open(r"D:\DoAnChuyenNganh\codeDA\Pictures\btnre.png")
        img= img.resize((200,50), Image.ANTIALIAS)
        self.photoimage= ImageTk.PhotoImage(img)
        b1 = Button(frame,image=self.photoimage , command = self.register_data , borderwidth=0,cursor="hand2",font= ("times new roman",15, "bold"),bg="white")
        b1.place(x=40, y=420, width=200)
        
        
        img1 = Image.open(r"D:\DoAnChuyenNganh\codeDA\Pictures\loginnow.jpg")
        img1= img1.resize((200,45), Image.ANTIALIAS)
        self.photoimage1= ImageTk.PhotoImage(img1)
        b1 = Button(frame,image=self.photoimage1,command= self.return_login ,borderwidth=0,cursor="hand2",font= ("times new roman",15, "bold"),bg="white")
        b1.place(x=330, y=420, width=200)
        
        
    # ============== Function declaration ==================
    
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error", "All fileds are required")
        elif self.var_pass.get()!= self.var_confpass.get():
            messagebox.showerror("Error", "Password & confirm password must same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        else:
            conn = mysql.connector.connect(host= "localhost",user="root",password="123456",database="mydata")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value= (self.var_email.get())
            my_cursor.execute(query,(value,))
            row = my_cursor.fetchone()
            if row!= None:
                messagebox.showerror("Error","User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get(),
                                                                                    ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Success!")

    def return_login(self):
        self.root.destroy()






if __name__ == "__main__":
    main()