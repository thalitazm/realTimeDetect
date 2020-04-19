########## Alterar o valor de forma dinâmica com estrutura de repetição ##########
import cv2

imagem = cv2.imread("foofighters.jpg")

#branco = [255, 255, 255]
#for i in range(0, imagem.shape[0], 10): #imagem branca de 10 em 10 pixels
    #for j in range(0, imagem.shape[1], 2 ): #imagem branca de 10 em 10 pixels
        #imagem[i][j] = branco

        #matriz => tridimensional; além das posições i e j, tem as posições 0, 1 e 2 que representam os canais de cor: B, G, R
        #imagem[i:i+5, j:j+5] #criação quadrados => importante! [i:i+5] siginifica que vai de i ATÉ a posição 5

branco = [255, 255, 255]

for i in range(0, imagem.shape[0]):
    for j in range(0, imagem.shape[1]):
        if imagem[i][j][1] == 255:
            imagem[1][j] = branco


cv2.imshow("janela", imagem)
cv2.waitKey(0)
