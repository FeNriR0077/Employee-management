import pickle
import os
from tkinter import messagebox
from tkinter import *
import employsubmit

def employ_checksubmit(self):
    name=self.en_name1.get()+self.en_name2.get()
    address=self.en_address.get()
    phoneno=self.en_phoneno.get()
    email=self.en_email.get()
    age=self.en_age.get()
    gender=gender=self.var.get()
    name1=self.en_name1.get()
    name2=self.en_name2.get()
    userid=self.en_userid.get()


    le = os.path.getsize('E:\python_class\homework\Final assignment\Employee form\employeetext.txt')
    if le > 0: 
        f = open('employeetext.txt', 'rb')
        ld = pickle.load(f)
        for i,j in ld.items():
            if userid==i:
                messagebox.showerror('Error','Userid already exists!!!!!!!',parent=self.wn)
                f.close()
                break
        if userid!=i:     
            if userid=='' or address=='' or phoneno=='' or email=='' or age=='' or gender=='' or name1=='' or name2=='':
                messagebox.showerror('Error','Please fill all the boxes!!!!!!!',parent=self.wn)
            else:
                employsubmit.employ_submit(self)
                
    else:
                
        if userid=='' or address=='' or phoneno=='' or email=='' or age=='' or gender=='' or name1=='' or name2=='':
            messagebox.showerror('Error','Please fill all the boxes!!!!!!!',parent=self.wn)
        else:
            employsubmit.employ_submit(self)