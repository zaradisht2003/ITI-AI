
from tkinter import *


root=Tk()
root.geometry("700x700")
radioButton1=IntVar()
radioButton2=IntVar()
radioButton3=IntVar()
radioButton4=IntVar()



textInputFrame=Frame(root,bg="#ffdb97")
textInputFrame.place(x=20,y=50)
TextInput=Text(textInputFrame,width=35,height=10)
TextInput.grid(column=0,row=0)

emptylabel=Label(textInputFrame,highlightthickness=0,background="#ffdb97")
emptylabel.grid(row=1,column=0)
showGraphButton = Button(textInputFrame,text="Show Graph",padx=10,pady=10)
showGraphButton.grid(column=0,row=3,rowspan=2)

propertiesFrame=Frame(root,borderwidth=2,relief="solid")
propertiesFrame.place(x=20,y=320)

stopLabel=Label(propertiesFrame,text="Stopping Criteria",highlightthickness=0)
saturationRadioButton=Radiobutton(propertiesFrame,text="Saturation",variable=radioButton1,value=1,command=lambda : print("You chose r1"),selectcolor="#7676EE")
AGradioButton=Radiobutton(propertiesFrame,text="After Generation",variable=radioButton2, value=2,command=lambda : print("You chose r2"),selectcolor="#7676EE")
AGInput=Entry(propertiesFrame,bg="#7676EE")
AGInput.grid(row=3,column=1,padx=20)
stopLabel.grid(row=0,rowspan=2,column=0,padx=20)
saturationRadioButton.grid(row=0,column=1)
AGradioButton.grid(row=1,column=1,)

canvas=Canvas(propertiesFrame, width=400, height=2,background='#000000')
canvas.grid(column=0,row=4,columnspan=2)
canvas.create_line(20,200,2000,200, fill="black", width=5)

popLabel=Label(propertiesFrame,text="Population",highlightthickness=0)
popLabel.grid(row=5,column=0)
populationInput=Entry(propertiesFrame,bg="#7676EE")
populationInput.grid(row=5,column=1,pady=10,padx=20)

crossLabel=Label(propertiesFrame,text="Crossover  ",highlightthickness=0)
crossLabel.grid(row=6,column=0)
crossoverInput=Entry(propertiesFrame,bg="#7676EE")
crossoverInput.grid(row=6,column=1,pady=10,padx=20)

MutationLabel=Label(propertiesFrame,text="Mutation   ",highlightthickness=0)
MutationLabel.grid(row=7,column=0)
MutationInput=Entry(propertiesFrame,bg="#7676EE")
MutationInput.grid(row=7,column=1,pady=10,padx=20)

elitismLabel=Label(propertiesFrame,text="Elitism        ")
elitismLabel.grid(row=8,column=0)
elitismInput=Entry(propertiesFrame,bg="#7676EE")
elitismInput.grid(row=8,column=1,pady=10,padx=20)

canvas=Canvas(propertiesFrame, width=400, height=2,background='#000000')
canvas.grid(column=0,row=9,columnspan=2)
canvas.create_line(20,200,2000,200, fill="black", width=5)

selectionLabel=Label(propertiesFrame,text="Selection",highlightthickness=0)
rankingRadioButton=Radiobutton(propertiesFrame,text="Ranking",variable=radioButton3,value=3,command=lambda : print("You chose r3"),selectcolor="#7676EE")
tournmentButton=Radiobutton(propertiesFrame,text="Tournment",variable=radioButton4, value=4,command=lambda : print("You chose r4"),selectcolor="#7676EE")

selectionLabel.grid(row=10,rowspan=2,column=0,padx=20)
rankingRadioButton.grid(row=10,column=1)
tournmentButton.grid(row=11,column=1,)


root.config(background="#ffdb97")

root.title("Traveling and Shipment Routing Using Genetic Algorithm")



def fun():
    x=radioButton1.get()
    y=radioButton2.get()
    a=radioButton3.get()
    b=radioButton4.get()
    c=populationInput.get()
    d=crossoverInput.get()
    e=MutationInput.get()
    f=elitismInput.get()
    g=AGInput.get()
    print(x)
    print(y)
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
b=Button(text="Show Result",highlightthickness=0,relief="solid",bg="#7676EE",command=lambda:fun())
b.place(x=170,y=620)
root.mainloop()








