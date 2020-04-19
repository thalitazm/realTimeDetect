import cv2

beatles = cv2.imread("beatles.jpg")
rotatepic = beatles[::-1, ::-1] #rotação eixos x e y

cv2.imshow("Arquivo rotacionado", rotatepic)
cv2.imshow("arquivo original", beatles)

cv2.waitKey(0)
