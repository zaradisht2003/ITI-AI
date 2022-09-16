
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter as Tk
import matplotlib.pyplot as plt  
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
showGraphButton = Button(textInputFrame,text="Show Graph",padx=10,pady=10,command=lambda :show_graph())
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
    global saturation
    saturation=radioButton1.get()
    AG=radioButton2.get()
    ranking=radioButton3.get()
    b=radioButton4.get()
    c=populationInput.get()
    d=crossoverInput.get()
    e=MutationInput.get()
    f=elitismInput.get()
    g=AGInput.get()

        
        
    return saturation,AG,ranking
    print(AG)
    print(ranking)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    
b=Button(text="Show Result",highlightthickness=0,relief="solid",bg="#7676EE",command=lambda:fun())
b.place(x=170,y=620)












from cmath import sqrt
import numpy as np
from numpy.random import shuffle
from numpy.random import randint
from random import choice
import matplotlib.pyplot as plt



class Point():
 
    COUNT = 0
 
    def __init__(self, x, y):
        self.X = x
        self.Y = y
 
    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return np.sqrt(dx**2 + dy**2)

class Individual():
 
    def __init__(self, init = False, map_point = []):
        self.score = 0
        self.route = []
        if init :
            shuffle(map_point)
            self.set_route(map_point)

    def set_route(self, map_point) :
        self.route = map_point
        for p in range(len(map_point) - 1) :
            self.score += map_point[p].distance(map_point[p+1])

    def crossover(self, other):
        child = Individual()
        half = int(np.floor(len(self.route)/2))
        first_segment = self.route[:half]
        last_segment  = []

        for i in range(len(self.route)) :
            if i <len(self.route) and i<len(other.route):
                if other.route[i] not in first_segment :
                    last_segment.append(other.route[i])
        child.set_route(first_segment + last_segment)
        return child
 

population=[]
a_map=[]

def init_map(nb):
    global a_map
    del a_map[:]
    for i in range(len(nb)):
        distances = []
        distance = nb [i][1]
        distances.append(distance)
        maxDistance = max(distances)
        ex = randint(0, maxDistance)
        wy = sqrt(abs((distance**2)-(ex**2))).real
        p = Point(ex, wy)
        a_map.append(p)


def init_pop(nb, map_point):
    global population
    del population[:]
    for i in range(nb):
        i = Individual(True, map_point.copy())
        population.append(i)


def selection(pop,func):
    pop.sort(key=lambda x: x.score, reverse=False)
    if func ==1:
        TS(pop)
    if func == 2:
        rank(pop)
    
def TS(population):
    new_offspring = []
    for _ in range( len(population)):
        candidates = [choice(population) for _ in range (3)]
        new_offspring.append(min(candidates,key = lambda ind : ind[0]))
        new_offspring.sort(key=lambda x: x.score, reverse=False)
    return new_offspring


def rank(pop):
    pop.sort(key=lambda x: x.score, reverse=False)

def mutation(pop,elitism):
    new_pop = []
    best_pop = population[0:elitism]
    for i in range(len(pop)-elitism) :
        new_pop.append(choice(best_pop).crossover(choice(population[elitism:])))
    return new_pop + best_pop

def play(nb_generation, userList,nbpop,elitism,AfterGeneration,saturation,) :

    init_map(userList)
    init_pop(nbpop, a_map)
    best=[50]
    generation=0
    for i in range(nb_generation) :
        global population
        selection(population,2)
        population = mutation(population,elitism)
        best_score = population[0].score
        
        distances = []
        for i in range(len(userList)):
            distance =  int(userList [i][1])
            distances.append(distance)
        
        if best_score<min(best):
            best.append(best_score)
        generation+=1
        
        
        ################# Saturation ########################
        if saturation ==1 and best[-1] == best[-2]and best[-1] ==best [-3]:
            break    
        ################# After Generation ##################
        if generation==AfterGeneration:
            break
    plt.title("Best Fitness function")
    plt.plot(best)
    plt.show()

userList =[[('S', 'A'),5], [('S', 'B'),2], [('S', 'C'),4],[ ('A', 'D'),9],[ ('A', 'E'),4], [('B', 'G'),6], [('C', 'F'),2], [('D', 'H'),7], [('E', 'G'),6], [('F', 'G'),1]]























def show_graph():
    graph = {}
    i = 1.0
    line = ''
    
    while i != 100:
        line = TextInput.get(i,i+1)
        if len(line) == 0:
            break
        tokens = line.split()
        node = tokens[0]
        graph[node] ={}
        for j in range (1,len(tokens) - 1,2):
            graph[node][tokens[j]] = int(tokens[ j + 1])
        i +=1
        print(i)
    print(len(graph))
    print(graph)
    NodesList =[]

    for i in graph:
        for j in graph[i]:
            nodeTuple= zip(i,j)
            NodesList += (nodeTuple)
    print(NodesList)
    print(type(NodesList[0]))
    
    
    
    
    
    
    
    
    
    G = nx.DiGraph()
    G.add_edges_from(NodesList)

    print(G.nodes)

    f = Figure(figsize=(2.5,2.5), dpi=100)
    a = f.add_subplot(111)
    black_edges = [edge for edge in G.edges() ]
    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                            node_size = 300,ax=a)
    nx.draw_networkx_labels(G, pos,ax=a)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True,ax=a)
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk( canvas, root )
    toolbar.update()
    canvas._tkcanvas.place(x=400,y=30)  
    fun()
     
    play(nb_generation=40,nbpop=100,userList=userList,elitism=20,AfterGeneration = 40,saturation=saturation)
    
root.mainloop()





























