# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:30:18 2021

@author: erick
"""

import numpy as np
from skimage import io
import matplotlib.pyplot as plt
import os
fileName = input("camaro.jpg")
while not os.path.isfile(fileName):
    fileName = input("Whoops! No such file! Please enter the name of the file you'd like to use.")







camaro=io.imread("Python Fundamentals/camaro.jpg")