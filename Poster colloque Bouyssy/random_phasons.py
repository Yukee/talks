#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:11:18 2017

@author: nicolas
"""

""" import the Tilings package... """
import sys
sys.path.insert(0, '../../gaps_topology/Tilings') # prepend the path to the Tiling package
import Tilings as tl
import AB_envs as envs
import Penrose_envs as Penvs
import QuantumGraph as QGraph
""" import the rest """
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx # graph tools
from scipy.sparse.linalg import eigsh
import random

# return one of the 8 possible unit vectors (4 basis vectors, 2 signs)
ei = lambda i: (-1)**((i) // 4)*e[(i)%4]

# the 8 possible triads of neighbors of an F site
def triads(p0):
    return [{tuple(p0 + ei(i0)), tuple(p0 + ei(i0+3)), tuple(p0 + ei(i0+5))} for i0 in range(8)]

def F(graph):
    """
    Return the F sites of the graph
    """
    return [p for p in graph if set(graph.neighbors(p)) in triads(p)]


i = 4
e = envs.e
syst = tl.A5(envs.square0(0*e[0], e[0], e[2]))
syst.it_sub(i)
graph = syst._graph.copy()

# projection matrices
P = syst.para()
Pi = syst.perp_proj()

def flip(graph, node):
    """
    Flip a node (must be an F site)
    """
    old_neighs = graph.neighbors(node)
    new_node = np.asarray(old_neighs[0]) + np.asarray(old_neighs[1]) + np.asarray(old_neighs[2]) - 2*np.asarray(node)
    new_node = tuple(new_node)
    old_vecs = -np.asarray(node) + old_neighs
    new_neighs = [(new_node, tuple(new_node - v)) for v in old_vecs if tuple(new_node - v) in graph.nodes()]
    
    # remove the node
    graph.remove_node(node)
    # add the new node and connect it to its neighbors
    graph.add_edges_from(new_neighs)
    
    # recompute the projections and change them
    graph.node[new_node]['para'] = np.dot(P, new_node)
    graph.node[new_node]['perp'] = np.dot(Pi, new_node)

# number of phason flips
Nflips = 500
for n in range(Nflips):
    # list the F nodes
    fnodes = F(graph)
    # pick one at random
    tojump = random.choice(fnodes)
    # perform the phason flip
    flip(graph, tojump)

QGraph.plot(graph, savename="flipped")
QGraph.plot(syst._graph, savename="unflipped")
    
#syst._graph = graph.copy()
#resolution = (2000, 2000)
#origin = (0., 0.)
#scaling = 0.5*(1.+np.sqrt(2))**i
#filename = "ammann"
#syst.draw(resolution, scaling, origin, filename)
#syst.save_image(filename)