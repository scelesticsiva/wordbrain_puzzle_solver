from skimage.io import imread,imshow
import os

image=imread('puzzle1.png',as_grey=True)
print(image)
imshow(image)

