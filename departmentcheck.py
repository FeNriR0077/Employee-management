import pickle
import os
from tkinter import messagebox
from tkinter import *
import departmentsubmit

def department_check(self):
    depname=self.var.get()
    depcode=self.var1.get()+self.en_depcode.get()

    le = os.path.getsize('E:\python_class\homework\Final assignment\Employee form\departmenttext.txt')
    if le > 0: 
        f = open('departmenttext.txt', 'rb')
        ld = pickle.load(f)
        for i,j in ld.items():
            if depcode==i:
                messagebox.showerror('Error','Use another code!!!!!!!',parent=self.wn)
                f.close()
                break
        if depcode!=i:     
            if self.en_depcode.get()=='':
                messagebox.showerror('Error','Please enter department code!!!!!!!',parent=self.wn)
            else:
                departmentsubmit.department_submit(self)
            
    else:
                
        if self.en_depcode.get()=='':
            messagebox.showerror('Error','Please enter department code!!!!!!!!',parent=self.wn)
        else:
            departmentsubmit.department_submit(self)