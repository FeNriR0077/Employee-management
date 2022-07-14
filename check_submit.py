import pickle
from tkinter import messagebox
import submitfile
import os
from tkinter import *
from employeeform import *

def check_submitt(self):
    uname=self.en_username.get()
    passwd=self.en_password.get()
    phoneno=self.en_phoneno.get()
    age=self.en_age.get()
    address=self.en_address.get()
    email=self.en_email.get()
    name1=self.en_name1.get()
    name2=self.en_name2.get()
    conf_passwd=self.en_confirm_password.get()
    name=name1+name2
    le = os.path.getsize('E:\python_class\homework\Final assignment\Employee form\data.txt')

    if le > 0: 
        f = open('data.txt', 'rb')
        ld = pickle.load(f)
        for i,j in ld.items():
            if uname==i:
                messagebox.showerror('Error','Username already exists!!!!!!!',parent=self.wn)
                f.close()
                break
        if uname!=i:
            if uname=='' or passwd=='' or email=='' or name1=='' or name2=='' or address=='' or age=='' or phoneno=='' or conf_passwd=='':
                messagebox.showerror('Error','Please fill all the boxes!!!!!!!',parent=self.wn)
            elif self.en_password.get()!=self.en_confirm_password.get():
                messagebox.showerror('Error','Passwords do not match!!!!!!!',parent=self.wn)  
            else:
                submitfile.submitfunc(self)
            
    else:
                
        if uname=='' or passwd=='' or name1=='' or name2=='' or email=='' or address=='' or age=='' or phoneno=='' or conf_passwd=='':
            messagebox.showerror('Error','Please fill all the boxes!!!!!!!',parent=self.wn)
        elif self.en_password.get()!=self.en_confirm_password.get():
            messagebox.showerror('Error','Passwords do not match!!!!!!!',parent=self.wn)
        else:
            submitfile.submitfunc(self)
        

  

    