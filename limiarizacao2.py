import cv2
import matplotlib.pyplot as plt

############## técnica 2 ##############

foo = cv2.imread("foofighters.jpg")
#foo é a variável declarada para a leitura da imagem jpg

for i in range(0, foo.shape[0]):
    for j in range(0, foo.shape[1]):
        foo[i][j] = (0, 0, 0) # define que toda a imagem é preta

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(foo, '255', (15, 65), font, 2, (255, 255, 255), 2)
cv2.putText(foo, '70', (125, 65), font, 2, (70, 70, 70), 2)
cv2.putText(foo, '100', (255, 65), font, 2, (100, 100, 100), 2)
cv2.putText(foo, '1', (405, 65), font, 2, (1, 1, 1), 2)

for i in range(0, foo.shape[0]):
    for j in range(0, foo.shape[1]):
        if foo[i][j][0] == 1: #branco
            foo[i][j] = (255, 255, 255)
        else:
            foo[i][j] = (0, 0, 0) # tudo o que é um, fica branco, o resto fica preto

cv2.imshow("janela", foo)
cv2.waitKey(0)
