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

"""
Ammann-Beenker
"""
i = 4
e = envs.e
syst = tl.A5(envs.square0(0*e[0], e[0], e[2]))
syst.it_sub(i)
