from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Simple image")
root.iconbitmap("C:/Users/sudhe/PycharmProjects/pythonProject/hi.ico")

my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/sudhe/PycharmProjects/pythonProject/Images/1.JPG"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/sudhe/PycharmProjects/pythonProject/Images/2.JPG"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/sudhe/PycharmProjects/pythonProject/Images/3.JPG"))
my_img4 = ImageTk.PhotoImage(Image.open("C:/Users/sudhe/PycharmProjects/pythonProject/Images/4.JPG"))
my_img5 = ImageTk.PhotoImage(Image.open("C:/Users/sudhe/PycharmProjects/pythonProject/Images/5.JPG"))
my_img6 = ImageTk.PhotoImage(Image.open("C:/Users/sudhe/PycharmProjects/pythonProject/Images/6.JPG"))
my_img7 = ImageTk.PhotoImage(Image.open("C:/Users/sudhe/PycharmProjects/pythonProject/Images/7.JPG"))
my_img8 = ImageTk.PhotoImage(Image.open("C:/Users/sudhe/PycharmProjects/pythonProject/Images/8.JPG"))
my_img9 = ImageTk.PhotoImage(Image.open("C:/Users/sudhe/PycharmProjects/pythonProject/Images/9.JPG"))
my_img10 = ImageTk.PhotoImage(Image.open("C:/Users/sudhe/PycharmProjects/pythonProject/Images/10.JPG"))
my_img11 = ImageTk.PhotoImage(Image.open("C:/Users/sudhe/PycharmProjects/pythonProject/Images/11.JPG"))

my_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9, my_img10, my_img11]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(img_number):
    global my_label
    global button_forward
    global button_backward
    my_label.grid_forget()
    my_label = Label(image=my_list[img_number - 1])

    button_forward = Button(root, text=">>", command=lambda: forward(img_number + 1))
    button_backward = Button(root, text="<<", command=lambda: backward(img_number - 1))

    if img_number == 11:
        button_forward = Button(root, text=">>", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_backward.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def backward(img_number):
    global my_label
    global button_forward
    global button_backward
    my_label.grid_forget()
    my_label = Label(image=my_list[img_number - 1])

    button_forward = Button(root, text=">>", command=lambda: forward(img_number + 1))
    button_backward = Button(root, text="<<", command=lambda: backward(img_number - 1))

    if img_number == 1:
        button_forward = Button(root, text=">>", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_backward.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_backward = Button(root, text="<<", command=backward, state=DISABLED)
button_exit = Button(root, text="EXIT", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_backward.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
