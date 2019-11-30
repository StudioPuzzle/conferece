from tkinter import *

canvas_width=800
canvas_height=650
brush_size=3
color="black"


def paint(event):
    global brush_size
    global color

    x1=event.x-brush_size
    x2=event.x+brush_size
    y1=event.y-brush_size
    y2=event.y+brush_size
    c.create_oval(x1,y1,x2, y2, fill=color, outline=color)


def brush_size_change(new_size):
    global brush_size
    brush_size=new_size


def color_change(new_color):
    global color
    color=new_color


def color_bg(new_color):
    
    c.configure(background=new_color)
    

root=Tk()
root.title("Drawer")


per=IntVar()
per.set(10)
bg_blue=Radiobutton(text="Синий", variable=per, value=2, command=lambda: color_bg("blue"))
bg_white=Radiobutton(text="Белый", variable=per, value=1, command=lambda: color_bg("white"))
bg_pink=Radiobutton(text="Розовый", variable=per, value=3, command=lambda: color_bg("pink"))
bg_yellow=Radiobutton(text="Желтый", variable=per, value=4, command=lambda: color_bg("yellow"))

red_button=Button(text="Красный", width=10, bg="red",command=lambda:color_change("red"))
green_button=Button(text="Зеленый", width=10, bg="green",command=lambda:color_change("green"))
white_button=Button(text="Белый", width=10, bg="white",command=lambda:color_change("white"))
blue_button=Button(text="Синий", width=10, bg="blue",command=lambda:color_change("blue"))
black_button=Button(text="Черный", width=10,command=lambda:color_change("black"))

clear_button=Button(text="Стереть все", width=10, command=lambda: c.delete("all"))
five_button=Button(text= "5", width=10, command=lambda:brush_size_change(5))
three_button=Button(text= "3", width=10, command=lambda:brush_size_change(3))
seven_button=Button(text= "7", width=10, command=lambda:brush_size_change(7))
ten_button=Button(text= "10", width=10, command=lambda:brush_size_change(10))
c=Canvas(root,width=canvas_width, height=canvas_height, bg="white")




c.grid(row=4, column=0, columnspan=10, padx=5, pady=5, sticky=E+W+S+N)

red_button.grid(row=0, column=2)
clear_button.grid(row=0, column=9)

five_button.grid(row=2, column=2)
three_button.grid(row=2, column=1)
seven_button.grid(row=2, column=3)
ten_button.grid(row=2, column=4)

bg_blue.grid(row=3, column=2)
bg_white.grid(row=3, column=1)
bg_pink.grid(row=3, column=3)
bg_yellow.grid(row=3, column=4)

green_button.grid(row=0, column=1)
blue_button.grid(row=0, column=3)
white_button.grid(row=0, column=5)
black_button.grid(row=0, column=4)

c.bind('<B1-Motion>',paint)
root.mainloop()
