import cv2

picture = cv2.imread("beatles.jpg")

#passando uma tupla
(b,g,r) = cv2.split(picture)
# a partir do comando de cima será uma matriz unica de cada cor

cv2.imshow("Imagem Original", picture)
cv2.imshow("Cor azul", b)
cv2.imshow("Cor verde", g)
cv2.imshow("Cor vermelha", r)

# quanto mais proximo ao 255, mais clara é a imagem

cv2.waitKey(0)
