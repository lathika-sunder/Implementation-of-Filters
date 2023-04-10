# Implementation-of-Filters
## Aim:

To implement filters for smoothing and sharpening the images in the spatial domain.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step 1:
Import the required libraries and read the image.

### Step 2:
Convert the saved BGR image to RGB using cvtColor().

### Step 3:
Use the filters required for image smoothing and sharpening.

### Step 4:
Apply the filters using cv2.filter2D() for each respective filters.
 

### Step 5:
Plot the images of the original one and the filtered one using plt.figure() and cv2.imshow().
 

## Program:
~~~
Developed By   : Javith farkhan S
Register Number: 212221240017
~~~
~~~
import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread('bike.jpg')
image2=cv2.cvtColor (image1, cv2.COLOR_BGR2RGB)
~~~
## 1. Smoothing Filters :
### i) Using Averaging Filter:
~~~
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
~~~
### ii) Using Weighted Averaging Filter:
~~~
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
~~~
### iii) Using Gaussian Filter:
~~~
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
~~~
### iv) Using Median Filter:
~~~
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
~~~
## 2. Sharpening Filters:
### i) Using Laplacian Kernal:
~~~
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
~~~
### ii) Using Laplacian Operator:

~~~
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
~~~

## Output:
### Smoothing Filters:

#### i)  Using Averaging Filter:

![img01](https://user-images.githubusercontent.com/94296805/230884846-961d3982-92d7-4eca-8bd2-7745780cabda.png)


#### ii) Using Weighted Average Filter:

![img02](https://user-images.githubusercontent.com/94296805/230884873-d0ec4f3a-2064-4070-ae96-4069b784c318.png)


#### iii) Using Gaussian Filter:

![img03](https://user-images.githubusercontent.com/94296805/230884891-d3e8c4ed-c636-422e-9062-57242fde3ea0.png)


#### iv) Using Median Filter:

![img04](https://user-images.githubusercontent.com/94296805/230884940-8823d14d-d72a-4531-bf34-06687f1370d7.png)


### Sharpening Filters:

#### i) Using Laplacian Kernel:

![img05](https://user-images.githubusercontent.com/94296805/230884964-190c327f-02fa-4026-88dc-2cd0d5f6bd0f.png)


#### ii) Using Laplacian Operator:

![img06](https://user-images.githubusercontent.com/94296805/230885000-eddf6fb6-5895-492e-8e1a-e857109a98d9.png)


## Result:
Thus the filters are designed for smoothing and sharpening the images in the spatial domain.
