#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 11:02:24 2021

@author: earnestt1234
"""

import fed3

import numpy as np

# load FED data
f1 = fed3.load("/Users/earnestt1234/Documents/fedviz/justin_data/FED2Cat.csv")
f2 = fed3.load("/Users/earnestt1234/Documents/fedviz/justin_data/FED3Cat.csv")

# define an analysis
A = fed3.ScatterPlot(y='pellets')

# run
A.run([f1, f2])

# plot
A.plot()
