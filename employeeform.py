from tkinter import *
import pickle
import os
from tkinter import messagebox
import check_submit
from PIL import Image,ImageTk
import re

class employee_form:
    def __init__(self, window):
        self.wn=window
        self.wn.geometry('900x700+300+0')
        self.wn.configure(background='white')
        self.wn.title('Register')

        def checkint(ent):
            if ent.isdigit():
                return True
            elif ent is '':
                return False
            else:
                return False
    
        #########Frame
        
        self.frame1=Frame(self.wn)
        self.frame1.configure(width=600,height=700,background='light yellow')
        self.frame1.place(x=0,y=0)
        self.frame2=Frame(self.wn,width=300,height=700,background='light blue')
        self.frame2.pack(side=RIGHT)

        #######image
        self.imgbg1='pic1.jpg'
        self.img1=ImageTk.PhotoImage(Image.open(self.imgbg1))
        self.img1_label=Label(self.frame2,image=self.img1,bd=0,height=700,width=600).place(x=0,y=0)

        ##########label and entry

        ##heading
        self.lb_heading=Label(self.wn,text='Register',font=('calibre',57,'bold'),bg='black',fg='dark cyan')
        self.lb_heading.place(x=600,y=0)

        ####name
        self.lb_name=Label(self.frame1,text='Full Name: ',font=('aerial',12,'bold'),bg='white',fg='blue')
        self.lb_name.place(x=20,y=0)

        self.en_name1=Entry(self.frame1,font=('aerial',20),fg='black',width=15)
        self.en_name1.place(x=20,y=30)

        self.en_name2=Entry(self.frame1,font=('aerial',20),fg='black',width=15)
        self.en_name2.place(x=300,y=30)

        #####address
        self.lb_address=Label(self.frame1,text='Address: ',font=('aerial',12,'bold'),bg='white',fg='blue')
        self.lb_address.place(x=20,y=80)

        self.en_address=Entry(self.frame1,font=('aerial',20),width=29)
        self.en_address.place(x=20,y=110)

        #####phoneno
        
        self.lb_phoneno=Label(self.frame1,text='Phone Number: ',font=('aerial',12,'bold'),bg='white',fg='blue')
        self.lb_phoneno.place(x=20,y=160)

        self.en_phoneno=Entry(self.frame1,font=('aerial',20),width=29)
        self.en_phoneno.place(x=20,y=190)


        ########age
        self.lb_age=Label(self.frame1,text='Age: ',font=('aerial',12,'bold'),bg='white',fg='blue')
        self.lb_age.place(x=20,y=240)

        self.en_age=Entry(self.frame1,font=('aerial',20),width=7)
        self.en_age.place(x=20,y=270)

        ######Email
        self.lb_email=Label(self.frame1,text='E-mail: ',font=('aerial',12,'bold'),bg='white',fg='blue')
        self.lb_email.place(x=150,y=240)

        self.en_email=Entry(self.frame1,font=('aerial',15),width=39)
        self.en_email.place(x=150,y=270)

        #######username
        self.lb_username=Label(self.frame1,text='Username: ',font=('aerial',12,'bold'),bg='white',fg='blue')
        self.lb_username.place(x=20,y=320)

        self.en_username=Entry(self.frame1,font=('aerial',20),width=29)
        self.en_username.place(x=20,y=350)

        ######password
        self.lb_password=Label(self.frame1,text='Password: ',font=('aerial',12,'bold'),bg='white',fg='blue')
        self.lb_password.place(x=20,y=400)

        self.en_password=Entry(self.frame1,font=('aerial',20),show='*',width=29)
        self.en_password.place(x=20,y=430)
        

        #######confirm password
        self.lb_confirm_password=Label(self.frame1,text='Confirm Password: ',font=('aerial',12,'bold'),bg='white',fg='blue')
        self.lb_confirm_password.place(x=20,y=480)

        self.en_confirm_password=Entry(self.frame1,font=('aerial',20),show='*',width=29)
        self.en_confirm_password.place(x=20,y=510)


        #########Openmenu


        #####gender
        l_gender=['Male','Female','Other']
        self.var=StringVar()
        self.var.set(l_gender[0])
        self.om_gender=OptionMenu(self.frame1,self.var,*l_gender)
        self.lb_gender=Label(self.frame1,text='Gender: ',font=('aerial',12,'bold'),bg='white',fg='blue')
        self.lb_gender.place(x=20,y=560)
        self.om_gender.place(x=120,y=560)

        #######date of birth
        month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
        day=[]
        for i in range(1,31):
            day.append(i)
        year=[]
        for j in range(1980,2021):
            year.append(j)
        
        self.lb_dob=Label(self.frame1,text='Date of Birth: ',font=('aerial',12,'bold'),bg='white',fg='blue')
        self.lb_dob.place(x=20,y=610)

        self.var1=StringVar()
        self.var2=StringVar()
        self.var3=StringVar()
        self.var1.set(day[0])
        self.var2.set(month[0])
        self.var3.set('2020')
        self.om_day=OptionMenu(self.wn,self.var1,*day)
        self.om_day.place(x=130,y=610)
        self.om_month=OptionMenu(self.wn,self.var2,*month)
        self.om_month.place(x=200,y=610)
        self.om_year=OptionMenu(self.wn,self.var3,*year)
        self.om_year.place(x=285,y=610)

        ###########button

        self.btn_submit=Button(self.wn,text='Submit',font=('aerial',15,'bold'),command=self.btn_submit)
        self.btn_submit.place(x=620,y=600)

        self.btn_reset=Button(self.wn,text='Reset',font=('aerial',15,'bold'),command=self.btn_reset)
        self.btn_reset.place(x=720,y=600)

        self.btn_login=Button(self.wn,text='Login',font=('aerial',15,'bold'),command=self.func_login)
        self.btn_login.place(x=810,y=600)
        
  

    def btn_submit(self):
        check_submit.check_submitt(self)

    def btn_reset(self):
        self.en_name1.delete(0,END)
        self.en_username.delete(0,END)
        self.en_password.delete(0,END)
        self.en_phoneno.delete(0,END)
        self.en_age.delete(0,END)
        self.en_address.delete(0,END)
        self.en_email.delete(0,END)
        self.en_name2.delete(0,END)
        self.var.set('Male')
        self.var1.set('1')
        self.var2.set('Jan')
        self.var3.set('2020')
        self.en_confirm_password.delete(0,END)
        
    def func_login(self):
        self.wn.destroy()

    
# wn=Tk()
# employee_form(wn)
# wn.mainloop()       
