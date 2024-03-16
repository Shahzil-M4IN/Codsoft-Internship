import os
from tkinter import *
import random
from tkinter import messagebox

code_dir=os.path.dirname(os.path.abspath(__file__))
score_path=os.path.join(code_dir,'hi_score.txt')

def confirm():
    global Score,Rounds
    try:
        p_ch=player_var.get()
        if not p_ch:
            raise ValueError('Please select an option')
        cpu_ch=random.choice(options)
        player_label2.config(text=f'Player chose: {p_ch}')
        cpu_label2.config(text=f'Cpu chose: {cpu_ch}')
        if p_ch=='Scissors' and cpu_ch=='Rock':
            status_label.config(text='Cpu wins')
        elif p_ch=='Scissors' and cpu_ch=='Paper':
            status_label.config(text='Player wins')
            Score+=1
        elif p_ch=='Rock' and cpu_ch=='Scissors':
            status_label.config(text='Player wins')
            Score+=1
        elif p_ch=='Rock' and cpu_ch=='Paper':
            status_label.config(text='Cpu wins')
        elif p_ch=='Paper' and cpu_ch=='Scissors':
            status_label.config(text='Cpu wins')
        elif p_ch=='Paper' and cpu_ch=='Rock':
            status_label.config(text='Player wins')
            Score+=1
        else:
            status_label.config(text='Tie')
        Rounds+=1
        score_label2.config(text=Score)
        rounds_label2.config(text=Rounds)
        with open(score_path,'r') as f:
            pair=f.readlines()
        f.close()
        if int(pair[0])<Score or (int(pair[0])==Score and int(pair[1])>Rounds):
            with open(score_path,'w') as f:
                f.write(f'{Score}\n{Rounds}\nend')
            f.close()
            hi_score_label2.config(text=Score)
            hi_rounds_label2.config(text=Rounds)
    except Exception as e:
        messagebox.showerror(title='Error',message=f'Error occurred: {e}')
     
        
main=Tk()
main.title('Rock Paper Scissors')
main['bg']='Light Blue'
main.geometry('1100x500')
Head_label=Label(main,text='Welcome to Rock Paper Scissors Game!',font=('Showcard Gothic',20),bg='Light Blue',fg='Dark Blue')
Head_label.grid(row=0,column=1)
head_corner1=Label(main,text='*',font=('Showcard Gothic',25),bg='Light Blue',fg='Dark Blue')
head_corner1.grid(row=0,column=0)
head_corner2=Label(main,text='*',font=('Showcard Gothic',25),bg='Light Blue',fg='Dark Blue')
head_corner2.grid(row=0,column=2)
options=['Rock','Paper','Scissors']
Score=0
Rounds=0
Player_label=Label(main,text="Player's Choice:",font=('Showcard Gothic',15),bg='Light Blue')
Player_label.grid(row=1,column=0)
player_var=StringVar()
player_choice=OptionMenu(main,player_var,*options)
player_choice.grid(row=2,column=0)
player_label2=Label(main,text='',bg='Light Blue',font=('Arial Black',15))
player_label2.grid(row=3,column=0)
cpu_label1=Label(main,text="CPU's Choice:",font=('Showcard Gothic',15),bg='Light Blue')
cpu_label1.grid(row=1,column=2)
cpu_label2=Label(main,text='',bg='Light Blue',font=('Arial Black',15))
cpu_label2.grid(row=3,column=2)
Confirm_button=Button(main,text='Confirm',bg='Dark Blue',font=('Arial Black',18),fg='White',command=lambda: confirm())
Confirm_button.grid(row=4,column=1)
status_label=Label(main,text='',font=('Arial Black',15),bg='Light Blue')
status_label.grid(row=5,column=1)
score_label1=Label(main,text='Score:',font=('Arial Black',15),bg='Light Blue')
score_label1.grid(row=6,column=0)
rounds_label1=Label(main,text='Rounds:',font=('Arial Black',15),bg='Light Blue')
rounds_label1.grid(row=6,column=2)
score_label2=Label(main,text='',font=('Arial Black',15),bg='Light Blue',fg='Grey')
score_label2.grid(row=7,column=0)
rounds_label2=Label(main,text='',font=('Arial Black',15),bg='Light Blue',fg='Grey')
rounds_label2.grid(row=7,column=2)
with open(score_path,'r') as f:
    p=f.readlines()
f.close()
hi_score_label1=Label(main,text=f'Highest Score:',font=('Arial Black',15),bg='Light Blue')
hi_score_label1.grid(row=9,column=0)
in_label=Label(main,text='in',font=('Arial Black',15),bg='Light Blue')
in_label.grid(row=9,column=1)
hi_rounds_label1=Label(main,text='Lowest Rounds:',font=('Arial Black',15),bg='Light Blue')
hi_rounds_label1.grid(row=9,column=2)
hi_score_label2=Label(main,text=f'{p[0]}',font=('Arial Black',15),bg='Light Blue',fg='Grey')
hi_score_label2.grid(row=10,column=0)
hi_rounds_label2=Label(main,text=f'{p[1]}',font=('Arial Black',15),bg='Light Blue',fg='Grey')
hi_rounds_label2.grid(row=10,column=2)
main.mainloop()