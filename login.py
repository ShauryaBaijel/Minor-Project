import os
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import pymysql


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #============Background=========
        self.bg_img=Image.open("images/b2.jpg")
        self.bg_img=self.bg_img.resize((1350,700),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        bg = Label(self.root, image=self.bg_img).place(x=0, y=0, relwidth=1, relheight=1)

        # =============Frames=========
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)

        title = Label(login_frame, text="LOGIN HERE", font=("Castellar", 30, "bold"), bg="white", fg="#4254f5").place(x=250, y=50)

        email=Label(login_frame, text="EMAIL ADDRESS", font=("Castellar", 18, "bold"), bg="white", fg="#53ad6b").place(x=250, y=150)
        self.txt_email=Entry(login_frame,font=("times new roman", 15, "bold"), bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)

        password=Label(login_frame, text="PASSWORD", font=("Castellar", 18, "bold"), bg="white", fg="#53ad6b").place(x=250, y=250)
        self.txt_password=Entry(login_frame,font=("times new roman", 15, "bold"), bg="lightgray")
        self.txt_password.place(x=250,y=280,width=350,height=35)

        btn_reg=Button(login_frame,text="REGISTER (New Account)",command=self.regester_window,font=("times new roman", 13,"bold"),bg="white",bd=0,fg="#B00857",cursor="hand2").place(x=246,y=320)

        btn_login=Button(login_frame,text="LOGIN",command=self.login,font=("times new roman", 18),bg="#4254f5",bd=0,fg="white",cursor="hand2").place(x=250,y=380,width=180,height=40)

        btn_forget=Button(login_frame, text="Forget Password?", command=self.forget_password_window, font=("times new roman", 13), bg="white", bd=0, fg="red", cursor="hand2").place(x=470, y=320)


        #===================login side image============
        self.left = Image.open("images/side2.png")
        self.left = self.left.resize((350, 450), Image.ANTIALIAS)
        self.left = ImageTk.PhotoImage(self.left)
        left = Label(self.root, image=self.left).place(x=90, y=125, width=350, height=450)


    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_password.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_email.delete(0,END)




    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_password.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root2)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=?", (self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please Select The 'CORRECT' Security Question / Answer",parent=self.root2)
                else:
                    cur.execute("update employee set password=? where email=?",(self.txt_new_password.get(), self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("SUCCESS","Your Password Has Been Reset, Please Login With New Password",parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due To: {str(es)}", parent=self.root2)


    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please Enter The EMAIL Address To Reset Your Password",parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Please Enter 'VALID' EMAIL Address To Reset Your Password",parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x420+500+155")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    self.root2.config(bg="#d6ffff")

                    t = Label(self.root2, text="FORGET PASSWORD ?", font=("times new roman", 20, "bold"), bg="white",fg="#0026ff").place(x=0, y=10, relwidth=1)

                    # =============Forget Pass===============
                    question = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"),bg="#d6ffff",fg="#1e2c63").place(x=50, y=100)

                    self.cmb_quest = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly",justify=CENTER)
                    self.cmb_quest['values'] = ("Select", "Your 1st Pet Name", "Your Birth Place", "Your Best Friend Name")
                    self.cmb_quest.place(x=50, y=130, width=250)
                    self.cmb_quest.current(0)

                    answer = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="#d6ffff",fg="#1e2c63").place(x=50, y=180)
                    self.txt_answer = Entry(self.root2, font=("times new roman", 15, "bold"), bg="white")
                    self.txt_answer.place(x=50, y=210, width=250)

                    new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"),bg="#d6ffff", fg="#1e2c63").place(x=50, y=260)
                    self.txt_new_password = Entry(self.root2, font=("times new roman", 15, "bold"), bg="white")
                    self.txt_new_password.place(x=50, y=290, width=250)

                    btn_change_password = Button(self.root2, text="Reset Password",font=("times new roman", 15, "bold"), bg="#4254f5", fg="white",cursor="hand2",command=self.forget_password).place(x=100, y=340)

            except Exception as es:
                messagebox.showerror("Error", f"Error Due To: {str(es)}", parent=self.root)



    def regester_window(self):
        self.root.destroy()
        os.system("python register.py")

    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Username Or Password", parent=self.root)
                else:
                    messagebox.showinfo("Success", "WELCOME", parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due To: {str(es)}", parent=self.root)






root = Tk()
obj = login_window(root)
root.mainloop()
