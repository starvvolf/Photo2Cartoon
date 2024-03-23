# -*- coding: utf-8 -*-
#Referenced by Googld Gemini
#Cartoonize 

import cv2
import numpy as np
ID='banana.jpg'
img=cv2.imread(ID)


#사진 크기 조절
img=cv2.resize(img,None,fx=1,fy=1,interpolation=cv2.INTER_AREA)

#필터 적용
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray=cv2.GaussianBlur(gray,(3,3),sigmaX=0,sigmaY=0)
edges=cv2.Canny(gray,100, 150)
#edges = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
ret, mask=cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
cartoon=cv2.bitwise_and(img, img, mask=mask)

#결과영상출력
cv2.imshow('Cartoon Image',cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()