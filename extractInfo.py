################# Extração de informações básicas de uma imagem #################

import cv2

picture = cv2.imread("foofighters.jpg")# leitura de uma imagem jpg
cv2.imshow("Foo Fighters", picture) # => mostra imagem

#print(foofighters) => mostra todos os valores de cada pixel desta imagem => como é gigante, fica um pouco difícil de ler, então é melhor fazer como está na linha baixo:
#como é uma matriz, tem que percorrer todas as linhas e todas as colunas

for i in range(0, picture.shape[0]): # para a coluna posição zero, percorrer todas as linhas
    for j in range(0, picture.shape[1]): # para a coluna na posição um, percorrer todas as linhas
        print(picture[i][j]) # varre valores R, G, B

print(picture.shape[0]) # => retorna o valor da altura da imagem em pixel
print(picture.shape[1]) # => retorna o valor da largura da imagem em pixel
print(picture.shape[2]) # => retorna a quantidade de canais de cores existentes em uma imagem

# cv2.waitKey(0) => fecha a imagem com qualquer tecla


