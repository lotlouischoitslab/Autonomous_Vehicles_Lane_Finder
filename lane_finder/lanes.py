import cv2
import numpy as np 
import matplotlib.pyplot as plt

# Average slope intercept
def average_slope_intercept(image,lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1,y1,x2,y2 = lines.reshape(4)
    

# Canny function traces the gradient of the roads
def canny(lane_image):
    gray = cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    canny = cv2.Canny(blur,50,150)
    return canny

# Gaussian Blur reduces noise in a given image
def gaussian(image):
    blur = cv2.GaussianBlur(gray,(5,5),0)

# Function display lines
def display_lines(image,lines):
    line_image = np.zeros_like(image)

    # Now we are going to reshape the lines to 1-D array
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line.reshape(4)
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0), 10)
    
    return line_image

# Region of Interest
def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
        [(200,height),(1100,height),(550,250)]
        ])
    mask = np.zeros_like(image) #creates array of zeros
    cv2.fillPoly(mask,polygons,255)
    masked_image = cv2.bitwise_and(image,mask)
    return masked_image

if __name__ == '__main__':
    image = cv2.imread('test_image.jpg')
    lane_image = np.copy(image)
    canny_image = canny(lane_image)
    cropped_image = region_of_interest(canny_image)
    lines = cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
    line_image = display_lines(lane_image,lines)
    combo_image = cv2.addWeighted(lane_image,0.8,line_image,1,1)
    cv2.imshow('result',combo_image)
    cv2.waitKey(0)

