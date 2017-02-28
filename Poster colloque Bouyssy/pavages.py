#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:57:07 2017

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

"""
Ammann-Beenker
"""
i = 4
e = envs.e
syst = tl.A5(envs.square0(0*e[0], e[0], e[2]))
syst.it_sub(i)

resolution = (2000, 2000)
origin = (0., 0.)
scaling = 0.5*(1.+np.sqrt(2))**i
filename = "ammann"
syst.draw(resolution, scaling, origin, filename)
syst.save_image(filename)