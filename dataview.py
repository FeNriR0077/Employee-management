from tkinter import *
import os
from PIL import Image,ImageTk
import pickle
from tkinter import messagebox 

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
        self.heading=Label(self.frame1,text='Employee Infoemantio',font=('aerial',30,'bold'),bg='white',fg='dark cyan')
        self.heading.place(x=0,y=50,relwidth=1)

        ########label


        le = os.path.getsize('E:\python_class\homework\Final assignment\Employee form\employeetext.txt')
        le2 = os.path.getsize('E:\python_class\homework\Final assignment\Employee form\departmenttext.txt')
        if le > 0: 
            f = open('employeetext.txt', 'rb')
            ld = pickle.load(f)
            for i,j in ld.items():
                if userid==j[6]:
                    self.lb_userid=Label(self.frame1,textvariable=j[6],font=('aerial',12,'bold'),bg='aqua')
                    self.lb_userid.place(x=20,y=380)
                    break
            if userid!=i:
                messagebox.showerror('Error','Userid do not exist!!!!!!!!!!!!')
        else:
            messagebox.showerror('Error','Userid do not exist!!!!!!!!!!!!')
        
        if le2 > 0: 
            f = open('departmenttext.txt', 'rb')
            ld2 = pickle.load(f)
            for i,j in ld2.items():
                if depcode==i:
                    b=0
                    break
            if depcode!=i:
                messagebox.showerror('Error','Department code do not exist!!!!!!!!!!!!')
        else:
            messagebox.showerror('Error','Department code do not exist!!!!!!!!!!!!')

# wn=Tk()
# department_form(wn)
# wn.mainloop()  