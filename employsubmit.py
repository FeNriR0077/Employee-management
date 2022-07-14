import pickle
import os
from tkinter import messagebox
from tkinter import *

def employ_submit(self):
    name=self.en_name1.get()+self.en_name2.get()
    address=self.en_address.get()
    phoneno=self.en_phoneno.get()
    email=self.en_email.get()
    age=self.en_age.get()
    gender=self.var.get()
    name1=self.en_name1.get()
    name2=self.en_name2.get()
    userid=self.en_userid.get()
    

    le = os.path.getsize('E:\python_class\homework\Final assignment\Employee form\employeetext.txt')

    def insert():
        d={}
        val=[name,address,phoneno,email,age,gender,userid]
        di = {userid:val}

        if le > 0:
            f = open('employeetext.txt', 'rb+')
            d = pickle.load(f)
            d.update(di)
            f.seek(0)
            pickle.dump(d, f)
            print('Data Saved Sucessfully')
            f.close()
            messagebox.showinfo('Confirmation','Data Saved')
            self.wn.destroy()
        else:
            f = open('employeetext.txt', 'wb')
            d.update(di)
            pickle.dump(d, f)
            f.close()
            messagebox.showinfo('Confirmation','Data Saved')
            self.wn.destroy()

    def load():
        le = os.path.getsize('E:\python_class\homework\Final assignment\Employee form\employeetext.txt')

        if le > 0:
            f = open('employeetext.txt', 'rb')
            ld = pickle.load(f)
            for i, j in ld.items():
                print(i, j)
            f.close()
            

        else:
            print('file is empty')

    insert()
    load()