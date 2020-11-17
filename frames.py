from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Simple image")
root.iconbitmap("C:/Users/sudhe/PycharmProjects/pythonProject/hi.ico")

frame = LabelFrame(root, text="This is first frame", padx=50, pady=50)
frame.pack(padx=50, pady=50)

b1 = Button(frame, text="hello")
b1.grid(row=0, column=0)
b2 = Button(frame, text="Sudheer")
b2.grid(row=1, column=1)




root.mainloop()
