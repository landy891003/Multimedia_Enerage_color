import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

def calc_energy(img):
    x = cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize=3) 
    y = cv2.Sobel(img, cv2.CV_16S, 0, 1, ksize=3)

    absX = cv2.convertScaleAbs(x) 
    absY = cv2.convertScaleAbs(y)

    # 將兩個軸向的測邊結果相加，形成完整輪廓
    dst = cv2.addWeighted(absX, 0.5, absY,0.5,0)
    cv2.imshow('energy',dst)  
    cv2.waitKey(0)
    return dst

def LinearEquation(energy,img):            
    (Blue,Green,Red)= cv2.split(img)
    Blue = Blue/255
    Green = Green/255
    Red =Red/255

    for i in range(len(energy)):
        for j in range(len(energy[0])):
            H =120 * energy[i][j]/255+ 180
            S=1
            I=2/3
                # print(H)
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
def main():
    # 讀取影像
    img = cv2.imread("dog.jpg")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    map = calc_energy(gray_img)
    LinearEquation(map,img)
     # 3 channel

    # print(G)
    # plt.imshow(map)
if __name__ == "__main__":
    main()
