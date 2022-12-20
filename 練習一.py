import numpy as np
import math as math
import matplotlib.pyplot as plt

color=[]
C=[]
x =[i for i in range(0, 256, 1)]
y =[i for i in range(0, 256, 1)]

def LinearEquation():
    for i in range(256):
        H =120 * x[i]/255 + 180
        HSI_Transform(H)

def HSI_Transform(H):
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

    color.append([min(1.0,R),min(1.0,G),min(1.0,B)]) 

def Normalize():
     for i in range(256):
        for j in range(256):
            C.append(color[i])
def Show():
    # print(r)
    LinearEquation()
    Normalize()
    X,Y = np.meshgrid(x,y)
    plt.scatter(Y/255,X/255,c=C,s=50)

    plt.show()

Show()