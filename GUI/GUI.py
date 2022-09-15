
from tkinter import *
from tkinter import filedialog
import tkinter


root=Tk()
r1ch=IntVar()
r2ch=IntVar()
c1ch=IntVar()
c2ch=IntVar()
c3ch=IntVar()


fram=Frame(root,width=100,height=3,borderwidth=2,bg="blue")
fram.place(x=20,y=400)
tex=Text(root,width=67,height=20)
tex.place(x=20,y=75)
r1=Radiobutton(fram, text="r1",variable=r1ch,value=1,width=70,height=1,command=lambda : print("You chose r1"))
r2=Radiobutton(fram, text="r2",variable=r2ch, value=2,width=70,height=1,command=lambda : print("You chose r2"))

l=Label(fram,text="choose")
l.pack()
r1.pack(padx=10)
r2.pack(padx=10)

fram1=Frame(root,width=100,height=40,borderwidth=2,bg="blue")
fram1.place(x=20,y=476)
l=Label(fram1,text="inputs")
l.pack()
e1=Entry(fram1,width=89)
e1.insert(0,"Input 1")
e1.focus_set()
e1.pack()


e2=Entry(fram1,width=89)
e2.insert(1,"input2")
e2.focus_set()
e2.pack()
fram2=Frame(root,width=100,height=40,borderwidth=2,bg="blue")
fram2.place(x=20,y=540)
l=Label(fram2,text="check")
l.pack()
c1=Checkbutton(fram2,variable=c1ch,text="c1",width=73)
c1.pack()                            
c2=Checkbutton(fram2,variable=c2ch,text="c2",width=73)
c2.pack()                            
c3=Checkbutton(fram2,variable=c3ch,text="c3",width=73)
c3.pack()

root.config(background="orange")

root.title("GUI")
#canvas=Canvas(bg="blue")
#
#canvas.create_rectangle(50,240,600,780)
#canvas.create_rectangle(50,420,600,780,fill="blue",outline="blue")
#canvas.create_rectangle(50,660,600,780,fill="blue",outline="blue")
#
#
#canvas.grid(row=1,column=1)


def fun():
    x=r1ch.get()
    y=r2ch.get()
    a=c1ch.get()
    b=c2ch.get()
    c=c3ch.get()
    d=e1.get()
    
    
    print(x)
    print(y)
    print(a)
    print(b)
    print(c)
    print(d)
b=Button(text="show in terminal",command=lambda:fun())
b.place(x=700,y=600)
root.mainloop()
#from tkinter import *
#from tkinter import ttk

##Create an instance of Tkinter frame


##Set the geometry of Tkinter frame
#root.geometry("750x250")

#def display_text():
#   global entry
#   string= entry.get()
#   print(string)



##Create an Entry widget to accept User Input
#entry= Entry(root, width= 40)
#entry.focus_set()
#entry.pack()

##Create a Button to validate Entry Widget









