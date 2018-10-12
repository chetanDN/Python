import tkinter as tk 
r = tk.Tk() 
r.title('A Window To close') 
r.geometry("300x300")
button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
button.pack() 
r.mainloop() 
