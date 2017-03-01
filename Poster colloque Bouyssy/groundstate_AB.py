#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 19:38:56 2017

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
# interpolation of irregularly spaced points
from scipy.interpolate import griddata

"""
Ammann-Beenker
"""
i = 5
e = envs.e
syst = tl.A5(envs.square0(0*e[0], e[0], e[2]))
#syst = tl.A5(envs.doubledSquaresPavel)
syst.it_sub(i)

wg = syst.integrate_arrow_field((0,0,0,0))
height = nx.get_node_attributes(wg, "weight")

P = syst.para()

# wavefunction
rho = .8
wf = np.array([rho**(height[p]) for p in wg])
norm = np.sum(wf**2.)
wf /= norm

"""
Plot (networkx)
"""
## drawing the tiling
#pos = nx.get_node_attributes(wg, "para")
#nx.draw_networkx(wg, pos, with_labels=False, node_size=4, node_color=wf, cmap="viridis")
#plt.axes().set_aspect("equal")
#plt.savefig("groundstate.pdf")

"""
Plot (scatter)
"""
pos = nx.get_node_attributes(wg, "para")
x, y = np.transpose([pos[p] for p in wg])
# set dark background
plt.axes().set_facecolor(plt.cm.viridis(0))
# point size
s = 4.
# plot!
plt.scatter(x, y, s=s, c=wf, edgecolor='', cmap="viridis")
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Densité électronique')
plt.axes().set_aspect('equal')
plt.savefig("groundstate.svg")


"""
Plot (interpolate)
"""
#def plotpts(bounds):
#    ((x0, y0), L) = bounds
#    def inreg(px, py):
#        return x0-L/2 <= px <= x0+L/2 and y0-L/2 <= py <= y0+L/2
#    # select points inside the region
#    x = []
#    y = []
#    z = []
#    for p, coeff in zip(wg, wf):
#        px, py = np.dot(P, p)
#        if inreg(px, py):
#            x.append(px)
#            y.append(py)
#            z.append(coeff)    
#    return x, y, z
#
#def plot(bounds, x, y, z, savename):
#    ((x0, y0), L) = bounds
#    # number of points in each direction for interpolation
#    N = int(400*L)
##    print(N)
##    N = 300
#    # define grid.
#    xi = np.linspace(x0-L/2,x0+L/2,N)
#    yi = np.linspace(y0-L/2,y0+L/2,N)
#    # grid the data.
#    zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')
#    # contour the gridded data, plotting dots at the randomly spaced data points.
#    vmin = np.min(z)
#    vmax = np.max(z)
#    eps = .06 # take a bit less for the interpolation to work well
#    plt.contourf(xi,yi,zi,15,cmap=plt.cm.viridis, vmin=vmin, vmax=vmax)
#        
##    # set limits
#    plt.xlim([x0-L/2+eps, x0+L/2-eps])
#    plt.ylim([y0-L/2+eps, y0+L/2-eps])
#    # equal aspect ratio, no axes
#    plt.axes().set_aspect('equal')
#    plt.axis('off')
#    
#    plt.savefig(savename + ".png", dpi=200, transparent = True)
#    plt.close()
#
#ri = np.array([-0.19, 0.136])
#Li = 0.4
#rf = np.array([0., 0.])
#Lf = 1.65
#
#def bounds(t):
#    r = (1.-t)*ri + t*rf
#    L = (1.-t)*Li + t*Lf
#    return (r, L)
#    
#ts = np.linspace(0., 1., 200.)
#count = 0
#for t in ts:
#    x, y, z = plotpts(bounds(t))
#    plot(bounds(t), x, y, z, str(count))
#    count += 1
