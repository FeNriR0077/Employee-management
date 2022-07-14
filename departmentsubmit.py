import pickle
import os
from tkinter import messagebox
from tkinter import *

def department_submit(self):
    depname=self.var.get()
    depcode=self.var1.get()+self.en_depcode.get()

    le = os.path.getsize('E:\python_class\homework\Final assignment\Employee form\departmenttext.txt')

    def insert():
        d={}
        di = {depcode:depname}

        if le > 0:
            f = open('departmenttext.txt', 'rb+')
            d = pickle.load(f)
            d.update(di)
            f.seek(0)
            pickle.dump(d, f)
            print('Data Saved Sucessfully')
            f.close()
            messagebox.showinfo('Confirmation','Data Saved')
            self.wn.destroy()
        else:
            f = open('departmenttext.txt', 'wb')
            d.update(di)
            pickle.dump(d, f)
            f.close()
            messagebox.showinfo('Confirmation','Data Saved')
            self.wn.destroy()

    def load():
        le = os.path.getsize('E:\python_class\homework\Final assignment\Employee form\departmenttext.txt')

        if le > 0:
            f = open('departmenttext.txt', 'rb')
            ld = pickle.load(f)
            for i, j in ld.items():
                print(i, j)
            f.close()
            

        else:
            print('file is empty')

    insert()
    load()