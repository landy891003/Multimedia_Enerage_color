import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

# read image
img = cv2.imread('dog.jpg')
 
# convert the image into grayscale before doing histogram equalization
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

new = gray_img.copy()
# gray_img=gray_img

# gray_img = gray_img/255
# plt.hist(gray_img.ravel(), 256, [0, 1],label= 'original image')
# plt.show()
# # image equalization

index = np.zeros([256])
for row in range(len(gray_img)):
    for column in range(len(gray_img[0])):
        grayvalue = gray_img[row][column]
        grayvalue = int(grayvalue)
        index[grayvalue] = index[grayvalue] + 1

cdf = np.zeros([256])
for i in range(256):
    if i == 0:
        cdf[i] = index[i]
        tem = index[i]
    else:
        tem = tem + index[i] 
        cdf[i] = tem

index_2 = np.zeros([256]) #轉換表: index是o~255 灰階 , value是指轉換後的灰階值

for i in range(256):
     index_2[i] = int(round(((cdf[i] - 1) /(cdf.max()-cdf.min()) ) * 255))

for i in range(len(gray_img)):
    for j in range(len(gray_img[0])):
        value = gray_img[i][j]
        new[i][j] = index_2[int(value)]

new=new/255
cv2.imshow('new',new)  
cv2.imwrite('out.jpg',new)
cv2.waitKey(0) 

def LinearEquation(energy,img):            
    (Blue,Green,Red)= cv2.split(img)
    Blue = Blue/255
    Green = Green/255
    Red =Red/255
    for i in range(len(energy)):
        for j in range(len(energy[0])):
            H =120 * energy[i][j]+ 180
            S=1
            I=2/3
            if(H>=0 and H<120):
                B = I*(1-S)
                R = I*(1+(S*math.cos(H*math.pi/180))/(math.cos((60-H)*math.pi/180)))
                G = 3*I-(R+B)
            elif(H>=120 and H<240):
                H=H-120
                R=I*(1-S)
                G=I*(1+(S*math.cos(H*math.pi/180))/(math.cos((60-H)*math.pi/180)))
                B=3*I-(R+G)
            elif(H>=240 and H<360):
                H=H-240
                G=I*(1-S)
                B=I*(1+(S*math.cos(H*math.pi/180))/(math.cos(60*math.pi/180-H*math.pi/180)))
                R=3*I-(B+G)
            Blue[i][j] = B
            Green[i][j] = G
            Red[i][j] = R
    
    new = cv2.merge([Blue,Green,Red])
    cv2.imshow('new',new)  
    cv2.waitKey(0)    

LinearEquation(new,img)
# # show image
# # cv2.imshow("equal_image", equalize_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # plot image histogram
# plt.hist(gray_img.ravel(), 256, [0, 255],label= 'original image')
# plt.hist(equalize_img.ravel(), 256, [0, 255],label= 'equalize image')
# plt.legend()
