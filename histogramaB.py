######################### histograma #########################
# histograma é a quantidade de vezes que um numero, de uma lista aparece, no caso, de uma cor

import cv2
import matplotlib.pyplot as plt # significa use como plt porque senão toda vez que fosse refernciar a biblioteca, teria que colocar matplotlib.pyplot

rasp = cv2.imread("entrada.jpg")
#rasp é a variável declarada para a leitura da imagem jpg
listaAzul = [] #lista azul é igual a uma lista
listaVerde = []
listaVermelho = []
resultadoAzul = []

# separa canais de cores:
#criação de 2 for // um para percorer as linhas e outro para percorrer as colunas
for i in range(0, rasp.shape[0]): #percorre do valor zero até imagem.shape na posição 0 // i => altura
    for j in range(0, rasp.shape[1]): #largura
        #cria lista => está abaixo da variável rasp
        listaAzul.append(rasp[i][j][0]) #adicione um elemento no final da lista a cada passada do laço
        listaVerde.append(rasp[i][j][1])
        listaVermelho.append(rasp[i][j][2])

# para identificar no histograma
# cria cópia => listaAzul // ela possui todos os valores da lista original, mas sem repetição!
listaSemAzul = sorted(set(listaAzul)) # elimina os valores repetidos // passa como parâmetro a lista original
#print(listaSemAzul)

#cria laço de repetição //
for i in range(0, len(listaSemAzul)): # percorre lista cópia
    somatoria = 0 #quando entra nesse for tem que zerar a somatória
    for j in range(0, len(listaAzul)): # precorre lista original
        if listaSemAzul[i] == listaAzul[j]:
            somatoria += 1 # senão armazenar esse valor em lugar nenhum, na proxima passada não se refere mais ao zero e sim ao um, daí perde todos os valores zero da imagem, por isso cria-se:
    resultadoAzul.append(somatoria)
print(resultadoAzul)

#cv2.imshow("Picture", rasp)
cv2.waitKey(0)