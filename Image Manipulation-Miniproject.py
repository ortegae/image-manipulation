# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:30:18 2021

@author: erick
"""

import numpy as np
from skimage import io
import matplotlib.pyplot as plt

camaro=io.imread('camaro.jpg')

print(camaro)

camaro.shape

plt.imshow(camaro)
plt.show()

cropped=camaro[0:500,:,:]
plt.imshow(cropped)
plt.show()

cropped=camaro[:,400:1000,:]
plt.imshow(cropped)
plt.show()

cropped=camaro[350:1100,200:1400,:]
plt.imshow(cropped)
plt.show()

io.imsave("camaro_cropped.jpg",cropped)

--Flip image

vertical_flip=camaro[::-1,:,:]
plt.imshow(vertical_flip)
plt.show()

io.imsave("camaro_verticalflip.jpg",cropped)

horizontal_flip=camaro[:,::-1,:]
plt.imshow(horizontal_flip)
plt.show()

--Color Channels 

red=np.zeros(camaro.shape,dtype="uint8")

red[:,:,0]=camaro[:,:,0]
plt.imshow(red)
plt.show()

green=np.zeros(camaro.shape,dtype="uint8")

green[:,:,1]=camaro[:,:,1]
plt.imshow(green)
plt.show()


blue=np.zeros(camaro.shape,dtype="uint8")

blue[:,:,2]=camaro[:,:,2]
plt.imshow(blue)
plt.show()

camaro_rainbow=np.vstack((red,blue,green))
plt.imshow(camaro_rainbow)
plt.show()

io.imsave("Camaro_raimbow.jpg",Camaro_rainbow)


