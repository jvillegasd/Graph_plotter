import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def drawGraph(G, longestPath):
    for e in G.edges():
        G[e[0]][e[1]]['color']='black'
    for i in range(len(longestPath)-1):
        G[longestPath[i]][longestPath[i+1]]['color']='blue'
    edge_color_list=[G[e[0]][e[1]]['color'] for e in G.edges()]
    pos=nx.shell_layout(G)
    nx.draw(G,pos, edge_color=edge_color_list)
    nx.draw_networkx_labels(G, pos)
    elabels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=elabels, label_pos=0.3)
    plt.show()

def strToInt(strAdj):
    Adj=[]
    for i in range(0, len(strAdj)):
        Adj.append([])
        for j in range(0, len(strAdj[0])):
            Adj[i].append(int(strAdj[i][j]))
    return Adj

def adjInput(m):
    rows=m.split(";")
    strAdj=[]
    for row in rows:
        strAdj.append(row.split(" "))
    newAdj=strToInt(strAdj)
    Adj=np.matrix(newAdj)
    return Adj

def sparseInput(m, n):
    rows=m.split(";")
    strAdj=[]
    for row in rows:
        strAdj.append(row.split(" "))
    newAdj=strToInt(strAdj)
    Adj=[[0]*n for i in range(n)]
    for i in range(len(strAdj[0])):
        Adj[newAdj[0][i]-1][newAdj[1][i]-1]=newAdj[2][i]
    return np.matrix(Adj)

tipo=int(input('1) Matriz de Adjacencia de pesos\n2) Lista de Adjacencia con pesos\nDigite opcion: '))
if tipo==1:
    m=input('Digite Matriz de Adjacencia de pesos: ')
    Adj=adjInput(m)
else:
    m=input('Digite Lista de Adjacencia de pesos: ')
    n=int(input('Digite numero de nodos: '))
    Adj=sparseInput(m, n)
G=nx.from_numpy_matrix(Adj, create_using=nx.DiGraph())
S=int(input('Digite el nodo fuente: '))
pred,lenght=nx.dijkstra_predecessor_and_distance(G, S)
path=nx.single_source_dijkstra_path(G, S)
print('\nDistancia a todos los nodos desde el nodo fuente', S,'usando Dijkstra:')
longestPath=v=0
for i in range(0, Adj.shape[0]):
    print(lenght[i], end=' ')
    if(lenght[i]>longestPath): 
        longestPath=lenght[i]
        v=i
    if(i==Adj.shape[0]-1): print()
print('\nPredecesores de cada nodo en la ruta con nodo fuente', S,'usando Dijkstra:')
for i in range(0, Adj.shape[0]):
    if(i!=S): print(str(pred[i]).strip("[]")," ", end='')
    else: print("-1 ", end=' ')
    if(i==Adj.shape[0]-1): print()
drawGraph(G, list(path[v]))
#Ejemplos de como se debe digitar la matriz de adj y la lista de adj:
#0 10 5 0 0;0 0 2 1 0;0 3 0 9 2;0 0 0 0 4;7 0 0 6 0 matriz
#1 1 2 2 3 3 3 4 5 5;2 3 3 4 2 4 5 5 1 4;10 5 2 1 3 9 2 4 7 6 lista - 5 nodos   