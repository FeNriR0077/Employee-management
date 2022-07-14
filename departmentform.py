from tkinter import *
import os
from PIL import Image,ImageTk
import departmentcheck

class department_form:
    def __init__(self,window):
        self.wn=window
        self.wn.title('Department Form')
        self.wn.geometry('900x700+300+0')
        self.imgbg='pic1.jpg'
        self.img=ImageTk.PhotoImage(Image.open(self.imgbg))
        self.img_label=Label(self.wn,image=self.img,bd=0).place(x=0,y=0)

        ###frame
        self.frame1=Frame(self.wn)
        self.frame1.configure(width=600,height=600,background='aqua')
        self.frame1.place(x=150,y=20)

        
        #####heading
        self.heading=Label(self.frame1,text='Department Form',font=('aerial',30,'bold'),bg='white',fg='dark cyan')
        self.heading.place(x=0,y=50,relwidth=1)

        #######label and entry
        depname=['Production','Marketing','Accounting and Finance','Security','Purchasing','Cleaning']

        self.var=StringVar()
        self.var.set(depname[0])
        self.om_depname=OptionMenu(self.frame1,self.var,*depname)
        self.om_depname.configure(width=20,height=2,bg='light yellow')
        self.lb_depname=Label(self.frame1,text='Department Name: ',font=('aerial',22,'bold'),bg='aqua')
        self.lb_depname.place(x=40,y=200)
        self.om_depname.place(x=310,y=200)
        
        depcode=['PRD','MRK','ACCFIN','SEC','PUR','CLN']
        self.var1=StringVar()
        
        self.var1.set(depcode[0])
        self.om_depcode=OptionMenu(self.frame1,self.var1,*depcode)
        self.om_depcode.configure(width=15,height=2,bg='light yellow')

        self.lb_depcode=Label(self.frame1,text='Department Code: ',font=('aerial',22,'bold'),bg='aqua')

        self.en_depcode=Entry(self.frame1,font=('aerial',28),fg='black',width=5)

        self.lb_depcode.place(x=40,y=300)
        self.om_depcode.place(x=310,y=300)
        self.en_depcode.place(x=450,y=300)

        self.lb_depcodeshow=Label(self.frame1,text='*Select four digit code with appropriate prefix!!!!!!',bg='aqua')
        self.lb_depcodeshow.place(x=300,y=350)

        ########button
        self.btn_submit=Button(self.frame1,text='Submit',font=('aerial',15,'bold'),command=self.btn_submit)
        self.btn_submit.place(x=150,y=520)

        self.btn_reset=Button(self.frame1,text='Reset',font=('aerial',15,'bold'),command=self.btn_reset)
        self.btn_reset.place(x=280,y=520)

        self.btn_back=Button(self.frame1,text='Back',font=('aerial',15,'bold'),command=self.btn_back)
        self.btn_back.place(x=400,y=520)
        
    def btn_submit(self):
        departmentcheck.department_check(self)
        

    def btn_reset(self):
        self.var.set('Production')
        self.var1.set('PRD')
        self.en_depcode.delete(0,END)

    def btn_back(self):
        self.wn.destroy()


# wn=Tk()
# department_form(wn)
# wn.mainloop()  