#To_do_list.txt is an important file to make this py program work. Get it from Shahzil-M4IN's github repositry Codsoft internship
import os
import tkinter as tk

program_dir=os.path.dirname(os.path.abspath(__file__))
program_path=os.path.join(program_dir,'To_do_list.py')
list_path=os.path.join(program_dir,'To_do_list.txt')

def show():
    with open(list_path,'r') as file:
        lst=file.readlines()
    display=tk.Toplevel(main)
    display.title('List')
    display.geometry('1000x1000')
    lenlst=len(lst)
    count=0
    for i in range(0,lenlst):
        if lst[i].strip('\n')!='':
            count+=1   
            labels=tk.Label(display,text=f'({count})\t{lst[i]}',font=('Calibri',15))
            labels.grid(row=i,column=0,sticky='w',padx=10)
    file.close()

def update_wind():
    def update():
        with open(list_path,'r') as f:
            lst=f.readlines()
        entry_val=entry.get()
        f.close()
        con=True
        if entry_val.strip()=='':
            con=False
        for i in lst:
            if entry_val.strip()==i.strip():
                con=False
                status_label.config(text='Already exists')
                break
        if con==True:
            with open(list_path,'a+') as file:
                file.write(f'\n{entry_val}')
            file.close()
            status_label.config(text='Updated Successfully')      
    display=tk.Toplevel(main)
    display.title('Update')
    display.geometry('400x300')
    entry_label=tk.Label(display,text='Enter task to update list: ',font=('Calibri',15))
    entry_label.pack(pady=10)
    entry=tk.Entry(display,font=('Calibri',15),width=20)
    entry.pack()
    update_b=tk.Button(display,text='Update',font=('Calibri',15),command=lambda: update())
    update_b.pack(pady=30)
    status_label= tk.Label(display,font=('Calibri',15),fg='red')
    status_label.pack(pady=10)

def delete_win():
    def dele():
        with open(list_path,'r') as file:
            lst=file.readlines()
        entry_val=entry.get()
        with open(list_path,'w') as f:
            for i in lst:
                if i.strip()!=entry_val.strip():
                    f.write(i)
        f.close()
        file.close()
        with open(list_path,'r') as file:
            lst2=file.readlines()
        if lst2==lst:
            status_label.config(text="Doesn't exists")
        else:
            status_label.config(text='Deleted Successfully')    
        file.close()  
    display=tk.Toplevel()
    display.title('Delete Content')
    display.geometry('400x300')
    entry_label=tk.Label(display,text='Enter task to delete from list: ',font=('Calibri',15))
    entry_label.pack(pady=10)
    entry=tk.Entry(display,font=('Calibri',15),width=20)
    entry.pack()
    delete_b=tk.Button(display,text='Delete',font=('Calibri',15),command=lambda: dele())
    delete_b.pack(pady=30)
    status_label= tk.Label(display,font=('Calibri',15),fg='red')
    status_label.pack(pady=10)

def delete_a():
    with open(list_path,'w') as f:
        f.write('')
    f.close()
    
main=tk.Tk()
main.title('To Do List')
main.geometry('400x400')
welcome_label=tk.Label(main,text='Welcome to ToDo List Program',font=('Calibri',15))
welcome_label.pack(pady=20)
show_list=tk.Button(main,text='Show List',font=('Calibri',15),command=lambda: show())
show_list.pack(pady=20)
update_lst=tk.Button(main,text='Update List',font=('Calibri',15),command=lambda: update_wind())
update_lst.pack(pady=20)
delete_content=tk.Button(main,text='Delete Content',font=('Calibri',15),command=lambda: delete_win())
delete_content.pack(pady=20)
delete_all=tk.Button(main,text='Delete All',font=('Calibri',15),command=lambda: delete_a())
delete_all.pack(pady=20)
main.mainloop()