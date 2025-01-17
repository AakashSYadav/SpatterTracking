import cv2
import numpy as np

for k in range(200):
    print("Processing frame ",k)
    img = cv2.imread('frames/IR_'+str(k)+'.png',0)
    width, height = img.shape

    nw=10 # divisions in width
    nh=10 # divisions in height
    dh=int(height/nh)
    dw=int(width/nw)

    for i in range(nw):
        for j in range(nh):
            # # TODO: handle the remain 4 pixels on RHS
            # if condition:
            #     pass
            #
            roi = img[dw*i:dw*i+dw, dh*j:dh*j+dh]
            # Otsu's thresholding after Gaussian filtering
            blur = cv2.GaussianBlur(roi,(5,5),0)
            ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            if int(th3.mean())==255:
                th3[:,:]=0
            img[dw*i:dw*i+dw, dh*j:dh*j+dh]=th3
    cv2.imwrite("thresh/TH_"+str(k)+".png",img)
