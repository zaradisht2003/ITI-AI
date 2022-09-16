# import networkx as nx
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# from matplotlib.figure import Figure
# import tkinter as Tk
# import matplotlib.pyplot as plt  
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# from tkinter import *


# root=Tk()
# root.geometry("700x700")
# radioButton1=IntVar()
# radioButton2=IntVar()
# radioButton3=IntVar()
# radioButton4=IntVar()



# textInputFrame=Frame(root,bg="#ffdb97")
# textInputFrame.place(x=20,y=50)
# TextInput=Text(textInputFrame,width=35,height=10)
# TextInput.grid(column=0,row=0)

# emptylabel=Label(textInputFrame,highlightthickness=0,background="#ffdb97")
# emptylabel.grid(row=1,column=0)
# showGraphButton = Button(textInputFrame,text="Show Graph",padx=10,pady=10,command=lambda :show_graph())
# showGraphButton.grid(column=0,row=3,rowspan=2)

# propertiesFrame=Frame(root,borderwidth=2,relief="solid")
# propertiesFrame.place(x=20,y=320)

# stopLabel=Label(propertiesFrame,text="Stopping Criteria",highlightthickness=0)
# saturationRadioButton=Radiobutton(propertiesFrame,text="Saturation",variable=radioButton1,value=1,command=lambda : print("You chose r1"),selectcolor="#7676EE")
# AGradioButton=Radiobutton(propertiesFrame,text="After Generation",variable=radioButton2, value=2,command=lambda : print("You chose r2"),selectcolor="#7676EE")
# AGInput=Entry(propertiesFrame,bg="#7676EE")
# AGInput.grid(row=3,column=1,padx=20)
# stopLabel.grid(row=0,rowspan=2,column=0,padx=20)
# saturationRadioButton.grid(row=0,column=1)
# AGradioButton.grid(row=1,column=1,)

# canvas=Canvas(propertiesFrame, width=400, height=2,background='#000000')
# canvas.grid(column=0,row=4,columnspan=2)
# canvas.create_line(20,200,2000,200, fill="black", width=5)

# popLabel=Label(propertiesFrame,text="Population",highlightthickness=0)
# popLabel.grid(row=5,column=0)
# populationInput=Entry(propertiesFrame,bg="#7676EE")
# populationInput.grid(row=5,column=1,pady=10,padx=20)

# crossLabel=Label(propertiesFrame,text="Crossover  ",highlightthickness=0)
# crossLabel.grid(row=6,column=0)
# crossoverInput=Entry(propertiesFrame,bg="#7676EE")
# crossoverInput.grid(row=6,column=1,pady=10,padx=20)

# MutationLabel=Label(propertiesFrame,text="Mutation   ",highlightthickness=0)
# MutationLabel.grid(row=7,column=0)
# MutationInput=Entry(propertiesFrame,bg="#7676EE")
# MutationInput.grid(row=7,column=1,pady=10,padx=20)

# elitismLabel=Label(propertiesFrame,text="Elitism        ")
# elitismLabel.grid(row=8,column=0)
# elitismInput=Entry(propertiesFrame,bg="#7676EE")
# elitismInput.grid(row=8,column=1,pady=10,padx=20)

# canvas=Canvas(propertiesFrame, width=400, height=2,background='#000000')
# canvas.grid(column=0,row=9,columnspan=2)
# canvas.create_line(20,200,2000,200, fill="black", width=5)

# selectionLabel=Label(propertiesFrame,text="Selection",highlightthickness=0)
# rankingRadioButton=Radiobutton(propertiesFrame,text="Ranking",variable=radioButton3,value=3,command=lambda : print("You chose r3"),selectcolor="#7676EE")
# tournmentButton=Radiobutton(propertiesFrame,text="Tournment",variable=radioButton4, value=4,command=lambda : print("You chose r4"),selectcolor="#7676EE")

# selectionLabel.grid(row=10,rowspan=2,column=0,padx=20)
# rankingRadioButton.grid(row=10,column=1)
# tournmentButton.grid(row=11,column=1,)


# root.config(background="#ffdb97")

# root.title("Traveling and Shipment Routing Using Genetic Algorithm")
# def fun():
#     x=radioButton1.get()
#     y=radioButton2.get()
#     a=radioButton3.get()
#     b=radioButton4.get()
#     c=populationInput.get()
#     d=crossoverInput.get()
#     e=MutationInput.get()
#     f=elitismInput.get()
#     g=AGInput.get()

        
        
#     print(x)
#     print(y)
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(e)
#     print(f)
#     print(g)
    
# b=Button(text="Show Result",highlightthickness=0,relief="solid",bg="#7676EE",command=lambda:fun())
# b.place(x=170,y=620)


# def show_graph():
#     graph = {}
#     i = 1.0
#     line = ''
#     while i != 100:
#         line = TextInput.get(i,i+1)
#         if len(line) == 0:
#             break
#         tokens = line.split()
#         node = tokens[0]
#         graph[node] ={}
#         for j in range (1,len(tokens) - 1,2):
#             graph[node][tokens[j]] = int(tokens[ j + 1])
#         i +=1
#         print(i)
#     print(len(graph))
#     print(graph)
#     NodesList =[]

