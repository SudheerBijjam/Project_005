from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Simple image")
root.iconbitmap("C:/Users/sudhe/PycharmProjects/pythonProject/hi.ico")


def imageopen():
    global myimg
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/sudhe/PycharmProjects/pythonProject/Images",
                                               title="select file",
                                               filetypes=(("png files", "*.png"), ("all files", "*.*")))

    my_label1 = Label(root, text=root.filename).pack()
    myimg = ImageTk.PhotoImage(Image.open(root.filename))
    my_label2 = Label(image=myimg).pack()


mybutton = Button(root, text="open Image", command=imageopen).pack()

root.mainloop()
