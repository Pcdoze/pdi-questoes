# import the necessary packages
from imutils import contours
from skimage import measure
import numpy as np
import argparse
import imutils
import cv2

# Detecta as posições e tamanho das alternativas e 
# armazena os valores em uma lista
def detectar_manchas(_image):
    
    # Inverter as cores da imagem
    image = cv2.bitwise_not(_image)
    # Transformar em grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Borrar | Kernel: 17x17
    image = cv2.GaussianBlur(image, (17, 17), 0)
    mostrar_parte(image)
    
    # Filtro de limiarização | Limiar: 100
    thresh = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)[1]
    mostrar_parte(thresh)
    
    # Erosão: Remove objetos menores (texto da questão)
    thresh = cv2.erode(thresh, None, iterations=2)
    mostrar_parte(thresh)
    
    # Dilatação: Preenche espaços vazios e Aumenta o tamanho dos objetos que sobraram (Alternativas)
    thresh = cv2.dilate(thresh, None, iterations=4)
    mostrar_parte(thresh)
        
    # measure.label: 
    #  cria um item label para cada grupo de pontos
    #  iguais conectados na imagem em uma lista de labels
    #  | connectivity: regra de agrupamento
    #  | background: cada pixel com esse valor será incluído no label background
    # np.zeros:
    #  cria uma imagem vazia que sera usada para guardar
    #  todos os maiores labels (mascara)
    labels = measure.label(thresh, connectivity=1, background=0)
    mask = np.zeros(thresh.shape, dtype="uint8")
    
    # Itera sobre os labels
    for label in np.unique(labels):
        # Ignorar o label se for o background
        if label == 0:
            continue
        
        # Adiciona o label a uma mascara e conta os pixels 
        labelMask = np.zeros(thresh.shape, dtype="uint8")
        labelMask[labels == label] = 255
        numPixels = cv2.countNonZero(labelMask)
        
        # Se o número de pixels na mascara for grande o suficiente
        # adiciona o label à mascara com todos os maiores labels
        if numPixels > 10:
            mostrar_parte(labelMask)
            mask = cv2.add(mask, labelMask)
            
    mostrar_parte(mask)
            
    # Encontra o contorno de cada label na mascara e adiciona a uma lista
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    
    # Cria uma lista e armazena os retângulos contendo os contornos
    manchas = []
    for (i, c) in enumerate(cnts):
        
        (x, y, w, h) = cv2.boundingRect(c)
        manchas.append((x, y, x+w, y+h))
        
    
    return manchas

def mostrar_parte(img):
    
    cv2.imshow('parte', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
