import numpy as np
import cv2

#Escrevendo imagem
font = cv2.FONT_HERSHEY_COMPLEX
pict2 = cv2.imread('imagem.jpg', cv2.IMREAD_COLOR)

#converte escala de cinza // é a mesma imagem
pic = cv2.imread('imagem.jpg', cv2.IMREAD_GRAYSCALE)

#conversão da imagem grayscale em imagem binária
_, threshold = cv2.threshold(pic, 110, 255, cv2.THRESH_BINARY)

#detecta contornos
contornos, _= cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# varrendo os contrnos encontrados na imagem
for cnt in contornos:

    approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)

    # delimitando o contorno dos contornos
    cv2.drawContours(pict2, [approx], 0, (0, 0, 255), 5)


    # achatar a matriz que contém as coordenadas dos vertices
    n = approx.ravel()
    i = 0


    for j in n:
        if(i % 2 == 0):
            x = n[i]
            y = n[i + 1]

            #string que contém as coordenadas
            string = str(x) + " " + str(y)

            if(i == 0):
                #texto localizado na parte superior da coordenada
                cv2.putText(pict2, "ponta flecha", (x, y),font, 0.5, (255, 0, 0))
            else:
                #texto restante da coordenada
                cv2.putText(pict2, string, (x, y), font, 0.5, (0, 255, 0))
        i = i + 1

# Imagem final
cv2.imshow('Resultado', pict2)

# saída do programa pressionando a tecla q:
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()