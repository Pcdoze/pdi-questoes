import cv2
from settings import settings

import modules


# Definir Constantes
_settings = settings()

# Ler e diminuir tamanho da imagem
img = cv2.imread('imagens/' + _settings.IMAGEM)
img = cv2.resize(img, None, fx=0.5, fy=0.5)

# Detectar alternativas na image
manchas = modules.manchas.detectar_manchas(img)
alternativas = modules.leitura.ler_alternativas(_settings, img, manchas)

# Se a alternativa certa não for encontrada,
# ela será considerada como marcada
if (_settings.CORRETA not in alternativas):
    print('RESPOSTA CERTA')
else:
    print('RESPOSTA ERRADA')

# Fechar janelas do cv2
cv2.waitKey(0)
cv2.destroyAllWindows()
