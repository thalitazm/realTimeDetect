import cv2

beatles = cv2.imread("beatles.jpg")
rotatepic = beatles[:, ::-1] #rotação eixo x
##### lembrete: #####
#[1, 2, 3, 4, 5] => o comando acima está realizando a inversão de pixel => [5, 4, 3, 2, 1]

cv2.imshow("Imagem rotacionada", rotatepic)
cv2.imshow("Imagem Original", beatles)

cv2.waitKey(0)
