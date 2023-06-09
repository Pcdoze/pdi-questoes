import pytesseract
import cv2 as cv
import numpy as np

import settings


img = cv.imread('questoes/5.png')
img = cv.resize(img, None, fx=1, fy=1)

cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

height, width, _ = img.shape

boxes = pytesseract.image_to_boxes(cinza, config="--psm 11 --oem 3")

alternativas = []
alternativa = None

for box in boxes.splitlines():
    box = box.split(" ")
    
    x1, y1, x2, y2 = int(box[1]), height-int(box[2]), int(box[3]), height-int(box[4])
    
    if alternativa:
        if box[0] == ')':
            alternativas.append(alternativa)
            
        alternativa = None

    if box[0] in settings.ALTERNATIVAS:
        alternativa = box[0]
        
        
if(settings.CORRETA not in alternativas):
    print('CERTA')
else:
    print('ERRADA')
        
print(alternativas)
cv.imshow('output', img)

cv.waitKey(0)
cv.destroyAllWindows()