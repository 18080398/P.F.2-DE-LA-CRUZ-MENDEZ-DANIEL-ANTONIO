from tkinter import *
window = Tk()
window.geometry('300x200')
window.title("bienvenidos")
lbl=Label(window, text="hola", font=("Arial Bold",50))
lbl.grid(column=0, row=0)

window.mainloop()