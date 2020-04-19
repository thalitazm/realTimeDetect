import cv2

beatles = cv2.imread("beatles.jpg")
rotatepic = beatles[::-1, :] #rotação eixo y

cv2.imshow("Imagem rotacionada", rotatepic)
cv2.imshow("Imagem Original", beatles)

cv2.waitKey(0)
