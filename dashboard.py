import os
from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import *
from time import *
from math import *
import sqlite3
from report import ReportClass
from course import CourseClass
from student import StudentClass
from result import ResultClass
from tkinter import messagebox,ttk

class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Managment System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")


        #====ICONS====
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")


        #====TITLE====
        title=Label(self.root,text="STUDENT RESULT MANAGEMENT SYSTEM",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)


        #====MENU====
        M_Frame=LabelFrame(self.root,text=("MENUS"),font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)

        btn_course=Button(M_Frame,text="COURSE",font=("goudy old style",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="STUDENT",font=("goudy old style",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="RESULT",font=("goudy old style",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="VIEW STUDENT RESULTS",font=("goudy old style",12,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_logout=Button(M_Frame,text="LOGOUT",font=("goudy old style",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)
        btn_exit=Button(M_Frame,text="EXIT",font=("goudy old style",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1120,y=5,width=200,height=40)


        #====Content Window====
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=165,width=920,height=350)


        #=====UPDATE DATAILS====
        self.lbl_course=Label(self.root,text="TOTAL COURSES\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="yellow")
        self.lbl_course.place(x=400,y=530,width=300,height=100)
        self.lbl_student=Label(self.root,text="TOTAL STUDENTS\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="yellow")
        self.lbl_student.place(x=710,y=530,width=300,height=100)
        self.lbl_result=Label(self.root,text="TOTAL RESULTS\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="yellow")
        self.lbl_result.place(x=1020,y=530,width=300,height=100)

        #===========Clock=======
        self.lbl=Label(self.root,text="\nShaurya's Clock",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923")
        self.lbl.place(x=10,y=180,width=350,height=450)
        self.working()

        #====FOOTER====
        footer=Label(self.root,text="SRMS - STUDENT RESULT MANAGEMENT SYSTEM\nMADE BY - SHAURYA BAIJEL (05590202019)  BCA-5B ",font=("goudy old style",12,"italic"),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

        self.update_details()


    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)


    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ResultClass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ReportClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do You Really Want To Logout ?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op = messagebox.askyesno("Confirm", "Do You Really Want To EXIT ?", parent=self.root)
        if op == True:
            self.root.destroy()


    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        bg=Image.open("images/c.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        draw.line((origin,200+80*sin(radians(min_)), 200-80 * cos(radians(min_))),fill="white",width=3)
        draw.line((origin, 200+100*sin(radians(sec_)), 200-100 * cos(radians(sec_))), fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="black")
        clock.save("images/clock_new.png")

    def working(self):
        h=int(datetime.now().time().hour)
        m=int(datetime.now().time().minute)
        s=int(datetime.now().time().second)

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360

        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)


    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"TOTAL COURSES\n[ {str(len(cr))} ]")

            cur.execute("select * from student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"TOTAL STUDENTS\n[ {str(len(cr))} ]")

            cur.execute("select * from result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"TOTAL RESULTS\n[ {str(len(cr))} ]")
            self.lbl_result.after(200, self.update_details)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


#====CONNECTION CLOSE====
if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
