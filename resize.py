########### Redimensionamento de imagem ###########

import cv2
picture = cv2.imread("beatles.jpg")

#larguraNova = 400
#alturaNova = 300
#picture = cv2.resize(picture, (larguraNova, alturaNova))

### para manter a proporcão ###

largura = picture.shape[1]
altura = picture.shape[0]

#calculo da proporção#
proporcao = float(altura/largura)
larguraNova = 350
alturaNova = int(larguraNova*proporcao)

picture = cv2.resize(picture, (larguraNova, alturaNova))

cv2.imshow("Imagem Original", picture)
cv2.waitKey(0)
