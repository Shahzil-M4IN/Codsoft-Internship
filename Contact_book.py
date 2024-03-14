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

def update_wind():
    def update():
        with open(list_path,'r') as f:
            lst=f.readlines()
        name_entry_val=Name_entry.get()
        number_entry_val=Number_entry.get()
        email_entry_val=Email_entry.get()
        address_entry_val=Address_entry.get()
        f.close()
        con=True
        if (name_entry_val.strip()=='') or (number_entry_val.strip()=='') or (email_entry_val.strip()=='') or (address_entry_val.strip()==''):
            con=False
        for i in lst:
            if (name_entry_val.strip() in i) or (number_entry_val.strip() in i) or (email_entry_val.strip() in i):
                con=False
                break
        if con==True:
            with open(list_path,'a+') as file:
                file.write(f'\n{name_entry_val} {number_entry_val} {email_entry_val} {address_entry_val}')
            file.close()
            status_label.config(text='Updated Successfully')
        else:
            if (name_entry_val.strip()=='') or (number_entry_val.strip()=='') or (email_entry_val.strip()=='') or (address_entry_val.strip()==''):
                status_label.config(text='Enter specified fields')
            else:   
                status_label.config(text='Already exists')      
    window=tk.Toplevel(main)
    window.title('Update')
    window.geometry('500x500')
    window['bg']='Green'
    Name_entry_label=tk.Label(window,text='Name: ',font=('Calibri',15),bg='Green')
    Name_entry_label.pack(pady=10)
    Name_entry=tk.Entry(window,font=('Calibri',15),width=20)
    Name_entry.pack()
    Number_entry_label=tk.Label(window,text='Phone no: ',font=('Calibri',15),bg='Green')
    Number_entry_label.pack(pady=10)
    Number_entry=tk.Entry(window,font=('Calibri',15),width=20)
    Number_entry.pack()
    Email_entry_label=tk.Label(window,text='Email: ',font=('Calibri',15),bg='Green')
    Email_entry_label.pack(pady=10)
    Email_entry=tk.Entry(window,font=('Calibri',15),width=20)
    Email_entry.pack()
    Address_entry_label=tk.Label(window,text='Address: ',font=('Calibri',15),bg='Green')
    Address_entry_label.pack(pady=10)
    Address_entry=tk.Entry(window,font=('Calibri',15),width=20)
    Address_entry.pack()
    update_b=tk.Button(window,text='Update',font=('Calibri',15),command=lambda: update(),bg='Light Green')
    update_b.pack(pady=30)
    status_label= tk.Label(window,font=('Calibri',15),fg='red',bg='Green')
    status_label.pack(pady=10)

def delete_win():
    def dele():
        with open(list_path,'r') as file:
            lst=file.readlines()
        name_entry_val=name_entry.get()
        with open(list_path,'w') as f:
            for i in lst:
                l=i.split()
                if name_entry_val.strip() not in l:
                    f.write(i)
        f.close()
        file.close()
        with open(list_path,'r') as file:
            lst2=file.readlines()
        if lst2==lst:
            if name_entry_val=='':
                status_label.config(text="Please fill the specified field")
            else:
                status_label.config(text="Doesn't exists")
        else:
            status_label.config(text='Deleted Successfully')    
        file.close()  
    window=tk.Toplevel()
    window.title('Delete Content')
    window.geometry('400x300')
    window['bg']='Green'
    name_entry_label=tk.Label(window,text='Enter name to delete from book: ',font=('Calibri',15),bg='Green')
    name_entry_label.pack(pady=10)
    name_entry=tk.Entry(window,font=('Calibri',15),width=20)
    name_entry.pack()
    delete_b=tk.Button(window,text='Delete',font=('Calibri',15),command=lambda: dele(),bg='Light Green')
    delete_b.pack(pady=30)
    status_label= tk.Label(window,font=('Calibri',15),fg='red',bg='Green')
    status_label.pack(pady=10)

def delete_a():
    with open(list_path,'w') as f:
        f.write('')
    f.close()

main=tk.Tk()
main['bg']='Green'
main.title('Contact Book')
main.geometry('500x500')
welcome_label=tk.Label(main,text='Welcome to Contact Book',font=('Arial Black',20),bg='Green')
welcome_label.pack(pady=20)
show_book=tk.Button(main,text='Show Contacts',font=('Calibri',15),bg='Light Green',width=15,command=lambda: display())
show_book.pack(pady=20)
update_book=tk.Button(main,text='Update Book',font=('Calibri',15),bg='Light Green',width=15,command=lambda: update_wind())
update_book.pack(pady=20)
delete_contacts=tk.Button(main,text='Delete Contacts',font=('Calibri',15),bg='Light Green',width=15,command=lambda: delete_win())
delete_contacts.pack(pady=20)
delete_all_button=tk.Button(main,text='Delete All',font=('Calibri',15),bg='Light Green',width=15,command=lambda: delete_a())
delete_all_button.pack(pady=20)
main.mainloop()