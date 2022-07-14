import pickle
import os
from tkinter import messagebox
from tkinter import *
# import view1


class view_class:
    def __init__(self,window):
        self.wn=window
        self.wn.title('Info')
        self.wn.geometry('900x700+300+0')

        ###frame
        self.frame2=Frame(self.wn)
        self.frame2.configure(width=600,height=300,background='aqua')
        self.frame2.place(x=170,y=20)
        #####heading
        self.heading=Label(self.frame2,text='View Info',font=('aerial',30,'bold'),bg='white',fg='dark cyan')
        self.heading.place(x=0,y=10,relwidth=1)

        ##########label entry
        self.lb_userid=Label(self.frame2,text='User ID: ',font=('aerial',12,'bold'))
        self.lb_userid.place(x=100,y=70)

        self.en_userid=Entry(self.frame2,font=('aerial',12),fg='black')
        self.en_userid.place(x=200,y=70)

        depcode=['PRD','MRK','ACCFIN','SEC','PUR','CLN']
        self.var1=StringVar()
        self.var1.set(depcode[0])
        self.om_depcode=OptionMenu(self.frame2,self.var1,*depcode)
        self.om_depcode.configure(bg='light yellow')

        self.lb_depcode=Label(self.frame2,text='Department Code: ',font=('aerial',12,'bold'))

        self.en_depcode=Entry(self.frame2,font=('aerial',18),fg='black',width=5)

        self.lb_depcode.place(x=70,y=120)
        self.om_depcode.place(x=220,y=115)
        self.en_depcode.place(x=290,y=115)

        self.lb_depcodeshow=Label(self.frame2,text='*Enter four digit code with appropriate prefix!!!!!!',fg='red')
        self.lb_depcodeshow.place(x=200,y=150)

        ########button
        self.btn_submit=Button(self.frame2,text='Submit',font=('aerial',15,'bold'),command=self.btn_submit)
        self.btn_submit.place(x=130,y=250)

        self.btn_reset=Button(self.frame2,text='Reset',font=('aerial',15,'bold'),command=self.btn_reset)
        self.btn_reset.place(x=220,y=250)

        self.btn_back=Button(self.frame2,text='Back',font=('aerial',15,'bold'),command=self.btn_back)
        self.btn_back.place(x=300,y=250)

    def view_check(self):
        userid1=self.en_userid.get()
        depcode1=self.var1.get()+self.en_depcode.get()
 
        a=1
        b=1
        le = os.path.getsize('E:\python_class\homework\Final assignment\Employee form\employeetext.txt')
        le2 = os.path.getsize('E:\python_class\homework\Final assignment\Employee form\departmenttext.txt')
        if le > 0: 
            f = open('employeetext.txt', 'rb')
            ld = pickle.load(f)
            for i,j in ld.items():
                if userid1==i:
                    a=0
                    break
            if userid1!=i:
                messagebox.showerror('Error','Userid do not exist!!!!!!!!!!!!')
        else:
            messagebox.showerror('Error','Userid do not exist!!!!!!!!!!!!')
        
        if le2 > 0: 
            f = open('departmenttext.txt', 'rb')
            ld2 = pickle.load(f)
            for i,j in ld2.items():
                if depcode1==i:
                    b=0
                    break
            if depcode1!=i:
                messagebox.showerror('Error','Department code do not exist!!!!!!!!!!!!')
        else:
            messagebox.showerror('Error','Department code do not exist!!!!!!!!!!!!')

        
        
        if a==0 and b==0:
            messagebox.showinfo('Success','Welcome!!!!',parent=self.frame2)
            self.frame2.destroy()
            
            self.frame1=Frame(self.wn)
            self.frame1.configure(width=600,height=700,background='aqua')
            self.frame1.place(x=150,y=0)


            self.btn_back=Button(self.wn,text='Back',font=('aerial',15,'bold'),command=self.btn_back)
            self.btn_back.place(x=450,y=650)

            
            #####heading
            self.heading=Label(self.frame1,text='Employee Information',font=('aerial',30,'bold'),bg='white',fg='dark cyan')
            self.heading.place(x=0,y=50,relwidth=1)

            le = os.path.getsize('E:\python_class\homework\Final assignment\Employee form\employeetext.txt')
            le2 = os.path.getsize('E:\python_class\homework\Final assignment\Employee form\departmenttext.txt')
            if le > 0: 
                f = open('employeetext.txt', 'rb')
                ld = pickle.load(f)
                for i,j in ld.items():
                    if userid1==j[6]:
                        self.lb_name=Label(self.frame1,text='Full Name: ',font=('aerial',12,'bold'),bg='aqua')
                        self.lb_name.place(x=20,y=120)

                        nam=StringVar()
                        nam.set(j[0])
                        self.lb_name1=Label(self.frame1,textvariable=nam,font=('aerial',16,'bold'),bg='aqua',fg='blue')
                        self.lb_name1.place(x=20,y=145)

                        ######address
                        self.lb_address=Label(self.frame1,text='Address: ',font=('aerial',12,'bold'),bg='aqua')
                        self.lb_address.place(x=20,y=180)

                        add=StringVar()
                        add.set(j[1])
                        self.lb_add=Label(self.frame1,textvariable=add,font=('aerial',16,'bold'),bg='aqua',fg='blue')
                        self.lb_add.place(x=20,y=205)

                        #######phone
                        self.lb_phoneno=Label(self.frame1,text='Phone Number: ',font=('aerial',12,'bold'),bg='aqua')
                        self.lb_phoneno.place(x=20,y=240)

                        phno=StringVar()
                        phno.set(j[2])
                        self.lb_phoneno1=Label(self.frame1,textvariable=phno,font=('aerial',16,'bold'),bg='aqua',fg='blue')
                        self.lb_phoneno1.place(x=20,y=275)

                        ########email
                        self.lb_email=Label(self.frame1,text='E-mail: ',font=('aerial',12,'bold'),bg='aqua')
                        self.lb_email.place(x=250,y=240)

                        em=StringVar()
                        em.set(j[3])
                        self.lb_email1=Label(self.frame1,textvariable=em,font=('aerial',16,'bold'),bg='aqua',fg='blue')
                        self.lb_email1.place(x=250,y=275)

                        #########age
                        self.lb_age=Label(self.frame1,text='Age: ',font=('aerial',12,'bold'),bg='aqua')
                        self.lb_age.place(x=20,y=310)

                        ag=StringVar()
                        ag.set(j[4])
                        self.lb_age1=Label(self.frame1,textvariable=ag,font=('aerial',16,'bold'),bg='aqua',fg='blue')
                        self.lb_age1.place(x=20,y=345)

                        #######gender
                        self.lb_gender=Label(self.frame1,text='Gender: ',font=('aerial',12,'bold'),bg='aqua')
                        self.lb_gender.place(x=250,y=310)

                        gen=StringVar()
                        gen.set(j[5])
                        self.lb_gender1=Label(self.frame1,textvariable=gen,font=('aerial',16,'bold'),bg='aqua',fg='blue')
                        self.lb_gender1.place(x=250,y=345)
                        
                    

                        
                        break
                if userid1!=i:
                    messagebox.showerror('Error','Userid do not exist!!!!!!!!!!!!')
            else:
                messagebox.showerror('Error','Userid do not exist!!!!!!!!!!!!')
            
            if le2 > 0: 
                f = open('departmenttext.txt', 'rb')
                ld2 = pickle.load(f)
                for i,j in ld2.items():
                    if depcode1==i:
                        self.lb_depname=Label(self.frame1,text='Department: ',font=('aerial',12,'bold'),bg='aqua')
                        self.lb_depname.place(x=20,y=380)
                        
                        dep=StringVar()
                        dep.set(j)
                        self.lb_depname1=Label(self.frame1,textvariable=dep,font=('aerial',16,'bold'),bg='aqua',fg='blue')
                        self.lb_depname1.place(x=20,y=415)
                        break
                if depcode1!=i:
                    messagebox.showerror('Error','Department code do not exist!!!!!!!!!!!!')
            else:
                messagebox.showerror('Error','Department code do not exist!!!!!!!!!!!!')
    
    def btn_submit(self):
        self.view_check()
        
        

    def btn_reset(self):
        self.en_userid.delete(0,END)
        self.en_depcode.delete(0,END)
        self.var1.set('PRD')
        
    def btn_back(self):
        self.wn.destroy()



   
    
    
    

# wn=Tk()
# view_class(wn)
# wn.mainloop()