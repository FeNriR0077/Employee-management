from tkinter import *
from tkinter import messagebox
from employeeform import *
import os
from PIL import Image,ImageTk
import check_submit1
import emp1

class employeelogin_form:
    def __init__(self,window):
        self.wn=window
        self.wn.title('Employee Form')
        self.wn.geometry('900x700+300+0')
        self.imgbg='pic1.jpg'
        self.img=ImageTk.PhotoImage(Image.open(self.imgbg))
        self.img_label=Label(self.wn,image=self.img,bd=0).place(x=0,y=0)

        ###frame
        self.frame1=Frame(self.wn)
        self.frame1.configure(width=400,height=500,background='white')
        self.frame1.place(x=280,y=100)

        
        #####heading
        self.heading=Label(self.frame1,text='Login Page',font=('aerial',30,'bold'),bg='white',fg='dark cyan')
        self.heading.place(x=0,y=50,relwidth=1)

        self.heading1=Label(self.frame1,text='Enter your details below to continue',font=('aerial',12,'underline','italic'),bg='white',fg='light grey')
        self.heading1.place(x=0,y=110,relwidth=1)

        #####label and entry

        self.lb_username=Label(self.frame1,text='Username ',font=('aerial',15),bg='white',fg='orange')
        self.lb_username.place(x=30,y=170)

        self.en_username=Entry(self.frame1,font=('aerial',20),fg='black',width=15,bd=3)
        self.en_username.place(x=30,y=210)

        self.lb_password=Label(self.frame1,text='Password ',font=('aerial',15),bg='white',fg='orange')
        self.lb_password.place(x=30,y=270)

        self.en_password=Entry(self.frame1,font=('aerial',20),fg='black',width=15,bd=3,show='*')
        self.en_password.place(x=30,y=310)

        self.lb_register=Label(self.frame1,text="Have'nt registered yet?",font=('aerial',15),bg='white',fg='orange')
        self.lb_register.place(x=30,y=430)

        #########button

        self.btn_login=Button(self.frame1,text='Login',font=('aerial',15,'bold'),fg='white',bg='purple',width=15,command=self.func_login)
        self.btn_login.place(x=105,y=380)

        self.btn_register=Button(self.frame1,text='click here',font=('aerial',15,'underline','italic'),relief=FLAT,bg='white',fg='purple',command=self.func_register)
        self.btn_register.place(x=240,y=425)
    

    def func_register(self):
        self.wn1=Toplevel()
        employee_form(self.wn1)

    def func_login(self):
        check_submit1.sunmit1(self)
    


wn=Tk()
employeelogin_form(wn)
wn.mainloop()