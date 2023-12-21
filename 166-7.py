from tkinter import*
from tkinter import ttk
root=Tk()
root.title("working on canvas using functions ")
root.geometry("100x600")

canvas=Canvas(root,width=990,height=490,bg="white",highlightbackground="grey")
canvas.pack()
label=Label(root,text="   Choose color - ")
label.place(relx=0.6,rely=0.9,anchor=CENTER)
fc=["red","blue","yellow","green"]
cd=ttk.Combobox(root,state="readonly",values=fc,width=10)
cd.place(relx=0.8,rely=0.9,anchor=CENTER)

sx=Label(root,text="start X ")
sx.place(relx=0.1,rely=0.85,anchor=CENTER)
cv=[10,50,100,200,300,400,500,600,700,800,900]
d1=ttk.Combobox(root,state="readonly",values=cv,width=10)
d1.place(relx=0.4,rely=0.85,anchor=CENTER)

sy=Label(root,text="start Y ")
sy.place(relx=0.3,rely=0.85,anchor=CENTER)
d2=ttk.Combobox(root,state="readonly",values=cv,width=10)
d2.place(relx=0.4,rely=0.85,anchor=CENTER)

ex=Label(root,text="end X ")
ex.place(relx=0.05,rely=0.85,anchor=CENTER)
d3=ttk.Combobox(root,state="readonly",values=cv,width=10)
d3.place(relx=0.6,rely=0.85,anchor=CENTER)

ey=Label(root,text="End Y ")
ey.place(relx=0.7,rely=0.85,anchor=CENTER)
d4=ttk.Combobox(root,state="readonly",values=cv,width=10)
d4.place(relx=0.8,rely=0.85,anchor=CENTER)

def circle(event):
    oldx=d1.get()
    oldy=d2.get()
    newx=d3.get()
    newy=d4.get()
    keypress='c'
    draw(keypress,oldx,oldy,newx,newy)

def rect(event):
    oldx=d1.get()
    oldy=d2.get()
    newx=d3.get()
    newy=d4.get()
    keypress='r'
    draw(keypress,oldx,oldy,newx,newy)

def line(event):
    oldx=d1.get()
    oldy=d2.get()
    newx=d3.get()
    newy=d4.get()
    keypress='l'
    draw(keypress,oldx,oldy,newx,newy)

def draw(keypress,oldx,oldy,newx,newy):
    color=cd.get()
    if keypress=='c':
        draw_circle=canvas.create_oval(oldx,oldy,newx,newy,fill=color)
    if keypress=='r':
        draw_rect=canvas.create_rectangle(oldx,oldy,newx,newy,fill=color)
    if keypress=='l':
        draw_line=canvas.create_line(oldx,oldy,newx,newy,fill=color)

root.bind("<c>",circle)
root.bind("<r>",rect)
root.bind("<l>",line)

root.mainloop()