################ Suavização com Mediana ################

#transforma a matriz em vetor, ordena por ordem crescente e deixa os números da matriz inteiros

import cv2
picture = cv2.imread("entrada.jpg")

suavidade = cv2.medianBlur(picture, 5) # os parâmetros são: a imagem e o tamanho do extrator
suavidade2 = cv2.medianBlur(picture, 35)

for i in range(0, picture.shape[0],15):
    for j in range(0, picture.shape[1],15):
        picture[i:i+3, j:j+3] = [255, 255, 255]

cv2.imshow(" Original Picture", picture)
cv2.imshow("Modified Picture", suavidade)
cv2.imshow("Modified Picture2", suavidade2)
cv2.waitKey(0)