#     for i in graph:
#         for j in graph[i]:
#             nodeTuple= zip(i,j)
#             NodesList += (nodeTuple)
#     print(NodesList)
#     print(type(NodesList[0]))
    
    
    
#     G = nx.DiGraph()
#     G.add_edges_from(NodesList)

#     print(G.nodes)

#     f = Figure(figsize=(2.5,2.5), dpi=100)
#     a = f.add_subplot(111)
#     black_edges = [edge for edge in G.edges() ]
#     pos = nx.spring_layout(G)

#     nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
#                             node_size = 300,ax=a)
#     nx.draw_networkx_labels(G, pos,ax=a)
#     nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True,ax=a)
#     canvas = FigureCanvasTkAgg(f, master=root)
#     canvas.draw()
#     canvas.get_tk_widget().pack()
#     toolbar = NavigationToolbar2Tk( canvas, root )
#     toolbar.update()
#     canvas._tkcanvas.place(x=400,y=30)   
# root.mainloop()
# st =input()
# tokens=st.split()
# num=(len(tokens)-1)/2
# ang=0
# inc=360/num
# print(tokens[0],"=",(0,0))
# for i in range(1,len(tokens)-1,2):
#     print(tokens[i]+"=",(int(tokens[i+1])*np.cos(ang),int(tokens[i+1])*np.sin(ang)))
#     ang+=inc
# a=np.sqrt(abs(-1-4))
# print(a)
from cmath import sqrt
from turtle import distance
import numpy as np
import pandas as pd
from numpy.random import shuffle
from numpy.random import randint
from random import choice
import matplotlib.pyplot as plt

class Point():
 
    COUNT = 0
 
    def __init__(self, x, y):
        self.X = x
        self.Y = y
 
    def __str__(self):
        return "Point(%s,%s)"%(self.X, self.Y) 
 
    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return np.sqrt(dx**2 + dy**2)
    
    def __eq__(self, other): 
        return self.X == other.X and self.Y == other.Y
    
class Individu():
 
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
        child = Individu()
        # je prends la moitier de moi-même.
        half = int(np.floor(len(self.route)/2))
        first_segment = self.route[:half]
        last_segment  = []
        # je complète avec l'autre
        for i in range(len(self.route)) :
            if other.route[i] not in first_segment :
                last_segment.append(other.route[i])
        child.set_route(first_segment + last_segment)
        return child
 
    def show_me(self):
        plt.figure(figsize=(5,5))
        xpoint=[]
        ypoint=[]
        for i,point in enumerate(self.route) :
            xpoint.append(point.X)
            ypoint.append(point.Y)
            x,y=point.X, point.Y
            plt.scatter(x,y)
            plt.text(x,y,'A'+str(i))
        plt.plot(xpoint,ypoint)
        plt.show()
population=[]
a_map=[]
# initialisation des points de la carte.
# prend en paramètre un nombre de points.
def init_map(nb):
    global a_map
    del a_map[:]
    for i in range(nb):
        userList =[[('S', 'A'),5], [('S', 'B'),2], [('S', 'C'),4],[ ('A', 'D'),9],[ ('A', 'E'),4], [('B', 'G'),6], [('C', 'F'),2], [('D', 'H'),7], [('E', 'G'),6], [('F', 'G'),1]]
        distances = []
        distances.append( int(userList [i][1]))
        maxDistance = max(distances)
        distance = userList [i][1]
        ex = randint(0, maxDistance)
        wy = sqrt(abs((maxDistance**2)-(ex**2))).real
        p = Point(ex, wy)
        a_map.append(p)
    print(a_map)
# initialisation de la population.
# prend en paramètre le nombre d'individus à créer.
def init_pop(nb, map_point):
    global population
    del population[:]
    for i in range(nb):
        i = Individu(True, map_point.copy())
        population.append(i)
    print(population)

# fonction qui sert à trier les individus suivant leur score.
# utile pour trouver les meilleurs.
def selection(pop):
    pop.sort(key=lambda x: x.score, reverse=False)

def crossover(pop,elitism):
    new_pop = []
    # elitism
    best_pop = population[0:elitism]
    # crossover
    for i in range(len(pop)-elitism) :
        new_pop.append(choice(best_pop).crossover(choice(population[elitism:])))
    return new_pop + best_pop

def play(nb_generation, nb_point,nbpop,elitism,seed) :
    np.random.seed(seed)
    init_map(nb_point)
    init_pop(nbpop, a_map)
    best=[]
    result=0
    for i in range(nb_generation) :
        global population
        selection(population)
        population = crossover(population,elitism)
        best_score = population[0].score
        best.append(best_score)
        znzn=0
        if best_score<1000:
            znzn+=1
            
            
            if znzn==2:
                break
    print ('Best Fit : ' + str(population[0].score))
    plt.title("Best Fitness function")
    plt.plot(best)
    plt.show()
    
play(nb_generation=40,nbpop=100,nb_point=10,elitism=20,seed=10)