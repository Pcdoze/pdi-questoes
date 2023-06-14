import pytesseract
import cv2 as cv
import numpy as np

import settings,  \
        contours, \
        tess_boxes


img = cv.imread('questoes/3.png')
img = cv.resize(img, None, fx=1, fy=1)

print("s")
manchas = contours.detectar_manchas(img)

if len(manchas) == 5:
    alternativas = tess_boxes.ler_alternativas(img, manchas)
else:
    alternativas = tess_boxes.ler_alternativas(img)

if (settings.CORRETA not in alternativas):
    print('CERTA')
else:
    print('ERRADA')

cv.waitKey(0)
cv.destroyAllWindows()
