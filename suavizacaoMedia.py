import cv2
#blur = utilizada em identificação de objetos
#primeiro tem definir o tamanho uam quantidade de pixels => tem que ser ímpar

picture = cv2.imread("entrada.jpg")
#cria pontos na imagem
for i in range(0, picture.shape[0],15):
    for j in range(0, picture.shape[1],15):
        picture[i:i+3, j:j+3] = (255, 255, 255)

############## aplicação blur ##############
# alteracão dos valores pela media aritmética
suave = cv2.blur(picture, (10, 10))

cv2.imshow("Raspberry", suave)
cv2.waitKey(0)