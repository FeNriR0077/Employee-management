from tkinter import *
import os
from PIL import Image,ImageTk
import employchecksubmit

class emp_form:
    def __init__(self,window):
        self.wn=window
        self.wn.title('Employee Form')
        self.wn.geometry('900x700+300+0')
        self.imgbg='pic1.jpg'
        self.img=ImageTk.PhotoImage(Image.open(self.imgbg))
        self.img_label=Label(self.wn,image=self.img,bd=0).place(x=0,y=0)

        ###frame
        self.frame1=Frame(self.wn)
        self.frame1.configure(width=600,height=600,background='aqua')
        self.frame1.place(x=150,y=20)

        
        #####heading
        self.heading=Label(self.frame1,text='Employee Form',font=('aerial',30,'bold'),bg='white',fg='dark cyan')
        self.heading.place(x=0,y=50,relwidth=1)

        #########label and entry

        ###name
        self.lb_name=Label(self.frame1,text='Full Name: ',font=('aerial',12,'bold'),bg='aqua')
        self.lb_name.place(x=20,y=120)

        self.en_name1=Entry(self.frame1,font=('aerial',12),fg='black')
        self.en_name1.place(x=20,y=145)

        self.en_name2=Entry(self.frame1,font=('aerial',12),fg='black')
        self.en_name2.place(x=250,y=145)

        ######address
        self.lb_address=Label(self.frame1,text='Address: ',font=('aerial',12,'bold'),bg='aqua')
        self.lb_address.place(x=20,y=180)

        self.en_address=Entry(self.frame1,font=('aerial',12),fg='black')
        self.en_address.place(x=20,y=205)

        #######phone
        self.lb_phoneno=Label(self.frame1,text='Phone Number: ',font=('aerial',12,'bold'),bg='aqua')
        self.lb_phoneno.place(x=20,y=240)

        self.en_phoneno=Entry(self.frame1,font=('aerial',12),fg='black')
        self.en_phoneno.place(x=20,y=275)

        #######email
        self.lb_email=Label(self.frame1,text='E-mail: ',font=('aerial',12,'bold'),bg='aqua')
        self.lb_email.place(x=250,y=240)

        self.en_email=Entry(self.frame1,font=('aerial',12),fg='black',width=30)
        self.en_email.place(x=250,y=275)

        #########age
        self.lb_age=Label(self.frame1,text='Age: ',font=('aerial',12,'bold'),bg='aqua')
        self.lb_age.place(x=20,y=310)

        self.en_age=Entry(self.frame1,font=('aerial',12),fg='black')
        self.en_age.place(x=20,y=345)

        ######gender
        l_gender=['Male','Female','Other']
        self.var=StringVar()
        self.var.set(l_gender[0])
        self.om_gender=OptionMenu(self.frame1,self.var,*l_gender)
        self.lb_gender=Label(self.frame1,text='Gender: ',font=('aerial',12,'bold'),bg='aqua')
        self.lb_gender.place(x=250,y=310)
        self.om_gender.place(x=330,y=310)
        
        ########user id
        self.lb_userid=Label(self.frame1,text='User ID: ',font=('aerial',12,'bold'),bg='aqua')
        self.lb_userid.place(x=20,y=380)

        self.en_userid=Entry(self.frame1,font=('aerial',12),fg='black')
        self.en_userid.place(x=20,y=415)

        ############Button
        self.btn_submit=Button(self.frame1,text='Submit',font=('aerial',15,'bold'),command=self.btn_submit)
        self.btn_submit.place(x=230,y=520)

        self.btn_reset=Button(self.frame1,text='Reset',font=('aerial',15,'bold'),command=self.btn_reset)
        self.btn_reset.place(x=350,y=520)

        self.btn_back=Button(self.frame1,text='Back',font=('aerial',15,'bold'),command=self.btn_back)
        self.btn_back.place(x=460,y=520)

    def btn_submit(self):
        employchecksubmit.employ_checksubmit(self)

    def btn_reset(self):
        self.en_name1.delete(0,END)
        self.en_name2.delete(0,END)
        self.en_address.delete(0,END)
        self.en_phoneno.delete(0,END)
        self.en_email.delete(0,END)
        self.en_age.delete(0,END)
        self.var.set('Male')
        self.en_name1.delete(0,END)
        self.en_name2.delete(0,END)
        self.en_userid.delete(0,END)
    def btn_back(self):
        self.wn.destroy()




# wn=Tk()
# emp_form(wn)
# wn.mainloop()