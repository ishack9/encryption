import tkinter as tk
from tkinter import *
import random
import time


form=tk.Tk()

form.title("Encrypt")
    
form.geometry("400x400+500+100")
form.config(background="black")
form.minsize(400,400)


def easy():
    
    try:
        
        uzunluk=int(entry.get())
    
    except ValueError:
        uyari2=tk.Label(text="Lütfen rakam kullanın ",font=("Times New Roman", 11), fg="red", bg="black")
        uyari2.place(x=134,y=75)
        uyari2.after(3000, uyari2.destroy)
        
    kharf="abcdefghijklmnoprstuvyzqwx"
    bharf="ABCDEFGHIJKLMNOPRSTUVYZQWX"
        
        
    if uzunluk >= 53:
        uyari1=tk.Label(text=" Kolay için en fazla 52 haneli seçebilirsiniz",font=("Times New Roman", 11), fg="red", bg="black")
        uyari1.place(x=70,y=75)
        uyari1.after(3000, uyari1.destroy)
    else:
        pass
            
    all = kharf+bharf
    parola ="".join(random.sample(all, uzunluk))
    
    parolabutton=tk.Entry()
    parolabutton.place(x=50,y=230, width=300 , height=30)
    parolabutton.insert("insert",parola)
    print(alan)

def medium():

    try:
        
        uzunluk=int(entry.get())
        
    
    except ValueError:
            uyari2=tk.Label(text="Lütfen rakam kullanın",font=("Times New Roman", 11), fg="red", bg="black")
            uyari2.place(x=134,y=75)
            uyari2.after(3000, uyari2.destroy)

    kharf="abcdefghijklmnoprstuvyzqwx"
    bharf="ABCDEFGHIJKLMNOPRSTUVYZQWX"
    sayılar="0123456789"
        

    
    if uzunluk >= 63:
        uyari1=tk.Label(text="Orta için en fazla 62 haneli seçebilirsiniz",font=("Times New Roman", 11), fg="red", bg="black")
        uyari1.place(x=70,y=75)
        uyari1.after(3000, uyari1.destroy)
    else:
        pass
        
    
        
        
    all = kharf+bharf+sayılar
    parola ="".join(random.sample(all, uzunluk))
    
    parolabutton=tk.Entry()
    parolabutton.place(x=50,y=230, width=300 , height=30)
    parolabutton.insert("insert",parola)


def hard():
        
    try:
        
        uzunluk=int(entry.get())
        
    
    except ValueError:
            uyari2=tk.Label(text="Lütfen rakam kullanın",font=("Times New Roman", 11), fg="red", bg="black")
            uyari2.place(x=134,y=75)
            uyari2.after(3000, uyari2.destroy)
        
    kharf="abcdefghijklmnoprstuvyzqwx"
    bharf="ABCDEFGHIJKLMNOPRSTUVYZQWX"
    sayılar="0123456789"
    semboller="[]{}*;&!/,.-+$#?"
        
            
    if uzunluk >= 79:
        uyari1=tk.Label(text="Zor için en fazla 78 haneli seçebilirsiniz",font=("Times New Roman", 11), fg="red", bg="black")
        uyari1.place(x=70,y=75)
        uyari1.after(3000, uyari1.destroy)
    else:
        pass
        
        
    all = kharf+bharf+sayılar+semboller
    parola ="".join(random.sample(all, uzunluk))
    
    parolabutton=tk.Entry()
    parolabutton.place(x=50,y=230, width=300 , height=30)
    parolabutton.insert("insert",parola)


        
entry=Entry(form)
entry.place(x=140,y=50)



kolayb=tk.Button(text="KOLAY", width=10, height=5, bg="yellow", command=easy).place(x=70,y=110)
ortab=tk.Button(text="ORTA", width=10,height=5, bg="orange", command=medium).place(x=160,y=110)
zorb=tk.Button(text="ZOR", width=10,height=5, bg="red", command=hard).place(x=250,y=110)


form.mainloop()
