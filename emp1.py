from tkinter import *
from PIL import Image,ImageTk
import os
import empform
import departmentform
import view
from tkinter import messagebox

class emp_1:
    def __init__(self,window):
        self.wn=window
        self.wn.title('Employee Management')
        self.wn.geometry('900x700+300+0')
        self.imgbg='pic1.jpg'
        self.img=ImageTk.PhotoImage(Image.open(self.imgbg))
        self.img_label=Label(self.wn,image=self.img,bd=0).place(x=0,y=0)

        ###frame
        self.frame1=Frame(self.wn)
        self.frame1.configure(width=400,height=500,background='white')
        self.frame1.place(x=280,y=100)

        
        #####heading
        self.heading=Label(self.frame1,text='WELCOME',font=('aerial',30,'bold'),bg='white',fg='dark cyan')
        self.heading.place(x=0,y=50,relwidth=1)

        ###########button
        self.btn_employee=Button(self.frame1,text='Employee',font=('aerial',25,'bold'),fg='white',bg='purple',width=15,command=self.func_employee)
        self.btn_employee.place(x=50,y=120)

        self.btn_department=Button(self.frame1,text='Department',font=('aerial',25,'bold'),fg='white',bg='purple',width=15,command=self.func_department)
        self.btn_department.place(x=50,y=200)

        self.btn_view=Button(self.frame1,text='View Details',font=('aerial',25,'bold'),fg='white',bg='purple',width=15,command=self.func_view)
        self.btn_view.place(x=50,y=280)

        self.btn_exit=Button(self.frame1,text='EXIT',font=('aerial',15,'underline','italic'),bg='white',fg='red',command=self.func_exit)
        self.btn_exit.place(x=240,y=425)
    
    def func_employee(self):
        self.wn1=Toplevel()
        empform.emp_form(self.wn1)
    def func_department(self):
        self.wn1=Toplevel()
        departmentform.department_form(self.wn1)
    def func_exit(self):
        exit1=messagebox.askyesno('Validate','Do you want to exit?')
        if exit1>0:
            self.wn.destroy()
    def func_view(self):
        self.wn1=Toplevel()
        view.view_class(self.wn1)


    

# wn=Tk()
# emp_1(wn)
# wn.mainloop()