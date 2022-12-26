import tkinter as tk
import os
import openai
from gpt import GPT
from gpt import Example

WIDTH=700
HEIGHT=500

root=tk.Tk()	

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ccffff')
canvas.pack(fill='both')

frame = tk.Frame(root, bg='#1affff')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

entry= tk.Entry(frame, bg='white', font=15)
entry.place(relx=0, rely=0.2, relwidth=0.8, relheight=0.1)

label = tk.Label(frame, bg='#00cccc', text='Type Query in English : ', font=18)
label.place(relx=0, rely=0.1, relwidth=0.8, relheight=0.1)

button = tk.Button(frame, bg='#00cccc', text='Submit', font=18)
button.place(relx=0.8, rely=0.097, relwidth=0.2, relheight=0.2)

label = tk.Label(frame, bg='#00cccc', text='Generated SQL Query is : ', font=18)
label.place(relx=0, rely=0.5, relwidth=0.8, relheight=0.1)

label1 = tk.Label(frame, bg='white', font=18)
label1.place(relx=0, rely=0.6, relwidth=0.8, relheight=0.3)

root.mainloop()
