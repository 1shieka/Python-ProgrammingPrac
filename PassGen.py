import tkinter as tk
from tkinter import *
import random

root = Tk()
root.title("Strong Password Generator")
root.configure(background='#FFC0CB')
root.geometry("400x250")
root.resizable(False, False)

passstr = StringVar()
passlen = IntVar()
passlen.set(8)  

def generate():
    characters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
        '9', '0', '!', '@', '#', '$', '%', '^', '&', '*',
    ]
    
    password = ""

    for x in range(passlen.get()):
      password = password + random.choice(characters)

    passstr.set(password)
 
Label(root, text="🔒 Strong Password Generator 🔒", font=("Arial", 16, "bold"), bg='#FFC0CB', fg='#333333').pack(pady=10)

Label(root, text="Enter Password Length:", font=("Arial", 12), bg='#FFC0CB', fg='#555555').pack(pady=5)
Entry(root, textvariable=passlen, font=("Arial", 12), justify="center", width=10).pack(pady=5)

Button(root, text="Generate Password", font=("Arial", 12, "bold"), bg='#9370DB', fg='white', command=generate).pack(pady=10)

Label(root, text="Your Password:", font=("Arial", 12), bg='#FFC0CB', fg='#555555').pack(pady=5)
Entry(root, textvariable=passstr, font=("Arial", 12), justify="center", width=30, state="readonly").pack(pady=5)


root.mainloop()
