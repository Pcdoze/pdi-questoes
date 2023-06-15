import pytesseract
import cv2

# Encontrar as alternativas na imagem usando a posição das alternativas (manchas)
def ler_alternativas(_settings, img, manchas):
    
    alternativas = []
    
    for i, mancha in enumerate(manchas):
        
        # Cortar a imagem na posição de cada alternativa
        crop = img[mancha[1]:mancha[3], mancha[0]:mancha[2]]
        # Inverter a cor da imagem cortada
        crop = cv2.bitwise_not(crop)
        
        # pytesseract.image_to_string(): Retorna uma string com o texto extraído da imagem
        # | config: 
        #       psm 10 - Busca por texto na imagem considerando a imagem como um único caracter
        string = pytesseract.image_to_string(crop, config="--psm 10 --oem 3")
        for char in string:
            # Se o caracter é uma alternativa válida, adicionar à lista de alternativas
            if(char in _settings.ALTERNATIVAS):
                alternativas.append(char)
        
        
        cv2.imshow('parte_' + str(i), crop)
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()
            
    print('Alternativas Encontradas: ', sorted(alternativas))
    print('Alternativas Não Encontradas: ', sorted([x for x in _settings.ALTERNATIVAS if x not in alternativas]))
    
    return alternativas
