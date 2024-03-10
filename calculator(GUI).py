import tkinter as tk
from tkinter import messagebox

def calc(n1_entry, n2_entry, operator_val, result_label):
    try:
        n1 = eval(n1_entry.get()) 
        n2 = eval(n2_entry.get())  
        op = operator_val.get()
        if n1==str or n2==str:
            raise TypeError  
        if op=='Addition':
            result=n1+n2
        elif op=='Subtraction':
            result=n1-n2
        elif op=='Multiplication':
            result=n1*n2
        elif op=='Division':
            result=n1/n2
        result_label.config(text=result)
    except Exception as e:
        messagebox.showerror('Alert', f'Error: {e}')
main=tk.Tk()
main.title('Calculator')
main.geometry('650x500')
n1_label=tk.Label(main,text='Number A:',font=('Xenara',15))
n1_label.grid(row=0,column=0,padx=5)
n1_entry=tk.Entry(main,font=('Xenara',15))
n1_entry.grid(row=1,column=0,padx=5)
n2_label=tk.Label(main,text='Number B:',font=('Xenara',15))
n2_label.grid(row=0,column=2,padx=5)
n2_entry=tk.Entry(main,font=('Xenara',15))
n2_entry.grid(row=1,column=2,padx=5)
operators=['Addition','Subtraction','Multiplication','Division']
operator_val=tk.StringVar(main)
operator_val.set('Select an Operation')
operator_drop=tk.OptionMenu(main,operator_val,*operators)
operator_drop.grid(row=2,column=1,pady=10)
result_label=tk.Label(main,font=('Xenara',15),fg='red')
result_label.grid(row=4,column=1,pady=20)
calculate=tk.Button(main,text='Calculate',font=('Xenara',15),bg='light grey',command=lambda: calc(n1_entry,n2_entry,operator_val,result_label))
calculate.grid(row=3,column=1,pady=20)
main.mainloop()