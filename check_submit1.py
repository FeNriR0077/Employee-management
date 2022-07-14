import pickle
from tkinter import messagebox
import os
import emp1
from tkinter import *


def sunmit1(self):
    uname1=self.en_username.get()
    passwd1=self.en_password.get()
    le = os.path.getsize('E:\python_class\homework\Final assignment\Employee form\data.txt')
    if le > 0:
        f = open('data.txt', 'rb')
        ld = pickle.load(f)
        a=''
        for i,j in ld.items():
            utpt=(uname1==i and passwd1==j[8])
            if utpt==True:
                a=0
                break

        if uname1=='' or passwd1=='':
            messagebox.showerror('Error','All entry should be filled!!!!!!!!!',parent=self.wn)
        elif a==0:
            messagebox.showinfo('Success','Welcome!!!!!!!')
            self.wn.destroy()
            wn2=Tk()
            emp1.emp_1(wn2)
        elif uname1!=i and passwd1!=j[8]:
            messagebox.showerror('Error','Invalid Username or Password!!!!!!!!!',parent=self.wn)
        else:
            messagebox.showerror('Error','Invalid Username or Password!!!!!!!!!',parent=self.wn)
        f.close()    
    else:
        messagebox.showerror('Error','Invalid Username or Password!!!!!!!!!',parent=self.wn)
                
