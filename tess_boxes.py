import pytesseract
import cv2

import settings

def ler_alternativas(img):
    cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    height, width, _ = img.shape

    boxes = pytesseract.image_to_boxes(cinza, config="--psm 11 --oem 3")

    alternativas = []
    alternativa = None

    for box in boxes.splitlines():
        box = box.split(" ")

        x1, y1, x2, y2 = int(box[1]), height - \
            int(box[2]), int(box[3]), height-int(box[4])

        if alternativa:
            if box[0] == ')':
                alternativas.append(alternativa)

            alternativa = None

        if box[0] in settings.ALTERNATIVAS:
            alternativa = box[0]

    return alternativas

def ler_alternativas(img, manchas):
    cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, None, fx=1, fy=1)

    height, width, _ = img.shape

    boxes = pytesseract.image_to_boxes(cinza, config="--psm 11 --oem 3")

    alternativas = []

    for box in boxes.splitlines():
        box = box.split(" ")

        x1, y1, x2, y2 = int(box[1]), height - \
            int(box[2]), int(box[3]), height-int(box[4])

        for mancha in manchas:
            #print((x1, y1), manchas)
            if ponto_no_rect((x1, y1), mancha):
                print(box[0])
                alternativas.append(box[0])

    return alternativas

def ponto_no_rect(ponto: tuple, rect: tuple):
    if(ponto[0] >= rect[0] and ponto[0] <= rect[2]):
        if(ponto[1] >= rect[1] and ponto[1] <= rect[3]):
            return True
    
    return False