import os
import tkinter as tk
from tkinter import font

program_dir=os.path.dirname(os.path.abspath(__file__))
program_path=os.path.join(program_dir,'Contact_book.py')
list_path=os.path.join(program_dir,'Contact_book.txt')

def heading_font():
    return font.Font(family='Calibri',size=15,weight='bold')

def display():   
    wind=tk.Toplevel(main)
    wind['bg']='Light Grey'
    wind.title('List')
    wind.geometry('1000x1000')
    name_label=tk.Label(wind,text='Name:',font=heading_font(),bg='Light Grey')
    name_label.grid(row=0,column=0)
    phone_label=tk.Label(wind,text='Phone No:',font=heading_font(),bg='Light Grey')
    phone_label.grid(row=0,column=1)
    email_label=tk.Label(wind,text='Email:',font=heading_font(),bg='Light Grey')
    email_label.grid(row=0,column=2)
    address_label=tk.Label(wind,text='Address:',font=heading_font(),bg='Light Grey')
    address_label.grid(row=0,column=3)
    with open(list_path,'r') as file:
        lines=file.readlines()
        count=0
        for line in lines:
            count+=1
            string=line.split()
            for i in range(0,len(string)):
                contact=tk.Label(wind,text=f'{string[i]}\t',font=('Calibri',15),bg='Light Grey')
                contact.grid(row=count,column=i)
    file.close()

main=tk.Tk()
main['bg']='Green'
main.title('Contact Book')
main.geometry('500x500')
welcome_label=tk.Label(main,text='Welcome to Contact Book',font=('Arial Black',20),bg='Green')
welcome_label.pack(pady=20)
show_book=tk.Button(main,text='Show Contacts',font=('Calibri',15),bg='Light Green',width=15,command=lambda: display())
show_book.pack(pady=20)
update_book=tk.Button(main,text='Update Book',font=('Calibri',15),bg='Light Green',width=15)
update_book.pack(pady=20)
delete_contacts=tk.Button(main,text='Delete Contacts',font=('Calibri',15),bg='Light Green',width=15)
delete_contacts.pack(pady=20)
delete_all_button=tk.Button(main,text='Delete All',font=('Calibri',15),bg='Light Green',width=15)
delete_all_button.pack(pady=20)
main.mainloop()