import cv2
import numpy as np 
import matplotlib.pyplot as plt


## Canny function traces the gradient of the roads
def canny(lane_image):
    gray = cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    canny = cv2.Canny(blur,50,150)
    return canny

## Gaussian Blur reduces noise in a given image
def gaussian(image):
    blur = cv2.GaussianBlur(gray,(5,5),0)

## Region of Interest
def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([[(200,height),(1100,height),(550,250)]])
    mask = np.zeros_like(image) #creates array of zeros
    cv2.fillPoly(mask,polygons,255)
    return mask

def display_image(image):
    plt.imshow(image)
    plt.show()


if __name__ == '__main__':
    image = cv2.imread('test_image.jpg')
    lane_image = np.copy(image)
    canny_image = canny(lane_image)
    display_image(canny_image)
    cv2.imshow('Result',region_of_interest(canny_image))
    cv2.waitKey(0)

    

