import tkinter as tk
from tkinter import messagebox
import random

def gen(length_val,complexity_val):
    try:
        l=int(length_val.get())
        c=complexity_val.get()
        numbers=['1','2','3','4','5','6','7','8','9']
        small_alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        Cap_alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        special_char=['!','?','/','$','#','@','&']
        ch=[small_alphabets,Cap_alphabets,special_char,numbers]
        password=''
        if c=='Slightly Complex':
            for i in range(0,l):
                if i==0:
                    element=random.choice(Cap_alphabets)
                elif i==l-2 or i==l-3:
                    element=random.choice(numbers)
                elif i==l-1:
                    element=random.choice(special_char)
                else:
                    element=random.choice(small_alphabets)
                password=password+element
            Password_label.config(text=password)
        elif c=='Highly Complex':
            for i in range(0,l):
                ran_pick=random.choice(ch)
                element=random.choice(ran_pick)
                password=password+element
            Password_label.config(text=password)
        else:
            messagebox.showerror('Alert','Error: Perhaps you forgot to pick complexity?')
    except Exception as e:
        messagebox.showerror('Alert','Error: Perhaps you forgot to pick length?')

main=tk.Tk()
main.title('Password Generator')
main.geometry('500x500')
Title_label=tk.Label(main,text='Welcome to Password Generator',font=('Arial Black',20))
Title_label.pack(pady=10)
lengths=[4,5,6,7,8,9,10]
length_label=tk.Label(main,text='Specify Length:',font=('Calibri',15))
length_label.pack(pady=10)
length_val=tk.StringVar(main)
length_picks=tk.OptionMenu(main,length_val,*lengths)
length_picks.pack()
complexities=['Slightly Complex','Highly Complex']
complexity_label=tk.Label(main,text='Specify Complexity:',font=('Calibri',15))
complexity_label.pack(pady=10)
complexity_val=tk.StringVar(main)
complexity_picks=tk.OptionMenu(main,complexity_val,*complexities)
complexity_picks.pack()
Generate_button=tk.Button(main,text='Generate',font=('Calibri',15),command=lambda: gen(length_val,complexity_val))
Generate_button.pack(pady=30)
Password_label=tk.Label(main,font=('Calibri',15),fg='Grey')
Password_label.pack(pady=10)
main.mainloop()