# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 14:33:10 2016

@author: nicolas
"""

""" import the Tilings package... """
import sys
sys.path.insert(0, '../../../gaps_topology/Tilings') # prepend the path to the Tiling package
import Tilings as tl
import AB_envs as envs
""" import the other stuff """
import matplotlib.pyplot as plt
import networkx as nx # graph tools
import QuantumGraph as QGraph

e = envs.e
zero = 0*e[0]
# return one of the 8 possible unit vectors (4 basis vectors, 2 signs)
ei = lambda i: (-1)**((i) // 4)*e[(i)%4]
        
def tlA():
    shapes = []
    # create the wheel
    for i in range(8):
        ea = ei(i)
        eb = ei(i+1)
        # inner lozenges
        shapes += envs.loz0(zero, ea, eb)
    return shapes
    
def tlB():
    shapes = []
    shapes += envs.loz0(zero, e[1], e[2])
    shapes += envs.loz0(zero, e[2], e[3])
    shapes += envs.loz0(zero, ei(3), ei(4))
    shapes += envs.loz0(-e[1]-e[0], e[0], e[1])
    shapes += envs.loz0(-e[2]-e[1], e[1], e[2])
    shapes += envs.loz0(-e[3]-e[2], e[2], e[3])
    shapes += envs.square0(zero, e[1], ei(7))
    
    return shapes
    
def tlC():
    shapes = []
    shapes += envs.square0(zero, e[1], ei(7))
    shapes += envs.square0(zero, ei(4), ei(6))
    shapes += envs.loz0(zero, e[1], e[2])
    shapes += envs.loz0(zero, e[2], e[3])
    shapes += envs.loz0(zero, ei(3), ei(4))
    shapes += envs.loz0(-e[3]-e[2], e[2], e[3])
    
    return shapes
    
def tlD1():
    shapes = []
    shapes += envs.loz0(zero, e[0], e[1])
    shapes += envs.loz0(zero, -e[0], e[3])
    shapes += envs.square0(zero, e[1], ei(3))
    
    shapes += envs.square0(zero, ei(4), ei(6))
    shapes += envs.square0(zero, ei(6), e[0])
    
    return shapes

def tlD2():
    shapes = []
    shapes += envs.loz0(zero, e[0], e[1])
    shapes += envs.loz0(zero, -e[0], e[3])
    shapes += envs.square0(zero, e[1], ei(3))
    
    shapes += envs.square0(-e[2], ei(2), ei(4))
    shapes += envs.square0(-e[2], ei(2), e[0])
    
    return shapes

def tlE():
    shapes = []
    shapes += envs.loz0(zero, e[1], e[2])
    shapes += envs.loz0(-e[3], -e[0], e[3])
    shapes += envs.square0(-e[0], e[0], e[2])
    shapes += envs.square0(-e[3], e[1], e[3])
    
    return shapes
    
def tlF():
    shapes = []
    shapes += envs.square0(-e[3]+e[1], e[3], -e[1])
    shapes += envs.loz0(-e[0], e[0], e[1])
    shapes += envs.loz0(-e[3], -e[0], e[3])
    
    return shapes
    
def tlE1():
    shapes = []
    shapes += envs.loz0(zero, e[1], e[2])
    shapes += envs.loz0(-e[0]-e[3], e[0], e[3])
    shapes += envs.square0(e[1], -e[1], -e[3])
    shapes += envs.square0(e[2], -e[0], -e[2])
    
    shapes += envs.square0(-e[0]-e[3]-e[1], e[1], e[3])
    shapes += envs.square0(-e[3]-e[0]-e[2], e[0], e[2])

    return shapes

def tlE2():
    shapes = []
    shapes += envs.loz0(zero, e[1], e[2])
    shapes += envs.loz0(-e[0]-e[3], e[0], e[3])
    shapes += envs.square0(e[1], -e[1], -e[3])
    shapes += envs.square0(e[2], -e[0], -e[2])
    
    shapes += envs.square0(-e[0]-e[3], -e[1], e[3])
    shapes += envs.loz0(-e[3]-e[0]-e[1],0,1)
    
    return shapes

def tlF1():
    shapes = []
    shapes += envs.square0(zero, -e[3], e[1])
    shapes += envs.loz0(-e[0], e[0], e[1])
    shapes += envs.loz0(-e[3]-e[0], e[0], e[3])
    
    shapes += envs.loz0(-e[3]-e[2], e[1], e[2])
    shapes += envs.loz0(-e[3]+e[1], e[2], e[3])
    
    return shapes

def tlF2():
    shapes = []
    shapes += envs.square0(zero, e[1], -e[3])
    shapes += envs.loz0(-e[0], e[0], e[1])
    shapes += envs.loz0(-e[3]-e[0], e[0], e[3])
    
    shapes += envs.square0(-2*e[3], e[1], e[3])
    
    return shapes    
    
def arrowed_graph(tiling, l, width):
    """
    plot the arrowed graph, after l inflations
    """
    # inflate
    tiling.it_sub(l)
    # construct and copy graph with arrows
    tiling.__construct_arrowed_graph__()
    arrG = tiling._arrowed_graph.copy()
    
    # keep only edges that are directed in the positive direction
    dictW = nx.get_edge_attributes(arrG,'arrow')
    for ed in dictW:
        if dictW[ed] == 1:
            arrG.remove_edge(*ed)
    
    # plot the arrowed graph
    QGraph.plot(arrG, weights=width, s = 0.)
            
    return None

# export the local envs as pdf files    
shapes = [tlA(), tlB(), tlC(), tlD1(), tlD2(), tlE(), tlF()]
names = ["A", "B", "C", "D1", "D2", "E", "F"]
for shape, name in zip(shapes, names):
    tiling = tl.A5(shape)
    arrowed_graph(tiling, 0, 1.)
    plt.savefig("env_"+name+"_raw.pdf")
    plt.close()
    
# export a large tiling as pdf file
eightfold = tl.A5(envs.eightfold)
arrowed_graph(eightfold, 2, .2)
plt.savefig("arrowed_tiling.pdf")

    