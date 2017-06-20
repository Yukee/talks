# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 10:51:10 2016

@author: nicolas
"""

""" import the Tilings package... """
import sys
sys.path.insert(0, '../../../gaps_topology/Tilings') # prepend the path to the Tiling package
import Tilings as tl
import QuantumGraph as QGraph

""" import the other stuff """
import math, cmath
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx # graph tools
import scipy

sq2 = math.sqrt(2)
lb = sq2 - 1.
pi = math.pi
e = np.exp(1j*pi*np.arange(4)/4)

def square(orig, ea, eb):
    """
    create a square with edges along ea and eb
    the arrows of the square are directed by ea and eb
    """
    if not math.isclose(np.vdot(ea, eb).real, 0, abs_tol = 1e-10):
        raise RuntimeError("The specified edges cannot be used to create a square " + str(np.vdot(ea, eb).real))
    
    B = orig
    A = orig + ea
    C = orig + ea + eb
    t1 = (1, (A, B, C))
    
    A = orig + eb
    t2 = (1, (A, B, C))
    
    return [t1, t2]

# scatter plot where pos is a list of tuples (x, y) and field is A(x,y)
def listplot(pos, field, ptsize=1, savename=None):
    x, y = np.array(pos).T
    color = field
    sc = plt.scatter(x, y, c=color, edgecolor='', marker='o', s=ptsize, cmap = 'viridis')
    plt.colorbar(sc)
    plt.axes().set_aspect('equal')
    plt.xlim((-1.,.85))
    plt.ylim((-0.45,1.5))

    dark = plt.cm.viridis(0)
    plt.gca().set_axis_bgcolor(dark)
    if(savename):
        plt.savefig(savename+'.png', dpi=300)
    plt.show()
    #fig.canvas.draw()

square = tl.A5(square(0, e[0], e[2]))
square.it_sub(6)
g = QGraph.periodize(square._graph)

""" node positions """
lift, pts = square.lift_tiling(0.) # lift in 4D
proj = square.perp_proj() # projection matrix from physical to internal space
pos = np.array([np.dot(proj, lift[pt]) for pt in g]) # node positions in internal space
real_space = np.array([(pt.real, pt.imag) for pt in g]) # node positions in real space

# compute the arrow potential
wg = square.integrate_arrow_field(0)
ptToPot = nx.get_node_attributes(wg,'weight')
pot = np.array([ptToPot[pt] for pt in g])

listplot(pos, pot, 2., "heights_ammann")