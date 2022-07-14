import pickle
import os
from tkinter import messagebox
from tkinter import *

def submitfunc(self):
    uname=self.en_username.get()
    passwd=self.en_password.get()
    phoneno=self.en_phoneno.get()
    age=self.en_age.get()
    address=self.en_address.get()
    email=self.en_email.get()
    name=self.en_name1.get()+self.en_name2.get()
    gender=self.var.get()
    date=(self.var1.get()+self.var2.get()+self.var3.get())
    le = os.path.getsize('E:\python_class\homework\Final assignment\Employee form\data.txt')     

    def insert():
        d={}
        val=[name,age,address,phoneno,gender,date,email,uname,passwd]
        di = {uname:val}

        if le > 0:
            f = open('data.txt', 'rb+')
            d = pickle.load(f)
            d.update(di)
            f.seek(0)
            pickle.dump(d, f)
            print('Data Saved Sucessfully')
            f.close()
            messagebox.showinfo('Confirmation','Data Saved')
            self.wn.destroy()
            

        else:
            f = open('data.txt', 'wb')
            d.update(di)
            pickle.dump(d, f)
            f.close()
            messagebox.showinfo('Confirmation','Data Saved')
            self.wn.destroy()
            

    def load():
        le = os.path.getsize('E:\python_class\homework\Final assignment\Employee form\data.txt')

        if le > 0:
            f = open('data.txt', 'rb')
            ld = pickle.load(f)
            for i, j in ld.items():
                print(i, j)
            f.close()
            

        else:
            print('file is empty')

    insert()
    load()

    