# -*- coding: utf-8 -*-
"""Image Processing in python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iQiWJAJSoPAwPIQHlIGnUrVHRwc5fA47

**Importing and image upload**
"""

import cv2
from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt

img = cv2.imread("/content/drive/MyDrive/MSCS/Sem-1/Theory of programming languages/Trump.png")

print(type(img))

"""**Original image**"""

cv2_imshow(img)

"""**Image Rotate**"""

height, width = img.shape[0:2]

img.shape[0:2]

rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)
rotatedImage = cv2.warpAffine(img, rotationMatrix, (width, height))
cv2_imshow(rotatedImage)

"""**Image Crop**"""

x=int(input("Enter Start point on x axis:"))
y=int(input("Enter Start point on y axis:"))

w=int(input("Enter width of cropped image:"))
h=int(input("Enter height of cropped image:"))

cropped_image = img[y:y+h, x:x+w] # Cropping using Slicing
plt.axis("off")
plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
plt.show() # Display the original image
print(cropped_image.shape)

"""**Image brightness**"""

import random
import numpy as np
def brightness(img, low, high):
    value = random.uniform(low, high)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv = np.array(hsv, dtype = np.float64)
    hsv[:,:,1] = hsv[:,:,1]*value
    hsv[:,:,1][hsv[:,:,1]>255]  = 255
    hsv[:,:,2] = hsv[:,:,2]*value 
    hsv[:,:,2][hsv[:,:,2]>255]  = 255
    hsv = np.array(hsv, dtype = np.uint8)
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return img
img = brightness(img, 0.5, 3)
cv2_imshow(img)

"""**Image zoom**"""

def fill(img, h, w):
    img = cv2.resize(img, (h, w), cv2.INTER_CUBIC)
    return img
def zoom(img, value):
    if value > 1 or value < 0:
        print('Value for zoom should be less than 1 and greater than 0')
        return img
    value = random.uniform(value, 1)
    h, w = img.shape[:2]
    h_taken = int(value*h)
    w_taken = int(value*w)
    h_start = random.randint(0, h-h_taken)
    w_start = random.randint(0, w-w_taken)
    img = img[h_start:h_start+h_taken, w_start:w_start+w_taken, :]
    img = fill(img, h, w)
    return img
img = zoom(img, 0.5)
cv2_imshow(img)

"""**Horizontal Shift**"""

def fill(img, h, w):
    img = cv2.resize(img, (h, w), cv2.INTER_CUBIC)
    return img
        
def horizontal_shift(img, ratio=0.0):
    if ratio > 1 or ratio < 0:
        print('Value should be less than 1 and greater than 0')
        return img
    ratio = random.uniform(-ratio, ratio)
    h, w = img.shape[:2]
    to_shift = w*ratio
    if ratio > 0:
        img = img[:, :int(w-to_shift), :]
    if ratio < 0:
        img = img[:, int(-1*to_shift):, :]
    img = fill(img, h, w)
    return img
img = horizontal_shift(img, 0.7)
cv2_imshow( img)