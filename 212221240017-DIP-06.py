#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opencv-python


# In[3]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread('car_6.png')
image2=cv2.cvtColor (image, cv2.COLOR_BGR2RGB)


# In[4]:


kernel1 = np.ones((11,11),np.float32)/121
avg_filter = cv2.filter2D(image2,-1,kernel1)
plt.figure(figsize = (9,9))
plt.subplot(1,2,1)
plt.imshow(image2)
plt.title("Original")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(avg_filter)
plt.title("Filtered")
plt.axis("off")


# In[5]:


kernel2 = np.array([[1,2,1],[2,4,2],[1,2,1]])/16
weighted_filter = cv2.filter2D(image2,-1,kernel2)
plt.figure(figsize = (9,9))
plt.subplot(1,2,1)
plt.imshow(image2)
plt.title("Original")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(weighted_filter)
plt.title("Filtered")
plt.axis("off")


# In[6]:


gaussian_blur = cv2.GaussianBlur(src = image2, ksize = (11,11), sigmaX=0, sigmaY=0)
plt.figure(figsize = (9,9))
plt.subplot(1,2,1)
plt.imshow(image2)
plt.title("Original")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(gaussian_blur)
plt.title("Filtered")
plt.axis("off")


# In[7]:


median = cv2.medianBlur(src=image2,ksize = 11)
plt.figure(figsize = (9,9))
plt.subplot(1,2,1)
plt.imshow(image2)
plt.title("Original")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(median)
plt.title("Filtered (Median)")
plt.axis("off")


# In[8]:


kernel3 = np.array([[0,1,0],[1,-4,1],[0,1,0]])
laplacian_kernel = cv2.filter2D(image2,-1,kernel3)
plt.figure(figsize = (9,9))
plt.subplot(1,2,1)
plt.imshow(image2)
plt.title("Original")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(laplacian_kernel)
plt.title("Filtered (Laplacian Kernel)")
plt.axis("off")


# In[9]:


laplacian_operator = cv2.Laplacian(image2,cv2.CV_64F)
plt.figure(figsize = (9,9))
plt.subplot(1,2,1)
plt.imshow(image2)
plt.title("Original")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(laplacian_operator)
plt.title("Filtered (Laplacian Operator)")
plt.axis("off")


# In[ ]:




