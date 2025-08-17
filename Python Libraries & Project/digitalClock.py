import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

#Define The Clock Label

Clock_label = tk.label (root,font=("Helvetica",48),bg="black",fg="cyan")

Clock_label.pack(anchor="center",fill="both",expand=True)


#Function to update The Time

def Update_time():
    current_time = strftime("%H:%M:%S")
    Clock_label.config(text=current_time)
    Clock_label.after(1000,Update_time)

Update_time()
root.mainloop()