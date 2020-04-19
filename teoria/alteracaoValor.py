########## Formas de alterar o valor de cada pixel da imagem ##########
import cv2

imagem = cv2.imread("beatles.jpg")
# tupla é uma estrutura de dados assim como a lista, porém a tupla é imutável, na lista é possivel alterar apenas o valor de um dado, na tupla não

imagem[0][0] = (0, 0, 0) ## alteração de valor da tupla; uma vez feito, não é possível reverter.
imagem[0:10, 0:10] = (255, 255, 255) ##altera de um valor até o outro => em x altera de 0 até 10 e em y altera de 0 até 10 também
imagem[0:10, :] = (255, 255, 255) ## somente : altera até o final da imagem, no caso o valor de y

cv2.imshow("janela", imagem)
cv2.waitKey(0)






