#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:58:30 2019

@author: nicolas
"""

import numpy as np
import matplotlib.pyplot as plt

###############
# Nicer plots #
###############
from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('mathtext', fontset = 'cm')
rc('font', family = 'STIXGeneral')
rc('text', usetex=True)
# colors
BostonBlue = np.array([0., 104., 139.])/255
comp = np.array([200., 35., 0.])/255
# linewidth of plots
rc('lines', lw = 2)
# fontsize of the labels
rc('axes', labelsize = 10)
# bbox='tight' tries to make the bounding box fit the plot area
# pad_inches is the distance between the bounding box and the plot area
# see http://matplotlib.org/users/tight_layout_guide.html
rc('savefig', bbox = 'tight', pad_inches = .1)


N = 500
Lx = 1
Ly = 0.6
nx, ny = N, N
eps = 0.1
x = np.linspace(-eps, Lx+eps, nx)
y = np.linspace(-eps, Ly+eps, ny)
xv, yv = np.meshgrid(x, y)
r = np.sqrt(xv**2. + yv**2.)
x1, y1 = 1, 0
r1 = np.sqrt((xv-x1)**2. + (yv-y1)**2.)
k0 = 50
k1 = k0
I0 = 1.
# amplitude of the first wave
A0 = np.cos(k0*r)/np.sqrt(r)
# amplitude of the second wave
A1 = np.cos(k1*r1)/np.sqrt(r1)

fig, ax = plt.subplots()
data = np.abs(A0 + A1)
plt.contourf(x, y, data, levels=80, cmap="viridis", vmax=0.3*np.max(data), vmin=0)
ax.set_aspect("equal")
plt.savefig('interf_cylindriques.png', dpi=250)
plt.show()